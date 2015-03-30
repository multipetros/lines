#!/usr/bin/python
#
# lines.py - v1.0
# A line numbering program for text files
# Copyright (c) 2013, Petros Kyladitis
# This is free software distributed under the terms of FreeBSD license
#

import argparse

def numbering(fin, fout, delimiter, lzeros=True, verbose=False):
    #if no output file path, use input path and append "-line-numbered" to the filename
    if fout == "" :
        fout = fin + "-line-numbered"
        
    if verbose:
        print "Reading from: " + fin + " ..."
        
    #read lines from file an load them to a list   
    fp = open(fin, "r")
    lines = fp.readlines()
    fp.close()
    
    if lzeros:
        #compute the digits of list size to fill with leading zeros
        digits = len(str(len(lines)))
    else:
        digits = 0

    #line counter
    i = 0

    #add the number (formated with leading zeros and a space) at the start of each line
    for line in lines:
        lines[i] = str(i+1).zfill(digits) + delimiter + line
        i = i + 1
        
    if verbose:
        print str(len(lines)) + " lines processed"
        print "Writing to: " + fout + " ..."
        
    #write the list as line to the file
    fp = open(fout, "w")
    fp.writelines(lines)
    fp.close()

    if verbose:
        print "Done!"
    
def main():
    parser = argparse.ArgumentParser(description="lines v1.0 - A line numbering program for text files", epilog="(c) 2013, Petros Kyladitis. This is free software distributed under the terms of FreeBSD license. For updates and more info see at <http://www.multipetros.gr/>")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Verbose output")
    parser.add_argument("-l", "--no-leading-zeros", action="store_false", dest="lzeros", default=True, help="Don\'t add leading zeros")
    parser.add_argument("input", help="Input file path", metavar="INPUT_FILE")
    parser.add_argument("-o", "--output", default="", dest="output", help="Output file path (if not specified, the output filename is as the input, appended \'-line-numbered\' at the end)", metavar="OUTPUT_FILE")
    parser.add_argument("-d", "--delimeter", default=" ", dest="delimiter", help="Delimeter between line nubers and the begining character of each line (by default, used a space)", metavar="DELIMETER")
    args = parser.parse_args()
    try:
        numbering(args.input, args.output, args.delimiter, args.lzeros, args.verbose)
    except Exception as err:
        print(err)
        
if __name__ == "__main__":
    main()
