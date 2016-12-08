'''
    GenZen: Version 1.0:
        A Simple Bioinformatics Sequence Test Data Generator For Use
        With training Intelligent Motif Detection, see pcsd.py

                        Author: Jeremy Scott
                        PID :    A11180142
                        Final Python Project
                        UCSD Fall 2016
                        CSE 180

    Genzen.py:
             Generates  toy dna and  rna pseudodata for testing
             a separate  module, (pcsd.py)'s, pattern learning.
             A Neural Network that can save the salient pattern
             features (sequence "concepts")

    Additional Notes
    1. Outputs forward and reverse strands on either psuedo DNA or RNA seq's
    2. Prepends every 'gene' with AUG
    3. Appends evere 'gene' with a Stop codon
    4. Inserts random noise triplets between genes
    5. Attempts to control dynamic probability of length effect on frequency
    6. Start codons may appear in the middle of genes (because they do),
       but just code for methionine
________________________________________________________________________________

'''
import random, math

# welcome
print('\nGenZen: toy dna and rna pseuedosequence generator, v1.0\n'
      'Author: Jeremy Scott\nWe will generate 4 toy sequence sets for you.')

# name the output file that will be appended by [fwd | rev] and [dna | rna]
file_output_name = raw_input('\nName for output file set: ')
output_file1 = open(file_output_name+'_fwd_rna','w')

#occurence of base chars only appear once
A = 'A'
T = 'T'
U = 'U'
C = 'C'
G = 'G'

#useful refs
base_rna = [A,U,C,G]
codonStartRNA   = A + U + G
stop_codons_rna = [U+G+A,U+A+G,U+A+A]

# we'll just convert rna sequence to dna sequences at the end of the program


# 64 types of triplets, indexed 1 through 64 and populating loops
dict_triplet = {}
n = 0
for i in range(0,4):
    for j in range(0,4) :
        for k in range(0,4):
            n += 1
            dict_triplet[n] = base_rna[i]+""+base_rna[j]+""+base_rna[k]

# not a stop triplet with 99.99%, <account for possible mutation>
# P(stop inserted in middle)->.01% * 3/64
def check_non_stop(trip):
    if random.random()<.9999 and (trip == U+G+A or trip ==
        U+A+G or trip == U+A+A):
        return False
    return True

# random number of types of genes
gene_type_count = random.randint(50, 500)

#min and max triplets allowed per gene
min_triplet_gene = 1
max_triplet_gene = 50

#genome range of length in terms of number of triplets
min_genome_triplet_len = 5000
max_genome_triplet_len = 50000

# threshold for entire sequence in terms of number of triplets
triplet_stop_threshold = random.randint(min_genome_triplet_len,max_genome_triplet_len)

#print '\ntriplet_stop_threshold: ' + str(triplet_stop_threshold)

# running rna sequence length generated so far
rna_seq_triplet_length = 0;

min_triplets = 1

max_tripplets_one_gene = int(0.02*triplet_stop_threshold)

# dictionary of genes
genes = {}

# populate gene types
for i in range(1,gene_type_count+1):

    # r is how many triplets we will randomly add to this concept
    r = random.randint(min_triplets,max_tripplets_one_gene)

    # sequence we generate to add to genes dictionary
    seq = ""

    # generate one gene
    for j in range(1,int(r+1)):
        #random triplet to select
        t = random.randint(1,64)
        while not check_non_stop(t):
            t = random.randint(1, 64)
        #add jth triplet of type t to this gene : mutations added later
        seq += dict_triplet[t]

    # prepend with AUG
    seq = A+U+G + seq

    #randomly select and append stop codon
    rstopn = random.randint(1,3)
    if rstopn == 1: seq = seq+U+G+A
    elif rstopn == 2: seq = seq+U+A+G
    else: seq = seq+U+A+A

    # add gene to dictionary, ignoring it and decrementing count if not unique seq
    if seq not in genes:
        genes[i] = seq

def printGenes(G):
    for i in range(1,len(genes)):
        print genes[i]
#test - printGene shows all the potential sequences that could be
# encoded by these rna
#printGenes(genes)


'''rna sequence to create'''
rna_seq = ""

'''
    popper: a multi-'time-remaining' buffer.
    when full, popcorn pops, out comes a sequence
        each gene starts with a number equal to its length, we'll decrease the count
        of all genes by 9 at each time step. any gene's count that goes
        below zero goes into a candidate list where one is randomly selected
        to be inserted into the rna genome.  these counts are reset to their own
        length, causing small sequences to be chosen more often and large sequences to
        be chosen more infrequently, to make this work even better well raise each length
        by a power of 1.618 - for example a sequence of 10^1.618 ~ 41 and 100^1.618 ~ 1721
        notice the count raises by a factor of about 4 for the small sequence, but a
        factor of over 17 for the large sequence, I assume longer sequences should repeat
        themselves less often than shorter sequences

        popper = {key_for_gene: count_for_gene}
'''
popper = {}
# give all poppers their wait times for a chance at insertion
for i in range(1,len(genes)):
    popper[i] = int(math.pow(len(genes[i])-2,1.618)) #this value is 'c' next,
    # may increase power too
    #print 'popper['+str(i)+'] = ' + str(popper[i])

# Begin random rna genome section creation
while rna_seq_triplet_length < triplet_stop_threshold:
   # print 'rna_seq: ' + rna_seq
    #list for potential insertion next
    candidates = []

    #reduce all wait times
    for i in range(1,len(genes)):
        popper[i] -= 9
        if popper[i] <= 0:
            candidates.append(genes[i])

    # candidates exist, choose one, randomly, append rna_seq, and update running
    # count
    if len(candidates) > 0:
        select = random.randint(1,len(candidates)+1)
        rna_seq += genes[select]
        rna_seq_triplet_length += len(genes[select])
        #print 'appending gene' + genes[select]

        # if a candidate has been selected for insertion, follow it with a
        # random amount of nucleotide sequences, sometimes
        rand1 = random.randint(0,1)
        rand2 = rand1 * random.randint(0, 3)
        rand3 = rand2 * random.randint(0,5)
        # it's %3 = 0
        rand = rand3 * 3
        for i in range(0,rand):
            sel = random.randint(0,3)
            rna_seq += base_rna[sel]

def sanifyOutput(outFile):
    withCR = ''
    for i in range(1,len(outFile)-1):
        withCR += outFile[i-1]
        if(i%60 ==0): withCR += '\n'
    return withCR

#print rna_seq
output_file1.write(sanifyOutput(rna_seq))
output_file1.close()

output_file2 = open(file_output_name+'_rev_rna','w')

#generate reverse rna template of the generated 'forward' one
out = ''
rev_seq = rna_seq[::-1]
for c in rev_seq:
    if c == A: out += U
    elif c == U: out += A
    elif c == C: out += G
    elif c == G: out += C

output_file2.write(sanifyOutput(out))
output_file2.close()

dna_seq_fwd = ''
#make DNA version of fwd sequence
for c in rna_seq:
    if(c == U): dna_seq_fwd += T
    else: dna_seq_fwd += c

output_file3 = open(file_output_name+'_fwd_dna','w')
output_file3.write(sanifyOutput(dna_seq_fwd))
output_file3.close()

dna_seq_rev = ''

#make DNA version of rev sequence
for c in rev_seq:
    if(c == U): dna_seq_rev += T
    else: dna_seq_rev += c

output_file4 = open(file_output_name+'_rev_dna','w')
output_file4.write(sanifyOutput(dna_seq_rev))
output_file4.close()

