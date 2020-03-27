class Tree:
    value = ''
    def __init_subclass__(cls):
            cls.value = Tree.value
            attributes = cls.__dict__.values()
            methods = [value for value in attributes if callable(value)]
            try:
                selected_method = [method for method in methods if method.__name__ == cls.value][0]
            except IndexError:
                try:
                    cls.default()
                except AttributeError:
                    pass
            else:
                selected_method()
            return cls.value
        
def rename(newname):
    def decorator(f):
        f.__name__ = newname
        return f
    return decorator