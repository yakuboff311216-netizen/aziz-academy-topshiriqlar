login = input().strip()
parol = input().strip()
natija = (login == "admin") and (len(parol) >= 6)
print(natija)