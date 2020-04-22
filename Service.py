import Dao,Exceptions,re

def getplayerdetails():
    try:
        playerlist=Dao.getplayerfromdb()
    except Exceptions.DaoExceptions:
        raise Exceptions.ServiceExceptions("Cant fetch player details form database!!!")
    else:
        return playerlist

def addplayer(player):
    try:
        playerid = Dao.insertplayertodb(player)
    except Exceptions.DaoExceptions:
        raise Exceptions.ServiceExceptions("Error while adding player to database!!!!!")
    else:
        return playerid

def getplayersforteam(team):
    name=team.upper()
    try:
        playerList= Dao.getplayerfromdb()
        teamList= Dao.getteamsfromdb()
        playerTeam= Dao.getTeamplayerList()
    except Exceptions.DaoExceptions:
        raise Exceptions.ServiceExceptions("Error while fatching  player from database!!!!!")
    else:
        for i in teamList:
            if i[1]==name:
                teamid=i[0]
                break
        playeridlist=[]
        for i in playerTeam:
            if i[1]==teamid:
                playeridlist.append(i[0])
        playerinfo=[]
        for i in playerList:
            if i[0] in playeridlist:
                playerinfo.append([i[1],i[2]])
        playerinfo.sort(key=lambda playerinfo: playerinfo[0])
        return playerinfo

def validatecategory(arg:str):
    category=arg.upper()
    if not (category=="BATSMAN" or category=="BOWLER" or category=='ALLROUNDER'):
        raise Exceptions.InvalidCategoryExceptions('Invalid category name please check your input!!!')
    else:
        return category

def validateteamname(arg:str):
    teamname= arg.upper()
    try:
        teamlist=Dao.getteamsfromdb()
    except Exceptions.DaoExceptions as e:
        raise Exceptions.ServiceExceptions(e.message)
    else:
        count=0
        for i in teamlist:
            if i[1]==teamname:
                count+=1
                break
        if count==0:
            raise Exceptions.InvalidTeamNameExceptions('Invalid team name check your input!!!!!')
        else:
            return teamname

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
        raise Exceptions.ServiceExceptions('Invalid score check your input:')

def validateduplicate(name:str,category:str,team:str):
    players=getplayersforteam(team)
    playersofcategory=[]
    flag=0
    for player in players:
        if player[1].upper()==category:
            playersofcategory.append(player)

    for player in playersofcategory:
        if player[0].upper()==name.upper():
            flag+=1

    if flag==0:
        return True
    else:
        raise Exceptions.DuplicateEntryException('Player details already exists in database!!!')




