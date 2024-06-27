class BSTNode:
    def __init__(self, data, priority):
        self.data = data  # 节点的数据部分
        self.priority = priority  # 节点的优先级部分
        self.left = None  # 左子节点，初始化为None
        self.right = None  # 右子节点，初始化为None

class BSTPriorityQueue:
    def __init__(self):
        self.root = None  # 树的根节点，初始化为None

    def insert(self, data, priority):
        if not self.root:  # 如果根节点为None，即树为空
            self.root = BSTNode(data, priority)  # 创建一个新的节点作为根节点
        else:
            self._insert(self.root, data, priority)  # 否则，递归地插入到树中

    def _insert(self, node, data, priority):
        if priority > node.priority:  # 如果新数据的优先级大于当前节点的优先级
            if node.left:   # 如果当前节点有左子节点
                self._insert(node.left, data, priority)   # 递归地插入到左子树中
            else:
                node.left = BSTNode(data, priority)  # 否则，将新数据插入为当前节点的左子节点
        else:  # 如果新数据的优先级小于或等于当前节点的优先级
            if node.right:  # 如果当前节点有右子节点 
                self._insert(node.right, data, priority)  # 递归地插入到右子树中
            else:
                node.right = BSTNode(data, priority)   # 否则，将新数据插入为当前节点的右子节点

    def extract_max(self):
        if not self.root:  # 如果树为空
            return None   # 返回None 
        parent, max_node = self._extract_max(self.root, None)   # 递归地查找最大优先级的节点和其父节点
        if parent:   # 如果存在父节点
            parent.left = max_node.right  # 将父节点的左子节点设置为最大节点的右子节点
        else:  # 如果不存在父节点（即最大节点是根节点）
            self.root = max_node.right  # 将根节点设置为最大节点的右子节点
        return max_node.data  # 返回最大节点的数据

    def _extract_max(self, node, parent):
        if node.left:  # 如果节点有左子节点 
            return self._extract_max(node.left, node)   # 递归地在左子树中查找
        return parent, node  # 返回父节点和当前节点（当前节点是左子树中的最大节点）


    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        left_result = self._search(node.left, data)
        if left_result:
            return left_result
        return self._search(node.right, data)

    def change_priority(self, data, new_priority):
        node = self.search(data)
        if node:
            self._delete(self.root, None, data)
            self.insert(data, new_priority)

    def _delete(self, node, parent, data):
        if node is None:
            return
        if data < node.data:
            self._delete(node.left, node, data)
        elif data > node.data:
            self._delete(node.right, node, data)
        else:
            if node.left is None and node.right is None:
                if parent is None:
                    self.root = None
                elif parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            elif node.left and node.right:
                successor = self._get_min(node.right)
                node.data, node.priority = successor.data, successor.priority
                self._delete(node.right, node, successor.data)
            else:
                child = node.left if node.left else node.right
                if parent is None:
                    self.root = child
                elif parent.left == node:
                    parent.left = child
                else:
                    parent.right = child

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node


    def __repr__(self):
        result = []  # 创建一个空列表用于存储节点的信息
        self._inorder(self.root, result)  # 使用中序遍历将节点的信息添加到列表中
        return str(result)  # 返回节点的信息列表的字符串表示形式

    def _inorder(self, node, result):
        if node:  # 如果节点不为None
            self._inorder(node.left, result)  # 先遍历左子树
            result.append((node.data, node.priority))  # 将当前节点的信息添加到结果列表中
            self._inorder(node.right, result)  # 然后遍历右子树

