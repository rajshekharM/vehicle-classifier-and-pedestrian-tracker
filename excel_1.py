import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': licPlate.strChars})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/home/chinmay/Automation/pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

#def export_val(val):
#		df = pd.DataFrame({'Data': val.strChars})

# Create a Pandas Excel writer using XlsxWriter as the engine.
#		writer = pd.ExcelWriter('/home/chinmay/Automation/pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
#		df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
#		writer.save()
		
