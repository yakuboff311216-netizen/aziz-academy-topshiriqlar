secret_number = 11
attempts = 0

while True:
    guess = int(input())
    attempts += 1
    
    if guess == secret_number:
        print(attempts)
        break