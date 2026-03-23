class metaWrapper():
    def __init__(self,token):
        self.token = token

        class mymeta(type):
            def __new__(cls,name,bases,dct):
                dx = super().__new__(cls,name,bases,dct)
                
                for kx in dct:
                    if kx.startswith(token):
                        print(kx,': ', dct[kx])
                    else:
                        pass
            
                return dx
        
        self.mclass = mymeta

mWrapper = metaWrapper('state')

class Class(metaclass=mWrapper.mclass):
    state_x = True
    state_y = False
    state_z = True

    x_state = False
    y_state = False
    z_state = False
