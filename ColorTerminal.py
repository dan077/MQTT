class Color():
    #HEADER = '\033[95m'
    #OKBLUE = '\033[94m'
    GREEN = '\033[92m'
    #WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


    @classmethod
    def Error(cls,str):
        print("{0} {1} {2}".format(cls.RED,str.capitalize(),cls.END));

    @classmethod
    def ErrorReturn(cls,str):
        return "{0} {1} {2}".format(cls.RED, str.capitalize(), cls.END);

    @classmethod
    def Succesfull(cls,str):
        print("{0} {1} {2}".format(cls.GREEN,str.capitalize(),cls.END))

    @classmethod
    def SuccesfullReturn(cls, str):
        return "{0} {1} {2}".format(cls.GREEN, str.capitalize(), cls.END);
