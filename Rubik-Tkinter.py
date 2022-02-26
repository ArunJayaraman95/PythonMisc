import tkinter as tk
from tkinter import *


O = "orange"
B = "blue"
Y = "yellow"
G = "lime"
W = "white"
R = "red"


#Cube orientation
cube = [[O, O, O, O, O, R, G, Y, Y], #Orange
        [B, Y, Y, B, B, Y, B, B, Y], #Blue
        [R, G, B, R, Y, O, B, B, O], #Yellow
        [R, G, G, B, G, G, G, G, G], #Green
        [W, W, W, W, W, W, W, W, W], #White
        [O, R, Y, Y, R, O, R, R, R]] #Red


#Intermediate pass
#cube = [['blue', 'orange', 'orange', 'yellow', 'orange', 'orange', 'lime', 'blue', 'lime'], ['red', 'lime', 'orange', 'blue', 'blue', 'orange', 'orange', 'red', 'red'], ['yellow', 'orange', 'yellow', 'lime', 'yellow', 'yellow', 'blue', 'red', 'red'], ['red', 'yellow', 'blue', 'blue', 'lime', 'lime', 'lime', 'lime', 'orange'], ['yellow', 'white', 'white', 'white', 'white', 'white', 'blue', 'white', 'lime'], ['yellow', 'yellow', 'white', 'blue', 'red', 'red', 'white', 'red', 'white']]


movesList = []

root = tk.Tk()
canvas = tk.Canvas(root, height = 600, width = 800, bg = "#BBB")
canvas.pack()



#Update the board graphically
def update():
    #s = canvas.create_rectangle(x0, y0, x1, y1, fill = testX)

    #xPos, yPos, and width
    x = 250
    y = 80
    w = 40


    for i in range(3):
        canvas.create_rectangle(x + w * i, y, x + w + w * i, y + w, fill = cube[0][i])
        canvas.create_rectangle(x + w * i, y + w, x + w + w * i, y + 2 * w, fill = cube[0][i + 3])
        canvas.create_rectangle(x + w * i, y + 2 * w, x + w + w * i, y + 3 * w, fill = cube[0][i + 6])

    x -= w * 3
    y += w * 3
    for i in range(3):
        canvas.create_rectangle(x + w * i, y, x + w + w * i, y + w, fill = cube[1][i])
        canvas.create_rectangle(x + w * i, y + w, x + w + w * i, y + 2 * w, fill = cube[1][i + 3])
        canvas.create_rectangle(x + w * i, y + 2 * w, x + w + w * i, y + 3 * w, fill = cube[1][i + 6])

    x += w * 3
    for i in range(3):
        canvas.create_rectangle(x + w * i, y, x + w + w * i, y + w, fill = cube[2][i])
        canvas.create_rectangle(x + w * i, y + w, x + w + w * i, y + 2 * w, fill = cube[2][i + 3])
        canvas.create_rectangle(x + w * i, y + 2 * w, x + w + w * i, y + 3 * w, fill = cube[2][i + 6])

    x += w * 3
    for i in range(3):
        canvas.create_rectangle(x + w * i, y, x + w + w * i, y + w, fill = cube[3][i])
        canvas.create_rectangle(x + w * i, y + w, x + w + w * i, y + 2 * w, fill = cube[3][i + 3])
        canvas.create_rectangle(x + w * i, y + 2 * w, x + w + w * i, y + 3 * w, fill = cube[3][i + 6])

    x += w * 3
    for i in range(3):
        canvas.create_rectangle(x + w * i, y, x + w + w * i, y + w, fill = cube[4][i])
        canvas.create_rectangle(x + w * i, y + w, x + w + w * i, y + 2 * w, fill = cube[4][i + 3])
        canvas.create_rectangle(x + w * i, y + 2 * w, x + w + w * i, y + 3 * w, fill = cube[4][i + 6])

    x -= w * 6
    y += w * 3
    for i in range(3):
        canvas.create_rectangle(x + w * i, y, x + w + w * i, y + w, fill = cube[5][i])
        canvas.create_rectangle(x + w * i, y + w, x + w + w * i, y + 2 * w, fill = cube[5][i + 3])
        canvas.create_rectangle(x + w * i, y + 2 * w, x + w + w * i, y + 3 * w, fill = cube[5][i + 6])

