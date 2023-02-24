import spacy

nlp = spacy.load('en_core_web_md')

planet_hulk = nlp(
    "Will he savetheir world or destroy it? When the Planet Hulk becomes too dangerous for theEarth, "
    "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Planet Hulk can live "
    "in peace. Unfortunately, Planet Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# This list will store the result of when the variable hulk is compared to the descriptions in movies.txt
probabilities = []


def similarities(movie):
    file = open("Tasks\movies.txt", "r", encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        split = line.split(":")
        # as the split variable has separated the title and the description, the variable below will the description using the nlp method
        # so that the comparison could be made with the planet_hulk variable
        token = nlp(split[1])
        title = nlp(split[0])
        print("Similarities between", title.text, "and Planet Hulk", token.similarity(movie))
        probabilities.append(token.similarity(movie))

    # The variable below will store the highest similarity with Planet Hulk
    highest_probability = max(probabilities)

    # The for loop below will check if the variable's value in line 27 is same as one of the similarities
    # if yes it will return the movie of the highest probability of the user watching that movie
    for line in lines:
        split = line.split(":")
        token = nlp(split[1])
        if highest_probability == token.similarity(movie):
            return f"The movie with the highest probability to be watched after Planet Hulk is {split[0]} " \
                   f"with a probability of {token.similarity(movie)}"


print(similarities(planet_hulk))