import pandas as pd
from sqlalchemy import create_engine,exc
import os
from dotenv import load_dotenv
load_dotenv()

#function to add data to database
def data_db(file1,file2, exist="append",db="contacts"):
    #reading two files with pandas 
    df = pd.read_csv(file1,sep=";")
    df1 = pd.read_csv(file2,sep=";")
    #pandas has concat function that will add two dataframes
    merged_df=pd.concat([df,df1], ignore_index=True)
    #function sqlalchemy.create_engine(url, **kwargs)
    engine = create_engine(os.environ.get('engine'))
    try:
        merged_df.to_sql(db, if_exists=exist, index=False,con=engine)
    except exc.IntegrityError:
        print("Data already exist")
    except Exception as e:
        print("Some error while merging", type(e))
    else:
        print("data transferred to database")

#2 files downloaded that are stored in one directory above the current        
file1 = "../data-import-1.csv"
file2 = "../data-import-2.csv"
if __name__ == '__main__':
    data_db(file1,file2)

