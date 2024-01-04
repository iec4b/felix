# direct_file_handling

## Branch goals

1. Eliminate the need for a data_warehouse.csv file altogether, and instead configure felix.py and fido.py to operate directly on sidecar or embedded metadata.
2. Explore a cache/shr folder system, where sidecar xml files are copied before they are handled. 
  - Should avoid accidental alterations to original source files.
  - Should speed up processing time by localizing all actions and files.
3. Create a config file that includes:
  - location of cache/shr folder
  - variable definitions based on XPath addresses of metadata
    - These variables can be used to populate MARC fields or other schemata
  - ISBD puncutation protocols to integrate when creating MARC fields
4. Explore the use of official metadata crosswalks.