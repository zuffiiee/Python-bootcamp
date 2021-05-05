#!/usr/bin/env python
# coding: utf-8

# In[129]:


import random


# In[130]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
            '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[131]:


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank+" of "+self.suit




# In[135]:


class Deck:
    def __init__(self):
        
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                a_card=Card(suit,rank)
                self.all_cards.append(a_card)
                
    def shuffling(self):
        random.shuffle(self.all_cards)
    
    def take_one(self):
        return self.all_cards.pop()
            




# In[163]:


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
       
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)    #for multiple cards
        else: 
            self.all_cards.append(new_cards)    #for single card
            
    def remove_card(self):
        return self.all_cards.pop(0)
    
    def __str__(self):
        return f" {self.name} has {len(self.all_cards)} number of cards."


# In[145]:




# In[173]:


player_one=Player(input("Player one's name: "))
player_two=Player(input("Player two's name: "))
new_deck=Deck()
new_deck.shuffling()

for x in range(26):              #splitting the deck between two
    player_one.add_cards(new_deck.take_one())
    player_two.add_cards(new_deck.take_one())


# In[174]:


game_on=True
rounds = 0


while game_on:

    rounds+=1
    if rounds>400:
        print("Game is getting boring...")
        game_on=False
        break

    print(f"\n***Round {rounds}***")
    
    if len(player_one.all_cards) == 0:
        print(f"{player_one.name} is out of cards.\n{player_two.name} WINS!!!")
        game_on=False
        break
    if len(player_two.all_cards) == 0:
        print(f"{player_two.name} is out of cards.\n{player_one.name} WINS!!!")
        game_on=False
        break
        
    #new round
    one_ontable=[]    #player one's cards on table
    one_ontable.append(player_one.remove_card())
    print(f"{player_one.name[0]}: {one_ontable[-1]}")
        
    two_ontable=[]     #player two's cards on table
    two_ontable.append(player_two.remove_card())
    print(f"{player_two.name[0]}: {two_ontable[-1]}")
        
    at_war=True
        
    while at_war:
            
        if (one_ontable[-1].value) > (two_ontable[-1].value) : 
            player_one.add_cards(one_ontable)
            player_one.add_cards(two_ontable)

            if len(one_ontable) > 5: #to shuffle after winning a war
                print(player_one)
                random.shuffle(player_one.all_cards)
                print(f"{player_one.name} shuffles")
            at_war=False
                
        elif  one_ontable[-1].value < two_ontable[-1].value:
            player_two.add_cards(one_ontable)
            player_two.add_cards(two_ontable)
            
            if len(two_ontable) > 5:     #to shuffle after winning a war
                print(player_two)
                random.shuffle(player_one.all_cards)
                print(f"{player_two.name} shuffles")
                
            at_war=False
                
        else:
            print("!!WAR!!")
            if len(player_one.all_cards) <5 :
                print(f"{player_one.name} don't have enough cards.\n{player_two.name} WINS!!!")
                game_on=False
                break
        
            elif len(player_two.all_cards) <5:
                print(f"{player_two.name} don't have enough cards.\n{player_one.name} WINS!!!")
                game_on=False
                break
                
            else:    #placing 5 cards as war occured
                 for num in range(5):
                    one_ontable.append(player_one.remove_card())
                    two_ontable.append(player_two.remove_card())
        
