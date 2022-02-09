import random
import time


class Game:
    def __init__(self, names, single_player=False):
        self.names = names
        self.single_player = single_player
        self.board = [' ' for x in range(10)]

    def insertBoard(self, letter, pos):
        self.board[pos] = letter

    def spaceIsFree(self, pos):
        return self.board[pos] == ' '

    @staticmethod
    def isWinner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[6] == le and bo[3] == le) or
        (bo[8] == le and bo[5] == le and bo[3] == le) or
        (bo[9] == le and bo[5] == le and bo[1] == le))

    def playerMove(self, letter="X"):
        run = True
        while run:
            move = input('Please select a position to place an \'%s\' (1-9):  ' %letter)
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if self.spaceIsFree(move):
                        run = False
                        self.insertBoard(letter, move)
                    else:
                        print('This position is already occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')

    @staticmethod
    def selectRandom(li):
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]

    def compMove(self):
        possibleMoves = [x for x, letter in enumerate(self.board) if letter == ' ' and x != 0]
        move = 0
        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = self.board[:]
                boardCopy[i] = let
                if self.isWinner(boardCopy, let):
                    move = i
                    return move

        cornersOpen = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = self.selectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = self.selectRandom(edgesOpen)
        return move

    def isBoardFull(self):
        if self.board.count(' ') > 1:
            return False
        else:
            return True

    def printBoard(self):
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')

    @staticmethod
    def save(name, score):
        try:
            f = open("scores.txt", "r")
        except FileNotFoundError:
            f = open("scores.txt", "w")
            f.close()
            f = open("scores.txt", "r")

        oldScores = {name: score}

        for line in f.readlines():
            sliced = line.strip().split(":")
            n = sliced[0]
            oldScore = int(sliced[1])
            if n == name:
                if score < oldScore:
                    oldScores[n] = score
                    print(n + "has earned a new high score of: " + str(score) + "s")
                else:
                    oldScores[n] = oldScore
            else:
                oldScores[n] = oldScore

        f.close()

        with open("scores.txt", "w") as f:
            for key in oldScores:
                f.write(key + ":" + str(oldScores[key]) + "\n")

    def main(self):
        startTime = time.time()
        print('Welcome to Tic Tac Toe!')
        self.printBoard()
        won = False

        while not (self.isBoardFull()):

            if not (self.isWinner(self.board, 'O')):
                self.playerMove("X")
                self.printBoard()
            else:
                print(self.names[1] + " has won the game!")
                won = self.names[1]
                break

            if not (self.isWinner(self.board, 'X')):

                if self.single_player:
                    move = self.compMove()
                    if move == 0:
                        print('Game is a Tie!')
                    else:
                        self.insertBoard('O', move)
                        print('Computer placed an \'O\' in position', move, ':')
                        self.printBoard()
                else:
                    if not (self.isBoardFull()):
                        self.playerMove("O")
                        self.printBoard()
                    else:
                        break

            else:
                print(self.names[0] + " has won the game!")
                won = self.names[0]
                break

        endTime = time.time() - startTime
        print("Game Completed in: " + str(round(endTime)) + "s")
        if self.isBoardFull() and not won:
            print('Game is a tie!')
        else:
            self.save(won, round(endTime))


def get_name(p):
    name = ""
    while len(name) < 2:
        name = input("Enter player " + str(p) + "\'s name: ")
        if len(name) < 2:
            print("Name must be at least 2 characters")

    return name


def view_highscores():
    try:
        with open("scores.txt", "r") as f:
            file = f.readlines()
            top = []
            for line in file:
                s = line.strip().split(":")
                score = s[1]
                name = s[0]

                if len(top) < 5:
                    top.append((name, score))
                else:
                    m = min(list(map(lambda x: x[1], top)))
                    if score > m:
                        top.sort(key=lambda x: x[1])
                        top[0] = (name, score)

        top.sort(key=lambda x: int(x[1]))
        for x, entry in enumerate(top):
            print(str(x + 1) + ". " + entry[0] + ": " + str(entry[1]) + "s")

    except FileNotFoundError:
        print("No Highscores to Display")


def ask_to_play():
    game_mode = input("Type \"S\" for single player and \"M\" for multiplayer and \"V\" to view top highscores: ")
    if game_mode.lower() == "v":
        view_highscores()

    elif game_mode.lower() == "m":
        single = False
        print('Starting multiplayer Tic Tac Toe')
        p1 = get_name(1)
        p2 = get_name(2)
        names = [p1, p2]
        game = Game(names, single)
        game.main()

    else:
        single = True
        print('Starting singleplayer Tic Tac Toe')
        p1 = get_name("")
        names = [p1, "Computer"]
        game = Game(names, single)
        game.main()


ask_to_play()

while True:
    answer = input('Do you want to play again? (Y/N): ')
    if answer.lower() == 'y' or answer.lower == 'yes':
        ask_to_play()
    else:
        break