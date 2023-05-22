class Node:
    def _init_(self, data):
        self.data = data
        self.children = []

class Tree:
    def _init_(self, root):
        self.root = root

    def sums(self, node):
        total = node.data
        for child in node.children:
            total += self.sums(child)
        return total

    def sibling(self, node):
        if node == self.root:
            return 0

        parent = self._find_parent(node)
        total = 0
        for sibling in parent.children:
            total += sibling.data
        return total

    def _find_parent(self, node):
        # Helper function to find the parent of a node
        return self._find_parent_recursive(self.root, node)

    def _find_parent_recursive(self, current_node, node):
        if node in current_node.children:
            return current_node

        for child in current_node.children:
            parent = self._find_parent_recursive(child, node)
            if parent:
                return parent

        return None

# Membangun struktur tree yang diberikan pada gambar
# Menggunakan angka-angka yang sama seperti pada gambar
val200 = Node(200)
val9 = Node(9)
val2 = Node(2)
val7 = Node(7)
val3 = Node(3)
val10 = Node(10)
val7_2 = Node(7)
val5 = Node(5)
val8 = Node(8)
val33 = Node(33)
val4 = Node(4)
val2_2 = Node(2)

val200.children = [val9, val2, val7]
val9.children = [val3]
val2.children = [val10]
val7.children = [val7_2]
val3.children = [val5, val8]
val7_2.children = [val33]
val8.children = [val4]
val33.children = [val2_2]

t = Tree(val200)

# Testcase 1
print(f'Total value of node {val200.data} and all of its descendants = {t.sums(val200)}')

# Testcase 2
print(f'Total value of all siblings on node {val33.data} = {t.sibling(val33)}')