class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        new_node = DoubleLinkedListNode(obj, None, None)
        if self.begin is None:
            self.begin = new_node
            self.end = self.begin
        elif self.end is None:
            self.end = new_node
            self.begin.next = self.end
            self.end.prev = self.begin
        else:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node

    def pop(self):
        """Removes the last item and returns it."""

    def shift(self, obj):
        """Actually just another name for push."""

    def unshift(self):
        """Removes the first item (from begin) and returns it."""

    @staticmethod
    def detach_node(node):
        """You'll need to
        inside remove().
        list, whether the
        node):
        use this operation sometimes, but mostly
        It should take a node, and detach it from the
        node is at the front, end, or in the middle."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
        return node

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        index = 0
        cur = self.begin

        if cur is None:  # no nodes; empty list
            return None
        elif cur.next is None:  # only one node, self.begin
            if cur.value == obj:
                self.begin = None  # use the `del` keyword?

                return index
            else:
                return None
        else:  # there are at least two nodes
            if cur.value == obj:
                self.begin = cur.next
                cur = None

                return index  # which is 0 since it's the first node
            else:
                before_cur = cur
                cur = cur.next

                while cur:
                    index += 1

                    if cur.value == obj:
                        # see if there's another node or if this is the end
                        if cur.next is None:
                            self.detach_node(cur)
                            before_cur = self.end

                            return index
                        else:
                            self.detach_node(cur)

                            return index
                    else:
                        if cur.next is None:
                            return None
                        else:
                            before_cur = cur
                            cur = cur.next

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end

    def count(self):
        """Counts the number of elements in the list."""
        temp = self.begin  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count

    def get(self, index):
        """Get the value at index."""
        count = 0
        cur = self.begin
        if cur is None:
            return None
        while cur:
            if count == index:
                return cur.value
            else:
                count += 1
                cur = cur.next

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        cur = self.begin
        to_print = ""

        while cur:
            if not (cur is self.end):
                to_print = to_print + str(cur.value) + ", "
            else:
                to_print = to_print + str(cur.value)

            cur = cur.next

        dump_string = f"{mark}:  {to_print}"
        print(dump_string, end=" ")
