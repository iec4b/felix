# felix.py

# Import modules.
# "fido" is an external python file that handles retrieval of metadata from a
# prepared csv file.
# this program requires the "pyperclip" module. See https://pypi.python.org/pypi/pyperclip

import sys
import pyperclip
import fido
import subprocess


# Set up for system options and arguments. 
# I copied this basic parser code and the if/elif statements structure from
# https://realpython.com/python-command-line-arguments/#a-few-methods-for-parsing-python-command-line-arguments

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# If your unique identifier or call number adheres to a standard format, you
# can use the following optional variable to simplify the input so that only
# the unique element of the identifier need be entered as the argument. For
# example, if your call numbers use a format such as, "Box ##:##", replace
# [your string] with "Box", and then you will only need to enter the numerical
# component of the identifier, without "Box" each time. This saves time and
# typing.  unique_id =  "[your string] " + " ".join(arg for arg in args)
# Currently, the unique_id is set up to accept arguments as they are entered.

unique_id  = " ".join(arg for arg in args)
print(unique_id)

# Run the fido.search function on the unique_id. See the file fido.py. 

metadata = fido.search(unique_id)

# Display the duration information as a MARC 300 field, and copy it to the
# system's clipboard.

if "-d" in opts:
    print(metadata['MARC300'])
    pyperclip.copy(metadata['MARC300'])

# Display the size information as a MARC 387 field, and copy it to the system's
# clipboard.

elif "-s" in opts:
    print(metadata['MARC387'])
    pyperclip.copy(metadata['MARC387'])

# Display the processing notes as a MARC 500 field, and copy it to the system's
# clipboard.

elif "-p" in opts:
    print(metadata['ProcessingNotes'])
    pyperclip.copy(metadata['ProcessingNotes'])

# Display the citation information as a MARC 524 field, and copy it to the
# system's clipboard.

elif "-c" in opts:
     print(metadata['MARC524'])
     pyperclip.copy(metadata['MARC524'])

# Display the location information as a MARC 852 field, and copy it to the
# system's clipboard.

elif "-l" in opts:
     print(metadata['MARC852'])
     pyperclip.copy(metadata['MARC852'])

# Open images associated with the items using the default viewer. The current
# configuration opens only jpeg files ending in ".JPG", but this can be
# adjusted as desired by changing the subprocess.call command below.  

elif "-i" in opts:
	print(f"Opening images from {metadata['FolderPath']}.")
	subprocess.call(['open *.JPG'], cwd=metadata['FolderPath'], shell='TRUE')

# Open audio associated with the items using the default player. The current
# configuration opens only mp3 files ending in ".mp3", but this can be adjusted
# as desired by changing the subprocess.call command below.  

elif "-a" in opts:
	print(f"Opening audio from {metadata['FolderPath']}.")
	subprocess.call(['open *.mp3'], cwd=metadata['FolderPath'], shell='TRUE')

# Open audio associated with the items using vlc CLI. The current
# configuaration opens only mp3 files ending in ".mp3", but this can be
# adjusted as desired by changing the subprocess.call command below. Requires
# VLC CLI. The "--no-media-library" option avoids opening the VLC CLI with
# other files already queued. 

elif "-ak" in opts:
	print(f"Opening audio from {metadata['FolderPath']}.")
	subprocess.call(['vlc --no-media-library *mp3'], cwd=metadata['FolderPath'], shell='TRUE')

# Display the path to the items with the entered unique id, and copy it to the
# system's clipboard.

elif "-f" in opts:
	print(metadata['FolderPath'])
	pyperclip.copy(metadata['FolderPath'])

# Display felix.py usage instructions.

elif "-h" in opts:
    raise SystemExit(f"Usage: felix [-opt] [Your unique identifier]\n\t-d <display and copy to clipboard MARC300>\n\t-s <display and copy to clipboard MARC387>\n\t-p <display and copy to clipboard Processing Notes>\n\t-c <display and copy to clipboard MARC524>\n\t-l <display and copy to clipboard MARC852>\n\t-i <Open images in default viewer>\n\t-a <Play audio in default media player>\n\t-ak <Play audio in console, requires VLC CLI>\n\t-h <display this instructional message>")

# Displays the same usage instructions as for "-h", if anything invalid is entered as an option.

else: 
    raise SystemExit(f"Usage: felix [-opt] [Your unique identifier]\n\t-d <display and copy to clipboard MARC300>\n\t-s <display and copy to clipboard MARC387>\n\t-p <display and copy to clipboard Processing Notes>\n\t-c <display and copy to clipboard MARC524>\n\t-l <display and copy to clipboard MARC852>\n\t-i <Open images in default viewer>\n\t-a <Play audio in default media player>\n\t-ak <Play audio in console, requires VLC CLI>\n\t-h <display this instructional message>")
