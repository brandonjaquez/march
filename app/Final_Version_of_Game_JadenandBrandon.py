from __future__ import print_function #imports the function: print_function

choices = [] #initiates the choices

for x in range (0, 9) :  #detects x within the range (0,9)
    choices.append(str(x + 1)) #if detected, add (str(x+1))

playerOneTurn = True #initiates player 1's turn
winner = False #a winner is not yet decided

def printBoard() : #defines printboard
    print( '\n -----') #prints the following. "( '\n -----')" 
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')#prints the following. "( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')" 
    print( ' -----')#prints the following. "" 
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')#prints the following. "( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')" 
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')#prints the following. "( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')" 
    print( ' -----\n')#prints the following. "( ' -----\n')" 

while not winner : #this will keep the game going until there is a winner
    printBoard() #this will keep repeating printBoard

    if playerOneTurn : #checks if the turn belongs to player 1
        print( "Player 1:") #if it does, then print "Player 1:"
    else : #if not...
        print( "Player 2:") #prints "Player 2:"

    try: #when decided if the turn belongs to one of the players, it'll continue with:
        choice = int(input(">> ")) #input for a choice
    except: #if the input does not meet requirements
        print("please enter a valid field") #this will be displayed after
        continue #after displayed, the code will continue on
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O': #decides whether and X or O will be on the gameboard or not
        print("illegal move, plase try again") #if the move tries to overlap, this will be displayed.
        continue #after the move, the game will continue

    if playerOneTurn : #if it is player one's turn, the code will continue. 
        choices[choice - 1] = 'X' #if this is true, an X will be displayed
    else : #if not... 
        choices[choice - 1] = 'O' #if not, an O will be displayed

    playerOneTurn = not playerOneTurn #if it is not player one's turn

    for x in range (0, 3) : #checks to see if X is within (0,3)
        y = x * 3 #if it is then this code will be added.
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) : #if the parameters are correct, a winner will be displayed
            winner = True #winner will be set to true
            printBoard() #printBoard will be executed after
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) : #if the parameters are correct, a winner will be displayed
            winner = True #winner will be set to true
            printBoard() #printBoard will be executed after

    if((choices[0] == choices[4] and choices[0] == choices[8]) or  #if the parameters are correct, a winner will be displayed
       (choices[2] == choices[4] and choices[4] == choices[6])) :  #if the parameters are correct, a winner will be displayed
        winner = True #the winner will be displayed
        printBoard() #after this, the variable, printBoard will be executed. 

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n") #prints whichever player had one the game!