# 0: Orange 1:Blue 2:Yellow 3:Green 4:White 5:Red
#Orientation Moves
def flipForward():
    movesList.append("FlipF")
    temp = cube[5].copy()

    #White to red
    cube[5][8] = cube[4][0]
    cube[5][5] = cube[4][3]
    cube[5][2] = cube[4][6]
    cube[5][7] = cube[4][1]
    cube[5][4] = cube[4][4]
    cube[5][1] = cube[4][7]
    cube[5][6] = cube[4][2]
    cube[5][3] = cube[4][5]
    cube[5][0] = cube[4][8]


    #Orange to White
    cube[4][8] = cube[0][0]
    cube[4][5] = cube[0][3]
    cube[4][2] = cube[0][6]
    cube[4][7] = cube[0][1]
    cube[4][4] = cube[0][4]
    cube[4][1] = cube[0][7]
    cube[4][6] = cube[0][2]
    cube[4][3] = cube[0][5]
    cube[4][0] = cube[0][8]

    #Yellow to Orange
    cube[0] = cube[2].copy()

    #Red to Yellow
    cube[2] = temp

    #Rotate Blue
    temp = cube[1].copy()
    cube[1][0] = temp[2]
    cube[1][1] = temp[5]
    cube[1][2] = temp[8]
    cube[1][3] = temp[1]
    cube[1][5] = temp[7]
    cube[1][6] = temp[0]
    cube[1][7] = temp[3]
    cube[1][8] = temp[6]

    #Rotate Green
    temp = cube[3].copy()
    cube[3][0] = temp[6]
    cube[3][1] = temp[3]
    cube[3][2] = temp[0]
    cube[3][3] = temp[7]
    cube[3][5] = temp[1]
    cube[3][6] = temp[8]
    cube[3][7] = temp[5]
    cube[3][8] = temp[2]

def flipBackward():
    flipForward()
    flipForward()
    flipForward()

def rotateLeft():
    movesList.append("RotateLeft")
    #Rotate yellow top
    temp = cube[2].copy()
    cube[2][0] = temp[2]
    cube[2][1] = temp[5]
    cube[2][2] = temp[8]
    cube[2][3] = temp[1]
    cube[2][4] = temp[4]
    cube[2][5] = temp[7]
    cube[2][6] = temp[0]
    cube[2][7] = temp[3]
    cube[2][8] = temp[6]

    #Rotate white bottom
    temp = cube[4].copy()
    cube[4][0] = temp[6]
    cube[4][1] = temp[3]
    cube[4][2] = temp[0]
    cube[4][3] = temp[7]
    cube[4][4] = temp[4]
    cube[4][5] = temp[1]
    cube[4][6] = temp[8]
    cube[4][7] = temp[5]
    cube[4][8] = temp[2]

    #Rotate
    #Store temp to red (front)
    temp = cube[5].copy()

    #Blue to red
    cube[5][0] = cube[1][2]
    cube[5][1] = cube[1][5]
    cube[5][2] = cube[1][8]
    cube[5][3] = cube[1][1]
    cube[5][4] = cube[1][4]
    cube[5][5] = cube[1][7]
    cube[5][6] = cube[1][0]
    cube[5][7] = cube[1][3]
    cube[5][8] = cube[1][6]

    #Orange to Blue
    cube[1][0] = cube[0][2]
    cube[1][1] = cube[0][5]
    cube[1][2] = cube[0][8]
    cube[1][3] = cube[0][1]
    cube[1][4] = cube[0][4]
    cube[1][5] = cube[0][7]
    cube[1][6] = cube[0][0]
    cube[1][7] = cube[0][3]
    cube[1][8] = cube[0][6]

    #Green to Orange
    cube[0][0] = cube[3][2]
    cube[0][1] = cube[3][5]
    cube[0][2] = cube[3][8]
    cube[0][3] = cube[3][1]
    cube[0][4] = cube[3][4]
    cube[0][5] = cube[3][7]
    cube[0][6] = cube[3][0]
    cube[0][7] = cube[3][3]
    cube[0][8] = cube[3][6]

    #Red (temp) to Green
    cube[3][0] = temp[2]
    cube[3][1] = temp[5]
    cube[3][2] = temp[8]
    cube[3][3] = temp[1]
    cube[3][4] = temp[4]
    cube[3][5] = temp[7]
    cube[3][6] = temp[0]
    cube[3][7] = temp[3]
    cube[3][8] = temp[6]

