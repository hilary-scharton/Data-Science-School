#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:17:43 2020

@author: hilaryscharton
"""
#	Create the file garden.py for this task.
#	Use some Garden Path sentences or think up your own (at least 5).
#   Here, tokenize and perform Entity recognition for each of the sentences 
# after you have stored them in a list called gardenpathSentences.
#	See how spaCy has categorized these sentences and look up the entities you dont understand
#	At the bottom of your file, write a comment about two unusual entities you 
# found that spaCy gave one of the words of your sentences - did you expect this?


import spacy #This statement should work fine if you have spaCy installed fine

nlp = spacy.load('en')



gardenpathSentences = [("The raft floated down the river sank."), 
                       ("We painted the wall with cracks."),
                       ("The man who whistles tunes pianos."), 
                       ("The girl told the story cried."),
                       ("The man who hunts ducks out on weekends.")]


result = []
for line in gardenpathSentences:
    sent = nlp(line)
    token_result = []
    for token in sent:
        token_result.append(token)
    result.append(token_result)
print(result)



paragraph = """The raft floated down the river sank.
We painted the wall with cracks. The man who whistles tunes pianos.
The girl told the story cried. The man who hunts ducks Katrina, Phoenix out on weekends."""
nlp_paragraph = nlp(paragraph)
print([(i, i.label_, i.label) for i in nlp_paragraph.ents])

# hah, i just spent far too much time thinking my code was bad because it 
# kept returning empty lists for the entities.  none of my sentence words
# were entities.  :eyeroll: 