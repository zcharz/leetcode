class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.front = ListNode()
        self.back = ListNode()
        self.map = dict()
        self.capacity = capacity

        self.front.next = self.back
        self.back.prev = self.front

    def get(self, key: int) -> int:
        if key in self.map:
            self.updateFront(key)
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.updateFront(key)
            self.map[key].val = value
            return

        if len(self.map.keys()) == self.capacity:
            deletenode = self.back.prev

            self.back.prev = self.back.prev.prev
            self.back.prev.next = self.back
            
            del self.map[deletenode.key]


        newnode = ListNode(key,value)
        self.map[key] = newnode
        self.updateFront(key)
        

    def updateFront(self, key):
        currnode = self.map[key]

        if currnode.prev and currnode.next:
            currnode.prev.next = currnode.next
            currnode.next.prev = currnode.prev

        self.front.next.prev = currnode
        currnode.next = self.front.next

        currnode.prev = self.front
        self.front.next = currnode