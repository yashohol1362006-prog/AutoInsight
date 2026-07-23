import pandas as pd

def load_csv(file_path):
    """ 
    Reads csv files and returns a pandas Dataframe
    """
    df= pd.read_csv(file_path)
    return df

def dataset_shape(df):
    rows, col = df.shape

    print(f'Rows : {rows}')
    print(f'Columns : {col}')

def colum_name(df):
    print(df.columns)
    
def missing_value(df):
    print('\nMissing Values\n')
    print(df.isna().sum())

def dataset_statistics(df):
    print('\n Dataset Statistics \n')
    print(df.describe())

def buisness_insight(df):
    revenue = df['Price'].sum()
    quantity = df['Quantity'].sum()
    avg_order = df['Order_ID'].mean()
    highest_sale = df['Price'].max()
    lowest_sale = df['Price'].min()
    max_price = df['Price'].max()
    row_max_price = df[df['Price'] == max_price]
    most_exp_product = row_max_price['Product'].iloc[0]
    min_price = df['Price'].min()
    row_of_minprice = df[df['Price'] == min_price]
    min_price_product = row_of_minprice['Product'].iloc[0]
    top_selling_category = df.groupby('Category')['Quantity'].sum().idxmax()
    top_selling_city = df.groupby('City')['Quantity'].max().idxmax()
    most_used_pay_mod = df.groupby('Payment_Mode')['Quantity'].max().idxmax()

    print('\nBuisness Insight\n')
    print(f'\nTotal Revnue is {revenue}\n')
    print(f'\nTotal Quantity is {quantity}\n')
    print(f'\nThe average value of order is {avg_order}\n')
    print(f'\nThe highest sale of orders is recorded as {highest_sale}\n')
    print(f'\nthe lowest sale of orders is recoreded as {lowest_sale}\n')
    print(f'\nThe Product which is most explensive is {most_exp_product}\n')
    print(f'\ncheapest product is {min_price_product}\n')
    print(f'\nthe most selled category {top_selling_category}\n')
    print(f'\n The most selled city is {top_selling_city}\n')
    print(f'\n The most used paymode is {most_used_pay_mod}\n')