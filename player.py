class Player(object):
    
    def hit(self,card_value):
        self.hand.append(card_value)
    
    def hand_value(self):
        sum = 0
        for card in self.hand:
            sum += card[2]
        if self.check_for_ace() and sum <= 11:
            sum += 10
        return sum

    def check_for_ace(self):
        ace = False
        for card in self.hand:
            if card[2] == 1:
                ace = True
        return ace

    def hand_face(self):
        face_list = []
        for card in self.hand:
            face_list.append(card[0])
        return face_list

    def __init__(self):
        self.hand = []
        self.name = 'Player'
        self.money = 0

    def __str__(self):
        cards = self.hand_face()
        hand_string = ' '.join('%-1s' for _ in cards)%tuple(cards)
        return "{}: {} = {}".format(self.name,hand_string,self.hand_value())

class Dealer(Player):
    
    def hidden(self):
        hand = self.hand_face()
        return "Dealer: ? {}".format(hand[1])
    
    def __init__(self):
        self.hand = []
        self.name = 'Dealer'
