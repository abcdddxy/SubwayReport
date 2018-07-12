"""

    Create by: FlyingBlade
    Create Time: 2018/6/12 20:23
"""

class Module(object):
    def __init__(self):
        from common.TempletLoader import TempletLoader
        self.__templete = TempletLoader('templets/module0.txt')
        self.__params = {}
        for param in self.__templete.get_params():
            self.__params[param] = ''

    def run(self, df):

        pass

    def maketext(self):
        return self.__templete.format_templet(self.__params)

    def makedata(self):  # js? db? whatever.
        return ''
#
# Module()
