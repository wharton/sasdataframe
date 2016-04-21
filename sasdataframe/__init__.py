from inlinesas import call_SAS
import numpy as np
import pandas as pd

def export_dsn_to_csv(path_to_libname, dsname, abs_path_to_csv):
    export_code = """
        libname current '{0}';

        proc export data=current.{1}
            outfile="{2}"
            dbms=csv
            replace;
        run;
        """.format(path_to_libname, dsname, abs_path_to_csv)

    return call_SAS(export_code)

def create_pd_dataframe(abs_path_to_csv, type_dict={}):
    if type_dict:
        return pd.read_csv(abs_path_to_csv, dtype=type_dict)
    else:
        return pd.read_csv(abs_path_to_csv)

def sas_to_dataframe(path_to_libname, dsname, abs_path_to_csv, type_dict={}):
    """
    path_to_libname [string]: 
        Absolute path to the directory that the SAS dataset resides in.

    dsname [string]:
        Name of the SAS dataset (Ex: 'returns', 'columns').

    abs_path_to_csv [string]:
        Absolute path of csv file that the SAS dataset will be exported to.

    type_dict [dictionary] (optional):
        A dictionary of columns and their types.
        See http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html for details.

    USAGE:
    ======

    df = sas_to_dataframe('/path/to/sasdataset/directory', 'dataset_name', '/home/user/tempdataset.csv')

    """
    return_obj = export_dsn_to_csv(path_to_libname, dsname, abs_path_to_csv)

    if return_obj.returncode not in (0,1):
        msg = "Couldn't convert {} to csv.\nSAS invocation was {}.\nPlease see log for details.\n".format(dsname, return_obj)
        raise Exception(msg)
    else:
        return create_pd_dataframe(abs_path_to_csv, type_dict=type_dict)

