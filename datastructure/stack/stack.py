class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        new_node = StackNode(obj, None)
        if self.top is None:
            self.top = new_node
        else:
            self.top.next = new_node
            self.top = new_node

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        if self.top is None:
            return None
        else:
            val = self.top.value
            cur = self
            if cur is None:
                return None
            else:
                popped = self.top
                self.top = self.top.next
                popped.next = None
                return popped.value

    def top(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.top

    def count(self):
        """Counts the number of elements in the stack."""

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""
