# extract-quickmemo
Extract LG quickmemo app data to .txt files

I found myself wanting to transfer my notes from quickmemo to another app.

Unfortunately I couldn't find a way of extracting that data cleanly from the app, so I wrote this.


# Install

requires: Python (probably works with 2.7, but I haven't tested it)


if git: *git clone https://github.com/rBrenick/extract-quickmemo*


if manual: download zip and put in some folder


# How To Use

1. Open the app and export the notes.

![export note 1](docs/quickmemo_export.png)
![export note 2](docs/quickmemo_export_as.png)


2. Get them to a computer somehow.

3. Put them in the 'quickmemo_lqm_files' folder.

4. Open Command Line in the folder

5. Run this commmand: python extract_files.py

.txt files with the content should be output into *extract_quickmemo\quickmemo_output*