import random
import sys

print('ROCK,PAPER,SCISSOR')
#these variable keep track of the number of wins,losses and ties
wins=0
losses=0
ties=0
# the main game loop
while True:
  print('%s wins,%s losses,%s ties\n\n'%(wins,losses,ties))
  break
while True:
  print('enter_the_move (r)ock,(p)aper,(s)cissors or quit')
  break
playerMove=input
if playerMove=='q':
       sys.excit()
#quit the program
elif playerMove=='r':
   print('rock')
elif playerMove=='p':
   print('paper')
elif playerMove=='s':
   print('scissors')
 #break out of the player input loop
print('type one of r,p,s or q')
   #display what the player choose
if playerMove=='r':
   print('ROCK versus.....')
elif playerMove=='p':
   print('PAPER versus...')
elif playerMove=='s':
   print('SCISSORS versus...')
      #display what computer chooose
randomNumber=random.randint(1,3)
if randomNumber==1:
    computerMove='r'
print('ROCK')
if randomNumber==2:
    compuuterMove='p'
print('PAPER')
if randomNumber==3:
    computerMove='s'
print('SCISSORS')

#NO ERROR IN CODE
#display and record the win/loss/tie
if playerMove==computerMove:
  print('it is a tie!')
  ties=ties+1
elif playerMove=='r' and computerMove=='s':
  print('you win!')
  wins=wins+1
elif playerMove=='p' and computerMove== 'r': 
  print('you win!')
  wins=wins+1
elif playerMove=='s' and computerMove=='p':
  print('you win!')
  wins=wins+1
elif playerMove=='r' and computerMove=='p':
  print('you loss!')
  losses=losses+1
elif playerMove=='p' and computerMove=='s':
  print('you loss!')
  losses=losses+1
elif playerMove=='s' and computerMove=='r':
  print('you lose!')
  losses=losses+1
  
    


