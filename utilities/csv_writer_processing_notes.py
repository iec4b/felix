#csv_writer_processing_notes.py
'''Combination of modules to create a csv file that matches xml filenames (sidecar metadata files generated during digitization) with the processing notes contained therein.'''

import csv
import sys

directory = sys.argv[1]

#Create the csv file
with open('processing_notes.csv', 'w') as csvout:
	csv = csv.writer(csvout)
	#run the iterate.py script to generate the list of filenames
	exec(open("iterate.py").read())
	#run the processing_notes.py script to extract the processing notes from each of the files on the above-generated list and create a list of lists called 'lol' where each list within contains the filename and its extracted processing notes
	exec(open("processing_notes.py").read())
	#Create a csv file from the list of lists (described above)
	for row in lol:
		csv.writerow(row)




