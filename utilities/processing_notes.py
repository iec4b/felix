#processing_notes.py

import xml.etree.ElementTree as ET
import sys
import os
#open a blank list, to be populated with lists. Each list in this list of lists will eventually be a row in a csv file when this script gets called by the csv_writer program.
lol = []
#loop through the child elements of 'output', which is the result of the iterate.py script. That script creates a list of filenames corresponding to each xml file that needs to be parsed.
for child in output:
	#create a blank list which will become a list within the above list of lists.
	row = []
	#add the child element of 'output', which is the name of the xml file about to be parsed.
	row.append(child)
	#this definition creates a more complete filepath for each of the xml files to be parsed so that the following code can find them.
	filepath = directory+"/"+child
	#run ElementTree on the xml file at each of the predefined paths.
	document = ET.parse(filepath)
	#Create a root map of the xml.
	root = document.getroot()
	#pinpoint the physical metadata elements within the xml.
	phys_metadata = root.findall('{http://www.loc.gov/METS/}amdSec/{http://www.loc.gov/METS/}digiprovMD/{http://www.loc.gov/METS/}mdWrap/{http://www.loc.gov/METS/}xmlData')
	#loop down through the children of the metadata parent elements until the one containing the processing notes.
	for child in phys_metadata:
		for gchild in child:
			for ggchild in gchild:
				#the following conditional narrows the focus to the needed metadata.
				if ggchild.tag == '{http://www.loc.gov/mods/v3}note':
					#add the processing notes metadata text to the row list.
					row.append(ggchild.text)
					#add that row list to the list of lists 'lol'
					lol.append(row)