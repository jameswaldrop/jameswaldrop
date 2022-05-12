import random
import time
import colorama
from colorama import Fore


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        moves = ['rock', 'paper', 'scissors']
        return random.choice(moves)


class RepeatPlayer(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    def move(self):
        while True:
            moves = ['rock', 'paper', 'scissors']
            move = input("rock, paper or scissors?").lower()
            if move in moves:
                return move
            print(f"The move {move} is invalid. Try again!")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    scoreP1 = 0
    scoreP2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print(f'{Fore.GREEN}***** Player 1 won the round! *****\n')
            self.scoreP1 += 1
        elif beats(move2, move1):
            print(f'{Fore.GREEN}***** Player 2 won the round! *****\n')
            self.scoreP2 += 1
        else:
            print(f'{Fore.GREEN}***** No one won the round! *****\n')
            print(f'Player1 Score:  {self.scoreP1} Player 2 Score:\
        {self.scoreP2}')

    def play_game(self):
        while True:
            try:
                rounds = int(input('Enter the number of rounds you want\
to play: '))
                break
            except ValueError:
                print('Please enter a valid number')
                self.play_game()

        print("*****Game start!*****\n")
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()

        print("*****Game over*****!\n")
        print(f'{Fore.BLUE}Final Scores:\nPlayer 1: ' + str(self.scoreP1) +
              '\nPlayer 2: ' + str(self.scoreP2) + '\n')
        if self.scoreP1 > self.scoreP2:
            print(f'{Fore.GREEN}Player 1 won the game!')
        elif self.scoreP1 < self.scoreP2:
            print(f'{Fore.GREEN}Player 2 won the game!')
        else:
            print(f'{Fore.GREEN}***** Game tie! *****')


if __name__ == '__main__':
    mode = {
        'human': HumanPlayer(),
        'reflect': ReflectPlayer(),
        'cycle': CyclePlayer(),
        'random': RandomPlayer(),
        'repeat': RepeatPlayer()
    }
    while True:
        print(f'{Fore.GREEN}*****ROCK, PAPER, SCISSORS*****,\n')
        time.sleep(1)

        choice = input(
            'SELECT A PLAYER MODE:\n -Random\n -Reflect\n -Repeat\n'
            ' -Cycle\n').lower()
        if choice in mode:
            game = Game(mode['human'], mode[choice])
            game.play_game()
        else:
            print(f'{Fore.GREEN}Invalid player. Try again!')
