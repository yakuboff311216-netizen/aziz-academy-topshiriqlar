secret_number = 20
attempts = 0

while True:
    guess = int(input())
    attempts += 1
    
    if guess == secret_number:
        print("Correct")
        print(attempts)
        break
    elif guess < 1 or guess > 20:
        print("Invalid")
    elif guess < secret_number:
        print("Low")
    else:
        print("High")