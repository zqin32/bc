#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Zhen
"""

import argparse
import os
import pysam as ps
import re
import sys
import shutil
              
def read_space(input_filename):
    
    # Note: informally, 'with' statements are used for file reading and
    # writing, among other things.  They guarantee that the file is properly
    # closed regardless of whether the code block runs normally or throws
    # an exception.  The line below opens the file in read mode and creates
    # a file object.
    with open(input_filename, "r") as in_file: 
      arrays = [line.strip() for line in in_file]   
      s = []
      for line in arrays:
          line.strip()
          s.append(line) 
    return s

     
def read_tab(input_filename):
    
    # Note: informally, 'with' statements are used for file reading and
    # writing, among other things.  They guarantee that the file is properly
    # closed regardless of whether the code block runs normally or throws
    # an exception.  The line below opens the file in read mode and creates
    # a file object.
    with open(input_filename, "r") as in_file: 
      arrays = [line.strip() for line in in_file]   
      s = []
      for line in arrays:
          line.strip()
          s.append(line.split("\t")) 
    return s    
   
      
# This is the main function provided for you.
# You can write whatever codes outside the main function
# and call it inside to run.
def main(args):
    # Parse input arguments
    # It is generally good practice to validate the input arguments, e.g.,
    # verify that the input and output filenames are provided 
    
    #SNPs we have
    s1_path = args.folder
    s2_path = args.diff
    
    diffid = read_tab(s2_path)
    #65 SNPs from nature
    #s2_path = args.file2
    out_file=args.out
    l = []

    for root, dirs, files in os.walk(args.folder):
     for name in files:
        #print(name)
        for i in range (len(diffid)):
          id = diffid[i][0]
          if id in name:
              if diffid[i][1] in name:
                l.append(name)
                shutil.copy2(os.path.join(root, name), '/Users/Zhen/Desktop/copy/'+name)

    print(len(l))
    
#==============================================================================
#     for i in range(len(s2)):
#         if s2[i] not in new:
#             new.append(s2[i])
#     
#     print(len(new))
#     print(*new,sep="\n")
#==============================================================================
    
    
    
    
    
            
            
        

             
          

if __name__ == "__main__":
    # Note: this example shows named command line arguments.  See the argparse
    # documentation for positional arguments and other examples.
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('--folder',
                        help='folder path.',
                        type=str,
                        default='')

    
    parser.add_argument('--diff',
                        help='rsem path.',
                        type=str,
                        default='')
    
    parser.add_argument('--out',
                        help='out path.',
                        type=str,
                        default='')

    args = parser.parse_args()
    # Note: this simply calls the main function above, which we could have
    # given any name
    main(args)

