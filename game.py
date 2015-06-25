import sys
import os
import time

from player import Player
from player import Dealer
from card import Deck

class Game(object):

    def setup(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        for _ in range(2):
            self.player.hit(self.deck.next_card())
            self.dealer.hit(self.deck.next_card())

    def player_turn(self):
        player_choice = input("[H]it, [S]tay, or [Q]uit?").lower()
        os.system('clear')

        if player_choice == 'h':
            self.player.hit(self.deck.next_card())
            self.display_info()
            if self.player.hand_value() > 21:
                pass
            else:
                self.player_turn()
        elif player_choice == 's':
            pass
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn

    def dealer_turn(self):
        while self.dealer.hand_value() <= 16:
            self.display_info(True)
            time.sleep(2)
            self.dealer.hit(self.deck.next_card())
    

    def check_for_outcome(self):
        if self.dealer.hand_value() > 21:
            print("Dealer bust! You Win!")
            self.play_again()
        elif self.player.hand_value() > self.dealer.hand_value():
            print("You win!")
        elif self.player.hand_value() < self.dealer.hand_value():
            print("You lose!")
        elif self.player.hand_value() == self.dealer.hand_value():
            print("Push!")

    def check_for_bust(self):
        if self.player.hand_value() > 21:
            print("You bust! You lose!")
            self.play_again()

    def display_info(self,show = False):
        os.system('clear')
        print("Blackjack")
        print("="*20)
        if show:
            print(self.dealer)
        else:
            print(self.dealer.hidden())
        print(self.player)
        print("="*20)
    
    def play_again(self):
        play_again = input("Do you want to play again? [Y]/[N]?").lower()
        if play_again == 'y':
            Game()
        else:
            sys.exit()

    def __init__(self):
        self.setup()
        
        self.display_info()
        self.player_turn()
        self.check_for_bust()
        self.display_info(True)
        self.dealer_turn()
        self.display_info(True)
        self.check_for_outcome()

        self.play_again()

Game()