def rotateRight():
    rotateLeft()
    rotateLeft()
    rotateLeft()


#Main Moves
def L():
    Li()
    Li()
    Li()

def Li():
    movesList.append("Li")
    temp = cube[1].copy()
    cube[1][0] = temp[2]
    cube[1][1] = temp[5]
    cube[1][2] = temp[8]
    cube[1][3] = temp[1]
    cube[1][5] = temp[7]
    cube[1][6] = temp[0]
    cube[1][7] = temp[3]
    cube[1][8] = temp[6]

    temp = [cube[2][6], cube[2][3], cube[2][0]]
    cube[2][6] = cube[5][6]
    cube[2][3] = cube[5][3]
    cube[2][0] = cube[5][0]

    cube[5][6] = cube[4][2]
    cube[5][3] = cube[4][5]
    cube[5][0] = cube[4][8]

    cube[4][2] = cube[0][6]
    cube[4][5] = cube[0][3]
    cube[4][8] = cube[0][0]

    cube[0][6] = temp[0]
    cube[0][3] = temp[1]
    cube[0][0] = temp[2]

def R():
    movesList.append("R")
    temp = cube[3].copy()
    cube[3][0] = temp[6]
    cube[3][1] = temp[3]
    cube[3][2] = temp[0]
    cube[3][3] = temp[7]
    cube[3][5] = temp[1]
    cube[3][6] = temp[8]
    cube[3][7] = temp[5]
    cube[3][8] = temp[2]

    temp = [cube[2][8], cube[2][5], cube[2][2]]

    cube[2][8] = cube[5][8]
    cube[2][5] = cube[5][5]
    cube[2][2] = cube[5][2]

    cube[5][8] = cube[4][0]
    cube[5][5] = cube[4][3]
    cube[5][2] = cube[4][6]

    cube[4][0] = cube[0][8]
    cube[4][3] = cube[0][5]
    cube[4][6] = cube[0][2]

    cube[0][8] = temp[0]
    cube[0][5] = temp[1]
    cube[0][2] = temp[2]

def Ri():
    R()
    R()
    R()

def F():
    movesList.append("F")
    temp = cube[5].copy()
    cube[5][0] = temp[6]
    cube[5][1] = temp[3]
    cube[5][2] = temp[0]
    cube[5][3] = temp[7]
    cube[5][5] = temp[1]
    cube[5][6] = temp[8]
    cube[5][7] = temp[5]
    cube[5][8] = temp[2]

    temp = [cube[2][6], cube[2][7], cube[2][8]]

    cube[2][6] = cube[1][6]
    cube[2][7] = cube[1][7]
    cube[2][8] = cube[1][8]

    cube[1][6] = cube[4][6]
    cube[1][7] = cube[4][7]
    cube[1][8] = cube[4][8]

    cube[4][6] = cube[3][6]
    cube[4][7] = cube[3][7]
    cube[4][8] = cube[3][8]

    cube[3][6] = temp[0]
    cube[3][7] = temp[1]
    cube[3][8] = temp[2]

def Fi():
    F()
    F()
    F()


def D():
    movesList.append("D")
    temp = cube[4].copy()
    cube[4][0] = temp[6]
    cube[4][1] = temp[3]
    cube[4][2] = temp[0]
    cube[4][3] = temp[7]
    cube[4][5] = temp[1]
    cube[4][6] = temp[8]
    cube[4][7] = temp[5]
    cube[4][8] = temp[2]

    temp = [cube[5][6], cube[5][7], cube[5][8]]

    cube[5][6] = cube[1][0]
    cube[5][7] = cube[1][3]
    cube[5][8] = cube[1][6]

    cube[1][0] = cube[0][2]
    cube[1][3] = cube[0][1]
    cube[1][6] = cube[0][0]

    cube[0][2] = cube[3][8]
    cube[0][1] = cube[3][5]
    cube[0][0] = cube[3][2]

    cube[3][8] = temp[0]
    cube[3][5] = temp[1]
    cube[3][2] = temp[2]

def Di():
    D()
    D()
    D()

