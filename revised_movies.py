#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:35:58 2020

@author: hilaryscharton
"""

# so the goal here is to compare one movie description to a handful of other
# movie descriptions and get back which other movie is most similar to the first

import spacy
nlp = spacy.load('en_core_web_md')

def recommend_movie(list_movies, movie_compare):
    slist = [nlp(item).similarity(movie_compare) for item in list_movies]
    merged_list = list(zip(slist, list_movies))

    best = max(merged_list)
    return best[1]

def main():
    # open the file and plop into  'contents'

    f = open('movies.txt', 'r')
    contents = f.readlines()
    f.close()

    # compare the movies in 'contents' with the target movie AND put the 
    # similarity values into a list 

    content_to_compare = """Will he save their world or destroy it? When the Hulk 
    becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle 
    and launch him into space to a planet where the Hulk can live in peace. 
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery 
    and trained as a gladiator."""

    model_contents = nlp(content_to_compare)
    # mush both lists together so i can see similarity score beside movie
    # important to NOT change the order of slist & contents when zipping (which, 
    # btw, is super fancy, thank you for that) or it'll return the wrong thing.
    print(recommend_movie(contents, model_contents)) # just checking

    sentence = nlp("Hello World")
    print(recommend_movie(contents, sentence)) # just checking


if __name__ == '__main__':
    main()

