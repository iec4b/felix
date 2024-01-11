#csv_writer.py


import csv
import sys

directory = sys.argv[1]

with open('file_list.csv', 'w') as csvout:
	csv = csv.writer(csvout)

	exec(open("iterate.py").read())
	exec(open("file_list.py").read())
	print(lol)
	for row in lol:
		csv.writerow(row)
	



