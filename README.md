# 
# Movie Recommendation System

This program is a movie recommendation system that uses spaCy's natural language processing library to find the most similar movie to the description provided by the user. The program reads a list of movies from a text file called "movies.txt" and finds the similarity between the user's input and the description of each movie.

## Installation

To run this program, you will need to have Python 3.x and the spaCy library installed. You can install spaCy by running the following command in your terminal:

pip3 install spacy


You will also need to download the `en_core_web_md` model by running the following command:

python -m spacy download en_core_web_md


## Usage

To use this program, simply run the `get_similar_movie` function with a description of the movie you just watched as an argument. The function will return the most similar movie from the list of movies.

```python
import spacy

#creating function that takes description to find similarity in a movies text file
description = """Will he save their world or destroy it? 
    When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
     Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

def get_similar_movie(description):
    nlp = spacy.load("en_core_web_md")
    #read movies file
    with open('movies.txt', "r") as f:
        movies = f.readlines()
    #process the description
    desc = nlp(description)
    movie_similarity = [] #list to hold value
    for line in movies:
        similar_movie = nlp(line).similarity(desc)
        # we add the line with the most similarity to the empty list
        movie_similarity.append((line, similar_movie))
    print("\nAccording with the description provided you should watch next:\n")
    print(max(movie_similarity,key=lambda x: x[1])[0])

get_similar_movie(description)

The program will output the name of the movie that is most similar to the input description.


