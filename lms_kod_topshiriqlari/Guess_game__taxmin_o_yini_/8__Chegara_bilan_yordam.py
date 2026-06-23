yashirin_son = 15

while True:
    son = int(input())
    
    if son == yashirin_son:
        print("Correct")
        break
    elif abs(son - yashirin_son) > 5:
        print("Far")
    else:
        print("Close")