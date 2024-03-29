import random
from tkinter import *

root = Tk()
root.title('Criss-cross')
Game_Status = True
Game_field = []
cross_count = 0


def new_game():
    for row in range(3):
        for col in range(3):
            Game_field[row][col]['text'] = ' '
            Game_field[row][col]['background'] = 'white'
    global Game_Status
    Game_Status = True
    global cross_count
    cross_count = 0


def Step(row, col):
    if Game_Status == True and Game_field[row][col]['text'] == ' ':
        Game_field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if Game_Status == True and cross_count < 5:
            computer_move()
            check_win('O')


def check_win(smb):
    for n in range(3):
        check_line(Game_field[n][0], Game_field[n][1], Game_field[n][2], smb)
        check_line(Game_field[0][n], Game_field[1][n], Game_field[2][n], smb)
    check_line(Game_field[0][0], Game_field[1][1], Game_field[2][2], smb)
    check_line(Game_field[2][0], Game_field[1][1], Game_field[0][2], smb)


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'red'
        global Game_Status
        Game_Status = False


def can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():
    for n in range(3):
        if can_win(Game_field[n][0], Game_field[n][1], Game_field[n][2], 'O'):
            return
        if can_win(Game_field[0][n], Game_field[1][n], Game_field[2][n], 'O'):
            return
    if can_win(Game_field[0][0], Game_field[1][1], Game_field[2][2], 'O'):
        return
    if can_win(Game_field[2][0], Game_field[1][1], Game_field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(Game_field[n][0], Game_field[n][1], Game_field[n][2], 'X'):
            return
        if can_win(Game_field[0][n], Game_field[1][n], Game_field[2][n], 'X'):
            return
    if can_win(Game_field[0][0], Game_field[1][1], Game_field[2][2], 'X'):
        return
    if can_win(Game_field[2][0], Game_field[1][1], Game_field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if Game_field[row][col]['text'] == ' ':
            Game_field[row][col]['text'] = 'O'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='white',
                        command=lambda row=row, col=col: Step(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    Game_field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
