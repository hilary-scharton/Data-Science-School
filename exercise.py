# coding=utf-8
# =========================
# Overview
# =========================

####################################################################################
# ========================
# Part 1: Vector and Complex Numbers
# ========================

# In this exercise you will use what you have learned to implement a Vector
# class and a complex number class.

# ========================
# The Vector class
# ========================

# Write definitions for a class called Vector.
# Your definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar multiplication,
# length, and comparison.
import cmath


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def smult(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __len__(self):
        return 2
# this length is always 2 ¯\_(ツ)_/¯

    def __cmp__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

# checking


u = Vector(0, 1)
print u

v = Vector(1, 0)
print v

w = Vector(1, 1)
print w

a = u + v
print a

b = u - v
print b

c = Vector(5, 5)

print(c.smult(u))

print(cmp(w, a))


# =========================
# The derived Complex class
# =========================

# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.

class MyComplex(Vector):
    pass

# import cmath, call it good


z1 = complex(2, 3)
z2 = complex(4, 5)

print(z1, z2)

add_comp = z1 + z2
print(add_comp)
print(z1.conjugate())

####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# In this task you will be writing a simple game of tic-tac-toe.
# You should expect to find this exercise more challenging than Part 1.
# Please write docstrings for each class and method.
# As you walk through each element, think about how the game's objects are organized.
# Does it seem like the most efficient way to do things to you?
# A common criticism of object-oriented programming is that it can lead to
# excessive abstractions and over complication.

# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:

class Piece(object):
    pass

# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:

class X(Piece):
    pass

class O(Piece):
    pass

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

# I feel like what you wanted us to see was that, even if you _can_ use a class, really think about
# if you _should_.  I started out with all four of the classes you asked for, but it was convoluted.
# also, it's very irritating to write the exact same stuff for both X and O.
# i was reading this book (Head First Python,) and it was talking about the point of functions and classes
# is really so you can reuse your code. if the point is reuse, seems crazysauce to have both.  in fact,
# i'd argue that you don't really need a piece class, except if you were thinking about
# "pieces" as "players," it might be nice to bucket just player things.

'''this will define the board, it's spaces, what winning looks like, and make stuff go'''
class Board:

    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.how_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.move_count = 0

    def make_board(self):
        print('')
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print('')

    def playing(self):
        while True:
            self.exes()
            self.ohs()

    def go(self):
        self.make_board()
        self.playing()

    def winning(self):
        for i in self.how_to_win:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] == "X":
                print('X wins')
                quit()
            elif self.board[i[0]] == self.board[i[1]] == self.board[i[2]] == "O":
                print('O wins')
                quit()
        while self.move_count == 9:
            print('tie')
            quit()

# this could be a piece or player class next, but why.  it _should_ be one reusable function that does the "moves,"

# if i were going to simplify so i didn't have one for X and one for Y,
# i'd do something like this:
#    def open_spot(self):
#        if self.board[place] != 'X' and self.board[place] != 'O':
#            return True

#    def full_board(self):
#        if self.open_spot:
#            return False
#        return True

# but now i'm getting quite far away from what you initially asked for, so i'm leaving this here so you can
# see it.  even though it's gross :)
    def exes(self):

        place = int(input('where do you want to put your X? '))
        if self.board[place] != 'X' and self.board[place] != 'O':
            self.board[place] = 'X'
            self.make_board()
            self.move_count += 1
        else:
            print('that spot is taken')
            self.exes()
        self.winning()
        print('')

    def ohs(self):
        place = int(input('where do you want to put your O? '))
        if self.board[place] != 'X' and self.board[place] != 'O':
            self.board[place] = 'O'
            self.make_board()
            self.move_count += 1
        else:
            print('that spot is taken')
            self.ohs()
        self.winning()
        print('')


start = Board()
start.go()

# this task was really long and, after working on it at least 5 days, i'm tired and discouraged.  i wonder if
# it could be split up into smaller chunks so students would feel like they're making progress? :)
