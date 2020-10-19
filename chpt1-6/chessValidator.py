#! python3

import sys

def chess_dictionary(chess_board):
    validation={'wking':1,'bking':1,'wqueen':1,'bqueen':1,'wbishop':2,'wrook':2,'wnight':2,'bbishop':2,'brook':2,'bnight':2,'bpawn':8,'wpawn':8}
    pieces={'wking':0,'bking':0,'wqueen':0,'bqueen':0,'wbishop':0,'wrook':0,'wnight':0,'bbishop':0,'brook':0,'bnight':0,'bpawn':0,'wpawn':0}
    
    # Check all positions on chess_board are valid
    for i,j in chess_board.items():
        if not (96 < ord(i[-1]) < 105 and 0 < int(i[:-1]) < 9):
            return False
        pieces[j] = pieces[j] + 1 

    # Check the pieces are within their limits
    for piece in pieces:
        if pieces[piece] > validation[piece]:
            return False
    
    # Check there is one wking & one bking
    if pieces['wking'] == 0 or pieces['bking'] == 0:
        return False

    return True
        
print(chess_dictionary({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '1b':'bpawn'}))