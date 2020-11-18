import time
import random
class Game:
    def __init__(self):
        # we are using '.' for an epmty space in the board.
        self.board=[['.' for _ in range(3)] for _ in range(3)]
        # Player X is the human Player
        self.player_turn='X' 
    
    def draw_board(self):
        for x in range(3):
            print(self.board[x])
        print()
        print([(0,0),(0,1),(0,2)])
        print([(1,0),(1,1),(1,2)])
        print([(2,0),(2,1),(2,2)])
        print()
    
    def is_valid(self,move_x,move_y):
        # To check if the move is inside the board
        if move_x<0 or move_x>2 or move_y<0 or move_y>2:
            return False
        #To check if the curent position is not already taken
        elif self.board[move_x][move_y]!='.':
            return False
        return True

    def is_ending(self):
        # [(0,0),(0,1),(0,2)]   
        # [(1,0),(1,1),(1,2)]           MAKING THE BOARD FOR LOOKING COORDINATES
        # [(2,0),(2,1),(2,2)]

        # checking for vertical wins
        for i in range(3):
            if self.board[0][i]!='.' and self.board[0][i]==self.board[1][i] and self.board[1][i]==self.board[2][i]:
                return self.board[0][i]
            
        #checking for hoirzontal wins
        for i in range(3):
            if self.board[i]==['X' for _ in range(3)]:
                return 'X'
            elif self.board[i]==['O' for _ in range(3)]:
                return 'O'
        
        #checking for diagonal wins (First)
        if self.board[0][0]!='.' and self.board[0][0]==self.board[1][1]==self.board[2][2]:
            return self.board[0][0]
        
        #checking for Diagonal (second).
        if self.board[0][2]!='.' and self.board[0][2]==self.board[1][1]==self.board[2][0]:
            return self.board[0][2]
        
        #any moves left?
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=='.':
                    return None

        #its a Tie   
        return 'TIE'
    
    def max(self):
        # this is for the AI i.e. "O"

        # if AI wins then +10 points
        # if AI looses then -10 points
        # if its a draw then 0 points

        score_max=-100

        move_x=None
        move_y=None
        
        result=self.is_ending()

        if result=="X":
            return (-10,0,0)
        elif result=="O":
            return (10,0,0)
        elif result=="TIE":
            return (0,0,0)
        

        for i in range(3):
            for j in range(3):
                if self.board[i][j]==".":
                    # on empty place the AI will play its turn
                    # we will mark the empty place as O and then will backtrack
                    self.board[i][j]="O"
                    (m,min_i,min_j)=self.min()      #Tuple unpacking
                    
                    # changing the value if we found a better option
                    if m>score_max:
                        score_max=m
                        move_x=i
                        move_y=j
                    
                    #backtracking
                    self.board[i][j]="."
        return (score_max,move_x,move_y)
    
    def min(self):
        # Here we want to minimize the score of human player even if they play optimally.
        # this is for player X

        # if AI wins then +10 points
        # if AI looses then -10 points
        # if its a draw then 0 points

        score_min=100

        move_x=None
        move_y=None

        result=self.is_ending()

        if result=="X":
            return (-10,0,0)
        elif result=="O":
            return (10,0,0)
        elif result=="TIE":
            return (0,0,0)
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==".":
                    self.board[i][j]="X"
                    (m,max_i,max_j)=self.max()
                    if m<score_min:
                        score_min=m
                        move_x=i
                        move_y=j
                    self.board[i][j]="."
        return (score_min,move_x,move_y)
    
    def play(self):
        chooser=random.randint(0,1)
        if chooser==0:
            self.player_turn="O"
            print('AI will go first')
        else:   print('Human will play first')
        while True:
            self.draw_board()
            result=self.is_ending()

            if result!=None:
                if result=="X":
                    print('The winner is X')
                elif result=='O':
                    print('The winner is AI')
                elif result=='TIE':
                    print('There was a TIE')
                
                print("want to play again Y/N")
                temp=input('Enter the response here: ')
                if temp.lower()=='y':
                    new=Game()
                    new.play()
                break
            if self.player_turn=="X":
                while True:
                    # Uncomment this code to recieve recommendations and evaluation time

                    # start=time.time()
                    # (_,move_x,move_y)=self.min()
                    # end=time.time()
                    # print('eval time: {}s'.format(round(end-start,7)))
                    # print('recommended move: X={},Y={}'.format(move_x,move_y))

                    move_x=int(input('Enter X coordinate: '))
                    move_y=int(input('Enter the Y coordinate: '))

                    if self.is_valid(move_x,move_y):
                        self.board[move_x][move_y]="X"
                        self.player_turn="O"
                        break
                    else:
                        print('invalid move try again')
                
            else:
                (_,move_x,move_y)=self.max()
                self.board[move_x][move_y]="O"
                self.player_turn='X'
            
new=Game()
new.play()
                    
        
        






    


