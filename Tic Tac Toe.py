#Tick Tack Toe
import random
print("Enter 1 to choose X and Enter 2 to choose O")
c=int(input("Enter your choice: "))
a=[0,0,0,0,0,0,0,0,0]
l=[0,1,2,3,4,5,6,7,8]
l1=[]
l2=[]
print("Rules are as the traditional game, Just use the grid to enter your choice")
wnum=[[0,1,2],[3,4,5],[6,7,8],[2,4,6],[2,5,8],[1,4,7],[0,3,6],[0,4,8]]
while 0 in a:
      print("Enter the number to pick your spot")
      print("[ 0 , 1 , 2  \n 3 , 4 , 5 \n 6  ,7 ,8 ]")
      z=int(input("Enter your pick: "))
      if z not in l:
            print("That spot is already taken")
            print("[")
            f=0
            for i in a:
                  if i==0:
                        print("-",end="      ")   
                  elif i==1:
                         print("X",end="       ")
                  elif i==2:
                        print("O",end="       ")
                  f+=1
                  if f%3==0:
                        print()
            print("]")
            for j in range(167):
                  print("-",end="")
            print()
      else:
            l.remove(z)
            l1.append(z)
            l1.sort()
            if len(l)>0:
                  q=random.choice(l)
                  l2.append(q)
                  l2.sort()
                  l.remove(q)
            if c==1:
                  a[z]=1
                  a[q]=2
            else:
                  a[z]=2
                  a[q]=1
            f=0
            for j in wnum:
                  s=0
                  for i in l1:
                        if i in j:
                              s+=1
                              if s==3:
                                    print("You won")
                                    break
                  if s==3:
                        break
            print("[")
            for i in a:
                  if i==0:
                        print("-",end="      ")   
                  elif i==1:
                         print("X",end="       ")
                  elif i==2:
                        print("O",end="       ")
                  f+=1
                  if f%3==0:
                        print()
            print("]")
            
            if s==3:
                  break
            for j in wnum:
                  f=0
                  for k in l2:
                        if k in j:
                              f+=1
                              if f==3:
                                    print("Computer won")
                                    break
                  if f==3:
                        break
            
            if f==3:
                  break
            if len(l)==0:
                  print("Its a draw")            
            for j in range(167):
                  print("-",end="")
            print()
      
            
      
