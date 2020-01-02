import numpy as np 
import pandas as pd

def conflictingDataTypes(df):
    """Takes a pandas dataframe, and returns two dictionnaries. The first one contains the different types of 
    each column. 
    key: column name 
    value: list of the different types a column has.

    The second one contains the conflicts:
    key: column with conflicting types
    value: the list of different types within the column
    
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


    conflictsDict = {}

    for k,v in valueTypeDict.items():
        if len(v) != 1:
            print(k,' has conflicting data types')
            for types in v:
                print(types)

            conflictsDict[k] = v

    return(valueTypeDict,conflictsDict)
    