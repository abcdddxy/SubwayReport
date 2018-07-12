"""
    Create by: FlyingBlade
    Create Time: 2018/6/19 21:02
"""


class Module(object):
    def __init__(self):
        from common.TempletLoader import TempletLoader
        self.__templete = TempletLoader('templets/module1.txt')
        self.__params = {}

    def run(self, df):
        # STATUS ==5 的是交易成功的
        df_suc = df[df['ORDER_STATUS'] == 5]
        tmp = df_suc.groupby(['START_NAME', 'END_NAME']).SINGLE_TICKET_NUM.sum().reset_index()
        starts = tmp.groupby('START_NAME').SINGLE_TICKET_NUM.sum().sort_values(ascending=False)
        ends = tmp.groupby('END_NAME').SINGLE_TICKET_NUM.sum().sort_values(ascending=False)
        self.__params['start_top10'] = starts[:10].index.tolist()
        self.__params['end_top10'] = ends[:10].index.tolist()
        self.__params['start_top10_percent'] = starts[:10].sum() / starts.sum() * 100
        self.__params['end_top10_precent'] = ends[:10].sum() / ends.sum() * 100

    def maketext(self, global_params=None):
        # 允许传入全局变量， 但局部变量的优先级更高
        if global_params and type(global_params) == dict:
            for param in global_params:
                if param not in self.__params:
                    self.__params[param] = global_params[param]
        # 如果有缺失的变量， 填空字符串
        for param in self.__templete.get_params():
            if param not in self.__params:
                self.__params[param] = ''
        # 返回format结果
        return self.__templete.format_templet(self.__params)

    def makedata(self):
        return ''
