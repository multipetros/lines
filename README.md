# lines.py - version 1.0
Copyright (c) 2013 - [Petros Kyladitis](http://www.multipetros.gr/)

---

## Description
A line numbering program for text files.  
It have Command Line Interface, using the GNU style for parameters.

## Usage
`lines.exe [-h] [-v] [-l] [-o OUTPUT_FILE] [-d DELIMETER] INPUT_FILE`

## Manual
Counting text file numbers and create a new one, with the lines numbered at the begining of each line. Supports custom delimiter, no leading zeros from line number. 

### Positional arguments
* `INPUT_FILE`
  => Input file path

### Optional arguments
* `-h`, `--help`
  => show this help message and exit

* `-v`, `--verbose`
  => Verbose output

* `-l`, `--no-leading-zeros`
  =>Don't add leading zeros

* `-o OUTPUT_FILE`, `--output OUTPUT_FILE`
  => Output file path (if not specified, the output filename is as the input, appended '-line-numbered the end)

* `-d DELIMETER`, `--delimeter DELIMETER`
  => Delimeter between line nubers and the begining character of each line (by default, used a space)


## Lisence
This program is free software distributed under the FreeBSD,
for license details see at 'LICENSE' file, distributed with
this program, or see at <http://www.multipetros.gr/freebsd-license/>.