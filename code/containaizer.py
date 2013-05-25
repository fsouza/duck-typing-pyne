_managers = {}
_current = None


def register(backend):
    _managers[backend.name] = backend


def set(name):
    global _current
    try:
        _current = _managers[name]
    except KeyError:
        raise BackendNotRegisteredError(name)


def create(id, *args, **kwargs):
    return _current.create(id, *args, **kwargs)


def destroy(id, *args, **kwargs):
    return _current.destroy(id, *args, **kwargs)


class BackendNotRegisteredError(Exception):

    def __init__(self, name):
        msg = "Backend not found: %s" % name
        super(BackendNotRegisteredError, self).__init__(msg)
