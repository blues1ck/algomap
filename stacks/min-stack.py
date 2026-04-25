class Element:

    def __init__(self, value, min_before, previous=None, next=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous
        self.min_before = min_before


class MinStack:

    def __init__(self):
        self.top_elem = None
        self.min = None

    def push(self, val: int) -> None:
        if self.top_elem is None:
            self.top_elem = Element(val, None)
            self.min = val
        else:
            prev = self.top_elem
            self.top_elem = Element(val, self.min, previous=prev)
            prev.next = self.top_elem
            self.min = min(self.min, val)

    def pop(self) -> None:
        if self.top_elem is None:
            return
        elif self.top_elem.previous is None:
            value = self.top_elem.value
            self.top_elem = None
            self.min = None
        else:
            value = self.top_elem.value
            self.min = self.top_elem.min_before
            self.top_elem = self.top_elem.previous
        return value 

    def top(self) -> int:
        value = self.top_elem.value
        return value

    def getMin(self) -> int:   
        return self.min