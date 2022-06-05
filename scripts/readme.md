# Instructions for Running Scripts for Pulling API Data and Creating DB

Setup Requirements

1. Pull this repository.
2. Create a config.py file in your Scripts directory with your PostgreSQL DB password for the "postgres" user.  
3. Create a new DB in your local PostgreSQL DB called last_freeze_analysis.  Ensure the user "postgres" has permission to create schema objects.
4. Open calls_to_each_script.ipynb from VSCode or Jupyter Notebook and review the Markdown notes prior to running.  There is an option to run a subset of the data or the full dataset for the 7-county metro.  The full dataset will take a long time to process so run a subset to test your environment first.
5. After running the script, you should have a database with tables, view and keys. There will also be .csv files created of the table data for reference/prototype testing.
6. Instructions for running the ML code can be found in the readme here https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/tree/main/machine_learning.  
 
