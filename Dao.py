import Utility,Exceptions
from Entity import Player,Team,TeamPlayer

"""
This module perform database interactions

"""


def getplayerfromdb() -> list:
    connector = None
    try:
        connector = Utility.getconnection()
        pointer = connector.cursor()
        pointer.execute("select* from player;")
        resultset = pointer.fetchall()
        playerlist = []
        for player in resultset:
            player_obj = Player(name = player[1],category = player[2],score = player[3],
                                bestfigure = player[4],id = player[0])
            playerlist.append(player_obj)
        return playerlist
    except Exception:
        raise Exceptions.DaoExceptions('Error occurred while fetching player data from database')
    finally:
        connector.close()


def getteamsfromdb()->list:
    connector = None
    try:
        connector = Utility.getconnection()
        pointer = connector.cursor()
        pointer.execute("select* from team;")
        resultset = pointer.fetchall()
        teamlist = []
        for team in resultset:
            team_obj = Team(team[0],team[1])
            teamlist.append(team_obj)
        return teamlist
    except Exception:
        raise Exceptions.DaoExceptions('Error occurred while fetching teams data from database')
    finally:
        connector.close()


def insertplayertodb(player: Player) -> int:
    connector = None
    try:
        connector = Utility.getconnection()
        pointer = connector.cursor()
        query = "insert into player(player_name,category,highest_score,best_figure) values (%s,%s,%s,%s);"
        values = [player.getname(),player.getcategory(),player.getscore(),
                  player.getbestfigure()]
        pointer.execute(query,values)
        connector.commit()
        playerId = pointer.lastrowid
        query = "insert into teamplayer  values(%s,%s);"
        teamlist = getteamsfromdb()
        teamid = None
        for team in teamlist:
            if team.getteamname() == player.getteamname():
                teamid = team.getteamid()
                break
        values = [playerId,teamid]
        pointer.execute(query,values)
        connector.commit()
        return playerId
    except Exception:
        raise Exceptions.DaoExceptions('Error occurred while adding player to database')
    finally:
        connector.close()


def getTeamplayerList()->list:
    connector = None
    try:
        connector = Utility.getconnection()
        pointer = connector.cursor()
        query = "select* from teamplayer;"
        pointer.execute(query)
        resultset = pointer.fetchall()
        teamplayerlist = []
        for teamplayer in resultset:
            teamplayer_obj = TeamPlayer(teamid = teamplayer[1],playerid = teamplayer[0])
            teamplayerlist.append(teamplayer_obj)
        return teamplayerlist
    except Exception:
        raise Exceptions.DaoExceptions('Error occurred while fetching teampalyer details')
    finally:
        connector.close()


