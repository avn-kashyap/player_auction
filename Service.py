import Dao,Exceptions,re


def addplayer(player):
    try:
        playerid = Dao.insertplayertodb(player)
    except Exceptions.DaoExceptions:
        raise Exceptions.ServiceExceptions("Error while adding player to database!!!!!")
    else:
        return playerid

def getplayersforteam(teamname:str)->list:
    name=teamname.upper()
    teamid = None
    try:
        playerList= Dao.getplayerfromdb()
        teamList= Dao.getteamsfromdb()
        playerTeam= Dao.getTeamplayerList()
    except Exceptions.DaoExceptions as e:
        raise Exceptions.ServiceExceptions(e.message)
    else:
        for team in teamList:
            if team.getteamname()==name:
                teamid=team.getteamid()
                break
        playeridlist=[]
        for playerteam in playerTeam:
            if playerteam.getteamid()==teamid:
                playeridlist.append(playerteam.getplayerid())
        playerinfo=[]
        for player in playerList:
            if player.getid() in playeridlist:
                playerinfo.append(player)
        playerinfo.sort(key=lambda playerinfo: playerinfo.getname())
        if len(playeridlist) == 0:
            raise Exceptions.NoPlayersFoundException('No players found!!!')
        else:
            return playerinfo

def validatecategory(arg:str):
    category=arg.upper()
    if not (category=="BATSMAN" or category=="BOWLER" or category=='ALLROUNDER'):
        raise Exceptions.InvalidCategoryExceptions('Invalid category name please check your input!!!')
    else:
        return category

def validateteamname(teamname:str):
    team_name= teamname.upper()
    try:
        teamlist=Dao.getteamsfromdb()
    except Exceptions.DaoExceptions as e:
        raise Exceptions.ServiceExceptions(e.message)
    else:
        count=0
        for team in teamlist:
            if team.getteamname()==team_name:
                count+=1
                break
        if count==0:
            raise Exceptions.InvalidTeamNameExceptions('Invalid team name check your input!!!!!')
        else:
            return team_name

def validatebestfigure(arg:str):
    bestfigure= arg
    pattern='[0-9]{1,2}/[0-9]{1,2}'
    if bool(re.fullmatch(pattern,bestfigure)):
        return bestfigure
    else:
        raise Exceptions.InvalidBestfigreException('Best figure should be in "11/11" format ')

def validatebatsman(score:int):
    if score in range(50,201):
        return score
    else:
        raise Exceptions.NotBatsmanException('Invalid batsman check your input!')

def validatebowler(score:int,bestfigure:str):
    if score in range(0,201) and not bool(re.fullmatch('[0]{1,2}/[0-9]{1,2}',bestfigure)):
        return score
    else:
        raise Exceptions.NotBowlerExceptions('Invalid bowler check your input!!')

def validatescore(score:int):
    if score in range(0,201):
        return score
    else:
        raise Exceptions.ServiceExceptions('Invalid score check your input!!')

def validateduplicate(name:str,category:str,team:str):
    players=getplayersforteam(team)
    playersofcategory=[]
    flag=0
    for player in players:
        if player.getcategory().upper()==category:
            playersofcategory.append(player)

    for player in playersofcategory:
        if player.getname().upper()==name.upper():
            flag+=1

    if flag==0:
        return True
    else:
        raise Exceptions.DuplicateEntryException('Player details already exists in database!!!')




