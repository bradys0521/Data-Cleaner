import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


#data_path = 'names.csv'
#data_name = ''

def data_cleaning_master(data_path):



    print("Thank you for giving the details")

    sec = random.randint(1, 5)
    print(f"Please wait while we retrieve your file. This may take {sec} seconds")
    time.sleep(sec)


    # checking if the path exists
    if not os.path.exists(data_path):
        print("Please enter correct path")
        # return
    else:
        #checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data_name = data_path.replace('.csv', '')
            data = pd.read_csv(data_path, encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data_name = data_path.replace('.xlsx', '')
            data = pd.read_excel(data_path)

        else:
            print('Unknown file type')
            #return

    #print delay message before printing the rows and columns
    sec = random.randint(1, 5)
    print(f'Please wait for {sec} seconds while we check the total number of rows and colummns')
    time.sleep(sec)

    #showing number of records
    print(f'The Dataset contains total rows: {data.shape[0]} \ntotal columns: {data.shape[1]}')

   
    #start cleaning

    sec = random.randint(1, 5)
    print(f'Please wait for {sec} seconds while we check the total duplicates')
    time.sleep(sec)

    #checking for duplicates
    duplicates = data.duplicated()
    total_duplicates = duplicates.sum()

    print(f'The Dataset contains total duplicates: {total_duplicates}')

    #print delay message before dealing with duplicates
    sec = random.randint(1, 5)
    print(f'Please wait for {sec} seconds while we remove the duplicates')
    time.sleep(sec)


    #saving the duplicate records
    if total_duplicates > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

    #deleting duplicates
    df = data.drop_duplicates()

    #print delay message before dealing with missing values
    sec = random.randint(1, 5)
    print(f'Please wait for {sec} seconds while we locate missing values')
    time.sleep(sec)


    #find missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_by_column = df.isnull().sum()

    print(f'The Dataset contains total missing values: {total_missing_values}')
    print(f'The Datasets missing values by column: \n{missing_value_by_column}')

    # dealing with missing values
    # fillna -- int and float columns
    # dropna -- any other object columns

    sec = random.randint(1, 5)
    print(f'Please wait for {sec} seconds while we remove fix the missing values')
    time.sleep(sec)


    columns = df.columns
    for col in columns:
        if df[col].dtype in (float, int):
            #filling missing number values with the mean of the column
            mean_value = df[col].mean()
            df[col] = df[col].fillna(mean_value)
        else:
            #dropping all of the rows with missing values in non-numeric columns
            df.dropna(subset=col, inplace=True)

    print(f"Congrats! The Dataset and is now cleaned!\nNumber of rows after cleaning: {df.shape[0]}\nNumber of columns after cleaning: {df.shape[1]}")

    #saving the cleaned dataset
    df.to_csv(f'{data_name}_cleaned.csv', index=None)

    print("Dataset has been saved!")


if __name__ == "__main__":
        
    print("Welcome to the Data Cleaning Master!")

    #ask path and file name
    data_path = input("Please enter dataset path: ")
        
    #call the master function
    data_cleaning_master(data_path)