import src.merge_receipts as rmerge
import os

"""
Usage: Just place this wherever your refund form is, ensure there 
is a folder called receipts, and then run the script
"""

# Change these two
parent_dir = os.path.dirname(os.path.realpath(__file__))
img_dir = "receipts/"

parent_dir = os.path.abspath(parent_dir)
rmerge.merge_receipts(parent_dir, img_dir)
