from random import randrange
class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix

    @staticmethod
    def create2(x, y):
        matrix = [[0 for i in range(x)] for j in range(y)]
        return matrix
    
    @staticmethod
    def create_unit(x):
        matrix = [[0 for i in range(x)] for j in range(x)]
        for i in range(x):
            matrix[i][i] = 1
        return matrix
    

    @staticmethod
    def fill_random(x, y):
        matrix = [[0 for i in range(x)] for row in range(y)]
        for i in range(x, y):
            n = randrange(x, y)
            matrix[i][i] = n
        return matrix
        
        
    
    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    

m = matrix.create2(3,3)
#m = matrix.create_unit(5)
m = matrix.fill_random(5, 9)
matrix.print(m)
