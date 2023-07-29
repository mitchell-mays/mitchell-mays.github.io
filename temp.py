import pandas as pd
import os
# assign directory
directory = 'data'
 
# iterate over files in
# that directory

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if (f != "data/.DS_Store"):
            print(f)
            df = pd.read_csv(f)
            
            df["CATEGORY"] = df["CRIME"]
            df.loc[df["CRIME"].str.match(r'ASSAULT') ,"CATEGORY"] = "ASSAULT"
            df.loc[df["CRIME"].str.match(r'BURG') ,"CATEGORY"] = "BURGLARY"
            df.loc[df["CRIME"].str.match(r'RAPE') ,"CATEGORY"] = "RAPE"
            df.loc[df["CRIME"].str.match(r'LARC') ,"CATEGORY"] = "LARCENY"
            df.loc[df["CRIME"].str.match(r'ROBBERY') ,"CATEGORY"] = "ROBBERY"
            df.loc[df["CRIME"].str.match(r'VEHICLE THEFT') ,"CATEGORY"] = "VEHICLE THEFT"

            '''
            df["DATE_"] = pd.to_datetime(df["DATE_"]).dt.strftime('%m/%d/%Y')

            # Default time to noon
            df.loc[(df["TIME"] == ":"), "TIME"] = "12:00"
            df.loc[(df["TIME"] == "99:99"), "TIME"] = "12:00"
            

            if (f == "data/IMPD_UCR_2010_Data.csv" or f == "data/IMPD_UCR_2019_Data.csv" or f == "data/IMPD_UCR_2021_Data.csv" ):
                df["TIME"] = pd.to_datetime(df["TIME"], format= '%H:%M:%S').dt.strftime('%H:%M')
            else:
                df["TIME"] = pd.to_datetime(df["TIME"], format= '%H:%M').dt.strftime('%H:%M')
            df["DATETIME"] = pd.to_datetime(df["DATE_"] + " " + df["TIME"], format= '%m/%d/%Y %H:%M')
            '''
            df.to_csv(f)



print(df.dtypes)
print(df.head())