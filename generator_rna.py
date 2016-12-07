'''
    Jeremy Scott
    A11180142
    Final Python Project
___________________________________________________________________________
    generator_rna

        generate a convincing RNA sequence

        This is a tool for testing my fast rna motif discovery tool.
        rna sequences from randomly generated rna 'concepts' of random
        length and random frequency inserted randomly into the sequence
        always starting with a start codon AUG and randomly ending with
        a stop codon from {UGA, UAG, UAA}

        This program will also write a file which is the reverse
        compliment  of the forward strand (which is generated first).

        the term 'gene' in this generator refers to rna sequences that
        encode proteins.

        however the main tool will 'learn' the important triplets and
        sequences on its own, without hard coding any markers like
        stop and start at all
___________________________________________________________________________
Py Notes- time savers:
___________________________________________________________________________
function:

    def a_function(param1, param2, ...):
        #code

    a_var = a_function(param1, param2, ...)
___________________________________________________________________________
class:

    class ClassName(object):
        class_variable1
        class_variable2...
        def __init__(self,*args):
            self.args = args
        def __repr__(self):
            return "Something to represent the object as a string"
        def other_method(self,*args):
            # do something else
___________________________________________________________________________
dictionary:

    a_dictionary = {}
    a_dictionary.update({"key_name_is_the_index" : for_the_value_here)}
    a_dictionary.get("using_key_here_returns_value_stored"}
___________________________________________________________________________
random:

    random.randint(a,b) <- random integer inclusive
    random.choice(array or tuple...)
___________________________________________________________________________
tuples: immutable

    tup = (a,b,...)
    x , y , z = (A, B, C), also x , y , z = A, B, C (expanding a tuple)
___________________________________________________________________________
list:

    a_list = [a,b,...]
    a_list.append(c)
___________________________________________________________________________
Generator Notes:

    Will have have some dictionaries useful to the neural network that analyses
    the data, ie 'generator_rna.base' and 'generator_rna.tripplets_to_amino'
    which should work better on real sequences, this generator is so i can
    manage my time better, yes doing more work initially to save time
    later is always a good thing
___________________________________________________________________________

'''
import random, math, subprocess, os

# welcome, and name rna generation file to make
print('\nRNA sequence generator: v1.0\nAuthor: Jeremy Scott')
file_output_name = raw_input('\nName your output file:\n')
output_file = open(file_output_name,'w')

'''Lists'''
# rna nucleotides:  A | U | G | C, start and stop codons
base = ['A','U','G','C']
start_codon = 'AUG'
stop_codons = ['UGA,UAG,UAA']


