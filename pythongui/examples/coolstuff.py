class CoolStuff(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def funcname(self):
        pass


stuff = CoolStuff()

print (stuff.funcname())