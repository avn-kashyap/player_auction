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
                category = None
                best = None
                team = None
                score = None
                name = input("Enter the name: ")
                while True:
                    try:
                        category=Service.validatecategory(input('Enter the category: '))
                        break
                    except Exceptions.ServiceExceptions as e:
                        print(e.message)
                        continue
                while True:
                    try:
                        best=Service.validatebestfigure(input("Enter best figure: "))
                        break
                    except Exceptions.ServiceExceptions as e:
                        print(e.message)
                        continue
                while True:
                    try:
                        if category=='BATSMAN':
                            score=Service.validatebatsman(int(input('Enter the score: ')))
                            break
                        elif category=='BOWLER':
                            score=Service.validatebowler(int(input('Enter the score: ')),best)
                            break
                        else:
                            score=Service.validatescore(int(input('Enter the score: ')))
                            break
                    except Exceptions.ServiceExceptions as e:
                        print(e.message)
                        continue
                while True:
                    try:
                        team=Service.validateteamname(input('Enter the team name: '))
                        break
                    except Exceptions.ServiceExceptions as e:
                        print(e.message)
                        continue
                while True:
                    try:
                        if Service.validateduplicate(name,category,team):
                            playerId=Service.addplayer(Entity.Player(name,category,score,best,team))
                            print()
                            print("=================================\nPlayer added with player Id: ",playerId)
                            break
                    except Exceptions.ServiceExceptions as e:
                        print(e.message)
                        continue
                print()
            elif choice==2:
                print("Display players!\n=======================")
                while True:
                    try:
                        playerinfo=Service.getplayersforteam(Service.validateteamname(input('Enter team name: ')))
                        print(f'{"player name":<20} - {"category":<20}\n-----------------------------')
                        for player in playerinfo:
                            # print(player.getname()," - ",player.getcategory())
                            print(f'{player.getname():<20} - {player.getcategory():<20}')
                        break
                    except Exceptions.NoPlayersFoundException as e:
                        print(e.message)
                        break
                    except Exceptions.ServiceExceptions as e:
                        print(e.message)
                        continue

            elif choice==3:
                exit(0)
            else:
                print('Invalid choice Try again!!!!')
                continue
        except ValueError:
            print('Select from the displayed options ')
            continue