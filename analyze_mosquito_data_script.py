import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

# read the data
data = pd.read_csv(filename)

print data.head()