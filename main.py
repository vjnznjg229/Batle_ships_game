import random
class Field:
    def __init__(self,size,ships):
        self.size=size
        self.ships=ships
        self.grid=[]
        self.ships_alive=ships
        for a in range(self.size):
            self.grid.append([None] *size)
    def display(self,show_ships=False):
        print('    A B C D E F G H I J ')
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None or show_ships==False:
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10:
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)
class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15
        self.computer_field=Field(self.size,self.ships)
        self.player_field=Field(self.size,self.ships)
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False
        return True
    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field,self.ships)
        self.computer_field.display(show_ships=False)
        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)

        self.player_field.display(show_ships=True)

        while True:
            xy=input('Введите кординату выстрела')
            x=xy[0]
            y=int(xy[1])
            self.player_turn(x,y)
            if self.computer_field.ships_alive == 0:
                print('Вы победили! Все корабли компьютера потоплены.')
                break
            self.computer_turn()
            if self.player_field.ships_alive == 0:
                print('Вы проиграли! Все ваши корабли потоплены.')
                break


    def player_turn(self, x, y):
        x='ABCDEFGHIJ'.index(x)
        if self.computer_field.grid[y-1][x]=='S':
            print("Вы попали!")
            self.computer_field.grid[y-1][x]='X'
            self.computer_field.ships_alive-=1
        else:
            print("Промах!")
    def computer_turn(self):
        x=random.randint(0,9)
        y=random.randint(0,9)
        if self.player_field.grid[y][x]=='S':
            print("Компьютер попал!")
            self.player_field.grid[y][x] = 'X'
            self.player_field.ships_alive -= 1
        else:
            print('Компьютер промахнулся!')
YTRUY=BattleshipGame()
YTRUY.play()