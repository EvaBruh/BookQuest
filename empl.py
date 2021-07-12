class Employee:
    def __init__(self, name, id, otdel, dolj):
        self.__name = name
        self.__id = id
        self.__otdel = otdel
        self.__dolj = dolj

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_otdel(self, otdel):
        self.__otdel = otdel

    def set_dolj(self, dolj):
        self.__dolj = dolj

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_otdel(self):
        return self.__otdel

    def get_dolj(self):
        return self.__dolj
