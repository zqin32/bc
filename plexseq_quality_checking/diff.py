#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Zhen
"""

import argparse
import pysam as ps
import re
import sys
              
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
    s1_path = args.file1
    #65 SNPs from nature
    #s2_path = args.file2
    out_file=args.out
    
    s1 = read_tab(s1_path)
    #s2 = read_tab(s2_path)
    
    #sample id well match
    sample = s1
    #diff list
    #difflist = s2
    l = []
    #print(sample)
    count = 0
    with open(out_file, "w") as out:
       for i in sample:
         print(*i,end = "\n",file=out)
         print("\n",file=out)
         print("\n",file=out)
         #print("\n",end="",file=out)
#==============================================================================
#     
#     print(len(sample))
#     print(len(difflist))
#==============================================================================
#==============================================================================
#     for i in range(len(sample)):
#        if len(sample[i])>2:
#         a = sample[i][2].strip()
#         for j in range(len(difflist)):
#            b = difflist[j][0].strip()
#            if a == b:
#                string = sample[i][0]+"\t"+sample[i][1]
#                if string not in l:
#                  l.append(string)
#                else:
#                  count = count+1
#                  #print(string)
#                  
#     #print(count)
#     print(l)
#     with open(out_file, "w") as out:
#      print(*l,sep="\n",file=out)
#==============================================================================

    #print(*unique65,sep="\n")
    
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
    
    parser.add_argument('--file1',
                        help='sam path.',
                        type=str,
                        default='')

    
    parser.add_argument('--file2',
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

