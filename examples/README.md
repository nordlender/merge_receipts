# Examples
**example_script.py** is meant to be edited for reuse, and is run with `python example_script.py`.

**example_cli.py** is run in the terminal and is run with arguments, `python example_cli.py ABSOLUTE_PARENT_DIR IMG_DIR`.

## General
**NOTE**: There is a constant `REGEX_STRING` defined in both scripts. Change this to match the name of your refund form, in my case, "refusjonsskjema". The `(?i)` flag makes it case insensitive.

Currently, this is set to `(?i)refusjonsskjema`, for my norwegian friends, meaning any file starting with refusjonsskjema will be put on the first page of the document.

For stable usage, it is important that you structure your files correctly. Organize a set of receipts and their respective refund form in a separate folder. For example,
```
~/refunds
├── jan25
│   ├── receipts/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── img3.jpg
│   └── refusjonsskjema_jan25.pdf
├── feb25
│   ├── receipts/
│   │   ├── img1.jpg
│   │   └── img2.jpg
│   └── refusjonsskjema_feb25.pdf
```
## In the CLI
Syntax:
```bash
python example_cli.py ABS_PARENT_DIR REL_CHILD_DIR
```

Example:
You've placed your refund form in the refunds folder below, and your receipt images in refunds/receipts/
```bash
    python example_cli.py /home/joeschmoe/Documents/refunds/ receipts/
```
Do `python example_cli.py --help` for some extra help

## As a script
1. Edit `example_script.py`, and change the variables `parent_dir` and `img_dir`
2. Run the script, `python example_script.py`
3. Celebrate
