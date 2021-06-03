# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:56:04 2021

@author: hankc
"""

from vpython import *
screen = [[0 for i in range(150)]for j in range(40)]
#screen = [[0 for i in range(5)]for j in range(8)] #for test

def light(chr, x ) :
    if chr == '0':
        screen[0][0] = 0
        screen[0][1] = 1
        screen[0][2] = 1
        screen[0][3] = 1
        screen[0][4] = 0
        screen[1][0] = 1
        screen[1][1] = 0
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 1
        screen[2][0] = 1
        screen[2][1] = 0
        screen[2][2] = 0
        screen[2][3] = 1
        screen[2][4] = 1
        screen[3][0] = 1
        screen[3][1] = 0
        screen[3][2] = 1
        screen[3][3] = 0
        screen[3][4] = 1
        screen[4][0] = 1
        screen[4][1] = 1
        screen[4][2] = 0
        screen[4][3] = 0
        screen[4][4] = 1
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 1
        screen[6][0] = 0
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 0
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0

    if chr == 'a':
        screen[0][0] = 0
        screen[0][1] = 0
        screen[0][2] = 0
        screen[0][3] = 0
        screen[0][4] = 0
        screen[1][0] = 0
        screen[1][1] = 0
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 0
        screen[2][0] = 0
        screen[2][1] = 1
        screen[2][2] = 1
        screen[2][3] = 1
        screen[2][4] = 0
        screen[3][0] = 0
        screen[3][1] = 0
        screen[3][2] = 0
        screen[3][3] = 0
        screen[3][4] = 1
        screen[4][0] = 0
        screen[4][1] = 1
        screen[4][2] = 1
        screen[4][3] = 1
        screen[4][4] = 1
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 1
        screen[6][0] = 0
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 1
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0

    if chr == 'b':
        screen[0][0] = 1
        screen[0][1] = 0
        screen[0][2] = 0
        screen[0][3] = 0
        screen[0][4] = 0
        screen[1][0] = 1
        screen[1][1] = 0
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 0
        screen[2][0] = 1
        screen[2][1] = 0
        screen[2][2] = 1
        screen[2][3] = 1
        screen[2][4] = 0
        screen[3][0] = 1
        screen[3][1] = 1
        screen[3][2] = 0
        screen[3][3] = 0
        screen[3][4] = 1
        screen[4][0] = 1
        screen[4][1] = 0
        screen[4][2] = 0
        screen[4][3] = 0
        screen[4][4] = 1
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 1
        screen[6][0] = 1
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 0
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0

    if chr == 'c':
        screen[0][0] = 0
        screen[0][1] = 0
        screen[0][2] = 0
        screen[0][3] = 0
        screen[0][4] = 0
        screen[1][0] = 0
        screen[1][1] = 0
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 0
        screen[2][0] = 0
        screen[2][1] = 1
        screen[2][2] = 1
        screen[2][3] = 1
        screen[2][4] = 0
        screen[3][0] = 1
        screen[3][1] = 0
        screen[3][2] = 0
        screen[3][3] = 0
        screen[3][4] = 1
        screen[4][0] = 1
        screen[4][1] = 0
        screen[4][2] = 0
        screen[4][3] = 0
        screen[4][4] = 0
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 1
        screen[6][0] = 0
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 0
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0
        
    if chr == 'd':
        screen[0][0] = 0
        screen[0][1] = 0
        screen[0][2] = 0
        screen[0][3] = 0
        screen[0][4] = 1
        screen[1][0] = 0
        screen[1][1] = 0
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 1
        screen[2][0] = 0
        screen[2][1] = 1
        screen[2][2] = 1
        screen[2][3] = 0
        screen[2][4] = 1
        screen[3][0] = 1
        screen[3][1] = 0
        screen[3][2] = 0
        screen[3][3] = 1
        screen[3][4] = 1
        screen[4][0] = 1
        screen[4][1] = 0
        screen[4][2] = 0
        screen[4][3] = 0
        screen[4][4] = 1
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 1
        screen[6][0] = 0
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 1
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0

    if chr == 'e':
        screen[0][0] = 0
        screen[0][1] = 0
        screen[0][2] = 0
        screen[0][3] = 0
        screen[0][4] = 0
        screen[1][0] = 0
        screen[1][1] = 0
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 0
        screen[2][0] = 0
        screen[2][1] = 1
        screen[2][2] = 1
        screen[2][3] = 1
        screen[2][4] = 0
        screen[3][0] = 1
        screen[3][1] = 0
        screen[3][2] = 0
        screen[3][3] = 0
        screen[3][4] = 1
        screen[4][0] = 1
        screen[4][1] = 1
        screen[4][2] = 1
        screen[4][3] = 1
        screen[4][4] = 1
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 0
        screen[6][0] = 0
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 0
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0

    if chr == 'f':
        screen[0][0] = 0
        screen[0][1] = 0
        screen[0][2] = 1
        screen[0][3] = 1
        screen[0][4] = 0
        screen[1][0] = 0
        screen[1][1] = 1
        screen[1][2] = 0
        screen[1][3] = 0
        screen[1][4] = 1
        screen[2][0] = 0
        screen[2][1] = 1
        screen[2][2] = 0
        screen[2][3] = 0
        screen[2][4] = 0
        screen[3][0] = 1
        screen[3][1] = 1
        screen[3][2] = 1
        screen[3][3] = 0
        screen[3][4] = 0
        screen[4][0] = 1
        screen[4][1] = 1
        screen[4][2] = 0
        screen[4][3] = 0
        screen[4][4] = 1
        screen[5][0] = 1
        screen[5][1] = 0
        screen[5][2] = 0
        screen[5][3] = 0
        screen[5][4] = 1
        screen[6][0] = 0
        screen[6][1] = 1
        screen[6][2] = 1
        screen[6][3] = 1
        screen[6][4] = 0
        screen[7][0] = 0
        screen[7][1] = 0
        screen[7][2] = 0
        screen[7][3] = 0
        screen[7][4] = 0

line1=input("please input line 1 ")
length_of_line1 = len(line1)
for i in range (length_of_line1) :
    light(line1[i] , i)
#print(screen)