print("Welcome to our Computer Quiz!!")
playing = input('Do you want to play?  ')
if playing.lower() != 'yes':
    quit()

print("Okay!! let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("Who invent the Gravity? ")
if answer.lower() == 'newton':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does PC stand for? ")
if answer.lower() == 'personal computer':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does IT stand for? ")
if answer.lower() == 'information technology':
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

print(f"Your Total Score : {score}")
print(f"Your Score Percentage : {(score/5)*100}%")
