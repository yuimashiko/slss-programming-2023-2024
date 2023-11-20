# Similar hobbies
# YUI MASHIKO
# November 14


# Calculate similarity scores between two people

person1_hobbies = [ 
 "skiing",
 "rockclimbing",
 "drawing",
 "soccer",
 "swimming",
 "movies",
 "pokemon",
]

person2_hobbies = [
 "baseball",
 "skiing",
 "cooking",
]


# Initialize the similarity score
similarity_score = 0



# Iterate through all movies in first list
for hobbies in person1_hobbies:
    if hobbies in person2_hobbies:
        similarity_score += 1


 # Display the results
print(f"The similarity score is: {similarity_score}")