import src.merge_receipts as rmerge
import os

"""
Example: 
Refusjonsskjema is stored in C:/users/joe/Documents/refusjoner/februar/\
Images of receipts are stored in februar/kvitteringer/\

Then,
parent_dir = 'C:/users/joe/Documents/refusjoner/februar/'
img_dir = 'kvitteringer/'
"""

REGEX_STRING = r"(?i)refusjonsskjema"

# Change these two
parent_dir = "ENTER REFUND FORM DIRECTORY/PATH HERE"
img_dir = "ENTER IMAGE DIRECTORY/PATH HERE"

parent_dir = os.path.abspath(parent_dir)
rmerge.merge_receipts(parent_dir, img_dir, REGEX_STRING) 
