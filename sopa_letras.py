#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#------------------------------
# Name:     
# Purpose:  
# 
# @uthor:   acph - dragopoot@gmail.com
#
# Created:     jue may 23 09:06:55 CDT 2013
# Copyright:   (c) acph 2012
# Licence:     GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
#------------------------------

"""Program for create a soup of letters. :P"""

import numpy as np
import codecs

letras = u"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def remove_accent(s):
    accents = {'Á': "A", 'É': "E", 'Í':"I", 'Ó':"O", 'Ú':"U",
               'Ü':"U",
               'á': "a", 'é': "e", 'í':"i", 'ó':"o", 'ú':"u",
               'ü': 'u'
                }
    for letter in accents.keys():
        if letter in s:
            s = s.replace(letter, accents[letter])
    return s


def create_grid(k, l):
    """Create a grid for spanish soup
    
    Arguments:
    - `k`: number of rows
    - `l`: number of columns
    """
    return np.zeros((k, l), dtype="<U1")


def grid_random_pos(n, m):
    """Return random indeces for n and m.
    
    Arguments:
    - `n`: number of rows of the array
    - `m`: number of columns of array
    """
    i = np.random.randint(0, n)
    j = np.random.randint(0, m)
    return i, j


def put_word_list(grid, word_list):
    """Place the word list in the grid
    
    Arguments:
    - `grid`:
    - `word_list`:
    """
    direction = ["|", "-", "/", "\\"]
    orientation = [1, -1]
    n, m = grid.shape
    new_grid = grid.copy()
    for word in word_list:
        O = np.random.choice(orientation)
        word = word[::O]        # change word orientation
        w_len = len(word)       # word lenght
        D = np.random.choice(direction)
        if D == "|":            # down vertical oriented
            flag = True
            while flag:
                init_i, init_j = grid_random_pos(n, m)
                final_i = init_i + w_len
                final_j = init_j
                if final_i >= n or final_j >= m:
                    continue
                # - check
                l_word = list(word)
                Is = range(init_i, final_i)
                js = [init_j] * w_len
                stop = False
                for index in range(w_len):
                    i = Is[index]
                    j = js[index]
                    char = l_word[index]
                    grid_char =  new_grid[i,j]
                    if grid_char != char and grid_char != '':
                        stop = True
                        break
                if stop:
                    continue
                # - check
                else:
                    l_word = list(word)
                    new_grid[init_i:final_i, init_j] = l_word
                    flag = False
        elif D == "-":          # right horizontal oriented
            flag = True
            while flag:
                init_i, init_j = grid_random_pos(n, m)
                final_i = init_i 
                final_j = init_j + w_len
                if final_i >= n or final_j >= m:
                    continue
                # - check -
                l_word = list(word)
                Is = [init_i] * w_len
                js = range(init_j, final_j)
                stop = False
                for index in range(w_len):
                    i = Is[index]
                    j = js[index]
                    char = l_word[index]
                    grid_char =  new_grid[i,j]
                    if grid_char != char and grid_char != '':
                        stop = True
                        break
                if stop:
                    continue
                # - check
                else:
                    l_word = list(word)
                    new_grid[init_i, init_j:final_j] = l_word
                    flag = False
        elif D == "/":          # up diagonal oriented
            flag = True
            while flag:
                init_i, init_j = grid_random_pos(n, m)
                final_i = init_i - w_len
                if final_i < 0:
                    continue
                final_j = init_j + w_len
                if final_j >= m:
                    continue
                # - check - /
                l_word = list(word)
                Is = range(final_i, init_i)[::-1]
                js = range(init_j, final_j)
                stop = False
                for index in range(w_len):
                    i = Is[index]
                    j = js[index]
                    char = l_word[index]
                    grid_char =  new_grid[i,j]
                    if grid_char != char and grid_char != '':
                        stop = True
                        break
                if stop:
                    continue
                # - check
                else:
                    l_word = list(word)
                    Is = range(final_i, init_i)[::-1]
                    js = range(init_j, final_j)
                    for index in range(w_len):
                        i = Is[index]
                        j = js[index]
                        char = l_word[index]
                        new_grid[i,j] = char
                    flag = False
        elif D == "\\":         # down diagonal oriented
            flag = True
            while flag:
                init_i, init_j = grid_random_pos(n, m)
                final_i = init_i + w_len
                final_j = init_j + w_len
                if final_i >= n or final_j >= m:
                    continue
                # - check - \
                l_word = list(word)
                Is = range(init_i, final_i)
                js = range(init_j, final_j)
                stop = False
                for index in range(w_len):
                    i = Is[index]
                    j = js[index]
                    char = l_word[index]
                    grid_char =  new_grid[i,j]
                    if grid_char != char and grid_char != '':
                        stop = True
                        break
                if stop:
                    continue
                # - check
                else:
                    l_word = list(word)
                    Is = range(init_i, final_i)
                    js = range(init_j, final_j)
                    for index in range(w_len):
                        i = Is[index]
                        j = js[index]
                        char = l_word[index]
                        new_grid[i,j] = char
                    flag = False
        else :
            print( "----------")
            print( "This is not posible ... :D")
            print( "----------")
    return new_grid


