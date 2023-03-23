import pandas as pd
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt


user_input = input("Enter a value: 1)Data analysis 2)Text manipulation 3)File conversion ")

if user_input == "1":
	doc = input("Enter the path to csv file contains the values to analyse ")
	valuecount = int(input("Enter approximate maximum number of values inside csv file "))
	# read data from a CSV file
	data = pd.read_csv(doc)
	
	# print the first few rows of the data
	print(data.head(valuecount))
	
	# calculate some basic statistics on the data
	print("Mean of column 'value':", data["value"].mean())
	print("Median of column 'value':", data["value"].median())
	print("Standard deviation of column 'value':", data["value"].std())
	
	# plot a histogram of the 'value' column
	data["value"].plot.hist()
	
	# Set plot title and axis labels
	plt.title("Histogram of Value Column")
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	
	# Show the plot
	plt.show()
    

elif user_input == "2":
    text = input("Enter some text ")
    
    print("Length:", len(text))

    
    print("Uppercase:", text.upper())

    
    print("Lowercase:", text.lower())

    adv = input("Do you need more text manipulations press yes or no ")
    if adv == "y":
        char = input("Enter a character to count: ")
        count = text.count(char)
        print(f"Number of occurrences of '{char}': {count}")
        more = input("Do you need advanced text manipulations press yes or no ")
        if more == "y":
            old_substring = input("Enter the substring to replace: ")
            new_substring = input("Enter the replacement substring: ")
            new_text = text.replace(old_substring, new_substring)
            print("New text:", new_text)
elif user_input == "3":
	addfile = input("Give the file name including the path ")
	# Read Excel file into a pandas dataframe
	df = pd.read_excel(addfile)

	# Create a PDF object
	pdf = FPDF()
	pdf.add_page()

	# Set column width based on the number of columns in the dataframe
	col_width = pdf.w / float(len(df.columns))

	# Set font and font size
	pdf.set_font('Arial', size=10)

	# Add table headers
	for col in df.columns:
	    pdf.cell(col_width, 10, str(col), border=1)

	# Add table rows
	for row in df.values:
		for item in row:
        		pdf.cell(col_width, 10, str(item), border=1)
		pdf.ln()

	# Save the PDF file
	pdf.output('output.pdf', 'F')
	print("")
	print("File conversion completed and saved to Desktop")


else:
    print("You did not enter A, B, or C")