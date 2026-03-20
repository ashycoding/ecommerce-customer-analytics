from data_cleaning import clean_data
from rfm import create_rfm

df = pd.read_csv('data.csv')

df = clean_data(df)
rfm = create_rfm(df)