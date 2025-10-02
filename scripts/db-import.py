import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
conn_string = 'postgresql://clinops:"changeme"@localhost/clinops'  
db = create_engine(conn_string)

# the folder containing the CSV files
path = '.'  

# the list of CSV file names
files = [f for f in os.listdir(path) if f.endswith('.csv')]  

# Remove spaces and lowercase file names, then load them into the database
with db.connect() as conn: 
    for file in files:
        df = pd.read_csv(os.path.join(path, file))
        # Lowercase column names, replace spaces and hyphens with underscores
        df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]
        # Generate table name by removing spaces, hyphens and converting to lowercase
        table_name = "raw_" + file.replace(' ', '_').replace('-', '_').replace('.csv', '').lower()
        # Load DataFrame into PostgreSQL
        df.to_sql(table_name, con=conn, if_exists='replace', index=False)