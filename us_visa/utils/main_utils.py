import os
import sys
import numpy as np
import pandas as pd
import dill
import yaml
from us_visa.logger import logging
from us_visa.exception import USvisaException


def save_numpy_array(filepath: str,array: np.array):
    try:
        dir_path=os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath,'wb') as file:
            np.save(file,array)
    except Exception as e:
        raise USvisaException(e,sys)
    
def load_numpy_array(filepath:str):
    try:
        with open(filepath,'rb') as file:
            return np.load(file)
    except Exception as e:
        raise USvisaException(e,sys)

def read_yaml_file(filepath):
    try:
        with open(filepath,'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise USvisaException(e,sys)

def write_yaml_file(filepath:str,content:object,replace:bool=False):
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,'wb') as file:
            return yaml.safe_dump(content,file)
    except Exception as e:
        raise USvisaException(e,sys)

def save_object(filepath,object):
    try:
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,'wb') as file:
            dill.dump(object,file)
    except Exception as e:
        raise USvisaException(e,sys)
    
def drop_columns(df:pd.DataFrame,cols:list)->pd.DataFrame:
    try:
        df=df.drop(columns=cols,axis=1)
        return df
    except Exception as e:
        USvisaException(e,sys)