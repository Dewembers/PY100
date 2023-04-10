board = "123456789" # значения клеток
print("*" * 50)
print("*" * 50)
for i in range(3):
    print("**" + " " * 46 + "**")
print("**  ДОБРО ПОЖАЛОВАТЬ В ИГРУ КРЕСТИКИ - НОЛИКИ!  **")
print("**         PY 100. Зачетное задание             **")
for i in range(3):
    print("**" + " " * 46 + "**")
print("*" * 50)
print("*" * 50)


 # функция рисования доски
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3] + " | " + board[1+i*3] + " | " + board[2+i*3] + " |")
        print("-" * 13)


  # функция обновления доски со значением, который ввел игрок
def update_board(move_player, choice_player):
    global board
    board = board[:int(move_player)-1] + choice_player + board[int(move_player):]

 # функция проверки на выигрыш
def check_win(choice_player):
    return ((board[0] == board[4] == board[8] == choice_player) or
            (board[2] == board[4] == board[6] == choice_player) or
            (board[0] == board[3] == board[6] == choice_player) or
            (board[1] == board[4] == board[7] == choice_player) or
            (board[2] == board[5] == board[8] == choice_player) or
            (board[0] == board[1] == board[2] == choice_player) or
            (board[3] == board[4] == board[5] == choice_player) or
            (board[6] == board[7] == board[8] == choice_player))

 # функция проверки введеных данных на повтор или несоответствие
def input_player():
    print('Определим кто будет ходить первым! "X" или "O"')
    while True:
        choice_player = input("Твой выбор? ----> ") # переменная "X" или "O" первого игрока
        if choice_player == "X" or choice_player == "O":
            print()
            print("Отличный выбор, начинаем! Хорошей игры!")
            break
        else:
            print('Неверный выбор. Повторите')
            continue
    print()
    if choice_player == "X":
        choice_player2 = "O" # переменная "X" или "O" второго игрока
    else:
        choice_player2 = "X"
    step = 0 # счетчик шага, поможет определить ничью
    step1 = 0
    while step < 5:
        move_player = input(f"Куда поставим {choice_player}? ") # переменная номера клетки, куда ставит первый игрок
        if move_player not in '123456789':
            print("Неверный ввод, повторите!")
            continue
        else:
            update_board(move_player, choice_player)
            draw_board(board)
            if check_win(choice_player):
                print(f"{choice_player} победил!")
                break
        step+=1
        if step == 5:
            print("Ничья!")
            break

        while step1< 4:
            move_player2 = input(f"Куда поставим {choice_player2}? ") # переменная номера клетки, куда ставит второй игрок
            if move_player2 not in '123456789':
                print("Неверный ввод, повторите!")
                continue
            else:
                update_board(move_player2, choice_player2)
                draw_board(board)
                if check_win(choice_player2):
                    print(f"{choice_player2} победил!")
                break


def main():
    draw_board(board)
    input_player()
main()
