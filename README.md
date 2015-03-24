# SAS -> Pandas DataFrame #

# Usage #


    from sasdataframe import sas_to_dataframe

    df = sas_to_dataframe('/path/to/sas/directory', 'dataset name', '/path/to/file.csv')

This is just a wrapper around some SAS that exports the dataset in question to a csv. The /path/to/file.csv should be where you'd like the csv to live on the file system. This location will later be used to import the data into Pandas.

If you have opinions about what types your columns ought to have, you can pass in a dictionary where each key is the column name and each value is the desired data type.

    type_dict = {'SYMBOL': object, 'NAME': object, 'CUSIP': object, 
                 'first_available_date': object, 'last_available_date': object}

    df = sas_to_dataframe('/path/to/sas/directory', 'dataset name', '/path/to/file.csv', type_dict=type_dict)

# Dependencies #

You'll want a copy of `inlinesas` installed for this one. 

