import collections.abc

class MyMapping(collections.abc,Mapping):
    def function(self):
        pass

    def get(self,key,default = None):
        return super().get(key,default)
    


