"""Module that let you choose the game version."""

def who_are_you(board,index,player):
    if board[index] not in [0,player]:
        return "ennemie"
    if board[index] == player:
        return "allier"
    return "rien"


def capture_classic(board, n, player, i):
    removed = []
    removeright = []
    removeleft = []

    #check a droite du pion
    mustclear = False
    for index in range(i+1,n+2,1):
        if index == n:
            break
        who = who_are_you(board,index,player)
        if who == "ennemie":
            removeright.append(index)
        elif who == "rien":
            mustclear = True
            break
        elif who == "allier":
            break

    if mustclear is True:
        removeright.clear()

    #check a gauche du pion
    mustclear = False
    for index in range(i-1,-2,-1):
        if index == -1:
            break
        who = who_are_you(board,index,player)
        if who == "ennemie":
            removeleft.append(index)
        elif who == "rien":
            mustclear = True
            break
        else:
            break
    if mustclear is True:
        removeleft.clear()

    removed.extend(removeleft)
    removed.extend(removeright)
    return removed


def capture_continu(board, n, player, i):
    removed = []
    removeright = []
    removeleft = []


    #check a droite du pion
    mustclear= False
    for index in range(i+1,n+3,1):
        if index == n:
            #check droite depuis la premiere cellule
            for index in range(0,n+3,1):
                who = who_are_you(board,index,player)
                if who == "ennemie":
                    removeright.append(index)
                elif who == "rien":
                    mustclear = True
                    break
                else:
                    break
        #check droite classique
        who = who_are_you(board,index,player)
        if who == "ennemie":
            removeright.append(index)
        elif who == "rien":
            mustclear = True
            break
        else:
            break
    if mustclear is True:
        removeright.clear()

    #check a gauche du pion
    mustclear= False
    for index in range(i-1,-2,-1):
        if index == -1:
            for index in range(n-1,-2,-1):
            #check gauche depuis la derniere cellule
                who = who_are_you(board,index,player)
                if who == "ennemie":
                    removeleft.append(index)
                elif who == "rien":
                    mustclear = True
                    break
                else:
                    break
        #check gauche classique
        who = who_are_you(board,index,player)
        if who == "ennemie":
            removeleft.append(index)
        elif who == "rien":
            mustclear = True
            break
        else:
            break
    if mustclear is True:
        removeleft.clear()





    removed.extend(removeleft)
    removed.extend(removeright)
    return removed


def capture_ambush(board, n, player, i):
    removed = []
    removeright = []
    removeleft = []
    #check si groupe allier est capturer
    #check a droite du pion
    mustclear = False
    for index in range(i+1,n+2,1):
        if index == n:
            break
        who = who_are_you(board,index,player)
        if who == "allier":
            removeright.append(index)
        elif who == "rien":
            mustclear = True
            break
        else:
            break
    if mustclear is True:
        removeright.clear()
    #check a gauche du pion
    mustclear = False
    for index in range(i-1,-2,-1):
        if index == -1:
            break
        who = who_are_you(board,index,player)
        if who == "allier":
            removeleft.append(index)
        elif who == "rien":
            mustclear = True
            break
        else:
            break
    if mustclear is True:
        removeleft.clear()

    removed.extend(removeleft)
    removed.extend(removeright)
    if not removed:
        removed = capture_classic(board, n, player, i)
    return removed
