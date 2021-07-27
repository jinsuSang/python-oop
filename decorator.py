def choco(func):
    def new_func():
        print('choco ', end='')
        func()

    return new_func


@choco
def bread():
    print('bread')


@choco
def cookie():
    print('cookie')


@choco
def milk():
    print('milk')


bread()
cookie()
milk()
'''
choco bread
choco cookie
choco milk
'''
