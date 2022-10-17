import requests
import bs4
import pandas as pd



# Make requests from webpage
url = 'https://www.digikey.in/en/products/filter/through-hole-resistors/53?s=N4IgTCBcDaIIwAYDWACATgUwM4EssBcB7NEAXQBoQBWKUAByjkrockQQF8Og'
result = requests.get(url)



# Creating soap object
soup = bs4.BeautifulSoup(result.text,'lxml')



# Searching div tags having maincounter-number class
cases = soup.find_all('div' ,class_= 'MuiGrid-root jss259 MuiGrid-item')
print(result.raw)



# List to store number of cases
# data = []

# # Find the span and get data from it
# for i in cases:
#     print(i)
#     span = i.find('jss262 jss246')
#     data.append(span.string)

# # Display number of cases
# print(data)



# # Creating dataframe
# df = pd.DataFrame({"CoronaData": data})

# # Naming the columns
# df.index = ['TotalCases', ' Deaths', 'Recovered']



# # Exporting data into Excel
# df.to_csv('Corona_Data.csv')
print("yes")