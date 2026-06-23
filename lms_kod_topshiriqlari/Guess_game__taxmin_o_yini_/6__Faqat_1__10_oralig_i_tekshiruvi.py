yashirin_son = 6

while True:
    son = int(input())
    
    if son < 1 or son > 10:
        print("Invalid")
        continue 
    
    if son == yashirin_son:
        print("Correct")
        break
    else:
        print("Xato")