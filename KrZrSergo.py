# РљСЂРµСЃС‚РёРєРё-РЅРѕР»РёРєРё. РљРѕРјРїСЊСЋС‚РµСЂ РїСЂРѕС‚РёРІ РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ

# Р“Р»Р°Р±Р°Р»СЊРЅС‹Рµ РєРѕРЅСЃС‚Р°РЅС‚С‹
X="X"
O="O"
EMPTY=" "
TIE = "РќРёС‡СЊСЏ"
NUM_SQUARES = 9

def display_instruckt():

    """Р’С‹РІРѕРґРёС‚ РёРЅСЃС‚СЂСѓРєС†РёСЋ РґР»СЏ РёРіСЂРѕРєР°"""
    print(
        """
        Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ РІ РёРіСЂСѓ РєСЂРµСЃС‚РёРєРё-РЅРѕР»РёРєРё.
        Р’РІРµРґРёС‚Рµ С†РёС„СЂСѓ РѕС‚ 0 РґРѕ 8:
        0 | 1 | 2
        - - - - -
        3 | 4 | 5
        - - - - -
        6 | 7 | 8

        РџСЂРёРіРѕС‚РѕРІСЊС‚РµСЃСЊ Рє Р±РѕСЋ! \n

        """
        )

def ask_yes_no(question):
    """Р—Р°РґР°РµС‚ РІРѕРїСЂРѕСЃ СЃ РѕС‚РІРµС‚РѕРј РґР° РёР»Рё РЅРµС‚"""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response

def ask_number(question, low, high):
    """РџСЂРѕСЃРёС‚ РІРЅРµСЃС‚Рё С‡РёСЃР»Рѕ РёР· РґРёР°РїР°Р·РѕРЅР°."""
    response = None
    while response not in range(low, high):
        response=int(input(question))
    return response

def pieces():
    """РћРїСЂРµРґРµР»СЏРµС‚ РїСЂРёРЅР°РґР»РµР¶РЅРѕСЃС‚СЊ РїРµСЂРІРѕРіРѕ С…РѕРґР°"""
    go_first = ask_yes_no("РҐРѕС‡РµС€СЊ РѕСЃС‚Р°РІРёС‚СЊ С…РѕРґ Р·Р° СЃРѕР±РѕР№? (y/n): ")
    if  go_first=="y":
        print("РРіСЂР°Р№ РїРµСЂРІС‹Р№. РРіСЂР°Р№ - РєСЂРµСЃС‚РёРєР°РјРё.")
        human = X
        computer = O
    else:
        print("РљРѕРјРїСЊСЋС‚РµСЂ Р±СѓРґРµС‚ С…РѕРґРёС‚СЊ РїРµСЂРІС‹Рј.")
        human = O
        computer = X
    return computer, human
def new_board():
    """РЎРѕР·РґР°РµС‚ РЅРѕРІСѓСЋ РёРіСЂРѕРІСѓСЋ РґРѕСЃРєСѓ"""
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """РћС‚РѕР±СЂР°Р¶Р°РµС‚ РёРіСЂРѕРІСѓСЋ РґРѕСЃРєСѓ РЅР° СЌРєСЂР°РЅРµ"""

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "_________")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "_________")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """РЎРѕР·РґР°РµС‚ СЃРїРёСЃРѕРє РґРѕСЃС‚СѓРїРЅС‹С… С…РѕРґРѕРІ"""
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """РѕРїСЂРµРґРµР»СЏРµС‚ РїРѕР±РµРґРёС‚РµР»СЏ РІ РёРіСЂРµ"""
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] ==board[row[1]] ==board[row[2]] !=EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """РџРѕР»СѓС‡Р°РµС‚ С…РѕРґ С‡РµР»РѕРІРµРєР°"""
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move= ask_number("РўРІРѕР№ С…РѕРґ. Р’С‹Р±РµСЂРё РѕРґРЅРѕ РёР· РїРѕР»РµР№ (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("РџРѕР»Рµ Р·Р°РЅСЏС‚Рѕ, РІС‹Р±РµСЂРё РґСЂСѓРіРѕРµ РїРѕР»Рµ.\n")
    return move

def computer_move(board, computer, human):

    """Р”РµР»Р°РµС‚ С…РѕРґ Р·Р° РєРѕРјРїСЊСЋС‚РµСЂРЅРѕРіРѕ РїСЂРѕС‚РёРІРЅРёРєР°"""
    board=board[:]

    # РџРѕР»СЏ РѕС‚ Р»СѓС‡С€РµРіРѕ Рє Р»СѓС‡С€РµРјСѓ
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print("РЇ РІС‹Р±РµСЂРёСѓ РїРѕР»Рµ РЅРѕРјРµСЂ", end=" ")

    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        board[move]=EMPTY

    for move in legal_moves(board):
        board[move]=human
        if winner(board)==human:
            print(move)
            return move
        board[move]=EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):
    """РћСЃСѓС‰РµСЃС‚РІР»СЏРµС‚ РїРµСЂРµС…РѕРґ С…РѕРґР°"""
    if turn ==X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """РџРѕР·РґСЂР°РІР»СЏРµРј РїРѕР±РµРґРёС‚РµР»СЏ"""
    if the_winner !=TIE:
        print("РўСЂРё", the_winner, " РІ СЂСЏРґ\n")
    else:
        print("РќРёС‡СЊСЏ!\n")
    if the_winner ==computer:
        print("Р’С‹РёРЅСЂР°Р» РєРѕРјРїСЊСЋС‚РµСЂ!\n")
    elif the_winner==human:
        print("Р’С‹РёРіСЂР°Р» С‡РµР»РѕРІРµРє!\n")
    elif the_winner==TIE:
        print("РќРёС‡СЊСЏ!\n")

def main():
    display_instruckt()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move]  = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#Р·Р°РїСѓСЃРє РїСЂРѕРіСЂР°РјРјС‹

main()
input("\n\n РќР°Р¶РјРёС‚Рµ etrer РґР»СЏ РІС‹С…РѕРґР°")