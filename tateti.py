
class TaTeTi():

    def  __init__(self):
            self.tablero_inicial = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n---+---+---\n3.1|3.2|3.3'
            self.positions = ['1.1', '1.2', '1.3',
                            '2.1', '2.2', '2.3',
                            '3.1', '3.2', '3.3']
                            
            self.valid = ['1.1', '1.2', '1.3',
                          '2.1', '2.2', '2.3',
                          '3.1', '3.2', '3.3']
            self.board = {value: value for value in self.positions}

    def __str__(self):
        self.expected = self.tablero_inicial
        return self.expected

    def input_position(self):
        play = True
        while(play):
            self.po = str(input('escriba una posición'))
            for correct in self.valid:
                if correct == self.po:
                    self.valid.remove(correct)
                return self.po       
   
    def win(self):

​       jugador = ' o '
​       jugadores = [' o ', ' x ']
​       result = False
​       for jugador in jugadores:
​
            if self.board['1.1'] == jugador and self.board['2.2'] == jugador and self.board['3.3'] == jugador:
                result = True

            if self.board['1.3'] == jugador and self.board['2.2'] == jugador and self.board['3.1'] == jugador:
                result = True

            if self.board['1.1'] == jugador and self.board['2.1'] == jugador and self.board['3.1'] == jugador:
                result = True
​
            if self.board['1.2'] == jugador and self.board['2.2'] == jugador and self.board['3.2'] == jugador:
                result = True
​
            if self.board['1.3'] == jugador and self.board['2.3'] == jugador and self.board['3.3'] == jugador:
                result = True

            if self.board['1.1'] == jugador and self.board['1.2'] == jugador and self.board['1.3'] == jugador:
                result = True

            if self.board['2.1'] == jugador and self.board['2.2'] == jugador and self.board['2.3'] == jugador:
                result = True

            if self.board['3.1'] == jugador and self.board['3.2'] == jugador and self.board['3.3'] == jugador:
                result = True
​    return result

    def game(self): 
        self.win = False
        self.valid = []
        self.piece = 'o'
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
            if len(self.valid) == 0:
                winner = 'Ninguno'
            return winner
 


if __name__ == '__main__':
    game = TaTeTi()
    print('Ganó ' + game.game())
