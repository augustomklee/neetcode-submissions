class MapNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        cur = self.root

        if not self.root:
            self.root = MapNode(key, val)
            return
        while True:
            if key > cur.key:
                if not cur.right:
                    cur.right = MapNode(key, val)
                    return
                cur = cur.right
            elif key < cur.key:
                if not cur.left:
                    cur.left = MapNode(key, val)
                    return
                cur = cur.left
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur != None:
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.findMinNode(self.root)
        return cur.val if cur else -1

    def findMinNode(self, node: MapNode) -> MapNode:
            while node and node.left:
                node = node.left
            return node

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
     
    def removeHelper(self, cur: MapNode, key:int) -> MapNode:
        if not cur:
            return None

        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            else:
                minNode = self.findMinNode(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        return cur

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res
    
    def inorderTraversal(self, root: MapNode, res: List[int]) -> None:
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.key)
            self.inorderTraversal(root.right, res)

