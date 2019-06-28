class GameGround(object):

    def __init__(self):
        self.scale_field = 3
        self.playingField = []
        self.firstPlayer = 'X'
        self.secondPlayer = 'O'


    def create_playing_field(self):
        #global scale_field
        #scale_field = self.scale_field
        scale = self.scale_field
        #global playingField
        for i in range(1, scale + 1):
            for j in range(1, scale + 1):
                cell = (i, j, ' ')
                self.playingField.append(cell)
        return self.playingField

    def print_grid(self):
        x, y = '', ''
        xy = ''
        nn = 0
        for j in range(1, self.scale_field + 1):
            for i in range(1, self.scale_field + 1):
                player = self.playingField[nn][2]
                y += '| ' + player + ' '
                x += '+---'
                nn += 1

            xy += x + '\n' + y + '|' + '\n'
            x = ''
            y = ''
        print(xy)

    def make_turn(self, cell: list):
        turn = False
        #global playingField
        i = 0

        for cellPlayingField in self.playingField:
            if cellPlayingField[2] == ' ' and cell[0] == cellPlayingField[0] and cell[1] == cellPlayingField[1]:
                # print("Attempt has been accepted!")
                turn = True
                self.playingField.pop(i)
                self.playingField.append(cell)
                self.playingField.sort()
                break
            else:
                turn = False
                i += 1
                continue

        return turn

    def check_draft(self):
        draft = True
        nn = 0
        for i in range(1, self.scale_field + 1):
            for j in range(1, self.scale_field + 1):
                if self.playingField[nn][2] == ' ':
                    draft = False
                    break
                nn += 1
        return draft

    def check_win_f(self, player: str):
        win = False
        nn = 0
        ii = self.scale_field
        res1 = ''
        res2 = ''
        res3 = ''
        for i in range(1, self.scale_field + 1):
            for j in range(1, self.scale_field + 1):
                if j == self.playingField[nn][1] and self.playingField[nn][2] == player:
                    res1 += self.playingField[nn][2]
                #i=1
                #j = 1 2 3
                if self.playingField[nn][1] == ii and self.playingField[nn][0] == i:
                    res2 += self.playingField[nn][2]
                    ii -= 1

                if j == self.playingField[nn][1] and i == j :
                    res3 += self.playingField[nn][2]
                    if i == self.scale_field:
                        nn -= 1
                nn += 1

                if j%3 == 0 and player * 3 in (res1, res3, res3):
                    break

                elif j%3 == 0:
                    res1 = ''
                else:
                    continue

            if player * 3 in (res1, res2, res3) :
                win = True
                break
            else:
                continue


        return win

    def check_win(self, player: str):

        win = False
        tempPlayingField = self.playingField.copy()
        if self.check_win_f(player):
            win = True
        else:
            transpPlayingField = []
            for nn in range(0, self.playingField.__len__()):
                x = self.playingField[nn][0]
                y = self.playingField[nn][1]
                transpPlayingField.append((y, x, self.playingField[nn][2]))
            transpPlayingField.sort()
            self.playingField = transpPlayingField
            if self.check_win_f(player):
                win = True
            else:
                win = False
            self.playingField = tempPlayingField

        return win



