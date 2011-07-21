from collections import MutableMapping

class JsonDB(dict):

    def __init__(self, data=None):
        if isinstance(data, MutableMapping):
            self.update(dict(data))

    def __getitem__(self, path):
        curr = self
        for node in path.split('/'):
            curr = dict.__getitem__(curr, node)
        return curr

    def __setitem__(self, path, value):
        curr = self
        parts = path.split('/')
        for i, node in enumerate(parts):
            if i + 1 == len(parts):
                dict.__setitem__(curr, node, value)
            if node not in curr:
                dict.__setitem__(curr, node, {})
            curr = dict.__getitem__(curr, node)

    def __delitem__(self, path):
        pass
