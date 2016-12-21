README CONTENTS
- Note for Professors
- Errata and clarifications for Report
- Updated file use

Note:
  For Niema/Mike/Pavel @ucsd and others 
  interested in the details of this project 
  and / or its future :  I will be working
  on more than I proposed, to build a robust
  system able to be called, used and return
  datum to other systems.

  Please understand this report was 
  written while having been awake for over
  60 hours straight. A bizzare thing happens
  where my brain thinks I wrote a sentence
  and sees what it believed it wrote, but
  some words are skipped over and clarifications,
  not clarified.

  After getting some sleep I've noticed
  several problems in the report.  

Erratum(E) and Clarification(C) in (where) of Report.
For Erratum, E -> X indicates fix
  C: (under title)
    Observe ♺ Sequence ♺ Integrate ♺ Concept ♺ Update ♺ Expectation ♺ Feedback ♺ Learning
    Indicates the future goal, not the proposal.  
    Tool submitted does include:
      Observing incomming Stimuli (chars)
        where the smallest incomming stimuli to 'observe' is S = Regex:[A|U|T|G|C|a|u|g|c|t|]+
          
          A stimulus maps to a neural register
            Example: A, AAAAAAAA: -> character repeating any number of times
            and gets its initial count = 1, increasing that each time it is observed again
          
          No other concepts are pre-registered as observable
          Waveforms are learned and Integrated into concepts, examples
            A, G: - not a concept, or registered stimulus yet, however
                  - imediately registers as a stimulus Possibility via "Linking"
                    Linking definition:  This concept registers last concept as a predecessor
                                         Last concept registers this concept as a follower
                  - when A, G ...[''|Regex:[AUTGCaugct]+]+.. A, G:
                      since A and G were linked before, they become a registerable
                      stimulus, AG, an immediately recognizable (collection) of concept
          After every concept, an integration is checked via merge which if combination
          of two concepts exists already, records the unified concept in history, as opposed
          to the single concept.
  E:  (paragraph under "Proposal"):
    - 'one pass through data' -> 'one pass through file'
       probably unnecessary fix, because this is still an O(N) time algorithm
       ie: all pairs linked, and when seen again are merged as new concept 
       becomming immediately recognizable through dictionary
              
  E:  (End of paragraph under "Proposal"):
    - 'the original proposal, but...missing piece:' -> 'the original proposal.'
      reason for deletion:  I wrote some of the report before my last code edits
      and this 'missing piece' is not missing now
      
  E: (under Living Toolset title)
    - 'as t for as' -> 'for as' 
    
  E
  
  woops sorry, gotta run, cant finish errata yet!
  I will finish this later (tomorrow maybe), just know I will update both the report and the code, 
  Have to build another Neural Network before midnight tonight (12-9)
  The report has tons of stuff I'd like to edit after an even better night's sleep
      
      
UPDATE 12/21/2016:
appologies if anyone has been waiting for an update on this, I'm still trying to finish NachOS, spend a few days finishing another NN project, and now christmas plans are taking time- still intend to work on this! its on my list
            
            
            


     
