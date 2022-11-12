# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:19:38 2022

@author: black
"""

import os

dir_containing_file = r'\Users\black\Python and Tableau\Data'

#change the directory containing file

os.chdir(dir_containing_file)

file_name = 'transaction.csv'
with open(file_name, 'r', encoding='utf-8') as f:
    lines = f.readline()
    
    print(lines)
    
import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';' )

#summary of the datat
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePertTransaction = NumberofItemsPurchased*SellingPricePerItem

#cost per transaction column calculation

#CostPerTransaction = CostperItem * NumberofItemPurchased
# variable = dataframe['column_name']

CostPerItem =data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit caluclation = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales -Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding Markup
roundmarkup = round(data['Markup'], 2)
data['MarkUp'] = round(data['Markup'], 2)

#change column type
day = data['Day'].astype(str)

year = data['Year'].astype(str)

my_date = day+'-'+data['Month']+'-'+year
data['date'] = my_date
#using iloc to view specific columns/rows
data.iloc[0] #view the row with index --0
data.iloc[0:3]

#Using split to solit the client keyword field
#new-var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Creating a new column for the split columns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LenghtOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LenghtOfContract'] = data['LenghtOfContract'].str.replace(']', '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new data set

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('value_inc_seasons.csv')

seasons = pd.read_csv('value_inc_seasons.csv', sep=';' )

# merging files: merg_df = pd.merge(df_old, df_new, on 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)


data = data.drop(['Year', 'Month'], axis = 1)

#Export into CSV

data.to_csv('ValueInc_cleaned.csv', index = False)


