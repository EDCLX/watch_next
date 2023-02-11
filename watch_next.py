
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

#I added a main function just to make this code functional in the future
# its commented out so it do not affect the task request

#def main():
    #description = str(input('Type the description of the movie you watched to recommend you one from my list: '))
    #get_similar_movie(description)

#main()
    