import random 
print("Number Guessing Game")

number = random.randint(1,9)
chances = 0

print("Guess A Number Between 1 and 9")

while chances < 5:
    guess = int(input("Enter Your Guess : "))
    if guess == number: 
        print("Congratulaisons!! You Won!!")
    elif (guess < number):
        print("Your guess was too low: Guess a number higher than ", guess)
    else: 
        print("Your guess was too high: Guess a number lower than ", guess)

    chances += 1

if not chances < 5: 
    print("YOU LOOSE!!, The number is", number)

    