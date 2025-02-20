import src.merge_receipts as rmerge
import sys
import os

if len(sys.argv) < 3 or len(sys.argv) > 3:
    if "--help" in sys.argv:
        print(
            "Error! No argument given.\
            \nsyntax: python cli_refusjon.py PARENT_FOLDER CHILD_IMG_FOLDER\
            \n\n Example: Refusjonsskjema is stored in C:/users/joe/Documents/refusjoner/februar/\
            \n Images of receipts are stored in refusjoner/februar/kvitteringer/\
            \n Then, run\
            \n python cli_refusjon.py C:/users/joe/Documents/refusjoner/februar/ images/"
        )
    else:
        print(
            "syntax: python cli_refusjon.py PARENT_FOLDER_PATH CHILD_IMG_FOLDER\
            \n For help, see\
            \n python example_cli.py --help"
        )
    exit()

parent_dir = os.path.abspath(sys.argv[1])
img_dir = sys.argv[2]
rmerge.merge_receipts(parent_dir, img_dir)
