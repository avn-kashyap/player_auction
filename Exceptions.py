class Client(Exception):
    def __init__(self,message):
        self.message = message


class ServiceExceptions(Client):
    def __init__(self,message):
        self.message = message


class DaoExceptions(Client):
    def __init__(self,message):
        self.message = message


class InvalidCategoryExceptions(ServiceExceptions):
    def __init__(self,message):
        self.message = message


class InvalidTeamNameExceptions(ServiceExceptions):
    def __init__(self,message):
        self.message = message


class NotBatsmanException(ServiceExceptions):
    def __init__(self,message):
        self.message = message


class NotBowlerExceptions(ServiceExceptions):
    def __init__(self,message):
        self.message = message


class InvalidBestfigreException(ServiceExceptions):
    def __init__(self,message):
        self.message = message


class DuplicateEntryException(ServiceExceptions):
    def __init__(self,message):
        self.message = message


class NoPlayersFoundException(ServiceExceptions):
    def __init__(self,message):
        self.message = message
