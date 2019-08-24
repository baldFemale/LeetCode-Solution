class FileSystem(object):

    def __init__(self):
        self.dic = {}

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        path = path.split("/")
        path = [p for p in path if p != ""]
        if len(path) == 0:
            return False
        cur = self.dic
        for i, p in enumerate(path):
            print(i, p)
            if i == len(path) - 1:
                cur[p] = {"zhou_value": value}
                return True
            else:
                if p not in cur:
                    return False
                cur = cur[p]
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        path = path.split("/")
        path = [p for p in path if p != ""]
        if len(path) == 0:
            return -1
        cur = self.dic
        for i, p in enumerate(path):
            if i == len(path) - 1 and p in cur:
                return cur[p]["zhou_value"]
            else:
                if p not in cur:
                    return -1
                else:
                    cur = cur[p]
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)
