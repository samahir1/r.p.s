moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPleyer(Player):
    def move(self):
        return random.choice(["scissors","paper","rock"])


class ReflectPleyer(Player):
    suk_move = 'rock'

    def move(self):
        return self.suk_move

    def learn(self, my_move, their_move):
        self.suk_move = their_move


class CyclePleyer(Player):
    cy_move = 'rock'

    def move(self):
        return self.cy_move

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.cy_move = 'paper'
        elif my_move == 'paper':
            self.cy_move = 'scissors'
        elif my_move == 'scissors':
            self.cy_move = 'rock'


class HumanPlayer(Player):
    def move(self):
        while True:
            self.user_input = input('rock, paper, scissors? > ')
            if self.user_input in moves:
                break
        return self.user_input


def beats(one, two):
    return ((one == 'rock' and two == 'scissors')
            or (one == 'scissors' and two == 'paper')
            or (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print ("Draw")
        elif beats(move1, move2):
            self.p1_score += 1
            print ("You win")
        else:
            self.p2_score += 1
            print ("Computer wins")
        print(
            f'Score: Player One {self.p1_score} , Player Two {self.p2_score}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def match_rounds(self):
        while True:
            try:
                self.user_input = int(
                    input('How many rounds you want to play? > '))
                break
            except ValueError:
                print("Please Enter a number")
                continue
            else:
                break
        return self.user_input

    def play_game(self):
        self.rounds = self.match_rounds()
        print("Game start!")
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePleyer())
    game.play_game()
