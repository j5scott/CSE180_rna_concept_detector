# coding=utf-8
#pcfpd.py
"""
    Jeremy Scott
    A11180142
    Final Project  For CSE180@UCSD~(Fall,2016)

    Proposal: build NN that learns all the patterns / motifs in sequence,
              - adding : generate sequences drawn from same probability
                         distribution of patterns as input file

    Rest of documentation + notes/playground @ bottom of this file
"""#############################################################################
#                                                                              #
#                           Class C : A 'Concept'                              #
#                           Author: Jeremy Scott                               #
#                                                                              #
#       Q: WHAT DO ALL OBSERVABLE CONCEPTS HAVE IN COMMON?                     #
#       A: POTENTIAL FOR INTEGRATION INTO OBSERVERS BRAIN AS A CONCEPT.        #
#                                                                              #
#        ...including, brains, stories, gods, ToM and Meta-cognition...        #
#           If you than with with or about it, it is a concept.                #
#           If you employ it to think for you, it is a concept agent:          #
#           a living concept holding it's own perspective based                #
#           on its experience                                                  #
#                                                                              #
#           Assumptions:                                                       #
#                                                                              #
#           *  stimuli have direct connection to brain neurons                 #
#                                                                              #
#           *  brains do not have a special place where all of their           #
#              expectations and predictive abilities lie.                      #
#                                                                              #
#           *  neurons learn to expect the stimuli that typically              #
#              follow.  neurons link expectation _across_ sense type           #
#                                                                              #
#------------------------------------------------------------------------------#
class C:
    locs = []       #locations an employer of this concept tells it they are

    """* A 'Concept' in all it's Contexts *"""#
    H = []          # History of concepts this concept/brain observed
    # * all dictionaries accessed by string key * #
    # dictionaries
    S  = {}         # Stimulus: {string:count}
    Si = {}         # Stimuli: {label: StimulusTypes={}} --when more senses
                    # ie: other brains sensor readings/ labeled sense
                    # files
    K  = {}         # Known concepts: {conceptstring : C}
    Y  = {}         # Policy's
    # ToDo- multiple labeled types of histories and knowns
    Hs = {}         # Histories: labeled, ie: brain.Hs['brain2'] -> brain2.H
    Ks = {}         # Knowns: labeled knowledge dictionaries
    # ToDo- control mechanisms
    Rs = {}         # Recognize: Who I can send/receive from
    As = {}         # Allow:     Who can request from or change this
    Ts = {}         # Targets:   Who this concept can control
    T = ''          # Target for my next action
    A = ''          # Some co
    R = ''          # When only one other concept has communication with this

    # dictionaries
    P = {}          # predescesorsofthisconcept{predkey:countvalue,...}
    F = {}          # followersofthisconcept{followerkey:countvalue,...}

    # Controlling other known brains: access map, brains employed. (ie: sub-proc)
    E = {}  # ToDo- Registered Employees (employees)
    I = {}  # Todo- Who is now here?
            #       'I' as in 'in' me ,rather than 'have' ie: agents can be
            #       a 'firm'-> can make legal agent-like decisions, and have
            #       human agent units inside it

    # strings:      strings are keys for use in dictionaries
    C = ''          # label for this concept?

    """chars never duplicated, live in same static/globally (in python)
    accessible plase until referenced and used, never duplicated in memory
    however, how big is the reference to this concept??? never bigger
    than an int of course, but strings inside can reference a massively big
    """

    allowed = ''

    dbgprint = True

    myname = '' #for agents, and original concept, default to Eva Scott 1.0
                #on init
    myCount= 0


