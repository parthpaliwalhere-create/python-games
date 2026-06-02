import os
os.system("cls")
print("Welcome to the math Game!")
print()
print("first round")
score = 0
print("score = 0")
print()
question1 = int(input("what is 31+22: "))
sum = 31+22
print()
if question1 == sum:
    print("🎉 Correct!")
    score+=1
    print(f"score = {score}")
else:
    print("❌ Wrong! The correct sum was", sum)
    print(f"score = {score}")

print()
input("press enter to continue to the next round...")
os.system("cls")

yes = input("oaky! let me know if you want to play again..: ")
print()

if yes == "yes":
    print("wow..i appreciate your dedication")
else:
    print("ohkk!as you wish!")
    exit()

if yes == "yes":
    os.system("cls")
    print()
    print("let's play a multiplication game!")
    print()

que = int(input("2*3= "))
quesy = 2*3

if que == quesy:
            print("ohh! you are correct")
            print()
            
            score+=1
            print(f"score = {score}")
else:
    print("no.. you are again wrong...this time the correct number was", quesy)
    score -=1
    print(f"score = {score}")

print()
print("thanks for playing")
                    
