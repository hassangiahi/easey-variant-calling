# easey-variant-calling 
genius.py is a free and easy pipline to variant discovery

# please download and install these files first:
python 2.7

fastqc

https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

trimmomatic Version 0.38

http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip

bwa aligner

sudo apt-get install bwa

# please install Requires.txt file on  ubuntu:
    bash Requires.txt


# usages

to find help:

    python genius.py -h
    

to quality control:

    python genius.py --t quality --f1 /mnt/nfs/share-drive/challenge/stage1/fq1.gz --f2 /mnt/nfs/share-drive/challenge/stage1/fq2.gz --d       output/

to trimming: 

    python genius.py --t trimming --f1  /mnt/nfs/share-drive/challenge/stage1/fq1.gz --f2 /mnt/nfs/share-drive/challenge/stage1/fq2.gz --     o1 fq1_trimmed.fastq --o2 fq2_trimmed.fastq --d output/

to refernce indexing: 

    python genius.py --t indexing --f1 reference/reference.fa
    
to mapping:

    python genius.py --t alignment --f1 reference/reference.fa --f2 /mnt/nfs/share-drive/challenge/stage1/fq1.gz --f3 /mnt/nfs/share-       drive/challenge/stage1/fq2.gz --o1 fq1.sai --o2 fq2.sai --o3 aligned.sam --o10 aligned.bam --d output/
    
to sorting: 

    python genius.py --t sorting --f1 NA_outputs/NA1.bam --f2 NA_outputs/NA2.bam --f3 NA_outputs/NA3.bam --f4 reference/reference.fa --     o1 NA1.sorted.bam --o2 NA2.sorted.bam --o3 NA3.sorted.bam --d NA_outputs/
    
to variant calling: 

    python genius.py --t variant --f1 reference/reference.fa --f2 NA_outputs/NA1.sorted.bam --o1 NA1.vcf  --d NA_outputs/


# ok ... you did it 
contact : hassangiahi@gmail.com
