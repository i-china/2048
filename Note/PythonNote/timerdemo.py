from threading import Timer

def hi():
    print('hi baby ')

t = Timer(3,hi())
t.start()