# functions
    #only 1 brain- use analyzeCharacterSequence3 for genomes
    def analyzeCharacterSequence(self, brain, allowedCharacters):

        # User specified characters to recognize
        brain.allowed = allowedCharacters

        if brain.dbgprint: print 'brain.allowed: ' + brain.allowed

        filename = raw_input('Enter filename to analyze: ')
        input = [line.rstrip('\n') for line in open(filename, 'r')]
        input = ''.join(input)

        stateConcepts = []

        # start with empty buffer and zero index
        buffer = ''

        i = 0
        while input[i] not in brain.allowed: i += 1
        j = i

        buffer = ''
        while i < len(input):
            start = True
            if input[i] in brain.allowed:
                buffer += input[j]
                while (i + 1 < len(input) - 1 and input[i + 1] == input[j]):
                    i += 1
                    buffer += input[i]
                j = i = i + 1
                stateConcepts.append(buffer)
                buffer = ''

        for concept in stateConcepts:
            brain.observe(brain, concept)


    #Given a Sequence File of genome, dna / rna, learn all patterns
    def analyzeCharacterSequence3(self, brain, allowedCharacters):

        #hiring 3 barnacles to oberve nucleotide sequences starting at
        #first+[0|1|2] to see if , don't worry, barnacle is just a barnacle

        barnacle1 = C()
        barnacle1.myname = 'barnacle1'
        barnacle2 = C()
        barnacle2.myname = 'barnacle2'
        barnacle3 = C()
        barnacle3.myname = 'barnacle3'



        #User specified characters to recognize
        brain.allowed = allowedCharacters

        filename = raw_input('Enter filename to analyze: ')
        input = [line.rstrip('\n') for line in open(filename, 'r')]
        input = ''.join(input)

        stateConcepts = []

        buff = ''

        i = 0
        while input[i] not in brain.allowed: i += 1
        j = i

        buff = ''
        while i < len(input):
            start = True
            if input[i] in brain.allowed:
                buff += input[j]
                while (i + 1 < len(input) - 1 and input[i + 1] == input[j]):
                    i += 1
                    buff += input[i]
                j = i = i + 1
                stateConcepts.append(buff)
                buff = ''

        wait = 2 #
        for concept in stateConcepts:
            #barnacles attack
            #brain.observe(brain, concept)

            barnacle1.observe(brain,concept)
            if wait < 1: barnacle1.observe(brain, concept)
            if wait < 2: barnacle3.observe(brain, concept)

            #hmmm- barnacles not smart idea- i am too tired
            #      could work if i changed it so barnacles had
            #       their own Q, this is why OS class was useful
            #       different concepts using the same resource,
            #       mixing it up...


        if brain.dbgprint: print 'brain.K.keys(): '.join(brain.K.keys())
        if brain.dbgprint: print 'brain.S.keys(): '.join(brain.S.keys())
        if brain.dbgprint: print 'brain.H: '.join([h.C for h in brain.H])

    #END analyze



    #pre-process chars return clean string to use
    def cleanInput(self,brain,input,allowed):
        buff = ''
        for c in input:
            if c in allowed:
                buff += c
        return buff

    # return characters I can sense
    def getAllowed(self,brain):
        return brain.allowed

    def recent(self,brain):
        #print '2'
        if len(brain.H) >= 2: return brain.H[-2]
        else: return ''

    def holding(self,brain):
        #print '3'
        if len(brain.H) >= 1: return brain.H[-1]


    '''
        Merge:
            pick op two concepts from list
                1st to 'hodling'       These are like my right and left
                2nd to 'recent'        hands, but
    '''
    def merge(self,brain):
        mergesThisRound = 0
        didmerge = False
        if len(brain.H) >= 2:
            holding = brain.H.pop()
            recent = brain.H.pop()
            brain.link(brain,recent,holding)

            #merge
            if brain.matchP(brain,recent,holding)\
                or brain.matchF(brain,recent,holding)\
                or holding.C == recent.C:
                #merge the two concepts
                if brain.dbgprint: print 'merging ' + holding.C + ', ' \
                                                                'with recent ' + recent.C
                merged = brain.recordStimulus(brain,recent.C + holding.C)

                merged.P = recent.P
                merged.F = recent.F
                didmerge = True
            else: #Popped earlier and couldn't merge couldn't merge, too unique
                if brain.dbgprint:
                    print 'no merge for '+recent.C+' and '+holding.C
                brain.H.append(recent)
                brain.H.append(holding)
        # if the merge happened, try to let caller (who is 'observe')
        # merge the new concept because it might also be known
        print 'merges this round (single) char integration: '+str(mergesThisRound)
        return didmerge

    def isKnown(self,brain,c):
        #print '6'
        if c in brain.K.keys(): return True
        return False

    #Record new (concept) or update counts
    def recordStimulus(self,brain,c):
        #print '8'
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
        if brain.dbgprint == True:
            #ordered R then H so it 'looks' right
            print'linking: ' + recent.C +' and ' + holding.C

        if recent.F.has_key(holding.C): recent.F[holding.C]+=1
        else: recent.F[holding.C] = 1

        if holding.P.has_key(recent.C): holding.P[recent.C]+=1
        else: holding.P[recent.C] = 1 #<-fixed (added)

        #print 'H: ',
        for i in range(len(brain.H)):
            print brain.H[i].C,
        print'\n'

    # all adjacent concats
    def adjacentConcats(self, brain):
        # print '5'
        if len(brain.H) > 1:
            ac = []
            for i in range(0, len(brain.H) - 1):
                ac.append(brain.H[i].C + brain.H[i + 1].C)

            return ac
        else:
            return []

    def matchP(self,brain,recent,holding):
        #print '10'
        if brain.K[holding.C] in brain.H[0:len(brain.H)]\
                and holding.P.has_key(recent.C):
            return True
        return False

    def matchF(self,brain,recent,holding):
        #print '12'
        if brain.K[recent.C] in brain.H[0:len(brain.H)] \
                and recent.F.has_key(holding.C):
            return  True
        return False

    def inTail(self,brain,subject,collection):
        #print '13'
        #print 'checking if '+subject+' at TAIL of '+collection
        #length of subject
        l = len(subject)
        if subject == collection[-l:]: return True
        return False

    def inHead(self,brain,subject,collection):
        #print '14'
        #print 'checking if '+subject+' at HEAD of '+collection
        l = len(subject)
        if subject == collection[0:l]: return True
        return False

    #observe: function of record stimulus, updates and/or creates and init's
    #         the known/unknown concept, check if merge-able immediatley
    def observe(self,brain,c):
        brain.recordStimulus(brain,c)
        didMerge = brain.merge(brain)
        while(didMerge):didMerge = brain.merge(brain)

    # initialize self
    def _init(self):
        #print '16'
        self.identity = id(self)

    def allchars(self,brain,r, c):
        #print '17'
        ok = True
        for e in r:
            if e != c: ok = False
        return ok
    # like recent without poppint()

    # given novel stimulus, conceive a concept
    def conceive(self,brain,s):
        #print 'conceiving: ' +s+ '-> got: '
        newConcept = C()
        newConcept.C = s;
        #print + newConcept.C
        return newConcept

    def test(self,brain,testName):
        #write tests here for each function,
        0

    #useful to print any dictionary the way i want to
    #this name is specified by the caller, can be anything
    def printDict(self,brain,label,obj):
        keys = obj.keys()
        print brain.obj[keys]
        # if type(obj[k]) is str:
        #     for k in keys: print label:+': '+k+'.: '+ str(obj[k])
        # else print

    def printHistory(self,brain):
        print 'HistoryList('+brain.myname+')\n'+\
              '\n'.join([h.C for h in brain.H])

    #print count and stimulus                 acc: brain.Keys()
    def printStims(self,brain): #stims {stringkey: integercount}
        keys = brain.S.keys();
        print('Stimuli Counts list: \n')
        for k in keys: print 'Count('+k+'): ' + str(brain.S[k])

    #output list of all predescessors and
    #countsfor all in known concepts
    #this time single line output per guy
    def printPall(self,brain):
        for k in brain.K:
            brain.printP(brain,brain.K[k])

    def printFall(self,brain):
        for k in brain.K:
            brain.printF(brain,brain.K[k])


    #given a concept, show it's predescessor list
    def printP(self,brain,concept):
        print 'Predescessor List('+concept.C+'): \n'+\
              '\n'.join([p for p in concept.P])

    # given a concept, show it's predescessor list
    def printF(self, brain, concept):
        print 'Followers(' + concept.C + '): \n' + \
              '\n'.join([f for f in concept.F])


