import requests
import xlrd

example_url = 'http://www.excel-easy.com/examples/excel-files/fibonacci-sequence.xlsx'
r = requests.get(example_url)  # make an HTTP request

workbook = xlrd.open_workbook(file_contents=r.content)  # open workbook
worksheet = workbook.sheet_by_index(0)  # get first sheet
specific_row = worksheet.row(12)  # you can iterate over rows of a worksheet as well

print(specific_row)  # list of cells