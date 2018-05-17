# clipExtractor

### extract transcript page:line designations for use in editing synchronized video depositions in TrialDirector.

USAGE: 

`python clipExtractor.py <path to designation file>`

Given a plaintext file containing page:line designations in the format:

`###:## - ###:##`

This script will automatically print a TrialDirector .CCS file (Clip Creation Script), with each new line in the designation file signifying a seperate clip.

The CCS header identifying which transcript the script should operate on needs to be added to the top of the file after this script is run. Those headers look like something like this:

`!(Lastname, FirstName - Volume - Date)`

The CCS will not have any timing information, so clips must be manually QC'd.

Features to Add:
- generate CCS header from command line input
- option to write output to a file
- more robust error handling
- more acceptable designation formats
- custom clip naming conventions
- ability to designate multi-segment clips
- simple GUI


