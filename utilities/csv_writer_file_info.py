#csv_writer.py
'''A program to extract file sizes and durations from multiple metadata files encoded in xml.'''

import csv
import sys

directory = sys.argv[1]

#Create the blank csv file and initialize the csv module.
with open('file_info.csv', 'w') as csvout:
	csv = csv.writer(csvout)
	#create the list of files to extract data from
	exec(open("iterate.py").read())
	#initiate the file_info.py program, which loops through the files listed and extracts filesizes and durations, adding all of that information to a list of lists (lol)
	exec(open("file_info.py").read())
#	print(lol)
	#Add each list within the list of lists as a row in the csv file
	for row in lol:
		csv.writerow(row)
	



