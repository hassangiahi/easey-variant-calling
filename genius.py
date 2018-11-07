import sys
import optparse 
import os
import argparse

#############
# CONSTANTS #
#############
FASTQC = "/root/FastQC/./fastqc"
TRIMMOMATIC = "java -jar ~/Trimmomatic-0.38/trimmomatic-0.38.jar"
BWA = "/usr/bin/bwa"
SAM2COUNT = "sam2counts-master/sam2counts.py"
SAMTOOLS = "/usr/local/bin/samtools"
BCFTOOLS_mpileup = "/usr/local/bin/bcftools"
BCFTOOLS_calls = "/usr/local/bin/bcftools"
#################
# END CONSTANTS #
#################
class OptionParser(optparse.OptionParser):
    """
    Adding a method for required arguments.
    Taken from:
    http://www.python.org/doc/2.3/lib/optparse-extending-examples.html
    """
    def check_required(self, opt):
        option = self.get_option(opt)


# END CLASSES #
###############
 
########
# MAIN #	
########
def main():
    opt_parser = OptionParser(usage=
"usage : python %prog [options] ", version="%prog 1.0")
    
    opt_parser.add_option("--f1",
                          dest="input1",
                          type="string",
                          help="""file1 to be analysed [quality(fasta , fastq), trimming(fastq, fastq), alignment(fasta refrence), variant].""",
                          default=None)
    opt_parser.add_option("--f2",
                          dest="input2",
                          type="string",
                          help="""file2 to be analysed [quality(fasta , fastq), trimming(fasta , fastq) and alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--f3",
                          dest="input3",
                          type="string",
                          help="""file3 to be analysed [alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--f4",
                          dest="input4",
                          type="string",
                          help="""file4 to be analysed [alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--f5",
                          dest="input5",
                          type="string",
                          help="""file5 to be analysed [alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--f6",
                          dest="input6",
                          type="string",
                          help="""file6 to be analysed [alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--f7",
                          dest="input7",
                          type="string",
                          help="""file7 to be analysed [alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--f8",
                          dest="input8",
                          type="string",
                          help="""file8 to be analysed [alignment(fastq)].""",
                          default=None)
    opt_parser.add_option("--o1",
                          dest="output1",
                          type="string",
                          help="""Name of output1 [trimming(yourname.fastq), alignment(yourname.sai)] .""",
                          default=None)
    opt_parser.add_option("--o2",
                          dest="output2",
                          type="string",
                          help="""Name of output2[trimming(yourname.fastq), alignment(yourname.sai)].""",
                          default=None)
    opt_parser.add_option("--o3",
                          dest="output3",
                          type="string",
                          help="""Name of output3 [alignment(yourname.sam)].""",
                          default=None)
    opt_parser.add_option("--o4",
                          dest="output4",
                          type="string",
                          help="""Name of output4 [alignment(yourname.sai)].""",
                          default=None)
    opt_parser.add_option("--o5",
                          dest="output5",
                          type="string",
                          help="""Name of output5 [alignment(yourname.sai)].""",
                          default=None)
    opt_parser.add_option("--o6",
                          dest="output6",
                          type="string",
                          help="""Name of output6 [alignment(yourname.sam)].""",
                          default=None)
    opt_parser.add_option("--o7",
                          dest="output7",
                          type="string",
                          help="""Name of output7 [alignment(yourname.sai)].""",
                          default=None)
    opt_parser.add_option("--o8",
                          dest="output8",
                          type="string",
                          help="""Name of output8 [alignment(yourname.sai)].""",
                          default=None)
    opt_parser.add_option("--o9",
                          dest="output9",
                          type="string",
                          help="""Name of output9 [alignment(yourname.sam)].""",
                          default=None)
    opt_parser.add_option("--o10",
                          dest="output10",
                          type="string",
                          help="""Name of output10 .""",
                          default=None)
    opt_parser.add_option("--o11",
                          dest="output11",
                          type="string",
                          help="""Name of output11 .""",
                          default=None)
    opt_parser.add_option("--o12",
                          dest="output12",
                          type="string",
                          help="""Name of output12 .""",
                          default=None)
    opt_parser.add_option("--t",
                          dest="task",
                          type="choice",
                          choices=['quality', 'trimming', 'indexing', 'alignment', 'count','sorting', 'variant',],
                          help="""Type of analysis (quality, trimming, indexing, alignment , count , sorting, variant).""",
                          default=None)
    opt_parser.add_option("--d",
                          dest="output_directory",
                          type="string",
                          help="Directory of outputs. Def=\".\"",
                          default=".")
    print ("-------------------------------------------")
    print ("Quality Control usage : python genius.py --t quality --f1 <fastq file1> --f2 <fastq file2> --f3 <fastq file3> --d <output directory>")
    
    print ("-------------------------------------------")
    print (" Trimming usage : python genius.py --t trimming --f1 <fastq file1> --f2 <fastq file2> --o1 <output1.fastq> --o2 <output2.fastq> --d <output directory>")
    print ("-------------------------------------------")
    print (" Indexing usage : python genius.py --t indexing --f1 <fasta reference genome.fa>")
    print ("-------------------------------------------")
    print (" Alignment usage : python genius.py --t alignment --f1 <fasta reference genome.fa> --f2 <fastq file1> --f3 <fastq file2> --f4 <fastq file3> --f5 <fastq file5> --f6 <fastq file6> --f7 <fastq file7> --f8 <fastq file8> --o1 <output file1.sai> --o2 <output file2.sai> --o3 <output file3.sam> --o4 <output file4.sai> --o5 <output file5.sai> --o6 <output file6.sam> --o7 <output file7.sai> --o8 <output file8.sai> --o9 <output file9.sam> --o10 <output file3.bam --o11 <output file6.bam> --o12 <output file9.bam> --d <output directory>")
    print ("-------------------------------------------")
    print (" Sorting usage : python genius.py --t sorting --f1 <input file1.bam> --f2 <input file2.bam> --f3 <input file3.bam> --f4 <fasta reference genome.fa> --o1 <output1.sorted.bam> --o2 <output2.sorted.bam> --o3 <output3.sorted.bam> --d <output directory>")
    print ("-------------------------------------------")
    print (" Variant calling usage: python genius.py --t variant --f1 <fasta reference genome> --f2 <input file2.sorted.bam> --o1 <final output.vcf> --d <output directory>")
    print ("-------------------------------------------")
    print (" read count usage : python genius.py --t count --f1 <input file1.sam> --f2 <input file2.sam> --f3 <input file3.sam> --o1 <output file1.txt> --o2 <output file2.txt> --o3 <output file3.txt> --d <output directory>")
    print ("-------------------------------------------")

    (options, args) = opt_parser.parse_args()

    print (options)
    print (args)

    opt_parser.check_required("--f1")
    opt_parser.check_required("--f2")
    opt_parser.check_required("--f3")
    opt_parser.check_required("--f4")
    opt_parser.check_required("--f5")
    opt_parser.check_required("--f6")
    opt_parser.check_required("--f7")
    opt_parser.check_required("--f8")

    opt_parser.check_required("--o1")
    opt_parser.check_required("--o2")
    opt_parser.check_required("--o3")
    opt_parser.check_required("--o4")
    opt_parser.check_required("--o5")
    opt_parser.check_required("--o6")
    opt_parser.check_required("--o7")
    opt_parser.check_required("--o8")
    opt_parser.check_required("--o9")
    opt_parser.check_required("--o10")
    opt_parser.check_required("--o11")
    opt_parser.check_required("--o12")

    opt_parser.check_required("--t")
    opt_parser.check_required("--d")

    fastqc_out = formatDir(options.output_directory)
    fastq_in_file1 = options.input1
    fastq_in_file2 = options.input2
    fastq_in_file3 = options.input3
    fastq_in_file4 = options.input4
    fastq_in_file5 = options.input5
    fastq_in_file6 = options.input6
    fastq_in_file7 = options.input7
    fastq_in_file8 = options.input8

    output_file1 = options.output1
    output_file2 = options.output2
    output_file3 = options.output3
    output_file4 = options.output4
    output_file5 = options.output5
    output_file6 = options.output6
    output_file7 = options.output7
    output_file8 = options.output8
    output_file9 = options.output9
    output_file10 = options.output10
    output_file11 = options.output11
    output_file12 = options.output12

    task = options.task
    
    if task == 'quality':

        print ("********** quality control of ngs data**********")
        cmd = "%s -o %s -f fastq -t 2 %s %s %s %s %s %s %s %s" % (FASTQC, fastqc_out, fastq_in_file1, fastq_in_file2, fastq_in_file3, fastq_in_file4, fastq_in_file5, fastq_in_file6, fastq_in_file7, fastq_in_file8)




    elif task == 'trimming':
        print ("********** trimming of paired end data started **********")
        cmd = "%s PE %s %s /%s/%s /%s/file1_unpaire.fastq /%s/%s /%s/file2_unpaire.fastq" " LEADING:15 TRAILING:15 SLIDINGWINDOW:4:15 MINLEN:36  CROP:97 " % (TRIMMOMATIC, fastq_in_file1, fastq_in_file2, fastqc_out, output_file1,fastqc_out, fastqc_out, output_file2, fastqc_out)


    elif task == 'indexing':
        print ("**********indexing of ngs data**********")
        cmd = "%s index %s" % (BWA, fastq_in_file1)


    elif task == 'alignment':

        print ("********** alignment started **********")

        cmd = "%s aln -t 2 %s %s > /%s/%s" % (BWA, fastq_in_file1, fastq_in_file2, fastqc_out, output_file1)
        os.system(cmd)

        cmd = "%s aln -t 2 %s %s > /%s/%s" % (BWA, fastq_in_file1, fastq_in_file3, fastqc_out, output_file2)
        os.system(cmd)

        cmd = "%s sampe %s /%s/%s /%s/%s %s %s > /%s/%s" % (BWA, fastq_in_file1, fastqc_out, output_file1, fastqc_out, output_file2, fastq_in_file2, fastq_in_file3, fastqc_out, output_file3)
        os.system(cmd)

        cmd = "%s aln -t 2 %s %s > /%s/%s" % (BWA, fastq_in_file1, fastq_in_file4, fastqc_out, output_file4)
        os.system(cmd)

        cmd = "%s aln -t 2 %s %s > /%s/%s" % (BWA, fastq_in_file1, fastq_in_file5, fastqc_out, output_file5)
        os.system(cmd)

        cmd = "%s sampe %s /%s/%s /%s/%s %s %s > /%s/%s" % (BWA, fastq_in_file1, fastqc_out, output_file4, fastqc_out, output_file5, fastq_in_file4, fastq_in_file5, fastqc_out, output_file6)
        os.system(cmd)

        cmd = "%s aln -t 2 %s %s > /%s/%s" % (BWA, fastq_in_file1, fastq_in_file6, fastqc_out, output_file7)
        os.system(cmd)

        cmd = "%s aln -t 2 %s %s > /%s/%s" % (BWA, fastq_in_file1, fastq_in_file7, fastqc_out, output_file8)
        os.system(cmd)

        cmd = "%s sampe %s /%s/%s /%s/%s %s %s > /%s/%s" % (BWA, fastq_in_file1, fastqc_out, output_file7, fastqc_out, output_file8, fastq_in_file6, fastq_in_file7, fastqc_out, output_file9)
        os.system(cmd)

        cmd = "%s view -Sb /%s/%s > /%s/%s" % (SAMTOOLS, fastqc_out, output_file3, fastqc_out, output_file10)
        os.system(cmd)

        cmd = "%s view -Sb /%s/%s > /%s/%s" % (SAMTOOLS, fastqc_out, output_file6, fastqc_out, output_file11)
        os.system(cmd)

        cmd = "%s view -Sb /%s/%s > /%s/%s" % (SAMTOOLS, fastqc_out, output_file9, fastqc_out, output_file12)
        os.system(cmd)

    elif task == 'count':

        print ("********** counting of sam files by samtocount.py **********")
        
        cmd = "python %s -o /%s/%s.txt %s" % (SAM2COUNT, fastqc_out, output_file1 , fastq_in_file1)
        os.system(cmd)

        cmd = "python %s -o /%s/%s.txt %s" % (SAM2COUNT, fastqc_out, output_file2 , fastq_in_file2)
        os.system(cmd)

        cmd = "python %s -o /%s/%s.txt %s" % (SAM2COUNT, fastqc_out, output_file3 , fastq_in_file3)
        os.system(cmd)

    elif task == 'sorting':
        print ("********** sorting and indexing of ngs data **********")

        cmd = "%s sort %s > /%s/%s" % (SAMTOOLS, fastq_in_file1, fastqc_out, output_file1)
        os.system(cmd)

        cmd = "%s sort %s > /%s/%s" % (SAMTOOLS, fastq_in_file2, fastqc_out, output_file2)
        os.system(cmd)

        cmd = "%s sort %s > /%s/%s" % (SAMTOOLS, fastq_in_file3, fastqc_out, output_file3)
        os.system(cmd)

        cmd = "%s faidx %s" % (SAMTOOLS, fastq_in_file4)
        os.system(cmd)


    elif task == 'variant':
        print ("********** variant calling of ngs data **********")
        cmd = "%s mpileup -f %s %s | %s call -mv -Ov -o /%s/%s" % (BCFTOOLS_mpileup, fastq_in_file1, fastq_in_file2, BCFTOOLS_calls, fastqc_out, output_file1)

    else:
        print (""" please choose a valid type of analysis:
                   quality, trimming, indexing, alignment,
                   sorting or variant""")

    os.system(cmd)

    sys.exit(0)


def formatDir(i_dir):
    i_dir = os.path.realpath(i_dir)
    if i_dir.endswith("/"):
        i_dir = i_dir.rstrip("/")
    return i_dir

if __name__ == "__main__": main()