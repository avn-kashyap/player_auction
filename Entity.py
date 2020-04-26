class Player:
    def __init__(self,name:str,category:str,score:int,bestfigure:str,team:str=None,id:int=None):
        self.__id = id
        self.__playerName=name
        self.__category=category
        self.__score=score
        self.__bestfigure=bestfigure
        self.__teamname=team


    def __str__(self):
       return '''
        Id: {}
        Name: {}
        Category: {}
        Score: {}
        Best Figure: {}'''.format(self.__id,self.__playerName,self.__category,self.__score,self.__bestfigure)


    def setname(self,name):
        self.__playerName=name

    def setid(self,id):
        self.__id=id

    def setcategory(self,category):
        self.__category=category

    def setscore(self,score):
        self.__score=score

    def setbestfigure(self,figure):
        self.__bestfigure=figure

    def setteamname(self,teamname):
        self.__teamname=teamname

    def getname(self):
        return self.__playerName

    def getid(self):
        return self.__id

    def getcategory(self):
        return self.__category

    def getscore(self):
        return self.__score

    def getbestfigure(self):
        return self.__bestfigure

    def getteamname(self):
        return self.__teamname

class Team:

    def __init__(self,team_id:int=None,team_name:str=None):
        self.__team_id = team_id
        self.__team_name = team_name

    def __str__(self):
        return f'''
        Team id: {self.__team_id}
        Team name: {self.__team_name}
        '''

    def setteamid(self,teamid):
        self.__team_id = teamid

    def setteamname(self,teamname):
        self.__team_name = teamname

    def getteamid(self):
        return self.__team_id

    def getteamname(self):
        return self.__team_name


class TeamPlayer:

    def __init__(self,teamid:int=None,playerid:int=None):
        self.__teamid = teamid
        self.__playerid = playerid

    def setteamid(self,teamid):
        self.__teamid = teamid

    def setplayerid(self,playerid):
        self.__playerid = playerid

    def getteamid(self):
        return self.__teamid

    def getplayerid(self):
        return self.__playerid

    def __str__(self):
        return f'''
                Team id: {self.__teamid}
                Player id: {self.__playerid}
                '''