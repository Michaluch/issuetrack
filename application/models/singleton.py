class Singleton(object):
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance
