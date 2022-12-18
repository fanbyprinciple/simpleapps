import sys, pygame, time


# generate rectangles for each square. rectangles for squares can be reference based on rectlist[x][y]
def generate_rectlist(coorlist):
    rectlist = []
    for pair in coorlist:
        rectlist.append((pygame.Rect(0 + (62.5 * pair[0]), 437.5 - (62.5 * pair[1]), 62.5, 62.5), pair))
    return rectlist


def shade_area(x, y):
    screen.blit(blue_square, (31.25 + (62.5 * x) - 25, 500 - 31.5 - 25 - (62.5 * y)))
    pygame.display.flip()


# draw board and pieces in pygame window based on squarelist
def reset_board(squarelist, shadelist=[]):
    screen.blit(background, (0, 0))
    for coor_pair in shadelist:
        shade_area(coor_pair[0], coor_pair[1])
    for column in squarelist:
        for space in column:
            if space:
                if space.color == True:
                    if space.type == 'rook':
                        screen.blit(b_rook, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'knight':
                        screen.blit(b_knight, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'bishop':
                        screen.blit(b_bishop, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'queen':
                        screen.blit(b_queen, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'king':
                        screen.blit(b_king, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'pawn':
                        screen.blit(b_pawn, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                else:
                    if space.type == 'rook':
                        screen.blit(w_rook, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'knight':
                        screen.blit(w_knight, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'bishop':
                        screen.blit(w_bishop, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'queen':
                        screen.blit(w_queen, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'king':
                        screen.blit(w_king, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'pawn':
                        screen.blit(w_pawn, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                # commented out because it didn't work for obvious reasons, but above seems very inneficient
                '''
                if space.color == True:
                    prefix = 'b_'
                else:
                    prefix = 'w_'
                screen.blit(prefix + space.type, (10 + space.square[0]*62.5, 445 - space.square[1]*)2.5))
                '''

    pygame.display.flip()


# size of piece in pixels: 500 / 8 = 62.5 px len per side
def generate_squarelist():
    # hardcoded stuff cause I already had it and I didn't feel like writing another way
    squarelist = [['w_rook', 'w_pawn', '', '', '', '', 'b_pawn', 'b_rook'],
                  ['w_knight', 'w_pawn', '', '', '', '', 'b_pawn', 'b_knight'],
                  ['w_bishop', 'w_pawn', '', '', '', '', 'b_pawn', 'b_bishop'],
                  ['w_queen', 'w_pawn', '', '', '', '', 'b_pawn', 'b_queen'],
                  ['w_king', 'w_pawn', '', '', '', '', 'b_pawn', 'b_king'],
                  ['w_bishop', 'w_pawn', '', '', '', '', 'b_pawn', 'b_bishop'],
                  ['w_knight', 'w_pawn', '', '', '', '', 'b_pawn', 'b_knight'],
                  ['w_rook', 'w_pawn', '', '', '', '', 'b_pawn', 'b_rook']]
    for column in range(0, 8):
        for row in range(0, 8):
            item = squarelist[column][row]
            if item != '':
                generated_piece = Piece()
                # fix color
                if item[0] == 'b':
                    generated_piece.color = True
                generated_piece.type = item[2::]
                generated_piece.square = (column, row)
                squarelist[column][row] = generated_piece
            else:
                squarelist[column][row] = None
    return squarelist


class Piece:
    # rook, knight, bishop, queen, king, pawn
    type = ''
    # True = black, False = white
    color = False
    square = ()
    possible_moves = []
    moved = False

    # funky stuff happening here check back when ur good to fix it
    def get_possible_moves(self, include_same_color = False):
        self.possible_moves = []
        global squarelist
        # CHECK FOR ROOK
        def check_diagonals():
            # check north-east
            y = self.square[1]
            for x in range(self.square[0] + 1, 8):
                y += 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if include_same_color == True or self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))
            # check south-east
            y = self.square[1]
            for x in range(self.square[0] + 1, 8):
                y -= 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if include_same_color == True or self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))
            # check north-west
            y = self.square[1]
            for x in range(self.square[0] - 1, -1, -1):
                y += 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if include_same_color == True or self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))
            # check south-west
            y = self.square[1]
            for x in range(self.square[0] - 1, -1, -1):
                y -= 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if include_same_color == True or self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))

        def check_parallels():
            # check left
            for xcor in range(self.square[0] - 1, -1, -1):

                if squarelist[xcor][self.square[1]]:
                    if include_same_color == True or self.color != squarelist[xcor][self.square[1]].color:
                        self.possible_moves.append((xcor, self.square[1]))
                    break
                else:
                    self.possible_moves.append((xcor, self.square[1]))
            # check right
            for xcor in range(self.square[0] + 1, 8):

                if squarelist[xcor][self.square[1]]:
                    if include_same_color == True or self.color != squarelist[xcor][self.square[1]].color:
                        self.possible_moves.append((xcor, self.square[1]))
                    break
                else:
                    self.possible_moves.append((xcor, self.square[1]))
            # check up
            for ycor in range(self.square[1] + 1, 8):

                if squarelist[self.square[0]][ycor]:
                    if include_same_color == True or self.color != squarelist[self.square[0]][ycor].color:
                        self.possible_moves.append((self.square[0], ycor))
                    break
                else:
                    self.possible_moves.append((self.square[0], ycor))
            # check down
            for ycor in range(self.square[1] - 1, -1, -1):

                if squarelist[self.square[0]][ycor]:
                    if include_same_color == True or self.color != squarelist[self.square[0]][ycor].color:
                        self.possible_moves.append((self.square[0], ycor))
                    break
                else:
                    self.possible_moves.append((self.square[0], ycor))

        if self.type == 'rook':
            check_parallels()
            '''
            if self.moved == False:
                if self.color == True:
                    if squarelist[4][7].moved == False:
                        self.possible_moves.append((4,7))
                else:
                    if squarelist[4][0].moved == False:
                        self.possible_moves.append((4,0))
            '''
        # CHECK FOR KNIGHT
        if self.type == 'knight':
            # calculate all possible moves
            moves = [(self.square[0] - 2, self.square[1] + 1), (self.square[0] - 2, self.square[1] - 1),
                     (self.square[0] + 2, self.square[1] + 1), (self.square[0] + 2, self.square[1] - 1),
                     (self.square[0] + 1, self.square[1] + 2), (self.square[0] - 1, self.square[1] + 2),
                     (self.square[0] + 1, self.square[1] - 2), (self.square[0] - 1, self.square[1] - 2)]
            for pair in moves:
                # for each possible move check if really possible, if so add to list
                if pair[0] <= 7 and pair[0] >= 0 and pair[1] <= 7 and pair[1] >= 0:
                    if squarelist[pair[0]][pair[1]]:
                        if include_same_color == True or self.color != squarelist[pair[0]][pair[1]].color:
                            self.possible_moves.append((pair[0], pair[1]))
                    else:
                        self.possible_moves.append((pair[0], pair[1]))

        # CHECK FOR BISHOP
        if self.type == 'bishop':
            check_diagonals()
        # CHECK FOR QUEEN
        if self.type == 'queen':
            check_diagonals()
            check_parallels()
        # CHECK FOR PAWN
        if self.type == 'pawn':
            if self.color == True:
                yiteration = -1
            else:
                yiteration = 1
            # check diagonal moves
            attacks = [(self.square[0] - 1, self.square[1] + yiteration),
                       (self.square[0] + 1, self.square[1] + yiteration)]
            for pair in attacks:
                if pair[0] <= 7 and pair[1] <= 7 and pair[0] >= 0 and pair[1] >= 0:

                    if squarelist[pair[0]][pair[1]]:
                        if include_same_color == True or self.color != squarelist[pair[0]][pair[1]].color:
                            self.possible_moves.append((pair[0], pair[1]))
            # check forward moves (including 2 up if hasnt moved)
            moves = [(self.square[0], self.square[1] + yiteration)]
            if self.square[1] == 1 and self.color == False:
                moves.append((self.square[0], self.square[1] + 2))
            elif self.square[1] == 6 and self.color == True:
                moves.append((self.square[0], self.square[1] - 2))
            # add to list if move empty
            for move in moves:
                if move[0] <= 7 and move[1] <= 7 and move[0] >= 0 and move[1] >= 0:
                    if squarelist[move[0]][move[1]] == None:
                        self.possible_moves.append((move[0], move[1]))
        #TODO: check kings after becasue their moves depend on previous pieces's possible moves. recomend update king positions in seperate tuple and reference it excluding kings previously
        #TODO: add moved parameters to all pieces ( use for castling )
        # CHECK FOR KING
        if self.type == 'king':
            moves = [(self.square[0] + 1, self.square[1] + 1), (self.square[0] + 1, self.square[1] - 1),
                     (self.square[0], self.square[1] + 1), (self.square[0], self.square[1] - 1),
                     (self.square[0] - 1, self.square[1] + 1), (self.square[0] - 1, self.square[1] - 1),
                     (self.square[0] + 1, self.square[1]), (self.square[0] - 1, self.square[1])]
            # change checklist
            if self.color == True:
                #says wpm not defined by the time it hits here
                checklist = wpm_include_self_color
            else:
                checklist = bpm_include_self_color

            #sort poss moves
            for pair in moves:
                # for each possible move check if really possible, if so add to list
                if pair[0] <= 7 and pair[0] >= 0 and pair[1] <= 7 and pair[1] >= 0 and pair not in checklist:
                    if squarelist[pair[0]][pair[1]]:
                        if include_same_color == True or self.color != squarelist[pair[0]][pair[1]].color:
                            self.possible_moves.append((pair[0], pair[1]))
                    else:
                        self.possible_moves.append((pair[0], pair[1]))

            #add castling moves
            '''
            if self.moved == False:
                if self.color == True:
                    if squarelist[0][7].moved == False:
                        self.possible_moves.append((0, 7))
                    if squarelist[7][7].moved == False:
                        self.possible_moves.append((7,7))
                else:
                    if squarelist[0][0].moved == False:
                        self.possible_moves.append((0, 0))
                    if squarelist[7][0].moved == False:
                        self.possible_moves.append((7,0))
            '''
        #change possible moves so you can't check yourself by moving something from in front of the king
        #TODO: replace this with a part that will add paramater to each piece attacked by a bishop rook or queen then add a way to catch kings moving backwards







def move_piece(init, final):
    global squarelist
    init_x, init_y, final_x, final_y = init[0], init[1], final[0], final[1]
    '''
    if squarelist[final_x][final_y]:
        #play_animation

    else:
        #play_animation switching Piece object and None
    '''
    squarelist[init_x][init_y].moved = True
    squarelist[final_x][final_y] = squarelist[init_x][init_y]
    squarelist[init_x][init_y] = None
    squarelist[final_x][final_y].square = final

def generate_white_possible_moves(list):
    global white_possible_moves
    global wpm_include_self_color
    global king_position
    white_possible_moves = []
    wpm_include_self_color = []
    king_position = [(),()]
    for column in list:
        for item in column:
            if item:
                if item.color == False:
                    if item.type != 'king':
                        item.get_possible_moves()
                        poss_mv= item.possible_moves
                        item.get_possible_moves()
                        poss_mv_inc_self_color = item.possible_moves
                        for move in poss_mv:
                            if move not in white_possible_moves:
                                white_possible_moves.append(move)
                        for move in poss_mv_inc_self_color:
                            if move not in wpm_include_self_color:
                                wpm_include_self_color.append(move)
                    elif item.type == 'king':
                        king_position[0] = item.square
                elif item.color == True and item.type == 'king':
                    king_position[1] = item.square

def add_white_king_moves(list):
    #update king poss moves for white
    global white_possible_moves
    global wpm_include_self_color
    item = list[king_position[0][0]][king_position[0][1]]
    item.get_possible_moves()
    poss_mv = item.possible_moves
    item.get_possible_moves()
    poss_mv_inc_self_color = item.possible_moves
    for move in poss_mv:
        if move not in white_possible_moves:
            white_possible_moves.append(move)
    for move in poss_mv_inc_self_color:
        if move not in wpm_include_self_color:
            wpm_include_self_color.append(move)



def generate_black_possible_moves(list):
    global black_possible_moves
    global bpm_include_self_color
    global king_position
    black_possible_moves = []
    bpm_include_self_color = []
    king_position = [(), ()]
    for column in list:
        for item in column:
            if item:
                if item.color == True:
                    if item.type != 'king':
                        item.get_possible_moves()
                        poss_mv = item.possible_moves
                        item.get_possible_moves()
                        poss_mv_inc_self_color = item.possible_moves
                        for move in poss_mv:
                            if move not in black_possible_moves:
                                black_possible_moves.append(move)
                        for move in poss_mv_inc_self_color:
                            if move not in bpm_include_self_color:
                                bpm_include_self_color.append(move)
                    elif item.type == 'king':
                        king_position[1] = item.square
                elif item.color == False and item.type == 'king':
                    king_position[0] = item.square

def add_black_king_moves(list):
    global black_possible_moves
    global bpm_include_self_color
    # update king poss moves for black
    item = list[king_position[1][0]][king_position[1][1]]
    item.get_possible_moves()
    poss_mv = item.possible_moves
    item.get_possible_moves()
    poss_mv_inc_self_color = item.possible_moves
    for move in poss_mv:
        if move not in black_possible_moves:
            black_possible_moves.append(move)
    for move in poss_mv_inc_self_color:
        if move not in bpm_include_self_color:
            bpm_include_self_color.append(move)


def take_turn(currcolor):
    global gameover
    global squarelist
    generate_white_possible_moves(squarelist)
    generate_black_possible_moves(squarelist)
    add_black_king_moves(squarelist)
    add_white_king_moves(squarelist)
    player_piece_coord = []
    for column in squarelist:
        for item in column:
            if item:
                if item.color == currcolor:
                    player_piece_coord.append(item.square)
                if item.type == 'king':
                    #TODO: add other ways king can lose?
                    # if king has no possible moves and is in check
                    if item.possible_moves == [] and (item.square in black_possible_moves or item.square in white_possible_moves):
                        gameover = True
                        #for now
                        if item.color == True:
                            print('White Wins!!!')
                        else:
                            print('Black Wins!!!')


    if white_possible_moves == [] or black_possible_moves == []:
        # for now
        print("Draw")
        gameover == True
    # generate list of rectangles ( could change to list of tuples that have coordinates too: eg
    rect_list = generate_rectlist(player_piece_coord)
    # wait for input then shade and select it
    turnover = False
    selectedsquare = None
    shadelist = []
    possible_moves = []
    while turnover == False and gameover == False:
        oldsquarelist = squarelist
        oldshadelist = shadelist
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            # if user clicks
            if event.type == pygame.MOUSEBUTTONUP:
                # pos = mouse click position
                pos = pygame.mouse.get_pos()
                # if no piece currently selected and turn still going
                if selectedsquare == None and turnover == False:
                    for rect_tuple in rect_list:
                        if rect_tuple[0].collidepoint(pos):
                            selectedsquare = (rect_tuple[1][0], rect_tuple[1][1])
                            possible_moves = squarelist[rect_tuple[1][0]][rect_tuple[1][1]].possible_moves
                            # if no moves, deselect and break rect checking loop
                            if len(possible_moves) == 0:
                                selectedsquare = None
                                break
                            shadelist = [(rect_tuple[1][0], rect_tuple[1][1])]
                            rect_list_possible_moves = generate_rectlist(possible_moves)
                            for move in squarelist[rect_tuple[1][0]][rect_tuple[1][1]].possible_moves:
                                shadelist.append((move[0], move[1]))

                # if piece is currently selected and turn still going
                elif turnover == False:
                    for rect_tuple in rect_list_possible_moves:
                        if rect_tuple[0].collidepoint(pos):
                            #castling
                            initial = selectedsquare
                            final = (rect_tuple[1][0], rect_tuple[1][1])
                            # castle 0,0 to 4,0
                            #TODO check validity of castling out of check and such
                            '''
                            if check_not_moved((0,0)) and check_not_moved((4,0)) and ((initial == (0,0) and final == (4,0) or (initial == (4,0) and final == (0,0)):
                                move_piece(initial, final)

                            else:
                            '''
                            move_piece(initial, final)
                            turnover = True
                    # if click wasn't on possible move, deselect square or if turn done, deselect square
                    selectedsquare = None
                    shadelist = []
        if shadelist != oldshadelist or squarelist != oldsquarelist:
            reset_board(squarelist,shadelist)
    if gameover == True:
        return 2
    else:
        return 1

# return True if not moved, False if moved or null value for space
def check_not_moved((x,y)):
    if squarelist[x][y]:
        if squarelist[x][y].moved == False:
            return True
    return False

def play_game():
    global currcolor
    currcolor = False
    while True:
        if take_turn(currcolor) == 2:
            break
        currcolor = not currcolor

def gamemenu():
    return 1

# set up pygame window
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

# load test images for UBUNTU LAPTOP
'''
background = pygame.image.load("/home/jeremy/Pictures/background.png")
blue_square = pygame.image.load('/home/jeremy/Pictures/blue.png')
blue_square = blue_square.convert()
blue_square.set_alpha(100)
b_king = pygame.image.load("/home/jeremy/Pictures/king.png")
b_queen = pygame.image.load("/home/jeremy/Pictures/queen.png")
b_knight = pygame.image.load("/home/jeremy/Pictures/knight.png")
b_bishop = pygame.image.load("/home/jeremy/Pictures/bishop.png")
b_rook = pygame.image.load("/home/jeremy/Pictures/rook.png")
b_pawn = pygame.image.load("/home/jeremy/Pictures/pawn.png")
w_king = b_king
w_queen = b_queen
w_knight = b_knight
w_bishop = b_bishop
w_rook = b_bishop
w_pawn = b_pawn
'''
# load images for WINDOWS DESKTOP

background = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\finalchessboard.png")
blue_square = pygame.image.load('C:\\Users\\Jeremy\\Pictures\\chess\\blue.png')
blue_square = blue_square.convert()
blue_square.set_alpha(100)
b_king = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_king.png")
b_queen = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_queen.png")
b_knight = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_knight.png")
b_bishop = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_bishop.png")
b_rook = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_rook.png")
b_pawn = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_pawn.png")
w_king = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_king.png")
w_queen = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_queen.png")
w_knight = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_knight.png")
w_bishop = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_bishop.png")
w_rook = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_rook.png")
w_pawn = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_pawn.png")

# end game menu
exit_game = False
while exit_game != True:
    squarelist = generate_squarelist()
    reset_board(squarelist)
    gameover = False
    play_game()
    gamemenu()

# comment out for use in testing drawing function and correct board-piece placement
'''
xcordinate = int(input("x: "))
ycordinate = int(input("y: "))
coordinates = (xcordinate, ycordinate)
squarelist[0][0].square = coordinates
squarelist[coordinates[0]][coordinates[1]],squarelist[0][0] = squarelist[0][0],squarelist[coordinates[0]][coordinates[1]]
reset_board(squarelist)
input()
'''