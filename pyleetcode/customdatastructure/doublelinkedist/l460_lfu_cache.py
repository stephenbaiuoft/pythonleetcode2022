from collections import OrderedDict


class Node:
    def __init__(self, key: int, value: int, cnt: int):
        self.key = key
        self.value = value
        self.cnt = cnt


class LFUCache:

    # cnt_dict with freq linked to OrderedDict()
    # dict for key, with node
    # node (value, cnt)
    # min_count keep track
    __slots__ = ["cnt_dict", "dict", "min_count", "capacity"]

    def __init__(self, capacity: int):
        self.cnt_dict = {}
        self.dict = {}
        self.min_count = 1
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1

        # if not found
        if key not in self.dict.keys():
            return -1
        # found case
        node = self.dict[key]

        # update cnt_dict, dict, min_count
        od = self.cnt_dict[node.cnt]
        # remove from od
        od.pop(node, None)
        if len(od) == 0:
            if self.min_count == node.cnt:
                self.min_count += 1
            # remove from cnt_dict
            self.cnt_dict.pop(node.cnt, None)

        # update node.cnt
        node.cnt += 1

        if node.cnt not in self.cnt_dict.keys():
            self.cnt_dict[node.cnt] = OrderedDict()
        # add to cnt_dict[node.cnt]
        self.cnt_dict[node.cnt][node] = None

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # update dict, cnt_dict, min_count, and the value
        if key in self.dict.keys():
            node = self.dict[key]
            node.value = value
            # this will update the cnt
            self.get(key)

        else:
            # insert mode
            # full, we need to evict one
            # update dict, cnt_dict, min_count
            if self.capacity == len(self.dict):
                # update cnt_dict && min_count
                od = self.cnt_dict[self.min_count]
                # remove the LRU node from od
                node: Node = od.popitem(False)[0]
                if len(od) == 0:
                    self.cnt_dict.pop(self.min_count, None)
                # update dict
                self.dict.pop(node.key)
                
            # now we can insert new one
            node = Node(key, value, 1)
            # update min_coutn
            self.min_count = 1
            self.dict[key] = node

            if 1 in self.cnt_dict.keys():
                od = self.cnt_dict[1]
                od[node] = None
            else:
                self.cnt_dict[1] = OrderedDict()
                self.cnt_dict[1][node] = None


lfu = LFUCache(2)
lfu.put(1, 1)
# cache=[1,_], cnt(1)=1
lfu.put(2, 2)
# cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1)
# return 1
# cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)
# 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
# cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2)
# return -1 (not found)
lfu.get(3)
# return 3
# cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)
# Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
# cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1)
# return -1 (not found)
lfu.get(3)
# return 3
# cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4)
# return 4
# cache=[4,3], cnt(4)=2, cnt(3)=3


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
