from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional, Any
from . import Node
import sys
T = TypeVar('T')

class DoublyLinkedList:
    # init
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # append
    def append(self, x: Any) -> None:
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # ... <=> tail -> new
            self.tail.tail = new_node
            # ... <=> tail <=> new
            new_node.head = self.tail
            self.tail = new_node
        
        self.length += 1

    # appendleft
    def appendleft(self, x: Any):
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # new <- head <=> ele <=> ...
            self.head.head = new_node
            # new <=> head <=> ele <=> ...
            new_node.tail = self.head
            self.head = new_node

        self.length += 1


    # pop
    def pop(self) -> Optional[Any]:
        res = None
        if self.head is None:
            return res

        crr = self.tail
        res = crr.val
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # ... <=> tail  pre_tail
            self.tail = self.tail.head
            # ... <=> tail -> None
            self.tail.tail = None
            # None <- pre_tail
            crr.head = None
        
        self.length -= 1
        return res
    
    # popleft
    def popleft(self) -> Optional[Any]:
        if self.head is None:
            return None
        
        crr = self.head
        res = crr.val
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # 
            # e1(=crr.tail) <=> e2 <=> ...  
            self.head = crr.tail
        self.length -= 1
        return res

    # get
    def get(self, index: int) -> Node:
        if self.length < index:
            print(f"you are choiced index is {index}.")
            print(f"but you should select a index less than {self.length}.")
            sys.exit(1)
        
        if index < 0:
            print(f"you are choiced index is {index}.")
            print(f"but you should select a index greater than 0.")
            sys.exit(1)

        if self.is_front(index):
            res = 0
            crr = self.head
            while res != index:
                crr = crr.tail
                res += 1
            return crr
        else:
            res = self.length - 1
            crr = self.tail
            while res != index:
                crr = crr.head
                res -= 1
            return crr

    # insert
    def insert(self, index, x) -> None:
        if self.length < index:
            print(f"you are choiced index is {index}.")
            print(f"but you should select a index less than {self.length}.")
            sys.exit(1)
        
        if index < 0:
            print(f"you are choiced index is {index}.")
            print(f"but you should select a index greater than 0.")
            sys.exit(1)

        if index == 0:
            return self.appendleft(x)
        if index == self.length:
            return self.append(x)
        
        pre_node = self.get(index-1)
        new_node = Node(x)

        # pre_node  new_node  nxt_node
        nxt_node = pre_node.tail
        # pre_node -> new_node
        pre_node.tail = new_node
        # pre_node <=> new_node
        new_node.head = pre_node
        # new_node -> nxt_node
        new_node.tail = nxt_node
        # new_node <=> nxt_node
        nxt_node.head = new_node

        self.length += 1
    
    # discard
    def discard(self, x: Any):
        n = 0
        crr = self.head
        if crr.val == x:
            return self.popleft() is not None
        while crr:
            if crr.tail is None:
                return False
            if crr.tail.val == x:
                if crr.tail.tail == None:
                    return self.pop() is not None
                else:
                    crr.tail = crr.tail.tail
                    return True
            crr = crr.tail
        return False
    
    # remove
    def remove(self, index: int) -> Any:
        if self.length < index:
            print(f"you are choiced index is {index}.")
            print(f"but you should select a index less than {self.length}.")
            sys.exit(1)
        
        if index < 0:
            print(f"you are choiced index is {index}.")
            print(f"but you should select a index greater than 0.")
            sys.exit(1)
        
        if index == 0:
            return self.popleft()
        if index == self.length:
            return self.pop()
        # pre_node <=> target <=> nxt_node
        target_node = self.get(index)
        pre_node = target_node.head
        nxt_node = target_node.tail

        # pre_node -> nxt_node
        pre_node.tail = nxt_node
        # pre_node <=> nxt_node
        nxt_node.head = pre_node
        # pre -/- target -/-  nxt
        target_node.head = None
        target_node.tail = None

        self.length -= 1
        return target_node.val

    # index
    def index(self, x: int) -> int:
        n = 0
        crr = self.head
        while crr:
            if crr.val == x:
                return n
            n += 1
            crr = crr.tail
        return -1
    
    # extend
    def extend(self, x: T) -> T:
        ori_head = self.head
        ori_tail = self.tail
        new_head = x.head
        new_tail = x.tail

        ori_tail.tail = new_head
        new_head.head = ori_tail
        self.tail = new_tail.tail

        self.length += x.length

        return self

    # traversal
    def traversal(self) -> str:
        res = []
        crr = self.head
        while crr:
            res.append(crr.val)
            crr = crr.tail
        return str(res)
    
    def is_front(self, index: int) -> bool:
        return index <= self.length//2

    def __len__(self) -> int:
        return self.length
    
    def __str__(self) -> str:
        return self.traversal()