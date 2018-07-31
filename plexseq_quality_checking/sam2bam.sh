#!/bin/sh

for i in *.sam
do 
    /Users/Zhen/anaconda/bin/EBV/RSEM_06_30_2017/RSEM-1.3.0/samtools-1.3/samtools view -Sb   $i  >  ${i}.bam
done


