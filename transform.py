import pandas as pd

# Creating dataframe for read CSV file with Pandas
df = pd.read_csv("data/spotify-2023.csv", encoding= 'latin-1')

# Visualizing table and data types
#print(df.head(5).T) # First five rows and all columns from table
#print(df.info()) # Information about data types from table
#print(df.shape) # Size of table, with the count of rows and columns

# Diagnosticating problems with a function
def problems(df):

    # Finding and summing null values
    nulls = df.isnull().sum() 
    print(f"Null values:\n{nulls[nulls > 0]}")

    # Finding and summing duplicate values
    duplicates = df.duplicated(subset=['track_name', 'artist(s)_name']).sum() 
    if duplicates > 0:
        print(f"Duplicate values: {duplicates}")
    else:
        print("No duplicate value found")

    # Finding empty strings
    for col in df.select_dtypes(include=['object', 'string', 'str']): 
        empty = (df[col] == '').sum()
        if empty > 0:
            print(f"Empty strings in {col}: {empty}")

problems(df)

#Problems that I found: 

#4 Duplicate values
#Null values in found in two columns: 'key' e 'in_shazam_charts'
#Columns - "released_year, released_month and released_day" with INT data types
#Columns - "streams, in_deezer_playlist, in_shazam_charts" with STR data type. 

# Removing duplicate values

df = df.drop_duplicates(subset=['track_name', 'artist(s)_name'])

# Filling null values

df['key'] = df['key'].fillna('C')

# Merging date columns to a unic date column and converting to date type

date_columns = ['released_year', 'released_month', 'released_day']

df['released_date'] = pd.to_datetime(df[date_columns].rename(columns={
    'released_year' : 'year',
    'released_month' : 'month',
    'released_day' : 'day'
}), errors= 'coerce')

# Removing old date columns
df = df.drop(columns=date_columns)

# Moving date column to the 3 index

last_column = df.columns[-1]
data_of_column = df.pop(last_column)
df.insert(3, last_column, data_of_column)

# Changing "streams, in_deezer_playlist, in_shazam_charts" to int data type

str_columns = ['streams', 'in_deezer_playlists', 'in_shazam_charts']

print(f"Quantity of null rows before:\n{df[str_columns].isnull().sum()}")

for col in str_columns:
    df[col] = pd.to_numeric(
    df[col].astype(str).str.replace(",", "", regex=False),
    errors="coerce",
)

print(f"Quantity of null rows after:\n{df[str_columns].isnull().sum()}")
