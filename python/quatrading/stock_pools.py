__author__ = 'wgf'
__date__ = ' 上午12:37'


class SelfPools:

    def __init__(self):

        self.routes = {}

    def route(self, route_str):

        def decorator(f):
            print('-----{}-----'.format(f.__name__))
            self.routes[route_str] = f

            return None

        return decorator

    def output(self, path):

        view_function = self.routes.get(path)

        if view_function:

            print("输出[{}]板块股票:".format(path))

            for str in view_function():
                print(str)

            return

        else:

            raise ValueError('Route "{}"" has not been registered'.format(path))


app = SelfPools()


@app.route(u"5G")
def Stock_pool():
    stock_name = [u"600776:东方通信", u"002792:通宇通信", u"002268:卫士通", u"300698:万马科技"]

    return stock_name


@app.route(u"量子通信")
def Stock_pool():
    stock_name = [u"600746:中国海防", u"002126:银轮股份", u"600522:中天科技", u"600468:百利电气"]

    return stock_name


def f():
    print('f1')


def f():
    print('f2')

if __name__ == "__main__":
    app.output('5G')
    app.output('量子通信')
    # f()