chickenBrain = C()
chickenBrain.myname = 'WickedChickenEnemy'

#chicken will ask you which file to analyse
chickenBrain.analyzeCharacterSequence(chickenBrain,'AUGTCaugtc')

chickenBrain.printHistory(chickenBrain)
chickenBrain.printStims(chickenBrain)
chickenBrain.printPall(chickenBrain)
chickenBrain.printFall(chickenBrain)

# Output File: Known K
# output_known = open(filename + brain.C, 'w')

# Output File: History H
# output_history = open(filename + brain.C , 'w')

# output File: Counts
# output_counts = open(filename+)

'''

    * Project History
        - Start: 12-8-16
        - End:   <tba>
        - 1. built test generator Genzen.py
            . run Genzen.py: enter name of sequence file to generate
            . Genzen will produce
            and store generated test
              data
        -   2. building (well enough for bio too) this file:  pcfd.y
           RNN analogue, built from scratch by my own ideas about
        -   character, concept, pattern+frequency learner, O(N) through

    * Use
        - generator Genzen.py
            . run Genzen.py: enter name of sequence file to generate
            . Genzen will produce 4 output files:
            [dna|rna](seq's)+[fwd|rev][strands}
            and store generated test
        -   Shell command(s)
         .  learn patterns in text: python pcfpdy.py
         .  prompts for filename >> prompts for filename, manually enter

    * result
        -   output files:
                .   learned concepts (string names, counts)
                .   learned  (currently text)


    * Note To Professors (Mike, Niema, Pavel)

        I've been wanting to build an AI learning system this powerful
        and dynamic for a long time and have been conceiving theory almost
        exactly as I've programmed here, on paper in the past, now reality!
        Maybe good will come from the 'great misunderstandings' that lead me
        here.

        Thank you for the opportunity to not only give  me a chance to
        build 'an' AI structure for credit: AFAIK this hasn't been done
        before. It was super fun to make and use and, as you can see, I
        do plan
'''