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
    if type_dict: 
        return_obj = export_dsn_to_csv(path_to_libname, dsname, abs_path_to_csv, type_dict=type_dict)
    else:
        return_obj = export_dsn_to_csv(path_to_libname, dsname, abs_path_to_csv)

    if return_obj.returncode != 0:
        raise Exception("Couldn't convert " + dsname + " to csv.")
    else:
        return create_pd_dataframe(abs_path_to_csv)

