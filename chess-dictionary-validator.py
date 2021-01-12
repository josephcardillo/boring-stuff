valid_board = {
    'a1': 'brook',
    'a2': 'bpawn',
    'b1': 'bknight',
    'b2': 'bpawn',
    'c1': 'bbishop',
    'c2': 'bpawn',
    'd1': 'bking',
    'd2': 'bpawn',
    'e1': 'bqueen',
    'e2': 'bpawn',
    'f1': 'bbishop',
    'f2': 'bpawn',
    'g1': 'bknight',
    'g2': 'bpawn',
    'h1': 'brook',
    'h2': 'bpawn',
    'a3': ' ',
    'a4': ' ',
    'a5': ' ',
    'a6': ' ',
    'b3': ' ',
    'b4': ' ',
    'b5': ' ',
    'b6': ' ',
    'c3': ' ',
    'c4': ' ',
    'c5': ' ',
    'c6': ' ',
    'd3': ' ',
    'd4': ' ',
    'd5': ' ',
    'd6': ' ',
    'e3': ' ',
    'e4': ' ',
    'e5': ' ',
    'e6': ' ',
    'f3': ' ',
    'f4': ' ',
    'f5': ' ',
    'f6': ' ',
    'g3': ' ',
    'g4': ' ',
    'g5': ' ',
    'g6': ' ',
    'h3': ' ',
    'h4': ' ',
    'h5': ' ',
    'h6': ' ',
    'a7': 'wpawn',
    'a8': 'wrook',
    'b7': 'wpawn',
    'b8': 'wknight',
    'c7': 'wpawn',
    'c8': 'wbishop',
    'd7': 'wpawn',
    'd8': 'wking',
    'e7': 'wpawn',
    'e8': 'wqueen',
    'f7': 'wpawn',
    'f8': 'wbishop',
    'g7': 'wpawn',
    'g8': 'wknight',
    'h7': 'wrook',
    'h8': 'wpawn'
    }

invalid_board = {
    'r4': 'brook',
    'a2': 'bpawn',
    'b1': 'bknight',
    'b2': 'bpawn',
    'c1': 'bbishop',
    'c2': 'bpawn',
    'd1': 'bking',
    'd2': 'bpawn',
    'e1': 'bqueen',
    'e2': 'bpawn',
    'f1': 'bbishop',
    'f2': 'bpawn',
    'g1': 'bknight',
    'g2': 'bpawn',
    'h1': 'brook',
    'h2': 'bpawn',
    'a3': 'brook',
    'a4': ' ',
    'a5': ' ',
    'a6': ' ',
    'b3': ' ',
    'b4': ' ',
    'b5': ' ',
    'b6': ' ',
    'c3': ' ',
    'c4': ' ',
    'c5': ' ',
    'c6': ' ',
    'd3': ' ',
    'd4': ' ',
    'd5': ' ',
    'd6': ' ',
    'e3': ' ',
    'e4': ' ',
    'e5': ' ',
    'e6': ' ',
    'f3': ' ',
    'f4': ' ',
    'f5': ' ',
    'f6': ' ',
    'g3': ' ',
    'g4': ' ',
    'g5': ' ',
    'g6': ' ',
    'h3': ' ',
    'h4': ' ',
    'h5': ' ',
    'h6': 'wpawn',
    'a7': 'wpawn',
    'a8': 'wrook',
    'b7': 'wpawn',
    'b8': 'wknight',
    'c7': 'wpawn',
    'c8': 'wbishop',
    'd7': 'wpawn',
    'd8': 'wking',
    'e7': 'wpawn',
    'e8': 'wqueen',
    'f7': 'wpawn',
    'f8': 'wbishop',
    'g7': 'wpawn',
    'g8': 'wknight',
    'h7': 'wrook',
    'h8': 'wpawn'
    }

def is_valid_chess_board(game_board, valid_board):
    board_status = ' '
    pieces_status = []
    for k, v in game_board.items():
        if k in valid_board.keys():
            board_status = 'VALID'
        else:
            board_status = 'INVALID'
        if v in valid_board.values():
            board_status = 'VALID'
        else:
            board_status = 'INVALID'
    if board_status == 'VALID':
        num_of_pieces = {}
        for v in game_board.values():
            num_of_pieces.setdefault(v, 0)
            num_of_pieces[v] += 1
        for k, v in num_of_pieces.items():
            if k in ('brook', 'wrook', 'bknight', 'wknight', 'bbishop', 'wbishop') and v <= 2:
                pieces_status.append('VALID')
            elif k in ('bking', 'wking', 'bqueen', 'wqueen') and v <= 1:
                pieces_status.append('VALID')
            elif k in ('bpawn', 'wpawn') and v <= 8:
                pieces_status.append('VALID')
            elif k in (' ') and v <= 32:
                pieces_status.append('VALID')
            else:
                pieces_status.append('INVALID')
        if 'INVALID' in pieces_status:
            return 'INVALID'
        else:
            return 'VALID'

test1 = is_valid_chess_board(valid_board, valid_board)
print(test1)
test2 = is_valid_chess_board(invalid_board, valid_board)
print(test2)