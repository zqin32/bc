#!/bin/sh

for i in *.bam
do  
    echo $i
    bam-readcount -f /ua/zqin32/plexseq/hg38.fa -l region.txt $i > ${i}.txt
    echo "--------------------------"
done


