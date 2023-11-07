# Mcdonald 
# YUI
# November 3

print("Welcom to Mcdonald's")

user_respond = input("Would you like a burger for 5$? (Yes / No)")

total = 0

if user_respond.lower() == "yes":
    total += 5


user_respond2 = input("Would you like freies for 3$? (Yes / No)")

if user_respond2.lower() == "yes" :
    total += 3

# Calculate the tax
# Print the result

sum =  int(total) * 1.14

print("Your total is",sum,"$" )