'''Dictionaries'''
# Recall the letter code or full name of rna tripplet
tripplet_to_amino = {
    'AAA': ('Lysine', 'K'),
    'AAU': ('Asparagine', 'N'),
    'AAG': ('Lysine', 'K'),
    'AAC': ('Asparagine','N'),
    'AUA': ('Isolucine', 'I'),
    'AUU': ('Isolucine', 'I'),
    'AUG': ('START(Methionine)'),
    'AUC': ('Isolucine', 'I'),
    'AGA': ('Arginine', 'R'),
    'AGU': ('Serine', 'S'),
    'AGG': ('Arginine', 'R'),
    'AGC': ('Serine', 'S'),
    'ACA': ('Threonine', 'T'),
    'ACU': ('Threonine', 'T'),
    'ACG': ('Threonine', 'T'),
    'ACC': ('Threonine', 'T'),
    'UAA': ('STOP', 'X'),
    'UAU': ('Tyrosine', 'Y'),
    'UAG': ('STOP', 'X'),
    'UAC': ('Tyrosine', 'Y'),
    'UUA': ('Leucine', 'L'),
    'UUU': ('Phenylalanine', 'F'),
    'UUG': ('Leucine', 'L'),
    'UUC': ('Phenylalanine', 'F'),
    'UGA': ('STOP', 'X'),
    'UGU': ('Cysteine', 'C'),
    'UGG': ('Tryptophan', 'W'),
    'UGC': ('Cystein', 'C'),
    'UCA': ('Serine', 'S'),
    'UCU': ('Serine', 'S'),
    'UCG': ('Serine', 'S'),
    'UCC': ('Serine', 'S'),
    'GAA': ('Glutamic-acid', 'E'),
    'GAU': ('Aspartic-acid', 'B'),
    'GAG': ('Glutamic-acid', 'E'),
    'GAC': ('Aspartic-acid', 'B'),
    'GUA': ('Valine', 'V'),
    'GUU': ('Valine', 'V'),
    'GUG': ('Valine', 'V'),
    'GUC': ('Valine', 'V'),
    'GGA': ('Glycine', 'G'),
    'GGU': ('Glycine', 'G'),
    'GGG': ('Glycine', 'G'),
    'GGC': ('Glycine', 'G'),
    'GCA': ('Alanine', 'A'),
    'GCU': ('Alanine', 'A'),
    'GCG': ('Alanine', 'A'),
    'GCC': ('Alanine', 'A'),
    'CAA': ('Glutamine', 'Q'),
    'CAU': ('Histidine', 'H'),
    'CAG': ('Glutamine', 'Q'),
    'CAC': ('Histidine', 'H'),
    'CUA': ('Leucine', 'L'),
    'CUU': ('Leucine', 'L'),
    'CUG': ('Leucine', 'L'),
    'CUC': ('Leucine', 'L'),
    'CGA': ('Arginine', 'R'),
    'CGU': ('Arginine', 'R'),
    'CGG': ('Arginine', 'R'),
    'CGC': ('Arginine', 'R'),
    'CCA': ('Proline', 'P'),
    'CCU': ('Proline', 'P'),
    'CCG': ('Proline', 'P'),
    'CCC': ('Proline', 'P')
}

# 64 types of triplets, indexed 1 through 64 and populating loops
dict_triplet = {}
n = 0
for i in range(0,4):
    for j in range(0,4) :
        for k in range(0,4):
            n += 1
            dict_triplet[n] = ''+base[i]+base[j]+base[k]

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

print '\ntriplet_stop_threshold: ' + str(triplet_stop_threshold)

# running rna sequence length generated so far
rna_seq_triplet_length = 0;

#dictionary of genes
genes = {}

min_triplets = 1

max_tripplets_one_gene = int(0.02*triplet_stop_threshold)

for i in range(1,gene_type_count+1):
    # r is how many triplets we will randomly add to this concept
    r = random.randint(min_triplets,max_tripplets_one_gene)      # 5 percent of the threshold
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
        #27 line outputs
        seq += dict_triplet[t]

        #test-uncomment to see possible genes to show up
        #if(j % 27 == 0): seq += '\n'


    # prepend with AUG
    seq = 'AUG' + seq

    #randomly select and append stop codon
    rstopn = random.randint(1,3)
    if rstopn == 1: seq = seq+'UGA'
    elif rstopn == 2: seq = seq+'UAG'
    else: seq = seq+'UAA'

    # add gene to dictionary, ignoring it and decrementing count if not unique seq
    if seq not in genes: genes[i] = seq
    else: i -=1

def printGenes(G):
    for i in range(1,len(genes)):
        print genes[i]
#test - printGene shows all the potential rna protein sequences that could be encoded by these rna
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
    popper[i] = int(math.pow(len(genes[i])-2,1.618)) #this value is 'c' next, may increase power too
    print 'popper['+str(i)+'] = ' + str(popper[i])

# Begin random rna genome section creation
while rna_seq_triplet_length < triplet_stop_threshold:
    print 'rna_seq: ' + rna_seq
    #list for potential insertion next
    candidates = []

    #reduce all wait times
    for i in range(1,len(genes)):
        popper[i] -= 9
        if popper[i] <= 0:
            candidates.append(genes[i])

    # candidates exist, choose one, randomly, append rna_seq, and update running count
    if len(candidates) > 0:
        select = random.randint(1,len(candidates)+1)
        rna_seq += genes[select]
        rna_seq_triplet_length += len(genes[select])
        print 'appending gene' + genes[select]

        #if a candidate has been selected for insertion, follow it with a random


print rna_seq
output_file.write(rna_seq)

