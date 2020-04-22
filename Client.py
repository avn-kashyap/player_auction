import Service,Exceptions,Entity


def displayMenue():
    print("1. Add player\n2. Display players\n3. Exit\n=================================")

if __name__=="__main__":
    while True:
        print("=================================")
        displayMenue()
        try:
            choice = int(input("Enter the option: "))
            print("=================================")
            if choice==1:
                try:
                    name = input("Enter the name: ")
                    category=Service.validatecategory(input('Enter the category: '))
                    best=Service.validatebestfigure(input("Enter best figure: "))
                    if category=='BATSMAN':
                        score=Service.validatebatsman(int(input('Enter the score: ')))
                    elif category=='BOWLER':
                        score=Service.validatebowler(int(input('Enter the score: ')),best)
                    else:
                        score=Service.validatescore(int(input('Enter the score: ')))
                    team=Service.validateteamname(input('Enter the team name: '))
                    if Service.validateduplicate(name,category,team):
                        playerId=Service.addplayer(Entity.Player(name,category,score,best,team))
                        print()
                        print("=================================\nPlayer added with player Id: ",playerId)
                except Exceptions.ServiceExceptions as e:
                    print(e.message)
                    continue
                print()
            elif choice==2:
                print("Display players!\n=======================")
                try:
                    playerinfo=Service.getplayersforteam(Service.validateteamname(input('Enter team name: ')))
                    print("Player Name   -   Category\n-----------------------------")
                    for player in playerinfo:
                        print(player[0]," - ",player[1])
                except Exceptions.ServiceExceptions as e:
                    print(e.message)

            elif choice==3:
                exit(0)
            else:
                print('Invalid choice Try again!!!!')
                continue
        except ValueError:
            print('Select from the correct displayed options ')
            continue