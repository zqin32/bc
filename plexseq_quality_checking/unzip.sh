#!/bin/sh

for i in *.gz
do 
	gunzip $i
done

