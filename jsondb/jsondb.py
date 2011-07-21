class JsonDB(dict):

    def from_path(self, path):
        curr = self
        for leaf in path.split('/'):
            curr = curr[leaf]

        return curr

