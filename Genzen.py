'''
    GenZen: Version 1.0:
        A Simple Bioinformatics Sequence Test Data Generator For Use
        With training Intelligent Motif Detection in One Pass Through
        Genomic Sequence Datum

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
________________________________________________________________________________

'''
import random, math

# welcome
print('\nGenZen: toy dna and rna pseuedosequence generator, v1.0\n'
      'Author: Jeremy Scott\nWe will generate 4 toy sequence sets for you.')

# name the output file that will be appended by [fwd | rev] and [dna | rna]
file_output_name = raw_input('\nName for output file set: ')
output_file1 = open(file_output_name+'_fwd_rna','w')

#occurence of base chars only appear once, no need to wast space
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

# not a start|stop triplet with 99.99%, P(start or stop inserted in middle)->.01% * 1/6
def check_non_start_stop(trip):
    if random.random()<.9999 and (trip == 'AUG' or trip == 'UGA' or trip == 'UAG' or trip == 'UAA'):
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

rt = 0 #running total (this is for line sanity in the file, adding \n)

# dictionary of genes
genes = {}

# populate gene types
for i in range(1,gene_type_count+1):

    #running total within the gene in case we don't add to set, can subtract
    # this from the running total, rt
    ct = 0

    # r is how many triplets we will randomly add to this concept
    r = random.randint(min_triplets,max_tripplets_one_gene)
    #print 'r: ' + str(r)
    # sequence we generate to add to genes dictionary
    seq = ""
    # generate one gene
    for j in range(1,int(r+1)):
        #random triplet to select
        t = random.randint(1,64)
        while not check_non_start_stop(t):
            t = random.randint(1, 64)
        #add jth triplet of type t to this gene : mutations added later
        seq += dict_triplet[t]

        rt += 3 # actually counting # rna bases, not triplets
        ct += 3
        if(rt % 60 == 0):
            seq += '\n' #60 chars per line/20 amino acids


    # prepend with AUG
    seq = 'AUG' + seq

    rt+=3
    ct+=3
    if (rt % 60 == 0):
        seq += '\n'  # 60 chars per line/20 amino acid

    #randomly select and append stop codon
    rstopn = random.randint(1,3)
    if rstopn == 1: seq = seq+'UGA'
    elif rstopn == 2: seq = seq+'UAG'
    else: seq = seq+'UAA'

    rt+=3
    ct+=3
    if (rt % 60 == 0):
        seq += '\n'  # 60 chars per line/20 amino acid

    # add gene to dictionary, ignoring it and decrementing count if not unique seq
    if seq not in genes:
        genes[i] = seq
    else:
        i -=1
        #remove ct from running total, for consististent line wrapping
        rt -= ct
        ct = 0;

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

#print rna_seq
output_file1.write(rna_seq)
output_file1.close()

output_file2 = open(file_output_name+'_rev_rna','w')

#generate reverse rna template of the generated 'forward' one
out = ''
rev_seq = rna_seq[::-1]
for c in rev_seq:
    if c == 'A': out += 'U'
    elif c == 'U': out += 'A'
    elif c == 'C': out += 'G'
    elif c == 'G': out += 'C'

output_file2.write(out)
output_file2.close()

dna_seq_fwd = ''
#make DNA version of fwd sequence
for c in rna_seq:
    if(c == U): dna_seq_fwd += T
    else: dna_seq_fwd += c

output_file3 = open(file_output_name+'_fwd_dna','w')
output_file3.write(dna_seq_fwd)
output_file3.close()

dna_seq_rev = ''

#make DNA version of rev sequence
for c in rev_seq:
    if(c == U): dna_seq_rev += T
    else: dna_seq_rev += c

output_file4 = open(file_output_name+'_rev_dna','w')
output_file4.write(dna_seq_rev)
output_file4.close()

