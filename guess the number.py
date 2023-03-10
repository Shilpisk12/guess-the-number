n=18
oh=1
print("Game Guess the number")
print("you have 5 guess time")
while(oh<=5):
    num=int((input("enter the number")))
    if num>18:
        print("you guess high please guess low")
    elif num<18:
        print("you guess low please guess high")
    else:
     print("congratulation you guess the right number",num)
     print(oh,"no of guesses you take to finished")
     break
    print(5-oh,"no of guess left")
    oh=oh+1

if (oh>5):
 print("Game over")




