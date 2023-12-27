# fido_demo.py

import csv

# Define a function to return values based on the unique_id entered with felix_demo.py.

def search(unique_id):

# Set up empty lists for duration and size values to be populated later.

	duration_field_value = []
	size_field_value = []

# Run the search function using the prepared csv file, data_warehouse_demo.csv. 

	with open('data_warehouse_demo.csv', mode='r', encoding='utf-8-sig') as f:
		file_reader = csv.DictReader(f, delimiter=',')

    # Match values by comparing unique_id to the value in FullCallNumber.

		for row in file_reader:
			if row['FullCallNumber'] == unique_id:
				minutes = row['durationMinutes']
				seconds = row['durationSeconds']

        # The manipulations below alter duration and size formats to suit the MARC fields. Ideally, they should adhere to ISBD standards.
        
				fixed_seconds = seconds.zfill(2)
				duration = minutes+":"+fixed_seconds
				size = float(row['filesizeKB'])
				just_size = str(format(size, '.2f'))

        # Populate the empty lists defined above.

				duration_field_value.append(duration)
				size_field_value.append(just_size)

        # Define variables to be used below, in the fido.search() return array.
        
				processing_notes = "500  "+row['ProcessingNotes']
				field_524 = f"524 [your citation string] {unique_id}."
				field_852 = f"8528 [Location] ǂb [Sublocation or collection] ǂc [Shelving location] ǂh {unique_id} ǂx [nonpublic note, e.g. cataloger's initials]"
				folder_path = row['FolderPath']

# The following conditional applies if there is more than one file associated with the digitized audio, i.e. for a two-sided cassette tape.

	if len(duration_field_value)>1:
		field_300="300  2 mp3 files ("+duration_field_value[0]+" min., "+duration_field_value[1]+" min.) : ǂb sound"
		field_387="387  audio file ǂb MP3 ǂc "+size_field_value[0]+", "+size_field_value[1]+" KB ǂ2 rda"

    # Define the return array for a two-sided cassette tape.

		return(
			{
			'MARC300' : field_300, 
			'MARC387' : field_387, 
			'ProcessingNotes':processing_notes,
			'FolderPath' : './' + folder_path,
			'MARC524' : field_524,
			'MARC852' : field_852
			}
			)

# The following conditional applies if there is a single file associated with the digitized audio, i.e. for a cassette tape where one side is blank.

	if len(duration_field_value)==1:
		field_300="300  1 mp3 file ("+duration_field_value[0]+" min.) : ǂb sound"
		field_387="387  audio file ǂb MP3 ǂc "+size_field_value[0]+" KB ǂ2 rda"

    # Define the return array for a "one-sided" cassette tape.

		return(
			{
			'MARC300' : field_300, 
			'MARC387' : field_387, 
			'ProcessingNotes':processing_notes,
			'FolderPath' : './' + folder_path,
			'MARC524' : field_524,
			'MARC852' : field_852
			}
			)
