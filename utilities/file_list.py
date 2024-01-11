#file_list.py
import xml.etree.ElementTree as ET
import sys
import os
import re

#exec(open("iterate.py").read())


lol = []
for child in output:

	#filename = child
	
	filepath = directory+"/"+child

	document = ET.parse(filepath)
	
	root = document.getroot()
	
	metadata = root.findall('{http://www.loc.gov/METS/}amdSec/{http://www.loc.gov/METS/}techMD/{http://www.loc.gov/METS/}mdWrap/{http://www.loc.gov/METS/}xmlData/{http://www.loc.gov/AMD/}AUDIOMD')
	for child in metadata:
		row = []
		row.append(filepath)
		item = child.attrib
		#if re.search('.+streaming.mp3', item['ID']):
		
		mp3s = re.findall('.+streaming.mp3', item['ID'])
		for side in mp3s:
			row.append(side)			
			lol.append(row)	