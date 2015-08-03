# coding: utf-8
import sys
import os
import xlrd

prompt_conent = 'Please type in the table name you want to find: '
# py2exe只支持3.3以上版本，所以原始脚本做了版本判别：
if sys.version.startswith('3'):
    target_table = input(prompt_conent)
else:
    target_table = raw_input(prompt_conent)

print('Press CTRL + Z to quit')

failed_file = []
for file_name in os.listdir(os.getcwd()):
    if file_name.endswith('xlsx') or file_name.endswith('xlsm'):
        try:
            xls = xlrd.open_workbook('%s' % file_name, on_demand=True)
            sheet_names = xls.sheet_names()
            if target_table in sheet_names:
                print("\nPERFECT MATCH!  Find  %s  in  %s\n" % (target_table, file_name))
            else:
                for table_name in sheet_names:
                    if target_table in table_name and target_table != table_name:
                        print("incomplete match, keyword is %s, find  %s  in  %s" % \
                              (target_table, table_name, file_name))
        except:
            failed_file.append(file_name)

print('\nSearching Complete!')

print("\nFAILED IN READING THESE FILES:")
for file_name in failed_file:
    print(file_name)
