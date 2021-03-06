#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os


def parse_vcf():
    sep = "\t"
    vcf_file = ""
    print sys.argv
    with open(sys.argv[1],"r") as f:
        for i in xrange(0,5):
            f.readline()
        header = f.readline()
        vcf_file = f.readlines()

    genomes = header.split(sep)[9:len(header.split(sep))]
    num_genomes = len(genomes)
    print "header: ",header
    print "genomes: ", genomes
    temp = header.rstrip().split(sep)
    #header:
    #CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	EEE_Florida91-4697.fasta.ref	EEE_FL93-939.fasta	EEE_NJ-60.fasta
    line_len = len(vcf_file[0].split(sep))
    output = "parsnp\n"
    num_snp_groups = len(vcf_file)
    output += str(num_snp_groups)+"\n"

    for line in vcf_file:
        #print"line: ",line
        l = line.rstrip().split(sep)
        pos = l[1]
        surrounding_bases = l[2]
        ref = l[3]
        altbase = l[4]
        #loop genomes per linje og de som er = 1 lagrer vi til:
        #EEE_FL93-939.fasta	286	C	gb|EF151502.1|gi|119633046|Eastern	F
        for i, snp_present in enumerate(l[9:line_len]):
            filename = temp[9+i]
            alt_num = int(snp_present)
            if alt_num > 0:
                alt_bases = altbase.split(",")
                output += filename+sep+pos+sep+alt_bases[alt_num-1]+sep+surrounding_bases+"\n" # DON't add those who have similar as reference genome as that isnt a snp
                #if len(num_alts) > 1:
                 #   output += filename+sep+pos+sep+altbase+"\n" # DON't add those who have similar as reference genome as that isnt a snp
                #if len(num_alts) == 1:
                 #   output += filename+sep+pos+sep+altbase+"\n" # DON't add those who have similar as reference genome as that isnt a snp

            
            
        #1	286	AGTACCACTG.TATTTGCCCA	T	C	40	PASS	NA	GT	0	1	0

    with open(sys.argv[2]+"/parsnp_snps_sorted.tsv","w") as f:
        f.write(output)


if __name__ == '__main__':
    parse_vcf()
