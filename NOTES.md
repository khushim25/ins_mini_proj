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

1. Start with quering on DBeaver.
    -> First convert the CSV file to tables in DBeaver. The script is:
    ```sql
    CREATE TABLE table_name AS
    SELECT *
    FROM read_csv_auto("your_csv_path");
    ```
    (Do it for all three CSV files)
--------
    -> Then go though the "sql" folder and check on various queries. Perform those queries understanding the questions well and check result. You can tweak out as per your choice. Your call!