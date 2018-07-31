#!/bin/sh

for i in *.bam
do 
    /Users/Zhen/anaconda/bin/EBV/RSEM_06_30_2017/RSEM-1.3.0/samtools-1.3/samtools sort -o /Users/Zhen/Desktop/mapped/${i}  $i
done


