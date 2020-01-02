import numpy as np 
import pandas as pd

def hasNanAndInfValues(df):
    """ Takes a pandas dataframe, and returns the column list having nan, inf, -inf values
        The first list is the list of columns with at least 1 of these nan, inf, -inf values
        The second dict is the dictionnary containing as key the column from the above list 
        and as values the list of the different nan values the column contains

    Arguments:
        df {pandas} -- The dataframe to inspect
    """

    nanOrInfCols = []
    for col in df.columns:
        if df[col].isin([np.nan,np.inf,-np.inf]).any():
            print(col, ' has missing/inf/-inf values')   
            nanOrInfCols.append(col)
    

    hasNanDict = {}

    for col in df.columns:
        if df[col].isin([np.nan,np.inf,-np.inf]).any():
            print(col)
            
            listValues = []
            
            if df[col].isin([np.nan]).any():
                    listValues.append(np.nan)
                    
            if df[col].isin([np.inf]).any():
                listValues.append(np.inf)
                
            if df[col].isin([-np.inf]).any():
                listValues.append(-np.inf)
                
            hasNanDict[col] = listValues



    return(nanOrInfCols,hasNanDict)
        





