'''
    PCFPD: Version 1.0:
        A one pass analyzer through genomic sequences to identify all
        interesting candidates for motifs and proteins

                        Author: Jeremy Scott
                        PID :    A11180142
                        Final Python Project
                        UCSD Fall 2016
                        CSE 180

    pcfpd.py:
             treats novel stimulus as a concept able to learn to expect
             and link other concepts.  concepts grow and large concepts
             that are similar to each other and within a small tolerance
             are of the same size are very interesting to bioinformaticians


workspace just:

Too dark for paper thinking so i'm experimenting here

A   A
T   At   aT
A   At   aTa  tA
T   <At  aTa> [tAt aT]
A   At   aTa  *tATa (at)A
T   <At  aTa> tATa [(at)At aT] *dont care that (at)precedes At
A   At   aTa  tATa *(at)ATa* (at)A
A   At   aTa  tATa  (at)ATa  (at)Aa aA
T   <At  aTa> tATa  (at)ATa  (at)Aa [aAt aT]
T   At   aTa  tATa  (at)ATa  (at)Aa *aATt* (at)T
A   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tA
A   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tAa   aA
T   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tAa  [aAt aT]
T   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tAa [*aATt* (at)T]
A   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tAa aATTa (att)A
T   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tAa aATTa [(att)At aT]
A   At   aTa  tATa  <(at)ATa  (at)Aa>  aATt  (at)Ta tAa aATTa [*(att)ATa* (at)A]
A   At   aTa  tATa  (at)ATa  (at)Aa  aATt  (at)Ta tAa aATTa (att)ATAa (ata)A

what have we learned?
that A, T, AT, ATT ATA are concepts
shit, not not TT, or A, keep thinking about it
ok should probably be checking first and lasts of concepts without worrying
about predecessors or followers

last letter is current concept not in history yet, 2nd to last: 'recent'
when C and R have been seen adjacently before, new C and R merge

Try new notation
A   A
T   A,  T
A   A,  T,  A
T   A,  T,  AT    Adjacent A and T before recent
A   A,  T,  AT, A
T   A,  T,  AT, AT
A   A,  T,  AT, AT, A
A   A,  T,  AT, AT, A, A
T   A,  T,  AT, AT, A, AT
T   A,  T,  AT, AT, A, AT, T
A   A,  T,  AT, AT, A, AT, T, A
A   A,  T,  AT, AT, A, AT, T, A, A
T   A,  T,  AT, AT, A, AT, T, AAT
T   A,  T,  AT, AT, A, AT, T, AAT, T
A   A,  T,  AT, AT, A, AT, T, AAT, T, A
T   A,  T,  AT, AT, A, AT, T, AAT, TAT
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, A
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, A, A
T   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT
T   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, T
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, T, A
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, T, A, A
T   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, TAAT
T   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, TAAT, T
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, TAAT, T, A
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, TAAT, T, A, A,
A   A,  T,  AT, AT, A, AT, T, AAT, TAT, AAT, TAAT, T, A, AA

*patterns are noticed by waveformity, not uniformity!
another variation
A:  A                   initial stim
A:  AA                  same as before, grows in length
A:  AAA                 same
B:  AAA, B              new stim, new concept!
A:  AAA, B, A           known stim, is it a new concept?
A:  AAA, B, AA
B:  AAA, B, AAB
A:  AAA, B, AAB, A
B:  AAA, B, AAB, AB
A:  AAA, B, AAB, ABA
B:  AAA, B, AAB, ABA, B
A:  AAA, B, AAB, ABA, BA
A:  AAA, B, AAB, ABA, BA, A  *Ahhh ok add this idea:  does C + recent fall
within + any other adjecent concats?
B:
B:
A:
A:
A:
B:
A:
B:
B:
B:
*idea:  have I ever seen this before?  if 2 is the same as one, yes, and put
them together, there should never be a C, C situation
2 steps:
    1: does this new concept match the recent concept (if exact size!)
        IE two identical/ adjacent concepts get grouped
    2: if not(1): have I ever seen
        - has the RECENT pattern appeared as the TAIL of a previous concept
          AND the CURRENT concept appeared as the HEAD of the concept
          following the previous match?


Cool that will work, so a new concept that mergest into recent concept, must
then look further back to see if it can be merged one more step back

or maybe
just check known concept list,



Pseudo, let
        n = new concept,
        r = most recent concept,
        k = known concept,
        p = previous where r is at least in the tail of p
        H = history stores largest concept sequence in a row of highest order
            concepts with a count of 1

        new stimulus
            add to known, count = 1
        next stimulus
            if same as new, add pair to known, count = 1 and so on
            if different
                if different is known
                    increase count
                    check to see if r+c is a substring of adjacent pair in H




Stimuli are states (levels) and frequencies and become raw concepts when
observed

AAAAAAAAAAAA is a state (with a length)
ABABABABABAB is a frequency/oscillation with a length

ABAABAABABBB is an oscillation of length 9 followed by a state of length 3
    oscilation ABA X 3,  state BBB
'''

class C:

    #dicts
    S = {}      # known stimuli sequences[stringkey:countvalue,...]
    K = {}      # known concepts - to track P and F without seeking

    #lists
    H = []      # history of concepts in sequence