def fill_grid(grid, blank=False):
    """Fill the grid with random letters.

    Arguments:
    - `grid`:
    """
    new_grid = grid.copy()
    n, m = grid.shape
    for i in range(n):
        for j in range(m):
            if new_grid[i, j] == '':
                if blank:
                    new_grid[i, j] = ' '
                else:
                    char = np.random.choice(list(letras))
                    new_grid[i, j] = char
    return new_grid


if __name__ == '__main__':
    import argparse

    def argument_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('wordlist',
                            help='File containing a list of words.')
        parser.add_argument('--gridsize', '-g', default=30,
                            help='Number of columns and rows [30].')
        parser.add_argument('--header', '-j', default='',
                            help='Text to put at the begining fo the file')

        return parser

    args = argument_parser().parse_args()
    # palabras = [u"PASITO", u"NACHO", u"IGNACIO", u"TORRE", u"CUBOS",
    #             u"ABUELO", u"NIÑO", u"ENFERMEDAD", u"INFARTO",
    #             u"ENSEÑANZA", u"CAMINAR", u"FELICIDAD", u"JUEGO",
    #             u"SUSTO", u"HOSPITAL", u"CAMA", u"ESPERANZA", u"ESTORNUDO",
    #             u"PARQUE", u"ELEFANTE"]
    # grid = create_grid(30, 30)
    ngrid =  int(args.gridsize)
    grid = create_grid(ngrid, ngrid)
    palabrasfile = args.wordlist
    header = args.header

    with open(palabrasfile, 'r') as inf:
        palabras = inf.read().split()
    palabras = [remove_accent(p.upper()) for p in palabras]

    w_grid = put_word_list(grid, palabras)
    b_grid = fill_grid(w_grid, True)
    
    with codecs.open('pru30.txt', 'w', 'utf-8') as outf:
        # outf.write("Escuela 21. 4to-C\n")
        # outf.write("SOPA DE LETRAS: \n")
        outf.write(header + '\n\n')

        for l in b_grid:
            line = ' '.join(list(l))
            line += "\n"
            outf.write(line)

        outf.write("\n\n")
        for word in palabras:
            line = word + '\n'
            outf.write(line)
            
    w_grid = fill_grid(w_grid)
    
    with codecs.open('pru_noblank30.txt', 'w', 'utf-8') as outf:
        # outf.write("Escuela 21. 4to-C\n")
        # outf.write("SOPA DE LETRAS: \n")
        outf.write(header + '\n\n')

        for l in w_grid:
            line = ' '.join(list(l))
            line += "\n"
            outf.write(line)

        outf.write("\n\n")
        for word in palabras:
            line = word + '\n'
            outf.write(line)

    
