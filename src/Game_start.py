import numpy as np
import os
from chess import *

if __name__=="__main__":
    #主函数
    GameType=input("Game:chess or go:")
    pl1,pl2=input("player1 and player's name:").split(' ')
    if GameType=="chess":
        myGame=Chess(pl1,pl2)
    elif GameType=="go":
        myGame=Go(pl1,pl2)
    i=0
    print('本游戏需输入正确的指令输入格式为：命令 id i 位置x 位置y')
    print('命令包括：eat，move,lift,positon,get')
    print('友情提示，输入错的命令会被认为是让一手~.~')
    print('如果不觉得眼睛疼')
    print('have fun')
    while True:
        if i%2==0:
            mystr=pl1+" please input:"
            player=pl1
        elif i%2==1:
            mystr=pl2+" please input:"
            player=pl2
        command=input(mystr)
        if command.upper()=="END":
            break
        i+=1
        decomm=command.split(' ')
        if decomm[0].upper() == "eat":
            myGame.Action.EAT(player, int(decomm[1]), int(decomm[2]), int(decomm[3]), int(decomm[4]))
            myGame.Board.ShowBoard()
        elif decomm[0].upper() == "move":
            myGame.Action.MOVE(player, int(decomm[1]), int(decomm[2]), int(decomm[3]), int(decomm[4]))
            myGame.Board.ShowBoard()
        elif decomm[0].upper() == "lift":
            myGame.Action.LIFT(player, int(decomm[1]), int(decomm[2]))
            myGame.Board.ShowBoard()
        elif decomm[0].upper() == "position":
            myGame.Action.Position(player, int(decomm[1]), int(decomm[2]), int(decomm[3]))
            myGame.Board.ShowBoard()
        elif decomm[0].upper() == "get":
            myGame.Action.GetPosInfo(int(decomm[1]), int(decomm[2]))
            i -= 1
            myGame.Board.ShowBoard()
        elif decomm[0].upper() == "5":
            myGame.Action.CountPiece()
            i -= 1
            myGame.Board.ShowBoard()
        else:
            print('输入错的指令让一手')
            continue














        
