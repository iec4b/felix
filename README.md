# felix
 **felix,** the cataloger's friend.

## Introduction

**felix** is a command line tool that assists catalogers who work with digitized
assets. It streamlines the process of reviewing digital assets, such as audio
and image files. It also parses metadata and generates MARC fields, which can be
copied directly into OCLC Connexion.

**felix** works with a separate module, called fido.py. Just like their namesakes,
fido.py will fetch files and metadata, and **felix** will hunt for something
specific. All commands are performed through *felix,* while fido.py works
behind the scenes. Let **felix** climb around the data from your xml trees and
folder hierarchies, and you can focus on other things.


## Using **felix**

```
Usage: felix [-opt] [Your unique identifier]
	-d <display and copy to clipboard MARC300>
	-s <display and copy to clipboard MARC387>
	-p <display and copy to clipboard Processing Notes>
	-c <display and copy to clipboard MARC524>
	-l <display and copy to clipboard MARC852>
	-i <Open images in default viewer>
	-a <Play audio in default media player>
	-ak <Play audio in console, requires VLC CLI>
	-h <display this instructional message>
```

The data_warehouse.csv file will need to be pre-populated with metadata
for **felix** to work properly. This can be done manually, or, more ideally,
using code. **felix** is best applied in medium or high-volume contexts, where
large quantities of files and their attendant metadata must be managed. For
example, if the digitization process yields sidecar metadata xml files in a
standard format, a script can be written to transfer information from those
individual files to data_warehouse.csv file. Note that as it is currently
configured, **felix** only draws on some of the csv columns
(durationMinutes, durationSeconds, filesizeKB, ProcessingNotes, and
FolderPath). Like everything in this repository, the data_warehouse.csv file
should be treated as an inspiration, not a final draft. These tools will need
to be customized to your needs.


## Demo

Included along with the basic felix.py, fido.py, and data_warehouse.csv files
are a series of demo files, all appended with the string, "demo". They are
designed to be used with the folder called "sample_repository_foldername",
which is a skeletal version of of the sort of folder trees **felix** can climb.
Imagine it with the same basic structure, but populated with hundreds or
thousands more folders and multimedia files, along with sidecard metadata files
or whatever else your digitizer provides (e.g., sidecard metadata files,
high-quality versions meant only for internal use or preservation, etc.) 

Feel free to take **felix** for a spin by using the demo files.

## Future steps

**felix** is a work in progress. As it is applied in different contexts, it will
evolve. Here is a vision for near-term improvements:

1. Reduce the amount of hard-coding for MARC fields. 
	- A more dynamic version
		would allow for more customization on the fly, perhaps by incorporating
		[pymarc](https://pypi.org/project/pymarc/).
2. Improve parsing of system arguments and options for security and error-proofing.
3. Include some scripts in the repository for transferring metadata from common schemas to the data_warehouse.csv file.
4. Eliminate the need for a data_warehouse.csv file altogether, and instead configure felix.py and fido.py to operate directly on sidecar or embedded metadata. 

## Dependencies

In addition to the custom-made fido.py, **felix** requires the following modules:

- pyperclip (https://pypi.org/project/pyperclip/)
- subprocess (https://docs.python.org/3/library/subprocess.html)
- csv (https://docs.python.org/3/library/csv.html)
- sys (https://docs.python.org/3/library/sys.html)

***
## References

For more information on MARC, see the [OCLC guide](https://www.oclc.org/bibformats/en.html) or the [documentation](https://www.loc.gov/marc/) 
provided by the Library of Congress.

**felix** was designed to parse and integrate metadata according to METS, MODS, MARC, and RDA.

## Attributions

### Sample_id_a_1 assets:

- 'sample_id_a_1_asset_front.JPG' was originally called
	['Cassette-tape_8192.jpg'](https://commons.wikimedia.org/wiki/File:Cassette-tape_8192.jpg), posted by Wwongbc, CC0, via Wikimedia Commons
- 'sample_id_a_1_side_a_streaming.ogg' was originally called 
	['Inkjet printer on and off.ogg'](https://commons.wikimedia.org/wiki/File:Inkjet_printer_on_and_off.ogg), posted by stephan, Public domain, via Wikimedia Commons

### Sample_id_a_2 assets:

- 'sample_id_a_2_asset_front_and_back.JPG' was originally called 
	['Compact_audio_cassette_4.jpg'](https://commons.wikimedia.org/wiki/File:Compact_audio_cassette_4.jpg), posted by Orion 8, Public domain, via Wikimedia Commons

- 'sample_id_a_2_side_a_streaming.ogg' was originally called 
	[Typing fast.ogg](https://commons.wikimedia.org/wiki/File:Typing_fast.ogg), posted by stephan, Public domain, via Wikimedia Commons

- 'sample_id_a_2_side_b_streaming.ogg' was originally called 
	[Typing hunt and peck.ogg](https://commons.wikimedia.org/wiki/File:Typing_hunt_and_peck.ogg), posted by teto_yasha, Public domain, via Wikimedia Commons
