'''
    pure concept sequence detector:

        A pattern/k-mer/motif detector gathering very detailed analysis of all
        interesting patterns in a DNA or RNA sequence in one pass through data

        all languages, including programming languages, feature learn-able
        patterns an agent can learn to recognize and expect.  neural nets
        are getting better at modeling this, but for the purpose of finding
        interesting patterns and sequences in DNA or RNA, the application
        is even simpler, as we aren't trying to predict or generate, but rather
        notice and infer

        thinking about how concepts are learned: all are built from smaller
        concepts consisting of smaller concepts and when there is no further
        collection of smaller concepts making up this one, we have reached
        a stimulus- a sensory reading. that registers in the brain, making
        a blue print- and when that stimulus happens again, it is compared with
        the other concepts exibiting temporal locality around both events, in
        an effort to find a pattern or make a prediction.

        We 'think' in a top down fashion when analyzing a problem, but we learn
        to expect small concepts following small concepts, first, that
        expecation itself being a concept, simply a construct in a brain.

        simplify that by removing the functions to expect and predict, rather
        just note along our path, the concepts we've observed so far.

        We need to really understand what a concept is. In my opinion, the
        smallest concept captured by a thinking agent
        is just a tiny thinking agent, the smallest possible!

        To model a brain we need an analogue of Neurons, which is why this
        program is a neural network, one for gleaning rather than labeling

        Basic idea:

        1.  if it happened at least once, it exists (at least somewhere in time)
            - it must be registered as a learned stimulus
        2.  if it happened twice, it is significant and may happen again and
            should now compare pre and proceding concepts of this and the last
            time this concept was observed
            - the stimulus captured and held by a neuron that is simply learning
              when to expect and how to react to this stimulus next time
        3.  our base concepts are A T G C or A U G C, dna/rna bases
        4.  If A->T was seen before and observed now, this 2-mer is a pattern,
            and a unique concept.  If all seven of A->A, A->T, A->G, A->C,
            C->A, G->A, T->A, and A->A also known concepts, then A,
            can be removed as a unique concept
        5.  Created higher order concepts are treated the same as basic
            concepts in that learn to look for other patterns following it.
        6.  ie: a secuence of 2, could learn to expect a sequence a 33
            but by the time a sequence of 33 has appeared twice, would there
            really be any sequences of 2 left have haven't been fully
            absorbed into all possible higher or concepts on a big dataset?
        7.  We can set parameters to limit the lengths of sequences we are
            interested in, but keep in mind this doesn't really matter- why?
            two things can
            represent a
            million things if those are containers whose sum of bases omo
        8.  This network is learning, not to predict the future, but to grow
            its concepts of dna/rna patterns, and should have within it some
            functionality to:

            - grow concepts
            - prune concepts
            - group similar concepts that be be off by some error fraction

        User input Parameters:
            - minLength : smallest sequence interested in
            - maxLenth  : largest sequence interested in
'''

