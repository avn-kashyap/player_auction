import Utility,Exceptions
"""
This module perform database interactions

"""
def getplayerfromdb():
    try:
        connector= Utility.getconnection()
        pointer = connector.cursor()
        pointer.execute("select* from player;")
        resultset=pointer.fetchall()
        playerlist=[]
        for i in resultset:
            playerlist.append(i)
        return playerlist
    except Exceptions.DaoExceptions as e:
        raise Exceptions.DaoExceptions(e.message)

def getteamsfromdb():
    try:
        connector= Utility.getconnection()
        pointer = connector.cursor()
        pointer.execute("select* from team;")
        resultset=pointer.fetchall()
        teamlist=[]
        for i in resultset:
            teamlist.append(i)
        return teamlist
    except Exceptions.DaoExceptions as e:
        raise Exceptions.DaoExceptions(e.message)



def insertplayertodb(player):
    try:
        connector= Utility.getconnection()
        pointer = connector.cursor()
        query="insert into player(player_name,category,highest_score,best_figure) values (%s,%s,%s,%s);"
        values=[player.getname(),player.getcategory(),player.getscore(),player.getbestfigure()]
        pointer.execute(query,values)
        connector.commit()
        playerId=pointer.lastrowid
        query = "insert into teamplayer  values(%s,%s);"
        teamlist=getteamsfromdb()
        teamid=0
        for i in teamlist:
            if i[1]==player.getteamname():
                teamid=i[0]
                break
        values=[playerId,teamid]
        pointer.execute(query,values)
        connector.commit()
        return playerId
    except Exceptions.DaoExceptions as e:
        raise Exceptions.DaoExceptions(e.message)



def getTeamplayerList():
    try:
        connector= Utility.getconnection()
        pointer = connector.cursor()
        query= "select* from teamplayer;"
        pointer.execute(query)
        resultset= pointer.fetchall()
        teamplayerlist=[]
        for i in resultset:
            teamplayerlist.append(i)
        return teamplayerlist
    except Exceptions.DaoExceptions as e:
        raise Exceptions.DaoExceptions(e.message)