def B():
    movesList.append("B")
    temp = cube[0].copy()
    cube[0][0] = temp[6]
    cube[0][1] = temp[3]
    cube[0][2] = temp[0]
    cube[0][3] = temp[7]
    cube[0][5] = temp[1]
    cube[0][6] = temp[8]
    cube[0][7] = temp[5]
    cube[0][8] = temp[2]

    temp = [cube[2][0], cube[2][1], cube[2][2]]

    cube[2][0] = cube[3][0]
    cube[2][1] = cube[3][1]
    cube[2][2] = cube[3][2]

    cube[3][0] = cube[4][0]
    cube[3][1] = cube[4][1]
    cube[3][2] = cube[4][2]

    cube[4][0] = cube[1][0]
    cube[4][1] = cube[1][1]
    cube[4][2] = cube[1][2]

    cube[1][0] = temp[0]
    cube[1][1] = temp[1]
    cube[1][2] = temp[2]

def Bi():
    B()
    B()
    B()

def U():
    movesList.append("U")
    temp = cube[2].copy()
    cube[2][0] = temp[6]
    cube[2][1] = temp[3]
    cube[2][2] = temp[0]
    cube[2][3] = temp[7]
    cube[2][5] = temp[1]
    cube[2][6] = temp[8]
    cube[2][7] = temp[5]
    cube[2][8] = temp[2]

    temp = [cube[5][0], cube[5][1], cube[5][2]]

    cube[5][0] = cube[3][6]
    cube[5][1] = cube[3][3]
    cube[5][2] = cube[3][0]

    cube[3][6] = cube[0][8]
    cube[3][3] = cube[0][7]
    cube[3][0] = cube[0][6]

    cube[0][8] = cube[1][2]
    cube[0][7] = cube[1][5]
    cube[0][6] = cube[1][8]

    cube[1][2] = temp[0]
    cube[1][5] = temp[1]
    cube[1][8] = temp[2]

def Ui():
    U()
    U()
    U()

def L2():
    L()
    L()

def R2():
    R()
    R()

def F2():
    F()
    F()

def B2():
    B()
    B()

def D2():
    D()
    D()

def U2():
    U()
    U()

update()
def solveCross():
    print("Starting solve cross")
    flag = False
    if cube[2][1] == W and cube[2][3] == W and cube[2][5] == W and cube[2][7] == W:
        flag = True

    while not flag:

        #TOP ROW

        if cube[5][1] == "white":
            print("R")
            Fi()
            U()
            Li()
            Ui()
        #print(cube[2])

        if cube[3][3] == "white":
            print("G")
            Ri()
            U()
            Fi()
            Ui()
        #print(cube[5])

        if cube[0][7] == "white":
            print("O")
            Bi()
            U()
            Ri()
            Ui()
        #print(cube[5])

        if cube[1][5] == "white":
            print("B")
            Li()
            U()
            Bi()
            Ui()

        # MIDDLE ROW

        #Red Front
        if cube[5][3] == "white":
            while cube[2][3] == "white":
                print("red mid")
                U()
            Li()
        if cube[5][5] == "white":
            while cube[2][5] == "white":
                print("red mid")
                U()
            R()

        #Blue Left
        if cube[1][1] == "white":
            while cube[2][1] == "white":
                print("blue mid")
                U()
            Bi()
        if cube[1][7] == "white":
            while cube[2][7] == "white":
                print("blue mid")
                U()
            F()

        #Green Right
        if cube[3][1] == "white":
            while cube[2][1] == "white":
                print("green mid")
                U()
            B()
        if cube[3][7] == "white":
            while cube[2][7] == "white":
                print("green mid")
                U()
            Fi()

        #Green Right
        if cube[0][3] == "white":
            while cube[2][3] == "white":
                print("orange mid")
                U()
            L()
        if cube[0][5] == "white":
            while cube[2][5] == "white":
                print("orange mid")
                U()
            Ri()

        #BOTTOM ROW (Push to middle)
        if cube[5][7] == "white":
            while cube[2][7] == "white":
                print("red bottom")
                U()
            F()

        if cube[1][3] == "white":
            while cube[2][3] == "white":
                print("blue bottom")
                U()
            L()

        if cube[3][5] == "white":
            while cube[2][5] == "white":
                print("green bottom")
                U()
            R()

        if cube[0][1] == "white":
            while cube[2][1] == "white":
                print("orange bottom")
                U()
            B()

        #WHITE BOTTOM
        if cube[4][1] == "white":
            print("ORANGE")
            while cube[2][1] == "white":
                U()
            B2()

        if cube[4][3] == "white":
            print("GREEN")
            while cube[2][5] == "white":
                U()
            R2()
            print("cube[2][5] is", cube[2][5])

        if cube[4][5] == "white":
            print("BLUE")
            while cube[2][3] == "white":
                U()
            L2()

        if cube[4][7] == "white":
            print("RED")
            while cube[2][7] == "white":
                U()
            F2()

        # if cube[2][1] == "white":
        #     print("Orange solved")
        # if cube[2][3] == "white":
        #     print("Blue solved")
        # if cube[2][5] == "white":
        #     print("Green solved")
        # if cube[2][7] == "white":
        #     print("Red solved")
        # else:
        #     print(cube[2])

        if cube[2][1] == "white" and cube[2][3] == "white" and cube[2][5] == "white" and cube[2][7] == "white":
            flag = True
    print("Setup white cross on yellow...DONE")

    #Flip up pieces to white
    while cube[5][1] != "red" or cube[2][7] != "white":
        U()
    F2()
    while cube[3][3] != "lime" or cube[2][5] != "white":
        U()
    R2()
    while cube[0][7] != "orange" or cube[2][1] != "white":
        U()
    B2()
    while cube[1][5] != "blue" or cube[2][3] != "white":
        U()
        print("Rotate", cube[1][5])
    L2()
    update()
    print("Solve for white cross...DONE")

