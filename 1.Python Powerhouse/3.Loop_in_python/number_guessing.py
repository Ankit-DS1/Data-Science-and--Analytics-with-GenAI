import random 

num = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess == num:
        print(f"Congrats! you found your number in {tries} tries")
        break
    elif guess > num:
        print("sorry, you need to go lower\n")
    else:
        print("sorry, you need to go a little upper\n")
