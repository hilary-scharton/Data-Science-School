#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:58:08 2020

@author: hilaryscharton
"""


import spacy

nlp = spacy.load('en')

word1 = nlp ("cat")
word2 = nlp ("monkey")
word3 = nlp ("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey fair book banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
        
# from the way cats like to lie on anything you're reading, i'd expect them
# to have a much higher similarity with books
        
sentence_to_compare = 'Why is my cat on the car'

sentences = ['Where did my dog go',
             'hello, where is my car',
             'i\'ve lost my cat in my car',
             'i\'d like my boat back', 
             'i will name my dog diana']
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence, "-", similarity)

"""
Where did my dog go - 0.5614408499709634
hello, where is my car - 0.6465274335456067
i've lost my cat in my car - 0.7837679880303869
i'd like my boat back - 0.4525051622015037
i will name my dog diana - 0.6012385297768889

Where did my dog go - 0.8794280609455339
hello, where is my car - 0.8944486476856313
i've lost my cat in my car - 0.9004783170559137
i'd like my boat back - 0.8219702288203602
i will name my dog diana - 0.8207846693942806
"""
# so....it's curious that package with more data in it marks "i'd like my 
# boat back" as so similar to the model.  also curious that there's such 
# a big size difference.  md is 4X small.  

