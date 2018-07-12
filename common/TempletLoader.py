"""
    TempletLoader of reports.
    Create by: FlyingBlade
    Create Time: 2018/6/12 15:29
"""


class TempletLoader(object):
    def __init__(self, path, encoding='utf-8'):
        with open(path, 'r', encoding=encoding) as file:
            params = file.readline()
            params = [p.strip() for p in params.split(',')]
            self.__params = set(params)
            self.__context = file.read()

    def format_templet(self, params):
        # check input type
        assert (type(params) == dict)
        # check params
        tmp_params = params.copy()
        for param in self.__params:
            if param not in params:
                tmp_params[param] = ''
                # warnings.warn(RuntimeWarning("Warning: Param %s not in params"%param))
        return self.__context.format_map(tmp_params)

    def get_params(self):
        return self.__params


if __name__ == "__main__":
    import datetime

    t = TempletLoader('../templets/module0.txt')
    params = {
        'city': '广州',
        'time': datetime.datetime.now(),
        'modules': ['测试', '进出站分析', '用户分析'],
        'user': 'root',
        'version': 0.1
    }
    print(t.format_templet(params))
