import random

#A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it

answer =""
choices = ['R','P','S']
random_answer= random.choice(choices)
def repeat():
        global answer
        answer = input("Let's play Rock Paper Scissors \n"
 "choose R for rock \n"
 "choose P for paper \n"
 "choose S for scissors \n")
repeat()        

while(answer not in choices):
    print("Wrong option\n")
   
    repeat()    
else:
    while(answer ==  random_answer):#for a tie
        
        print("A tie \n")
        print("Player {} : CPU {}".format(answer,random_answer))
        repeat()

    else:
         if(answer =="R" and random_answer=="S"): # Rock beats Scissors
            
            print("Player Wins {} : CPU {}".format(answer,random_answer))
         elif(answer =="S" and random_answer=="R"):#rock beats Scissors
             print("Player  {} : CPU  wins{}".format(answer,random_answer))
         elif(answer =="S" and random_answer=="P"):#Scissors beats paper
             print("Player wins  {} : CPU  {}".format(answer,random_answer))  
         elif(answer =="P" and random_answer=="S"):
             print("Player  {} : CPU  wins {}".format(answer,random_answer))  
         elif(answer =="P" and random_answer=="R"):
             print("Player Wins {} : CPU  {}".format(answer,random_answer)) 
         elif(answer =="R" and random_answer=="S"):
             print("Player  {} : CPU  wins {}".format(answer,random_answer))




        
              




