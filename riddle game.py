import os
import time
def u():
    os.system("cls")
def w():
      input("Press enter to continue")
def i():
      print()
def submit():
       input("press enter to submit your answer")
u()
print("Starting Game",end="")
for o in range(3):
      print(".",end="",flush=True)
      time.sleep(0.5)
u()
print("="*70)
print("🧩 THE ULTIMATE RIDDLE GAME 🧩".center(70))
print("="*70)
print()
print("Welcome buddy! Get ready to test your brain...")
print()
def g1():
      u()
      print("="*50)
      print("RULES".center(50))
      print("="*50)
      print("🟢 selected easy mode")
      i()
      print("❤️  Total Lives : 2")
      print("🧩 Total Riddles : 3")
      print("🏆 Solve all riddles to win")
      print("❌ Lose all lives = Game Over")
      i()
      w()
      u()   
def g2():
      u()
      print("="*50)
      print("RULES".center(50))
      print("="*50)
      print("🔴 selected hard mode")
      i()
      print("❤️  Total Lives : only 1")
      print("🧩 Total Riddles : 5")
      print("🏆 Solve all riddles to win")
      print("❌ Lose all lives = Game Over")
      i()
      w()
      u()
def g22():
    print("Preparing riddles...")
    time.sleep(1)
    u()
    print("1st riddle")
    user=input('''I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?
''').lower().strip()
    i()
    submit()
    answer="map"
    if user==answer :
          u()
          print("you are correct")
          i()
          w()
    else:
           print("that's wrong.....you are out of the game")
           i()
           w()
           u()
           ho()

    user2=input('''2nd.What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?
''').lower().strip()
    i()
    submit()
    answer2="r"
    if user2==answer2 :
          u()
          print("you are correct")
          i()
          w()
    else:
           print("that's wrong.....you are out of the game")
           i()
           w()
           u()
           ho()

    user3=input('''3rd..I have keys, but no locks , i have space, but no rooms. You can enter, but you can’t go outside. What am I?
''').lower().strip()
    i()
    submit()
    answer3="keyboard"
    if user3==answer3 :
          u()
          print("you are correct")
          i()
          w()
    else:
           print("that's wrong.....you are out of the game")
           i()
           w()
           u()
           ho()

    user4=input('''4th..What has to be broken before you can use it?
''').lower().strip()
    i()
    submit()
    answer4="egg"
    if user4==answer4 :
          u()
          print("you are correct")
          i()
          w()
    else:
           print("that's wrong.....you are out of the game")
           i()
           w()
           u()
           ho()
    user5=input('''5th..This belongs to you, but everyone else uses it. What is it?
''').lower().strip()
    i()
    submit()
    answer5="name"

    if user5==answer5 :
          u()
          print("you are correct")
          i()
          print("congratulations...you won and earned the victory!!")
          i()
          w()
          ho()
    else:
           print("that's wrong.....you are out of the game")
           i()
           w()
           u()
           ho()
      
def ho():
      i()
      op=input("Do you want to play again (yes/no): ").lower().strip()
      if op=="yes":
            u()
            uio()
            goi()
      else:
            print("Thanks for playing..see you next time!!")
            time.sleep(2)
            exit()
def g11():   
         print("Preparing riddles...")
         time.sleep(1)
         u()
         print("1st riddle")
         print("What gets smaller every time it takes a bath?")
         a=input("").lower().strip()
         i()
         submit()
         if a=="soap":
            u()
            print("Good..you are correct")
            i()
            print(f"❤️  Lives Remaining: {life}")
            i()
            w()
            u()
            return True
         else:
            return False

            
def g12():
         
         print("2nd..I have a neck, but no head. I have two arms, but no hands. What am I?")
         p=input("").lower().strip()
         i()
         submit()
         if p=="shirt":
                  u()
                  print("Good..you are correct")
                  i()
                  print(f"❤️  Lives Remaining: {life}")
                  i()
                  w()
                  u()
                  return True
         else:
                return False
