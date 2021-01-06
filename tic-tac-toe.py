class Tictactoe(object):
    game_board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
                  'ML': ' ', 'MM': ' ', 'MR': ' ',
                  'BL': ' ', 'BM': ' ', 'BR': ' '}

    def print_board(self, game_board):
        print(game_board['TL'] + '|' + game_board['TM'] + '|' + game_board['TR'])
        print('-+-+-')
        print(game_board['ML'] + '|' + game_board['MM'] + '|' + game_board['MR'])
        print('-+-+-')
        print(game_board['BL'] + '|' + game_board['BM'] + '|' + game_board['BR'])

    def player1_pick(self):
        while self.player1_pick != 'X' and self.player1_pick != 'O':
            self.player1_pick = input("Player 1, choose X or O > ")
        print(f"Player 1 is > {self.player1_pick}")
        return self.player1_pick

    def player2_pick(self, player1_pick):
        if self.player1_pick == 'X':
            self.player2_pick = 'O'
        else:
            self.player2_pick = 'X'
        print(f"Player 2 is > {self.player2_pick}")
        return self.player2_pick

    def player1_move(self):
        self.player1_move = input(f"Player 1 > ")
        print(f"Player 1 move is > {self.player1_move}")
        return self.player1_move

    def player2_move(self):
        self.player2_move = input(f"Player 2 > ")
        print(f"Player 2 move is > {self.player2_move}")
        return self.player2_move

    def update_game_board(self, game_board, player_move, player_pick):
        self.player_move = player_move
        self.game_board = game_board
        self.player_pick = player_pick
        self.game_board[self.player_move] = self.player_pick
        # print(self.game_board)
        # print(self.print_board)
        return self.game_board
    
    win_combinations = [['X', ' ', ' ',
                         'X', ' ', ' ',
                         'X', ' ', ' '],
                        [' ', 'X', ' ',
                         ' ', 'X', ' ',
                         ' ', 'X', ' '],
                        [' ', ' ', 'X',
                         ' ', ' ', 'X',
                         ' ', ' ', 'X'],
                        ['X', ' ', ' ',
                         ' ', 'X', ' ',
                         ' ', ' ', 'X'],
                        [' ', ' ', 'X',
                         ' ', 'X', ' ',
                         'X', ' ', ' '],
                        ['X', 'X', 'X',
                         ' ', ' ', ' ',
                         ' ', ' ', ' '],
                        [' ', ' ', ' ',
                         'X', 'X', 'X',
                         ' ', ' ', ' '],
                        [' ', ' ', ' ',
                         ' ', ' ', ' ',
                         'X', 'X', 'X']]


new_game = Tictactoe()
board = new_game.game_board
# new_print_board = new_game.print_board(board)
new_player1_pick = new_game.player1_pick()
new_player2_pick = new_game.player2_pick(new_player1_pick)

while list(game_board.values())
for i in range(9):


new_player1_move = new_game.player1_move()
updated_game_board = new_game.update_game_board(board, new_player1_move, new_player1_pick)
update_print_board = new_game.print_board(board)
new_player2_move = new_game.player2_move()
updated_game_board = new_game.update_game_board(board, new_player2_move, new_player2_pick)
update_print_board = new_game.print_board(board)



