import random
print("welcome to the guessing game")
print()
print("plzz select the level of difficulty")
print("1. easy ")
print("2. normal")
print("3. hard")
print()
choi = int(input("level?? : "))
print()
score = 0
print()
if choi ==1:
      limit=20
elif choi ==2:
      limit=50
elif choi ==3:
      limit=100
num=random.randint(1,limit)
def ip():
    score = 0
    oi = int(input("Enter Your Guess : "))
    print()
    if oi > num:
        print("so ahead...")
        print()
        return False
    elif oi < num:
        print("slightly behind...")
        print()
        return False
    else:
        print("yupp,... you are correct")
        print()
        score += 1
        print(f"score = {score}")
        print()
        print("thankyouu!!")
        exit()
        return True


if choi == 1:
      print("4 life")
      limit = "1 to 20"
      print(limit," limit")
      print(f"score = {score}")
      print()
      ip()
      ip()
      ip()
      ip()
      print("number was ",num)

elif choi == 2:
        print("3 life")
        limit = "1 to 50"
        print(limit," limit")
        print(f"score = {score}")
        print()
        ip()
        ip()
        ip()
        print("number was ",num)
elif choi == 3:
        print("2 life")
        limit = "1 to 100"
        print(limit," limit")
        print(f"score = {score}")
        print()
        ip()
        ip()
        print("number was ",num)
else:
      print("invalid input")
      exit()
print("thankyouu!!")
exit()
