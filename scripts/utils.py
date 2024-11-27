import pandas as pd
def load_data(filepath):
    """ Load datasets from parquet files using the pd_parquet function.
    Args: 
        filepath(str): Path to the parquet file.
    Returns: 
        pandas dataframe: loaded dataframe
    """

    return pd.read_parquet(filepath)



