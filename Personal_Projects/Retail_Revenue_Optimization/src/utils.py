import pandas as pd

def get_data():
    data = pd.read_csv("../data/sales_data_with_marketing_intervention.csv")
    
    # data.head()
    # data.columns

    data_clean = data.copy()
    data_clean.drop("Unnamed: 0", inplace = True, axis = 1)
    
    # data_clean.head()
    # data_clean[data_clean['date'].isna()]
    # data_clean[data_clean['customer_id'].isna()]
    # data_clean[data_clean['product_id'].isna()]
    # data_clean[data_clean['quantity'].isna()]
    # data_clean[data_clean['unit_price'].isna()]
    # data_clean[data_clean['revenue'].isna()]
    # data_clean[data_clean['marketing_campaign'].isna()]
    
    return data_clean