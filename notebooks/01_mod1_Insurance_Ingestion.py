# Databricks notebook source
# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.default.insurance_raw

# COMMAND ----------

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/default/insurance_raw/customer.csv")
)

display(df)

# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp

customers_stream =  (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .option("cloudFiles.inferColumnTypes", "true")
    .option("cloudFiles.schemaLocation", "/Volumes/workspace/default/insurance_raw/_schemas/customers")
    .option("rescuedDataColumn", "_rescued_data")
    .load("/Volumes/workspace/default/insurance_raw/")
    .select(
        "*",
        col("_metadata.file_path").alias("source_file"),
        current_timestamp().alias("ingestion_timestamp")
    )
)

customers_stream.printSchema()

# COMMAND ----------

print("Spark is Alive")

# COMMAND ----------

# Bronze Write

query = (
    customers_stream.writeStream
    .format("delta")
    .option(
        "checkpointLocation",
        "/Volumes/workspace/default/insurance_raw/_checkpoints/customers"
    )
    .trigger(availableNow=True)
    .toTable("workspace.default.bronze_customers")
)

query.awaitTermination()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.default.bronze_customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     COUNT(*) AS record_count
# MAGIC FROM workspace.default.bronze_customers
# MAGIC GROUP BY customer_id
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) as total_records,
# MAGIC     COUNT(customer_id) as customer_id_present,
# MAGIC     COUNT(name) as name_present,
# MAGIC     COUNT(city) as city_present,
# MAGIC     COUNT(occupation) as occupation_present
# MAGIC FROM workspace.default.bronze_customers;

# COMMAND ----------

# for other table policies

policies_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/default/insurance_raw/policies/policies.csv")
)

display(policies_df)

# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp

policies_stream =  (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .option("cloudFiles.inferColumnTypes", "true")
    .option("cloudFiles.schemaLocation", "/Volumes/workspace/default/insurance_raw/_schemas/policies")
    .option("rescuedDataColumn", "_rescued_data")
    .load("/Volumes/workspace/default/insurance_raw/policies/")
    .select(
        "*",
        col("_metadata.file_path").alias("source_file"),
        current_timestamp().alias("ingestion_timestamp")
    )
)

policies_stream.printSchema()

# COMMAND ----------

claims_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/default/insurance_raw/claims/claims.csv")
)

display(claims_df)

# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp

claims_stream =  (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .option("cloudFiles.inferColumnTypes", "true")
    .option("cloudFiles.schemaLocation", "/Volumes/workspace/default/insurance_raw/_schemas/claims")
    .option("rescuedDataColumn", "_rescued_data")
    .load("/Volumes/workspace/default/insurance_raw/claims/")
    .select(
        "*",
        col("_metadata.file_path").alias("source_file"),
        current_timestamp().alias("ingestion_timestamp")
    )
)

claims_stream.printSchema()

# COMMAND ----------

query = (
    policies_stream.writeStream
    .format("delta")
    .option(
        "checkpointLocation",
        "/Volumes/workspace/default/insurance_raw/_checkpoints/policies"
    )
    .trigger(availableNow=True)
    .toTable("workspace.default.bronze_policies")
)

query.awaitTermination()

# COMMAND ----------

query = (
    claims_stream.writeStream
    .format("delta")
    .option(
        "checkpointLocation",
        "/Volumes/workspace/default/insurance_raw/_checkpoints/claims"
    )
    .trigger(availableNow=True)
    .toTable("workspace.default.bronze_claims")
)

query.awaitTermination()

# COMMAND ----------

# MAGIC %sql
# MAGIC LIST '/Volumes/workspace/default/insurance_raw'

# COMMAND ----------

from pyspark.sql.functions import col, trim, upper

silver_customer = (
    spark.table("workspace.default.bronze_customers")
    .select(
        col("customer_id").cast("string"),
        trim(col("name")).alias("name"),
        col("age").cast("int"),
        trim(col("city")).alias("city"),
        trim(col("occupation")).alias("occupation")
    )
    .dropDuplicates(["customer_id"])
)

silver_customer.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_customers")

# COMMAND ----------

display(
    spark.table("workspace.default.silver_customers")
)