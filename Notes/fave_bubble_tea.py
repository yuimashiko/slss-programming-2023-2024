# Bubble Tea algo
# Author: YUI MASHIKO
# Date: October 27 2023

# Ask 5 users what theire favourite bubble tea place is
# Print out a summary of the data


NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite bbt place is
    print("What's your favourite bubble tea place?")
    fave_bbt = input().strip(",.?! ").lower()

    # Tallying/Counting Algo
    # Options: CoCo, Chatime, SunTea, Xing Fu Tang, Bubble Queen
    # If they say CoCo, increase the counter for CoCo by one, etc.
    if fave_bbt == "coco":
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime":
        chatime_likes + 1
    elif fave_bbt == "suntea":
        suntea_likes + 1
    elif fave_bbt == "xinghfutang":
        xingfutang_likes + 1
    elif fave_bbt == "bbqueen":
        bbqueen_likes + 1


# Print a summary of the results
print(f"CoCo Likes: {coco_likes}) {coco_likes/NUM_RESPONDENTS * 100}%")
print(f"chattime Likes : {chatime_likes}) {chatime_likes/NUM_RESPONDENTS * 100}%")
print(f"Suntea Likes: {suntea_likes} | {chatime_likes/NUM_RESPONDENTS * 100}%")
print(f"XingFuTang Likes: {xingfutang_likes} | {xingfutang_likes/NUM_RESPONDENTS * 100}%")
print(f"Bbqueen Likes: {bbqueen_likes} | {bbqueen_likes/NUM_RESPONDENTS * 100}%")
      