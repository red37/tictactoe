import sys

chkbrd =[" "," "," "," "," "," "," "," "," "]

player1 = "O" #use dictionary keys instead
player2= "X"

print("Welcome to tictactoe.Player 1 choose hugs or kisses")
choice1= str(input())

try:
    if choice1.upper() == "HUGS":
        player1 = "O"
        player2= "X"
        print("Player 2 is Kisses")

    elif choice1.upper() == "KISSES":
        player2 = "O"
        player1= "X"
        print("Player 2 is hugs")
    else:
         print("You did not enter a valid choice my friend.")
         print("Now both player2 and your mom hates you.")
         print("Also game over asshat")
         sys.exit(0)
            
except ValueError:
         print("Game over asshat")
         sys.exit(0)
            
print("Player 2 quit complaining. Life is also not fair.")            
print("Press Enter idiot")
input()
print("Here is the layout,choices and positioning of the game. Learn it, memorize it")
print("""
            tl|tc|tr
            ---------    
            ml|mc|mr
            ---------
            dl|dc|dr
            """)


def get_my_position(move):
    num = 9
    if move.lower() == "tl":
    	num=0
    elif move.lower() == "tc":
        num=1
    elif move.lower()== "tr":
        num=2
    elif move.lower()== "ml":
        num=3       
    elif move.lower()== "mc":
        num=4        
    elif move.lower() == "mr":
        num=5       
    elif move.lower()== "dl":
        num=6        
    elif move.lower()== "dc":
        num=7        
    elif move.lower() == "dr":
        num=8
    else:
    	sys.exit()
        
    return num
    
    
    
def board():
    print("""
            {a} | {b} | {c}
            ---------    
            {d} | {e} | {f}
            ---------
            {g} | {h} | {i}
            """.format(a=chkbrd[0],b=chkbrd[1],c=chkbrd[2],d=chkbrd[3],e=chkbrd[4],f=chkbrd[5],g=chkbrd[6],h=chkbrd[7],i=chkbrd[8])) 

def input_into_board(player,position):
    chkbrd[position]= player

def check_win():
    if chkbrd[0]=="O" and chkbrd[1]=="O" and chkbrd[2]=="O" or chkbrd[3]=="O" and chkbrd[4]=="O" and chkbrd[5]=="O"  or chkbrd[6]=="O" and chkbrd[7]=="O" and chkbrd[8]=="O":
        print (player2 + " wins straightfowardly")
        sys.exit()
    elif chkbrd[0]=="O" and chkbrd[3]=="O" and chkbrd[6]=="O" or chkbrd[1]=="O" and chkbrd[4]=="O" and chkbrd[7]=="O"  or chkbrd[2]=="O" and chkbrd[5]=="O" and chkbrd[8]=="O":
        print (player2 + " wins straightfowardly")   
        sys.exit()
    elif chkbrd[0]=="O" and  chkbrd[4]=="O" and chkbrd[8] == "O" or chkbrd[2]=="O" and  chkbrd[4]=="O" and chkbrd[6] == "O":
        print (player2 + " wins you crisscrossing bastard")
        sys.exit()
    elif chkbrd[0]=="X" and chkbrd[1]=="X" and chkbrd[2]=="X" or chkbrd[3]=="X" and chkbrd[4]=="X" and chkbrd[5]=="X"  or chkbrd[6]=="X" and chkbrd[7]=="X" and chkbrd[8]=="X":
        print (player2 + " wins straightfowardly")
        sys.exit()
    elif chkbrd[0]=="X" and chkbrd[3]=="X" and chkbrd[6]=="X" or chkbrd[1]=="X" and chkbrd[4]=="X" and chkbrd[7]=="X" or chkbrd[2]=="X" and chkbrd[5]=="X" and chkbrd[8]=="X":
        print (player2 + " wins straightfowardly")   
        sys.exit()
    elif chkbrd[0]=="X" and  chkbrd[4]=="X" and chkbrd[8] == "X" or chkbrd[2]=="X" and  chkbrd[4]=="X" and chkbrd[6] == "X":
        print (player2 + " wins you crisscrossing bastard")
        sys.exit()
    else:
        pass

for i in range(0,9):
    if i%2 == 0:    
        print("player1 make move. Input the position")#use try to control what is inputted
        move=input()
        print (get_my_position(move))
        move= int(get_my_position(move))
        global player1
        input_into_board(player1,move)
        board()
        check_win()
    else:
        print("player2 make move. Input the position")
        move=input()
        print (get_my_position(move))
        move= int(get_my_position(move))
        global player2
        input_into_board(player2,move)
        board()
        check_win()



    






    