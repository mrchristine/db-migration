# Databricks Metastore Migration

This document discusses the metastore migration options and process. 

1. Export the metastore DDL 
2. Import the metastore DDL  
   a. The tool will import `TABLES` first  
   b. The tool will sideline `VIEWS` to be applied after all tables are created  
   c. The tool will import all `VIEWS`   
3. Copy the underlying DBFS / root table data
4. Report on legacy table DDLs to be repaired within the new workspace and metastore 


Recommendation:
1. Use the `--metastore-unicode` option to export and import if you do not know if tables contain unicode characters. 
   This should be applied to both export and import operations.
2. Use DBR 6.x / Spark 2.x releases if you have legacy table definitions. 
   Spark 3.x deprecates `SERDE` support and can cause import issues if you require those tables to use `SERDE` 
   definitions. 
3. If you manually register table partitions using `ALTER TABLE table_name ADD PARTITION ()` to tables, you will need 
   to manually report and add these partitions. The tool does not support this today. 
   Or if you need to drop partitions, you can use `ALTER TABLE table_name DROP PARTITION ()`