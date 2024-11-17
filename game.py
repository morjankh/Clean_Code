from Matrix import Matrix
import random


class GoldRush(Matrix):
    coin="$"  # add static variables
    wall="wall"
    empty="."
    MIN_COINS_INBOARD=10
    WINNING_SCORE=100
    VALUE_COINS=10



    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.score1 = 0 #change name to score1 becuse we used this name in getattr fun
        self.score2 = 0 # change name
        self.win = ""
        self.coins = 0

    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return

        self.matrix = []
        # elements = [GoldRush.coin, GoldRush.empty, GoldRush.wall] #change to statice variables
        coins = 0

        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_index = random.randint(0, 1)
                    rand_element =  GoldRush.coin if rand_index == 0 else GoldRush.empty #use just the static variables and remove list elemnt
                    self.matrix[i].append(rand_element)
                    if rand_element == GoldRush.coin:
                        coins += 1
                else:
                    self.matrix[i].append(GoldRush.wall)

            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_element =  GoldRush.coin if random.randint(0, 1) == 0 else GoldRush.empty #use just the static variables and remove list elemnt
                self.matrix[i][k] = rand_element
                if rand_element == GoldRush.coin:
                    coins += 1

        self.matrix[0][0] = "player1"
        self.matrix[self.rows - 1][self.cols - 1] = "player2"
        self.coins = coins

        if coins < GoldRush.MIN_COINS_INBOARD: # changed to variable
            return self.load_board()
        else:
            return self.matrix

    def _check_win(self, player):
        player_number = player[-1] #change name
        score = getattr(self, f"score{player_number}")
        if score == GoldRush.WINNING_SCORE: #changed to variable
            self.win = player
            return self.win

    def _check_other_player(self, player):
        otherPlayer = None
        if player == "player1":
            otherPlayer = "player2"
        elif player == "player2":
            otherPlayer = "player1"
        return otherPlayer  #one return
        

    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in ["wall", other_player]:
            if self.matrix[new_row][new_col] == GoldRush.coin:
                self._update_score(player)

            self.matrix[curr_row][curr_col] = "."
            self.matrix[new_row][new_col] = player

        return self._check_win(player)



    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break
        if direction == "down":
            return self._move(curr_row, curr_col, player, 1, 0) # change the fun
        elif direction == "up":
            return self._move(curr_row, curr_col, player, -1, 0)
        elif direction == "right":
            return self._move(curr_row, curr_col, player, 0, 1)
        elif direction == "left":
            return self._move(curr_row, curr_col, player, 0, -1)



    def _update_score(self, player): #change name fun
        player_num = player[-1]
        score_attr = f"score{player_num}"
        setattr(self, score_attr, getattr(self, score_attr) + GoldRush.VALUE_COINS)# change variable
        print(getattr(self, score_attr))
