class Player:
    def __init__(self,name,category,score,bestfigure,team):
        self.__playerName=name
        self.__category=category
        self.__score=score
        self.__bestfigure=bestfigure
        self.__teamname=team


    def display(self):
        print('''
        Id: {}
        Name: {}
        Category: {}
        Score: {}
        Best Figure: {}'''.format(self.__playerNo,self.__playerName,self.__category,self.__score,self.__bestfigure))


    def setname(self,name):
        self.__playerName=name

    def setid(self,id):
        self.__playerNo=id

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
        return self.__playerNo

    def getcategory(self):
        return self.__category

    def getscore(self):
        return self.__score

    def getbestfigure(self):
        return self.__bestfigure

    def getteamname(self):
        return self.__teamname
