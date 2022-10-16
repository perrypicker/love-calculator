print("Welcome to love calculator\n")

name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

score1 = 0
score2 = 0

# Concatenate both names variables
names = name1 + name2

# Score1 (TRUE) incrementation
score1+=names.count("t")
score1+=names.count("r")
score1+=names.count("u")
score1+=names.count("e")

# Score2 (LOVE) incrementation
score2+=names.count("l")
score2+=names.count("o")
score2+=names.count("v")
score2+=names.count("e")

# Convert scores variables to strings
score1 = str(score1)
score2 = str(score2)

# Concatenate scores variables
final_score =  int(score1 + score2)

msg_output = f"Your score is {final_score}"

if final_score < 10 or final_score > 90 :
    print(f"{msg_output}, you go together like coke and mentos.")

elif final_score >= 40 and final_score <= 50 :
    print(f"{msg_output}, you are alright together.")

else :
    print(f"{msg_output}.")


