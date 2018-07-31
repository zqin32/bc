#!/bin/sh

for i in copy/*.fastq.gz
do 
        skewer -q 30 ${i}
done

