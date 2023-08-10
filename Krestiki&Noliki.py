size = 3

field = [[' ' for _ in range(size)] for _ in range(size)]

def print_field():
    print('  0 1 2')
    for i in range(size):
        print(f'{i} {" ".join(field[i])}')
def check_winner(mark):
    for i in range(size):
        if all(field[i][j] == mark for j in range(size)) or all(field[j][i] == mark for j in range(size)):
            return True
    if all(field[i][i] == mark for i in range(size)) or all(field[i][size-i-1] == mark for i in range(size)):
        return True
    return False

current_mark = 'X'
while True:
    print_field()
    row = int(input('Введите номер строки (0-2): '))
    col = int(input('Введите номер столбца (0-2): '))
    if row < 0 or row >= size or col < 0 or col >= size or field[row][col] != ' ':
        print('Ошибка: некорректные координаты или клетка уже занята')
        continue
    field[row][col] = current_mark
    if check_winner(current_mark):
        print(f'Игрок {current_mark} победил!')
        break
    if all(field[i][j] != ' ' for i in range(size) for j in range(size)):
        print('Ничья!')
        break
    current_mark = 'O' if current_mark == 'X' else 'X'