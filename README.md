# Simple receipt merger
Append images of receipts to the end of a pdf file. For example, a receipt form with images of receipts on the following pages. Great if your accounting agency charges you per file uploaded.

## Usage
For stable usage, it is important that you structure your files correctly. Organize a set of receipts and their respective refund form in a separate folder. For example,
```
~/refunds
├── jan25
│   ├── receipts/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── img3.jpg
│   └── refusjonsskjema.pdf
├── feb25
│   ├── receipts/
│   │   ├── img1.jpg
│   │   └── img2.jpg
│   └── refusjonsskjema.pdf
```

### Functions
```python
merge_receipts(parent_dir, img_dir, regex_str)
"""Merges images of rececipts in img_dir with refund form, matched with
regex_str in parent_dir"""
```


## Requirements
To install requirements, do `pip install --upgrade requirements.txt` or `uv add requirements.txt`
- pypdf
- Pillow

## To do
- Add another script, that takes a relative parent directory in cli instead, for uber fast usage
- Structure project for build
- Make Qt app for newbies
