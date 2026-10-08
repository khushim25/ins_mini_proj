## Insurance Analytics Dashboard
_______

Phase 1: Gathering Data

The Data of this project is synthesized and used for learning purpose!

1. Created Data files in csv format through Pandas script given in <a href = src\genearate_data.py>Date Generating Code</a>. Check out this!

2. The Data files created are claims.csv, customer.csv and policies.csv with 50 rows of data. You can check out!

Phase 2: Set up

I have used DuckDB and Dbeaver for learning purpose over here. You can choose setup of you choice.

I have connected the DBeaver with DuckDB and created a connection to start with the playing on the Dataset generated with SQL queries.

Phase 3: Play with Dataset through SQL queries

(NOTE: This phase expects you to know SQL good enough to understand the logic. You can check out on various function used here if you dont know. Google things you dont know and understand.)

1. Start with quering on DBeaver:

    -> First convert the CSV file to tables in DBeaver. The script is:
    ```sql
    CREATE TABLE table_name AS
    SELECT *
    FROM read_csv_auto("your_csv_path");
    ```
    (Do it for all three CSV files)


    -> Then go though the "sql" folder and check on various queries. Perform those queries understanding the questions well and check result. You can tweak out as per your choice. Your call!

Phase 4: Daabricks Hands-on

This section we will play with the dataset by uploading it to Databrocks, creating volumes, UC tables, and Bronze tables of our datasets (All three Files)

We will be using Databricks Free Edition (Assuming one knows Databricks a bit)

Follow the Steps:

1. Create account in Databricks Free Edition
2. And Then Create New Notebook in your work space
3. Start experimenting once the csv files are uploaded in the new Volume made (make sure the csv files - all three are in different folder. It will be help ful when creating Bronze table)
4. Follow the script given in the notebooks folder (01_mod1_Insurance_Ingestion)
5. Once the Bronze tables are created play with those ( this will induce in learning SQL + PySpark(more))
6. One can try uploading the another csv to check with increamental ingestion
7. Before Creating Silver table Explore Jobs and Tasks and how it will be useful in creationg projects
8. Cerate Silver table for the three Bronze Tables.