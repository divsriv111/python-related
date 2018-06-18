import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
a=0
b='as'
expenses = (
    ['flag',"ans"],
    [a,b]
   )

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
#worksheet.write(row, 0, 'Total')
#worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
