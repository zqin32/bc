# bc
breast cancer project scripts and documents
#############################
1. Guildeline in processing Plexseq and Mayo data
2. Plexseq and Mayo overlap comparison
#############################
1. All the processing details, references, and explaination of concepts can be found in "mayo&plexseq_data_process_guideline.pdf"
	All the scripts or program that are used for processing can be found in "plexseq_quality_checking/" folder

2. For the first 213 SNPs that Mayo and Plexseq sequenced separately, there are 13 SNP overlaps. 
  "Mayo_QC_and_Mayo_Plexseq_comparison.pdf" summarized the comparison of the 13 SNPs between Mayo's and Plexseq's results.
  We noticed that Mayo has a much lower threshold for a call for SNP's genotype, and the total reads for each SNP from Mayo are
  also lower. For instance, if a sample has 5 reads of A in total, Mayo make a call of A at this SNP position for this sample. However, 
  Plexseq will only make a call of A if the total reads number reaches 20.
  
