import random
l=["rock","scissor","paper"]
'''
 rock vs paper:- paper win
 rock vs scissor:-rock win
 paper vs scissor:- scissor win
'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start....
1 YES
2 NO
         '''))
    if uc==1:
     for a in range(1,6):
         userinput=int(input('''
1 rock
2 scissor
3 paper 
          '''))
         if userinput==1:
             uchoice="rock"
         elif userinput==2:
             uchoice="scissor"
         elif userinput==3:
             uchoice="paper"
         cchoice=random.choice(l)
         if cchoice==uchoice:
             print("computer choice :- ",cchoice)
             print("your choice :-" , uchoice)
             print("game draw")

         elif (uchoice=="rock" and cchoice=="scissor") or (uchoice
             =="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
             print("computer choice :-", cchoice)
             print("your choice :-", uchoice)
             print("you win")
             ucount=ucount+1
         else:
             print("computer choice :-", cchoice)
             print("your choice :-", uchoice)
             print("computer win")
             ccount=ccount+1
     if ucount==ccount:
        print("final game draw")
     elif ucount>ccount:
        print(" final game you win",ucount)
     else:
        print("final game computer  win",ccount)
    else:
        break;
