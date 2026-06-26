a, b = map(int, input().split())
amal = input().strip()
natija = {"add": a + b, "sub": a - b, "mul": a * b, "div": a / b}
print(natija[amal])