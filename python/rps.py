#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
class HumanPlayer(Player):
    #Task 4
    def move(self):
        return valid_input("Pick a move: ", moves).lower()
    
def valid_input(message, moves):
    while True:
        move = input(message).lower()
        if move in moves:
            return move
        print('Sorry, the input is invalid. '
                    'Please try again!')
        

class ReflectPlayer(Player):
    def __init__(self):
        self.my_next_move = random.choice(moves)

    def move(self):
        return self.my_next_move
    
    def learn(self, my_move, their_move):
        self.my_next_move = their_move
    
    
    
class CyclePlayer(Player):
    def __init__(self):
        self.my_next_move = random.choice(moves)

    def move(self):
        return self.my_next_move
    
    def learn(self, my_move, their_move):
        prev_to_next = {"rock": "paper",
                        "paper": "scissors",
                        "scissors": "rock"}
        
        self.my_next_move = prev_to_next[my_move]
        

    
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        self.p1_score = 0
        self.p2_score = 0
        self.ties = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # For task 3:
        if beats(one=move1, two=move2):
            print("You win this round!")
            self.p1_score += 1

        elif beats(move2, move1):
            print("Player 2 wins this round!")
            self.p2_score += 1

        else:
            print("It's a tie!")
            self.ties += 1
            
        
    def play_game(self):
        print("GAME START!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("***GAME OVER!***")
        self.print_final_score()

    def print_final_score(self):
        # For task 3:
        print(f"Final score: Player 1: {self.p1_score} |",
              f"Player 2: {self.p2_score} | Ties: {self.ties}")
        if self.p1_score > self.p2_score:
            print("---YOU WIN THE GAME!---")
        elif self.p1_score < self.p2_score:
            print("---PLAYER 2 WINS THE GAME!---") 
        else:
            print("---IT'S A TIE!---")
        
        
if __name__ == '__main__':
    # Task 2:
    bots =[RandomPlayer(), CyclePlayer(), ReflectPlayer(), Player()]
    game = Game(HumanPlayer(), random.choice(bots))
    game.play_game()

    # Task 4:
    #print("\nPlaying against RandomPlayer:")
    #game = Game(HumanPlayer(), RandomPlayer())
    #game.play_game()
    
     # Task 5:
    #print("\nPlaying against ReflectPlayer:")
    #game = Game(HumanPlayer(), ReflectPlayer())
    #game.play_game()

    #print("\nPlaying against CyclePlayer:")
    #game = Game(HumanPlayer(), CyclePlayer())
    #game.play_game()
    
    #print("\nPlaying against rock-Player:")
    #game = Game(HumanPlayer(), Player())
    #game.play_game()


    
    

    #!/usr/bin/env python3
import random
import time
import enum

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def valid_input(message, moves):
    while True:
        move = input(message).lower()
        if move in moves:
            return move
        print_pause('Sorry, the input is invalid. '
                    'Please try again!')

class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    
    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])

def print_pause(message, sleep_time=1):
    print(Color.get_color() + message)
    time.sleep(sleep_time)

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
class HumanPlayer(Player):
    def move(self):
        return valid_input("Pick a move: ", moves).lower()
    

class ReflectPlayer(Player):
    def __init__(self):
        self.my_next_move = random.choice(moves)

    def move(self):
        return self.my_next_move
    
    def learn(self, my_move, their_move):
        self.my_next_move = their_move
    
    
    
class CyclePlayer(Player):
    def __init__(self):
        self.my_next_move = random.choice(moves)

    def move(self):
        return self.my_next_move
    
    def learn(self, my_move, their_move):
        prev_to_next = {"rock": "paper",
                        "paper": "scissors",
                        "scissors": "rock"}
        
        self.my_next_move = prev_to_next[my_move]
        

    
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        self.p1_score = 0
        self.p2_score = 0
        self.ties = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(one=move1, two=move2):
            print_pause("You win this round!")
            self.p1_score += 1

        elif beats(move2, move1):
            print_pause("Player 2 wins this round!")
            self.p2_score += 1

        else:
            print_pause("It's a tie!")
            self.ties += 1

    
    def play_game(self):
        print_pause("GAME START!")
        for round in range(1, 4):
            print_pause(f"<<Round {round}>>")
            self.play_round()
        print_pause("***GAME OVER!***")
        self.print_final_score()

    def print_final_score(self):
        print_pause(f"Final score: Player 1: {self.p1_score} | "
                    f"Player 2: {self.p2_score} | Ties: {self.ties}")
        if self.p1_score > self.p2_score:
            print_pause("---YOU WIN THE GAME!---")
        elif self.p1_score < self.p2_score:
            print_pause("---PLAYER 2 WINS THE GAME!---")
        else:
            print_pause("---IT'S A TIE!---")


if __name__ == '__main__':

    bots = [RandomPlayer(), CyclePlayer(), ReflectPlayer(), Player()]
    while True:
        game = Game(HumanPlayer(), random.choice(bots))
        game.play_game()
        user_answer = valid_input("Play again? <y/n>: ", ["y", "n"])
        if user_answer == "n":
            break
    print_pause("Thanks for playing! Good-bye!")

