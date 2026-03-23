class StateManager:
    def __init__(self, obj):
        for k, v in obj.__class__.__dict__.items():
            if k.startswith("state"):
                setattr(self, k, v)

class MyClass:
    state_x = True
    state_y = False

obj = MyClass()
obj.states = StateManager(obj)
