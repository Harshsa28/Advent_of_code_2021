





def get_coor(pos1, score1, pos2, score2):
    assert(1 <= pos1 <= 10)
    assert(0 <= score1 <= 30)
    assert(1 <= pos2 <= 10)
    assert(0 <= score2 <= 30)
    return (31*(pos1-1)+score1, 31*(pos2-1)+score2)



def get_pos_score(i):
    pos = int(i / 31)+1
    score = int(i % 31)
    return pos, score


def is_coor_winning(x, y):
    _, score_x = get_pos_score(x)
    _, score_y = get_pos_score(y)
    return score_x > 20 or score_y > 20


def go_forward(pos, num):
    new_pos = (pos + num) % 10
    if new_pos == 0:
        new_pos = 10
    return new_pos

def get_unis(board):
    p = 0
    w = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if is_coor_winning(i, j):
                w += board[i][j]
            else:
                p += board[i][j]
    return (p, w)


class Player:
    def __init__(self, num):
        self.num = num
    
    def play(self, board):
        for k in range(3):
            new_board_1 = [[0 for j in range(len(board[i]))] for i in range(len(board))]
            assert(len(board) == len(new_board_1) and len(board[0]) == len(new_board_1[0]))
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if is_coor_winning(i, j):
                        new_board_1[i][j] += board[i][j]
                    else:
                        pos_x, score_x = get_pos_score(i)
                        pos_y, score_y = get_pos_score(j)
                        
                        if self.num == 1:
                            pos_x_1 = go_forward(pos_x, 1)
                            c = get_coor(pos_x_1, score_x, pos_y, score_y)
                            new_board_1[c[0]][c[1]] += board[i][j]

                            pos_x_1 = go_forward(pos_x, 2)
                            c = get_coor(pos_x_1, score_x, pos_y, score_y)
                            new_board_1[c[0]][c[1]] += board[i][j]

                            pos_x_1 = go_forward(pos_x, 3)
                            c = get_coor(pos_x_1, score_x, pos_y, score_y)
                            new_board_1[c[0]][c[1]] += board[i][j]
                        
                        elif self.num == 2:
                            pos_y_1 = go_forward(pos_y, 1)
                            c = get_coor(pos_x, score_x, pos_y_1, score_y)
                            new_board_1[c[0]][c[1]] += board[i][j]

                            pos_y_1 = go_forward(pos_y, 2)
                            c = get_coor(pos_x, score_x, pos_y_1, score_y)
                            new_board_1[c[0]][c[1]] += board[i][j]

                            pos_y_1 = go_forward(pos_y, 3)
                            c = get_coor(pos_x, score_x, pos_y_1, score_y)
                            new_board_1[c[0]][c[1]] += board[i][j]
                        
                        else:
                            raise("unexpected case")
            board = new_board_1
        
        new_board_2 = [[0 for j in range(len(new_board_1[i]))] for i in range(len(new_board_1))]
        assert(len(new_board_1) == len(new_board_2) and len(new_board_1[0]) == len(new_board_2[0]))
        for i in range(len(new_board_1)):
            for j in range(len(new_board_1[i])):
                if is_coor_winning(i, j):
                    new_board_2[i][j] += new_board_1[i][j]
                else:
                    pos_x, score_x = get_pos_score(i)
                    pos_y, score_y = get_pos_score(j)

                    if self.num == 1:
                        score_x_1 = score_x + pos_x
                        c = get_coor(pos_x, score_x_1, pos_y, score_y)
                        new_board_2[c[0]][c[1]] += new_board_1[i][j]
                    elif self.num == 2:
                        score_y_1 = score_y + pos_y
                        c = get_coor(pos_x, score_x, pos_y, score_y_1)
                        new_board_2[c[0]][c[1]] += new_board_1[i][j]
                    else:
                        raise("unexpected case")

        return new_board_2

class Game:
    def __init__(self, pos1, pos2):
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.board = [[0 for _ in range(310)] for _ in range(310)]
        coor = get_coor(pos1, 0, pos2, 0)
        self.board[coor[0]][coor[1]] = 1

    def play(self):
        while True:
            self.board = self.player1.play(self.board)
            print("p1 played")
            self.board = self.player2.play(self.board)
            print("p2 played")
            print(f"total universes are {get_unis(self.board)}")
            if self.is_game_over():
                return self.calc_wins()

    def is_game_over(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0 and not is_coor_winning(i, j):
                    return False
        return True

    def calc_wins(self):
        wins1 = 0
        wins2 = 0
        #print(self.board)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                is_1_winning = is_coor_winning(i, i) # intentional i, i
                is_2_winning = is_coor_winning(j, j) # intentional j, j
                #assert(not is_1_winning or not is_2_winning)
                if is_1_winning:
                    wins1 += self.board[i][j]
                if is_2_winning:
                    wins2 += self.board[i][j]
        return (wins1, wins2)



if __name__=="__main__":
    game = Game(6, 9)
    print(game.play())