def solveWhiteCorners():
    flag = False
    def cornerSwap():
        Fi()
        Di()
        F()
        D()

    def cornerRotation():
        # Under spot
        if cube[5][6] == cube[5][4] and cube[4][8] == cube[1][4] and cube[1][6] == cube[2][4]:
            print("HIT1")
            while cube[2][6] != "white" or cube[5][0] != cube[5][4] or cube[1][8] != cube[1][4]:
                cornerSwap()
                print("11111111111111", cube[2][6], cube[5][0], cube[1][8])

        if cube[1][6] == cube[5][4] and cube[5][6] == cube[1][4] and cube[4][8] == cube[2][4]:
            print("HIT2")
            while cube[2][6] != "white" or cube[5][0] != cube[5][4] or cube[1][8] != cube[1][4]:
                cornerSwap()
                print("222222222222", cube[2][6], cube[5][0], cube[1][8])
        if cube[4][8] == cube[5][4] and cube[1][6] == cube[1][4] and cube[5][6] == cube[2][4]:
            print("HIT3")
            while cube[2][6] != "white" or cube[5][0] != cube[5][4] or cube[1][8] != cube[1][4]:
                cornerSwap()
                print("33333333333333",cube[2][6], cube[5][0], cube[1][8])
        print("White face", cube[2])


    flipForward()
    flipForward()
    print(cube)
    while not flag:
        #Look for front-left o-b corner
        if cube[2][6] != "white" or cube[5][0] != cube[5][4] or cube[1][8] != cube[1][4]:
            print("Looking for cornerpiece")
            #On spot
            if cube[1][8] == cube[2][4] and cube[2][6] == cube[5][4] and cube[5][0] == cube[1][4]:
                print("on spot 1")
                while cube[2][6] != "white" or cube[5][0] != cube[5][4] or cube[1][8] != cube[1][4]:
                    cornerSwap()
            if cube[1][8] == cube[5][4] and cube[2][6] == cube[1][4] and cube[5][0] == cube[2][4]:
                print("on spot 2")
                while cube[2][6] != "white" or cube[5][0] != cube[5][4] or cube[1][8] != cube[1][4]:
                    cornerSwap()
            #Under spot
            cornerRotation()
            D()
            cornerRotation()
            D()
            cornerRotation()
            D()
            cornerRotation()
            D()

            if cube[5][2] != cube[5][4] or cube[2][8] != cube[2][4] or cube[3][6] != cube[3][4]:
                Ri()
                Di()
                R()
                cornerRotation()

            if cube[0][8] != cube[0][4] or cube[2][2] != cube[2][4] or cube[3][0] != cube[3][4]:
                R()
                Di()
                Ri()
                cornerRotation()

            if cube[0][6] != cube[5][4] or cube[2][0] != cube[2][4] or cube[1][2] != cube[1][4]:
                Li()
                Di()
                L()
                cornerRotation()

        #If corners are white, set flag to true
        if cube[2][6] == "white" and cube[5][0] == cube[5][4] and cube[1][8] == cube[1][4]:
            flag = True


    flipForward()
    flipForward()
    print("Corner solved")

