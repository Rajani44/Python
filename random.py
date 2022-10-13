import random
number=random.randrange(1,10)
guess=0
count=0
while guess!=number and guess!="exit":
    guess=input("please guess a number b/w 1 and 10.end the game print 'exit:")
    if guess=="exit":
        print("game over")
        break
    guess=int(guess)
    count+=1
    if guess not in range(1,10):
        print("guess number b/w 1 and 9")
    else:
        if count==1:
            print("you won the game")



  OUTPUT:
    
please guess a number b/w 1 and 10.end the game print 'exit:6
you won the game
please guess a number b/w 1 and 10.end the game print 'exit:40
guess number b/w 1 and 9
please guess a number b/w 1 and 10.end the game print 'exit:exit
game over
