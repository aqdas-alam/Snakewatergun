import random
# snake water gun or rock paper scissors
def gameWin(comp,you):
    #If two values are equal,declare a tie!
   if comp==you:
      return None
   # check for all possibilities when computer choose s
   elif comp=='s':
      if you=='w':
         return False
   elif you=='g':
      return True
   # check for all possibilities when computer choose w
   elif comp=='w':
      if you=='g':
         return False
      elif you=='s':
         return True
      #check for all possibilities when computer choose g
      elif comp=='g':
         if you=='s':
            return False
         elif you=='w':
            return True
         
print("Comp turn:Snake(s) water(w) or gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
   comp='s'
elif randNo==2:
   comp='w'
elif randNo==3:
   comp='g'
you=input("Your turn: snake(s) water(w) or gun(g)?")
a=gameWin(comp,you)

print(f"computer chose {comp}")

print(f"you chose {you}")
if a==None:
   print("The game is a tie!")
elif a:
   print("You win!")
else:
   print("You lose!")






