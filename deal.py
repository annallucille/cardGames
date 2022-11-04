def random_deal(delt_cards):
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
    card = random.choice(list(cards))
    if card in delt_cards:
        card = random.choice(list(cards))
    else:
        delt_cards.append(card)
        return card

def deal(ammount,hands):
    dealt_cards = []
    for n in range(ammount):
        for hand in hands:
            hand.append(random_deal(dealt_cards))
        n+=1
    return hands