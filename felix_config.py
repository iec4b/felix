#felix_config.py

#folder locations

#file locations

#variable definitions
##consider removing the text() function from the end and adding it in with code
##later. Better to maximize the pull from the xml by getting the entire element.

side_a_duration=  "/mets:mets/mets:amdSec/mets:techMD[5]/mets:mdWrap/mets:xmlData/amd:AUDIOMD/amd:audio_info/amd:duration/text()"

side_b_duration=  "/mets:mets/mets:amdSec/mets:techMD[6]/mets:mdWrap/mets:xmlData/amd:AUDIOMD/amd:audio_info/amd:duration/text()"

side_a_file_size= "/mets:mets/mets:amdSec/mets:techMD[5]/mets:mdWrap/mets:xmlData/amd:AUDIOMD/amd:file_data/amd:format_note/text()"

side_b_file_size= "/mets:mets/mets:amdSec/mets:techMD[6]/mets:mdWrap/mets:xmlData/amd:AUDIOMD/amd:file_data/amd:format_note/text()"

processing_notes= "/mets:mets/mets:amdSec/mets:digiprovMD/mets:mdWrap/mets:xmlData/mods:physicalDescription/mods:note/text()"

speed=            "/mets:mets/mets:amdSec/mets:sourceMD/mets:mdWrap/mets:xmlData/amd:AUDIOSRC/amd:physical_data/amd:speed/text()"

speed_note=       "/mets:mets/mets:amdSec/mets:sourceMD/mets:mdWrap/mets:xmlData/amd:AUDIOSRC/amd:physical_data/amd:speed_note/text()"

stock_brand=      "/mets:mets/mets:amdSec/mets:sourceMD/mets:mdWrap/mets:xmlData/amd:AUDIOSRC/amd:audio_info/amd:note[1]/text()"

track_format=     "/mets:mets/mets:amdSec/mets:sourceMD/mets:mdWrap/mets:xmlData/amd:AUDIOSRC/amd:physical_data/amd:track_format/text()"
#ISBD protocols