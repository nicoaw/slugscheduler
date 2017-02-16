def object_decoder(obj, gbls):
    if isinstance(obj, dict):
        name = obj.pop('__name__', None)
        if name:
            cls = eval(name, gbls)
            result = cls.__new__(cls)
            result.__dict__ = obj
            return result
    return obj

def object_encoder(obj):
    ignore = {list, tuple, str, unicode, int, long, float, bool, type(None)}
    if type(obj) not in ignore:
        encoded = {'__name__': type(obj).__name__}
        encoded.update(obj.__dict__)
        return encoded
    return obj
