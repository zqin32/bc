#!/bin/sh

for i in copy/*.fastq-trimmed.fastq
do 
        bwa aln hg38.fa ${i} > ${i}.sai
	bwa samse hg38.fa ${i}.sai $i > ${i}.sam
done

