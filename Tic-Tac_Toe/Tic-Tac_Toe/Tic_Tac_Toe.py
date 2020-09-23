import random

class Tic_Tac_Toe():
    
    def game_start(self):
        
        print('''This game contains several game modes. \n
There are "user" player (which is a human player) and 3 types of bots - "easy", "medium", "hard". \n
You can choose "human vs human", "human vs bot" or "bot vs bot" game modes. 
Example: user easy \n
First player will draw "X" and the second - "O". \n
Have a nice game! \n ''')

        self.super_menu()

    def super_menu(self):

        a = input(f'Input command: ')
        self.command = a.split()
        check_digit = ''.join(self.command)
        self.word = set(self.command)

        if len(self.command) != 3:
            print('Bad parameters!')
            self.super_menu()

        elif check_digit.isdigit() == True:
            print('Bad parameters!')
            self.super_menu()
        
        elif self.command[0] != 'start':
            print('Bad parameters!')
            self.super_menu()

        elif any('user' in x for x in self.word) == False and any('easy' in x for x in self.word) == False and any('medium' in x for x in self.word) == False \
           and any('hard' in x for x in self.word) == False:
            print('Bad parameters!')
            self.super_menu()

        else:
            self.menu()
    
    def game_mode(self):

        if self.command[1] == 'user' and self.command[2] == 'user': # human player vs human player
            self.w = 1
            self.shape()

        elif (self.command[1] == 'user' and self.command[2] == 'easy') or (self.command[1] == 'easy' and self.command[2] == 'user'): # human player vs easy bot
            self.w = 2_1
            self.shape()

        elif (self.command[1] == 'user' and self.command[2] == 'medium') or (self.command[1] == 'medium' and self.command[2] == 'user'): # human player vs medium bot
            self.w = 2_2
            self.shape()
        
        elif (self.command[1] == 'user' and self.command[2] == 'hard') or (self.command[1] == 'hard' and self.command[2] == 'user'): # human player vs hard bot
            self.w = 2_3
            self.shape()

        elif self.command[1] == 'easy' and self.command[2] == 'easy': # easy bot game
            self.w = 3_1
            self.shape()

        elif self.command[1] == 'medium' and self.command[2] == 'medium': # medium bot game
            self.w = 3_2
            self.shape()

        elif self.command[1] == 'hard' and self.command[2] == 'hard': # hard bot game
            self.w = 3_3
            self.shape()

        elif (self.command[1] == 'easy' and self.command[2] == 'medium') or (self.command[1] == 'medium' and self.command[2] == 'easy'): # easy vs medium bot game
            self.w = 4_1
            self.shape()
        
        elif (self.command[1] == 'easy' and self.command[2] == 'hard') or (self.command[1] == 'hard' and self.command[2] == 'easy'): # easy vs hard bot game
            self.w = 4_2
            self.shape()

        elif (self.command[1] == 'hard' and self.command[2] == 'medium') or (self.command[1] == 'medium' and self.command[2] == 'hard'): # hard vs medium bot game
            self.w = 4_3
            self.shape()


    def menu(self):
        field = '_' * 9
        symbols = list(field)
        for i in range(len(symbols)):
            if symbols[i] == '_':
                symbols[i] = ' '

        table = ' '.join(symbols)
        table_2 = ''.join(symbols)
        
        tab_1 = table[:5]
        tab_2 = table[6:11]
        tab_3 = table[12:17]

        tab1 = table_2[:3]
        tab2 = table_2[3:6]
        tab3 = table_2[6:9]

        print('---------')
        print(f'| {tab_1} |')
        print(f'| {tab_2} |')
        print(f'| {tab_3} |')
        print('---------')

        self.l = []
        self.l.append(list(tab1))
        self.l.append(list(tab2))
        self.l.append(list(tab3))

        self.game_mode()

    def shape(self): # the next figure

        b_sum_1 = self.l[0].count('X')
        b_sum_2 = self.l[0].count('O')

        c_sum_1 = self.l[1].count('X')
        c_sum_2 = self.l[1].count('O')

        d_sum_1 = self.l[2].count('X')
        d_sum_2 = self.l[2].count('O')

        if (b_sum_1 + c_sum_1 + d_sum_1) == (b_sum_2 + c_sum_2 + d_sum_2):
            
            self.figure = 'X'
            
            if self.w == 1:
                self.move_check()

            elif self.w == 2_1:

                if self.command[1] == 'user':
                    self.move_check()
                
                elif self.command[1] == 'easy':
                    self.easy()

            elif self.w == 2_2:

                if self.command[1] == 'user':
                    self.move_check()
                
                elif self.command[1] == 'medium':
                    self.medium()

            elif self.w == 2_3:

                if self.command[1] == 'user':
                    self.move_check()
                
                elif self.command[1] == 'hard':
                    self.hard_1()

            elif self.w == 3_1:
                self.easy()

            elif self.w == 3_2:
                self.medium()

            elif self.w == 3_3:
                self.hard_1()

            elif self.w == 4_1:
                
                if self.command[1] == 'easy':
                    self.easy()
                
                elif self.command[1] == 'medium':
                    self.medium()
             
            elif self.w == 4_2:
                
                if self.command[1] == 'easy':
                    self.easy()
                
                elif self.command[1] == 'hard':
                    self.hard_1()

            elif self.w == 4_3:
                
                if self.command[1] == 'hard':
                    self.hard_1()
                
                elif self.command[1] == 'medium':
                    self.medium()
        else:
            self.figure = 'O'
            
            if self.w == 1:
                self.move_check()

            elif self.w == 2_1:
                
                if self.command[2] == 'user':
                    self.move_check()
                
                elif self.command[2] == 'easy':
                    self.easy()

            elif self.w == 2_2:
                
                if self.command[2] == 'user':
                    self.move_check()
                
                elif self.command[2] == 'medium':
                    self.medium()

            elif self.w == 2_3:
                
                if self.command[2] == 'user':
                    self.move_check()
                
                elif self.command[2] == 'hard':
                    self.hard_2()

            elif self.w == 3_1:
                self.easy()

            elif self.w == 3_2:
                self.medium()

            elif self.w == 3_3:
                self.hard_2()

            elif self.w == 4_1:
                
                if self.command[2] == 'easy':
                    self.easy()
                
                elif self.command[2] == 'medium':
                    self.medium()

            elif self.w == 4_2:
                
                if self.command[2] == 'easy':
                    self.easy()
                
                elif self.command[2] == 'hard':
                    self.hard_2()

            elif self.w == 4_3:
                
                if self.command[2] == 'hard':
                    self.hard_2()
                
                elif self.command[2] == 'medium':
                    self.medium()
    
    def move_check(self):
        
        c = input(f'Enter the coordinates: ')
        words = c.split()
        self.numbers = c.split()
        a = ''.join(words)
        words_c = len(words)
        
        if words_c < 2:
            print('You should enter numbers!')
            self.move_check()
        
        elif a.isdigit() == False: 
            print('You should enter numbers!')
            self.move_check()
        else:
            self.move()
        
    def move(self):

        c1 = self.numbers[0]
        c2 = self.numbers[1]
                     
        c1_1, c2_2 = (int(c1) - 1), (int(c2) - 1)
        self.l.reverse()

        if (c1_1 < 0 or c1_1 > 2) or (c2_2 < 0 or c2_2 > 2):
            print("Coordinates should be from 1 to 3!")
            self.l.reverse()
            self.move_check()

        elif self.l[c2_2][c1_1] == 'X' or self.l[c2_2][c1_1] == 'O':
            print('This cell is occupied! Choose another one!')
            self.l.reverse()
            self.move_check()        

        elif self.l[c2_2][c1_1] != 'X' and self.l[c2_2][c1_1] != 'O':
            
            self.l[c2_2][c1_1] = self.figure
            self.l.reverse()                
            
            self.game_rule()

            
    def game_rule(self): #win, draw or continue
        
        a_1 = ' '.join(self.l[0])
        a_2 = ' '.join(self.l[1])
        a_3 = ' '.join(self.l[2])

        print('---------')
        print(f'| {a_1} |')
        print(f'| {a_2} |')
        print(f'| {a_3} |')
        print('---------')
        
        if self.l[0][0] == self.l[0][1] == self.l[0][2] and self.l[0][0] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[1][0] == self.l[1][1] == self.l[1][2] and self.l[1][0] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif (self.l[2][0] == self.l[2][1] == self.l[2][2]) and self.l[2][0] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[0][0] == self.l[1][0] == self.l[2][0] and self.l[0][0] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[0][1] == self.l[1][1] == self.l[2][1] and self.l[0][1] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[0][2] == self.l[1][2] == self.l[2][2] and self.l[0][2] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[0][0] == self.l[1][1] == self.l[2][2] and self.l[0][0] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[0][2] == self.l[1][1] == self.l[2][0] and self.l[0][2] != ' ':
            print(f'{self.figure} wins')
            self.w = self.figure

        elif self.l[0].count(' ') == 0 and self.l[1].count(' ') == 0 and self.l[2].count(' ') == 0:
            print('Draw')
            self.w = ' '

        else:
            self.shape()

    def easy(self): #easy bot

        b = ['0', '1', '2']
        c1 = int(''.join(random.choice(b)))
        c2 = int(''.join(random.choice(b)))

        if self.l[c1][c2] != 'X' and self.l[c1][c2] != 'O':
            self.l[c1][c2] = self.figure
            print('\n', "Making move level 'easy'", end='\n')

            self.game_rule()
        else:
            self.easy()
    
    def medium(self): #medium bot

        b = ['0', '1', '2']
        c1 = int(''.join(random.choice(b)))
        c2 = int(''.join(random.choice(b)))

        list_1 = [self.l[0][0], self.l[1][0], self.l[2][0]]
        list_2 = [self.l[0][1], self.l[1][1], self.l[2][1]]
        list_3 = [self.l[0][2], self.l[1][2], self.l[2][2]]

        if (self.l[0].count("X") == 2 or self.l[0].count("O") == 2) and self.l[0].count(" ") == 1:
            e = self.l[0].index(" ")
            self.l[0][e] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()
            
        elif (self.l[1].count("X") == 2 or self.l[1].count("O") == 2) and self.l[1].count(" ") == 1:
            e = self.l[1].index(" ")
            self.l[1][e] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif (self.l[2].count("X") == 2 or self.l[2].count("O") == 2) and self.l[2].count(" ") == 1:
            e = self.l[2].index(" ")
            self.l[2][e] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][0] == self.l[1][0] and self.l[2][0] == " ":
            self.l[2][0] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()
            
        elif self.l[0][0] == self.l[2][0] and self.l[1][0] == " ":
            self.l[1][0] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[2][0] == self.l[1][0] and self.l[0][0] == " ":
            self.l[0][0] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][1] == self.l[1][1] and self.l[2][1] == " ":
            self.l[2][1] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][1] == self.l[2][1] and self.l[1][1] == " ":
            self.l[1][1] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()
           
        elif self.l[2][1] == self.l[1][1] and self.l[0][1] == " ":
            self.l[0][1] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][2] == self.l[1][2] and self.l[2][2] == " ":
            self.l[2][2] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][2] == self.l[2][2] and self.l[1][2] == " ":
            self.l[1][2] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[2][2] == self.l[1][2] and self.l[0][2] == " ":
            self.l[0][2] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][0] == self.l[1][1] and self.l[2][2] == " ":
            self.l[2][2] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][0] == self.l[2][2] and self.l[1][1] == " ":
            self.l[1][1] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[2][2] == self.l[1][1] and self.l[0][0] == " ":
            self.l[0][0] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()
            
        elif self.l[0][2] == self.l[1][1] and self.l[2][0] == " ":
            self.l[2][0] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        elif self.l[0][2] == self.l[2][0] and self.l[1][1] == " ":
            self.l[1][1] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()
        
        elif self.l[2][2] == self.l[1][1] and self.l[0][2] == " ":
            self.l[0][2] = self.figure
            print('\n', "Making move level 'medium'", end='\n')
            self.game_rule()

        else:
            if self.l[c1][c2] != 'X' and self.l[c1][c2] != 'O':
                self.l[c1][c2] = self.figure
                print('\n', "Making move level 'medium'", end='\n')

                self.game_rule()
            else:
                self.medium()
    
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.l[0][i] != ' ' and
                self.l[0][i] == self.l[1][i] and
                self.l[1][i] == self.l[2][i]):
                return self.l[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.l[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.l[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.l[0][0] != ' ' and
            self.l[0][0] == self.l[1][1] and
            self.l[0][0] == self.l[2][2]):
            return self.l[0][0]

        # Second diagonal win
        if (self.l[0][2] != ' ' and
            self.l[0][2] == self.l[1][1] and
            self.l[0][2] == self.l[2][0]):
            return self.l[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.l[i][j] == ' '):
                    return None

        return ' '

    def max(self):

        maxv = -2

        px = None
        py = None

        result = self.is_end()

        if result == 'X':
            maxv = -1
        elif result == 'O':
            maxv = 1
        elif result == ' ':
            maxv = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.l[i][j] == ' ':
                    self.l[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    
                    self.l[i][j] = ' '
        return (maxv, px, py)

    def min(self):

        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            minv = -1
        elif result == 'O':
            minv = 1
        elif result == ' ':
            minv = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.l[i][j] == ' ':
                    self.l[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.l[i][j] = ' '

        return (minv, qx, qy)

    def hard_1(self):
        (m, px, py) = self.min()
        print(f'Making move, level \"hard\"')
        self.l[px][py] = 'X'

        self.game_rule()

    def hard_2(self):
        (m, qx, qy) = self.max()
        print(f'Making move, level \"hard\"')
        self.l[qx][qy] = 'O'

        self.game_rule()

user = Tic_Tac_Toe()
user.game_start()