# Simple receipt merger
Append images of receipts to the end of a pdf file. For example, a receipt form with images of receipts on the following pages. Great if your accounting agency charges you per file uploaded.

## Usage
**NOTE**: There is a constant `REGEX_STRING` defined on line 8 of `src/merge_receipts.py`. Change this to match the name of your refund form, in my case, "refusjonsskjema". The `(?i)` flag makes it case insensitive.

### In the CLI
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

### As a script
1. Edit `example_script.py`, and change the variables `parent_dir` and `img_dir`
2. Run the script, `python example_script.py`
3. Celebrate

## Requirements
To install requirements, do `pip install --upgrade requirements.txt` or `uv add requirements.txt`
- pypdf
- Pillow

## To do
- Add another script, that takes a relative parent directory in cli instead, for uber fast usage
- Structure project for build 