#for this concept even if it does not think

    #strings
    C = ''      #composition

    #dicts
    P = {}      #predescesorsofthisconcept{predkey:countvalue,...}
    F = {}      #folowersofthisconcept{followerkey:countvalue,...}

    #concepts this concept is allowed to receive from
    recognize = {'':False}

    #concep

    lastStim = ''

    #if this concept is working/controlling others
    #if the key exists, that concept worked for this at some point
    #if the value is true, the concept is currently being used by
    #this one
    employing = {'':False}



#functions
    def analyseSeqFile(self, brain):
        print '1'
        brain.H = []

        filename = raw_input('Enter filename to analyze: ')
        input = [line.rstrip('\n') for line in open(filename, 'r')]
        input = ''.join(input)

        buffer = input[0]
        for i in range(1,len(input)):
            if input[i] == 'A' or 'U' or 'G' or 'C' or 'T':


                while input[i] == buffer[0] and i < len(input)-1:
                    buffer += input[i]
                    i += 1

                brain.observe(brain,buffer)
                brain.lastStim = buffer
                buffer = input[i]

        if len(brain.H) > 1:
            print 'H:',
            for i in range(len(brain.H)): print brain.H[i].C,
            # print 'AdjacentConcats: '.join(brain.adjacentConcats(brain))
        print '\nS: '.join(brain.S.keys())
        print '\nK: '.join(brain.K.keys())
        print 'H: '.join(c.C for c in brain.H)




    def recent(self,brain):
        print '2'
        if len(brain.H) >= 2: return brain.H[-2]
        else: return ''

    def holding(self,brain):
        print '3'
        if len(brain.H) >= 1: return brain.H[-1]


    def merge(self,brain):
        print '4'
        #prerequisite to merging - otherwise just letting observe append
        if len(brain.H) >= 2:

            #would be dumb to check the list for repeats
            holding = brain.H.pop()
            recent = brain.H.pop()

            #first link the concepts
            brain.link(brain,recent,holding)

            #they aren't the same, because we take in a buffer of strings
            #until we reach a unique one, so we have to check history for a
            #merge
            if brain.matchP(brain,recent,holding)\
                or brain.matchF(brain,recent,holding)\
                or holding.C == recent.C:
                    #merge the two concepts

                    merged = brain.recordStimulus(brain,recent.C + holding.C)
                    merged.P = recent.P
                    merged.F = recent.F


            else:
                #couldn't merge, too unique
                brain.H.append(recent)
                brain.H.append(holding)



    #all adjacent concats
    def adjacentConcats(self,brain):
        print '5'
        if len(brain.H)>1:
            ac = []
            for i in range(0,len(brain.H)-1):

                ac.append(brain.H[i].C + brain.H[i+1].C)

            return ac
        else: return []

    def isKnown(self,brain,c):
        print '6'
        if c in brain.K.keys(): return True
        return False

    def lastC(self,brain):
        print '7'
        return brain.lastStim


    '''
        Record Stimulus
            create entries in stim's and known's
            or generate then
    '''
    def recordStimulus(self,brain,c):
        print '8'
        if brain.K.has_key(c):
            brain.S[c]+=1
        else:
            brain.K[c] = brain.conceive(brain,c)
            brain.S[c] = 1
        brain.H.append(brain.K[c])
        if len(brain.H) >= 2 :
            brain.link(brain,brain.H[-2],brain.H[-1])
        return brain.K[c] #return the concept sensed


    #link current to recent's followers and recent to current's predecessors
    def link(self,brain,recent,holding):
        print '9'
        print'linking: ' + holding.C + ' and ' + recent.C

        if recent.F.has_key(holding.C): recent.F[holding.C]+=1
        else: recent.F[holding.C] = 1

        if holding.P.has_key(recent.C): holding.P[recent.C]+=1

        print 'H: ',
        for i in range(len(brain.H)):
            print brain.H[i].C,
        print'\n'

    def matchP(self,brain,recent,holding):
        print '10'
        if brain.K[holding.C] in brain.H[0:len(brain.H)-2]\
                and holding.P.has_key(recent.C):
            return True
        return False

    def matchF(self,brain,recent,holding):
        print '12'
        if brain.K[recent.C] in brain.H[0:len(brain.H)-2] \
                and recent.F.has_key(holding.C):
            return  True
        return False

    def inTail(self,brain,subject,collection):
        print '13'
        print 'checking if '+subject+' at TAIL of '+collection
        #length of subject
        l = len(subject)
        if subject == collection[-l:]: return True
        return False

    def inHead(self,brain,subject,collection):
        print '14'
        print 'checking if '+subject+' at HEAD of '+collection
        l = len(subject)
        if subject == collection[0:l]: return True
        return False


    def observe(self,brain,c):
        print '15'
        if not brain.K.has_key(c): holding = brain.recordStimulus(brain,c)
        else: holding = brain.K[c]

        brain.H.append(holding)       # add to list, may merge

        brain.merge(brain)




        lastStim = holding.C

    # initialize self
    def _init(self):
        print '16'
        self.identity = id(self)

    def allchars(self,brain,r, c):
        print '17'
        ok = True
        for e in r:
            if e != c: ok = False
        return ok
    # like recent without poppint()

    # given novel stimulus, conceive a concept
    def conceive(self,brain,s):
        print '18'
        newConcept = C()
        newConcept.C = s;
        return newConcept






#chicken concept holds the functionality to analyze a sequence file
#  analyseSequence creates a concept 'brain' that tracks all the machine learns
chicken = C()

#chicken will ask you which file to analyse
chicken.analyseSeqFile(chicken)

