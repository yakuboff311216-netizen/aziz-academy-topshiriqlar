secret_number = 10
attempts = 5

for i in range(attempts):
    guess = int(input())
                      
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You lost")