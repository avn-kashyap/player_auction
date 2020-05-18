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


        """pointer = connector.cursor(dictionary = True) // to return the data from database
        in form of dictionary and the key: name of the column
                                      value: data of the column
                                      
        pointer = connector.cursor(named_tuple = True) // returns data in the form of named
        tuples
        
        """

        try:
            pointer.execute("select* from player;")
            resultset = pointer.fetchall()
        except :
            raise Exceptions.DaoExceptions('table not found!!')
        playerlist = []
        for player in resultset:
            player_obj = Player(name = player[1],category = player[2],score = player[3],
                                bestfigure = player[4],id = player[0])
            playerlist.append(player_obj)
        return playerlist
    except Exceptions.DaoExceptions as e:
        raise Exceptions.DaoExceptions(e.message+'\nError occurred while fetching player data from database')
    finally:
        if connector is not None:
            connector.close()


def getteamsfromdb()->list:
    connector = None
    try:
        connector = Utility.getconnection()
        pointer = connector.cursor()
        try:
            pointer.execute("select* from team;")
            resultset = pointer.fetchall()
            resultset
        except:
            raise Exceptions.DaoExceptions('table not found!!')
        teamlist = []
        for team in resultset:
            team_obj = Team(team[0],team[1])
            teamlist.append(team_obj)
        return teamlist
    except Exceptions.DaoExceptions as e:
        raise Exceptions.DaoExceptions(e.message+'\nError occurred while fetching teams data from database')
    finally:
        if connector is not None:
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
    except Exception as e:
        raise Exceptions.DaoExceptions('Error occurred while adding player to database')
    finally:
        if connector is not None:
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
        if connector is not None:
            connector.close()