def g13():
         global life
         print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
         o=input("").lower().strip()
         i()
         submit()
         if o=="swims":
                          u()
                          print("You won buddy!!...congratulations!!")
                          i()
                          ho()
         else:
                              w()
                              u()
                              life-=1
                              print("you are wrong buddy...")
                              i()
                              print(f"❤️  Lives Remaining: {life}")
                              w()
                              u()
                              print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
                              o=input("").lower().strip()
                              if o=="swims":
                                     print("congratulations....you won!!")
                                     i()
                                     w()
                                     ho()
                              else:
                                     print("that's wrong.....you are out of the game")
                                     i()
                                     w()
                                     u()
                                     ho()

                              
def uio():
      u()
      for j in range(2):

       for i in range(4):

        print("\rLoading" + "." * i + "   ", end="", flush=True)

        time.sleep(0.5)

      u()
      print("="*70)
      print("🧩 THE ULTIMATE RIDDLE GAME 🧩".center(70))
      print("="*70)
      print()
      print("Welcome buddy! Get ready to test your brain...")
      print()
      print()
      print("There are modes  in this game")
      print("1. easy")
      print("2. hard")
      print()
def goi():
      global life
      life=2
      poi=input("Select your mode (1 or 2): ")
      if poi=="1":
            g1()
            if not g11():
                   life-=1
                   u()
                   print("you are wrong buddy...")
                   print()
                   print(f"❤️   Lives Remaining: {life}")
                   print()
                   w()
                   u()
                   print("What gets smaller every time it takes a bath?")
                   a=input("").lower().strip()
                   i()
                   submit()
                   if a=="soap":
                     u()
                     print("Good..you are correct")
                     i()
                     print(f"❤️   Lives Remaining: {life}")
                     w()
                   else:
                      u()
                      life-=1
                      u()
                      print("you are wrong buddy...")
                      i()
                      print(f"❤️    Lives Remaining: {life}")
                      i()
                      print(f"you are out of game...0 lives remaining...better luck next time")
                      w()
                      u()
                      ho()
                   u()
                   print("2nd..I have a neck, but no head. I have two arms, but no hands. What am I?")
                   p=input("").lower().strip()
                   i()
                   submit()
                   if p=="shirt":
                        u()
                        print("Good..you are correct")
                        i()
                        print(f"❤️  Lives Remaining: {life}")
                        w()
                   else:
                        u()
                        life-=1
                        print("you are wrong buddy...")
                        i()
                        print(f"❤️  Lives Remaining: {life}")
                        i()
                        print(f"you are out of game...0 lives remaining...better luck next time")
                        w()
                        u()
                        ho()
                   
                   u()
                   print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
                   o=input("").lower().strip()
                   i()
                   submit()
                   if o=="swims" :
                          u()
                          print("You won buddy!!...congratulations!!")
                          w()
                          ho()
                   else:
                          u()
                          life-=1
                          print("you are wrong buddy...")
                          i()
                          print(f"you are out of game...0 lives remaining...better luck next time")
                          w()
                          u()
                          ho()
            
            if not g12():
                              life-=1
                              u()
                              print("you are wrong buddy...")
                              i()
                              print(f"❤️  Lives Remaining: {life}")
                              i()
                              w()
                              u()
                              print("2nd..I have a neck, but no head. I have two arms, but no hands. What am I?")
                              p=input("").lower().strip()
                              i()
                              submit()
                              if p=="shirt":
                                    u()
                                    print("Good..you are correct")
                                    i()
                                    print(f"❤️  Lives Remaining: {life}")
                                    i()
                                    w() 
                              else:
                                    u()
                                    print("you are wrong buddy...")
                                    i()
                                    print(f"you are out of game...0 lives remaining...better luck next time")
                                    w()
                                    u()
                                    ho()
                              u()
                              print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
                              o=input("").lower().strip()
                              if o=="swims" :
                                print("You won buddy!!...congratulation!!")
                                w()
                                ho()
                              else:
                                u()
                                life-=1
                                print("you are wrong buddy...")
                                i()
                                print(f"you are out of game...0 lives remaining...better luck next time")
                                w()
                                u()
                                ho()
            
            g13()       
      elif poi=="2":
            g2()
            g22()
uio()
goi()
