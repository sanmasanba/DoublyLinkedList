from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional, Any
T = TypeVar('T')

class Node:
    def __init__(self, val: Any = None) -> None:
        self.head = None
        self.val = val
        self.tail = None