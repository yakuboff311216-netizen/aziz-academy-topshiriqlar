secret_number = 8
attempts = 5

for i in range(attempts):
    guess = int(input())
    
    if guess == secret_number:
        print("Correct")
        break
    else:
        if i == 0:
            if guess < secret_number:
                print("Low")
            else:
                print("High")
        else:
            print("Wrong")
else:
    print("You lost")