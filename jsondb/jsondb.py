from collections import MutableMapping

class JsonDB(MutableMapping):

    def __init__(self, data=None):
        if isinstance(data, MutableMapping):
            self.root = dict(data)
        else:
            self.root = {}

    def __getitem__(self, path):
        curr = self.root
        print "getitem_curr: %s" % self.root
        for node in path.split('/'):
            curr = curr[node]
        return curr

    def __setitem__(self, path, value):
        curr = self.root
        parts = path.split('/')
        for i, node in enumerate(parts):
            if i + 1 == len(parts):
                curr[node] = value
            if node not in curr:
                curr[node] = {}
            curr = curr[node]

    def __delitem__(self, path):
        del self.root[path]

    def __iter__(self):
        return self.root.__iter__()

    def __len__(self):
        return self.root.__len__()
    
    def __repr__(self):
        return repr(self.root)