def allWhite():
    solveWhiteCorners()
    rotateRight()
    solveWhiteCorners()
    rotateRight()
    solveWhiteCorners()
    rotateRight()
    solveWhiteCorners()
    flipForward()
    flipForward()
    D()
    while cube[2][0] != "white":
        Li()
        Di()
        L()
        D()

def middleLayer():
    def edgeLeft():
        Ui()
        Li()
        U()
        L()
        U()
        F()
        Ui()
        Fi()
    def edgeRight():
        U()
        R()
        Ui()
        Ri()
        Ui()
        Fi()
        U()
        F()


    while cube[5][4] != "red":
        rotateLeft()

    for i in range(4):
        for j in range(4):
            if cube[5][1] == cube[5][4]:
                if cube[2][7] == cube[1][4]:
                    edgeLeft()
                else:
                    edgeRight()
            if cube[2][7] == cube[5][4] and cube[5][1] == cube[1][4]:
                rotateLeft()
                U()
                edgeRight()
                rotateRight()
            if cube[2][7] == cube[5][4] and cube[5][1] == cube[3][4]:
                rotateRight()
                Ui()
                edgeLeft()
                rotateLeft()
            U()
        if cube[3][7] == cube[5][4]:
            edgeRight()
        elif cube[3][1] == cube[5][4] or cube[1][5] == cube[5][4]:
            rotateRight()
            edgeRight()
            rotateLeft()
        elif cube[1][3] == cube[5][4] or cube[1][1] == cube[5][4]:
            rotateLeft()
            edgeLeft()
            rotateRight()
        elif cube[1][7] == cube[5][4]:
            edgeLeft()

        rotateLeft()






def condenseMoves():
    c = []
    x = None
    streak = False
    count = 0
    for i in range(len(movesList)):
        if i == 0:
            x = movesList[i]
            count += 1
        elif movesList[i] == x and count != 3:
            count += 1
        else:
            #print(movesList[i], x)
            if count == 1:
                c.append(x)
            elif count == 2:
                if x == "R":
                    c.append("R2")
                elif x == "Li":
                    c.append("L2")
                elif x == "F":
                    c.append("F2")
                elif x == "B":
                    c.append("B2")
                elif x == "U":
                    c.append("U2")
                elif x == "D":
                    c.append("D2")
                else:
                    c.append(x)
                    c.append(x)
            elif count == 3:
                if x == "R":
                    c.append("Ri")
                elif x == "Li":
                    c.append("L")
                elif x == "F":
                    c.append("Fi")
                elif x == "B":
                    c.append("Bi")
                elif x == "U":
                    c.append("Ui")
                elif x == "D":
                    c.append("Di")
                else:
                    c.append(x)
                    c.append(x)
                    c.append(x)
            x = movesList[i]
            #("New x is ", x)
            count = 1
        #print(c, count)

    if count == 1:
        c.append(x)
    elif count == 2:
        if x == "R" or x == "Ri":
            c.append("R2")
        elif x == "Li" or x == "L":
            c.append("L2")
        elif x == "F" or x == "Fi":
            c.append("F2")
        elif x == "B" or x == "Bi":
            c.append("B2")
        elif x == "U" or x == "Ui":
            c.append("U2")
        elif x == "D" or x == "Di":
            c.append("D2")
    elif count == 3:
        if x == "R":
            c.append("Ri")
        elif x == "Ri":
            c.append("R")
        elif x == "L":
            c.append("Li")
        elif x == "Li":
            c.append("L")
        elif x == "B":
            c.append("Bi")
        elif x == "Bi":
            c.append("B")
        elif x == "D":
            c.append("Di")
        elif x == "Di":
            c.append("D")
        elif x == "F":
            c.append("Fi")
        elif x == "Fi":
            c.append("F")
        elif x == "U":
            c.append("Ui")
        elif x == "Ui":
            c.append("U")
    #print(count)
    return c



#Execute These Steps
#solveCross()
#allWhite()
middleLayer()
U2()
Ui()
Li()
U()
L()
U()
F()
Ui()
Fi()

print(cube)
print(movesList)
#Condense the movesList down to compact size
movesList = condenseMoves()
movesList = condenseMoves()

print("\nMove List:", movesList)
#print(cube)

update() #Draw cube on canvas

root.mainloop()