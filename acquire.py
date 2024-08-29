import pandas as pd
import env
import seaborn as sns
import requests
import os

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_telco_data():
    query = '''
    Select *
    from customers JOIN contract_types USING(contract_type_id) JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
    JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id;
    '''
    return pd.read_sql(query, get_connection('telco_churn'))

