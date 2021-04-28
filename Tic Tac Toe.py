#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import clear_output


# In[3]:


test_board =['#','X','O','X','O','X','O','X','O','X']
refer_board = ['#','1','2','3','4','5','6','7','8','9']
board1= [' ']*10


# In[5]:


def display_board(b):
    row1 = '  '+b[1]+' | '+b[2]+' | '+b[3] 
    row2 = '  '+b[4]+' | '+b[5]+' | '+b[6] 
    row3 = '  '+b[7]+' | '+b[8]+' | '+b[9] 
    hdash= ' '+'---+---+---'
    print(row1+'\n'+hdash+'\n'+row2+'\n'+hdash+'\n'+row3)


# In[7]:


def player_input():
    p1= '#'
    ch=['X','O']
    while p1 not in ['X','O']:
        p1= input('Hey Player1! Wanna be X or O?') #player1 choice
        if p1 not in ['X','O']:
            clear_output()
            print('---- Wrong input -----')
        else:
            print('Player1 is ' + p1)
            ch.remove(p1) #removing p1 to get player 2's choice
            print('Player2 is '+ch[0])
            
    return (p1,ch[0])


# In[8]:


import random

def choose_first():
    return  random.randint(1,2)


# In[9]:


def replay():
    play=input("Do you want to play again? Y or N?")
    if play=='Y':
        return True
    else:
        return False


# In[10]:


def space_check(board, position):
    return board[position] == ' '


# In[27]:


def player_choice(board):
    pos=int(input("Choose your next position to place your marker: "))
    return pos


# In[12]:


def place_marker(board, marker, position):
    board[position] = marker


# In[24]:


def win_check(b,mark):
    return((b[1] == b[2] == b[3] == mark) or (b[4] == b[5] == b[6] == mark) or (b[7] == b[8] == b[9] == mark) or
          (b[1] == b[4] == b[7] == mark) or (b[2] == b[5] == b[8] == mark) or (b[3] == b[6] == b[9] == mark) or
          (b[1] == b[5] == b[9] == mark) or (b[7] == b[5] == b[3] == mark))


# In[36]:


def the_game(board1,gp,marker):
            display_board(board1)
            print("\nPlayer"+str(gp)+'\'s turn....')
            pos=player_choice(board1)
            while space_check(board1,pos) == False:
                print("This position is already filled") 
                pos= player_choice(board1)
    
            place_marker(board1, marker[gp], pos)
            


# In[ ]:





# In[40]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    ans=input("Are you ready to play? Y or N :  ")
    if ans=='Y':
        gameon=True
    elif ans=='N':
        print("See you next time!")
        break
    else:
        print('---Wrong input---')

    while gameon:
        board1= [' ']*10
        plyrs=[1,2]
        count=0
        p1mark,p2mark = player_input()
        marker={1:p1mark,2:p2mark}
        clear_output()
        print("So Player1 is " + p1mark +" and Player2 is " +p2mark)
        
        first= choose_first()
        plyrs.remove(first)
        second=plyrs[0]
        print("Let Player" + str(first) + " start the game.")
        
        print("\n This is how our board looks like.")
        
        while count<10:
            if count>0:
                clear_output()
            print("\n **Select the required grid in accordance with the number marked.")
            display_board(refer_board)
            print("\nPlace your marker here..")
            
            #Player first Turn
            
            the_game(board1,first,marker)
            count=count+1
            if count>=5 and win_check(board1,marker[first]):
                display_board(board1)
                print("\nPlayer "+str(first)+' WON the game!!!!')
                break
              
            if count==9: #Board full
                print("\n--GAME OVER--\n")
                break
            # Player second turn
                  
            the_game(board1,second,marker)
            count=count+1
            if count>5 and win_check(board1,marker[second])==True:
                display_board(board1)
                print("\nPlayer "+str(second)+' WON the game!!!!')
                break
            
            #pass
            
        gameon = False
    if not replay():
        print("Thanks for playing!")
        break
    else:
        gameon = True
        


# In[ ]:




