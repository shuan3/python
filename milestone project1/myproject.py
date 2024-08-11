from IPython.display import clear_output



class BoardGame:
    # board=['0']*9
    def __init__(self):
        pass
    # @property
    # def board(self):
    #     return self.board
    # @board.setter
    # def board(self, position,value):
    #     self.board[position] = value
    def display_board(self,board):
        clear_output()  # Remember, this only works in jupyter!
        
        print('   |   |')
        print(' 6' + board[6] + ' | 7' + board[7] + ' | 8' + board[8])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' 3' + board[3] + ' | 4' + board[4] + ' | 5' + board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' 0' + board[0] + ' | 1' + board[1] + ' | 2' + board[2])
        print('   |   |')

    def place_marker(self,board, marker, position):
        board[position] = marker

    def win_check(self,board,mark):
        return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
        (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
        (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
        (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
        (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
        (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
        (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal
    def play(self,name,board,position,maker):
        if (maker=='X' or maker=='O') and len(board)>int(position)>=0 and board[int(position)] not in ['X','O']:
            print(f'Player {name} choose')   
            board[int(position)]=maker
        else:
            print('Invalid maker or position or position has been filled!')
        return board
    def game(self,board,player1,player2):
        game_on=True
        while game_on:
            self.display_board(board)
            position=input(f"{player1} Type position")
            board=self.play(player1,board,position,'X')
            if self.win_check(board,'X'):
                print(f'{player1} wins!')
                game_on=False
            
            self.display_board(board)
            position=input(f"{player2} Type position")
            board=self.play(player2,board,position,'O')
            if self.win_check(board,'O'):
                print(f'{player2} wins!')
                game_on=False
            if '0' not in board:
                print('It is a tie!')
                game_on=False
        print('Game ends!')

# BoardGame().board(0,'X')
# print(BoardGame(board=['0']*9).display_board(BoardGame(board=['0']*9).board))


board=['0']*9
player1='Superman'
player2='homelander'
BoardGame().game(board,player1,player2)