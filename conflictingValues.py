import numpy as np 
import pandas as pd

def conflictingDataTypes(df):
    """Takes a pandas dataframe, and returns a dictionnary containing the conflicting values of 
    each column. 
    key: column with conflcit 
    value: list of the different types a column has.
    
    Arguments:
        df {pandas} -- The dataframe to inspect
    """

    valueTypeDict = {}

    for col in df.columns:
        
        typeSet = set()
        
        for vals in df[col].values:
            typeSet.add(type(vals))
            
        valueTypeDict[col] = typeSet

    for k,v in valueTypeDict.items():
        print(k,' has the following types of values: ',v)

    for k,v in valueTypeDict.items():
        if len(v) != 1:
            print(k,' has conflicting data types')
            for types in v:
                print(types)

    return(valueTypeDict)
    