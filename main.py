
print("  0  1  2    cols") #second element value
print("0  |  |    row")
print("-----------")
print("1  |  |    row")
print("-----------")
print("1  |  |    row")


player1_row = input("Player 1 Pick Your Row")
player1_col = input("Player 1 Pick Your Col")

int_player1_row = int(player1_row)
int_player1_col = int(player1_col)


print("Player One Picked", int_player1_row, int_player1_col)
myArray = ["0"]*5

print(myArray)

myArray[4] = "X"
print(myArray)

board = [
    ["X ", "O", "O"],
    [" ", " ", " "],
    [" ", " ", " "]
]
print(board[2][1])

board[int_player1_row]
def player_1_turn():
    def didIwin():

#someone wins 8 conditions
#6 more of these

    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        print(board[0][0], "is the winner col")
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        print(board[0][0], "is the winner row")
    if board[0][0] == board[0][3] and board[0][0] == board[0][4]:
            print(board[0][0], "is the winner col")
    if board[0][0] == board[3][0] and board[0][0] == board[4][0]:
            print(board[0][0], "is the winner row")
    if board[0][0] == board[0][5] and board[0][0] == board[0][6]:
           print(board[0][0], "is the winner col")
    if print[0][0] == board[5][0] and board[0][0] == board[6][0]:
            print(board[0][0], "is the winner row ")
    if board[0][0] == board[0][7] and board[0][0] == board[0][8]:
            print(board[0][0], "is the winner col")
    if board[0][0] == board[7][0] and board[0][0] == board[8][0]:
            print(board[0][0], "is the winner row")

board = [
    ["X", "X", "X"],
    [" ", "x", " "],
    [" ", " ", "0"]
]
print(f'''
    0 1 2
   _______
0 | {board[0][0]}|{board[0][1]}|{board[0][2]} |
  | -+-+- | 
1 | {board[1][0]}|{board[1][1]}|{board[1][2]} |
  | -+-+- |                                    
2 | {board[2][0]}|{board[2][1]}|{board[2][2]} | 
   -------
''')
def game_play():
    player_1_turn()
    




board[int_player1_col]
def player_2_turn():
    def didIwin():
