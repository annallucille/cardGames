from deal import deal, random_deal
import random 

cards = {'2':['H', 'D', 'C', 'S'],
        '3':['H', 'D', 'C', 'S'],
        '4':['H', 'D', 'C', 'S'],
        '5':['H', 'D', 'C', 'S'],
        '6':['H', 'D', 'C', 'S'],
        '7':['H', 'D', 'C', 'S'],
        '8':['H', 'D', 'C', 'S'],
        '9':['H', 'D', 'C', 'S'],
        'T':['H', 'D', 'C', 'S'],
        'J':['H', 'D', 'C', 'S'],
        'Q':['H', 'D', 'C', 'S'],
        'K':['H', 'D', 'C', 'S'],
        'A':['H', 'D', 'C', 'S'],}

def round_card_probaility(card, round):
    suit_value ={'S': 10,'H': 1,'D': 1,'C': 1}
    card_value = {'2':2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13,'A': 14}
    
    

def hand_score(hands, round):
    hand_dictionaries =[]
    hand_dictionary = {}
    for hand in hands: 
        for n in range(len(hands)):
            hand_dictionaries.append(hand_dictionary)
            for card in hand:
                value = round_card_probaility(card,round)
                hand_dictionaries[n][card] = value
            n+=1
            
def turn_rules(hand_dictionary, played):
    playable =[]
    for card in hand_dictionary:
        if len(list(played)) == 0:
            string = [*card]
            if string[1] != 'S':
                playable.append(card)
        if len(playable) !=0:
            old = 0
            playing = 0
            for card in playable:
                value = hand_dictionary[card]
                if value > old:
                    old = value
                    playing = card
            return playing
    for card in hand_dictionary:
        string = [*card]
        if string[1] in played:
            playable.append(card)
    if len(playable) != 0: 
        for card in playable:
            string = [*card]
            for i in played[string[1]]:
                
def turn(hands, player):
    for hand in hands:
        if hand != player:
            card = random.radient(hand)
            string = [*card]
