# parental_bot
# yui mashiko
# November 16\

score = 0

user_respond = input("Did you eat?")
if user_respond.lower() == "yes":
   score += 1

user_respond2 = input("Did you study?")
if user_respond2.lower() == "yes":
   score += 1


user_respond3 = input("Did you do your laundry?")
if user_respond3.lower() == "yes":
   score += 1


user_respond4 = input("Did you call grandma?")
if user_respond4.lower() == "yes":
   score += 1


   
if score > 2 :
   print("Good job")

elif score == 2 :
   print("Okay")

else :
   print("🤬")


