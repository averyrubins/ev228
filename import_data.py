import numpy as np
import pandas as pd
# file_path = '/Users/averyrubins/data/ev228_data/'
# df = pd.read_csv(file_path + 'KRDU_temp_188708-202508.csv')

def fun_import_data(file_path, file_name, column_index, row_index):
    df = pd.read_csv(file_path + file_name)
    select_variable = df[column_index]
    select_data = select_variable[row_index]
    print(select_data)

fun_import_data('/Users/averyrubins/data/ev228_data/', 'KRDU_temp_188708-202508.csv', 'JAN', 118)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'AYW00090001_temp_195702-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'BR038014410_temp_189601-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'IN020100400_temp_189101-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'KSM00047108_temp_190710-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'ROE00108901_temp_188001-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'RSM00021432_temp_193601-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'SG000061641_temp_189906-202508.csv', 'JAN', 7)
fun_import_data('/Users/averyrubins/data/ev228_data/Practical4_Data/', 'USW00093009_temp_190801-202508.csv', 'JAN', 7)