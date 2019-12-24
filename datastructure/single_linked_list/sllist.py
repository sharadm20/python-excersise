class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""

        if self.begin is None:
            self.begin = SingleLinkedListNode(obj, None)
            self.end = self.begin
        elif self.end is None:  # don't even need this branch!
            self.end = SingleLinkedListNode(obj, None)
            self.begin.next = self.end
        else:
            new_node = SingleLinkedListNode(obj, None)
            self.end.next = new_node
            self.end = new_node

    def pop(self):
        """Removes the last item and returns it."""
        first = self.begin
        if first is None:
            return None
        elif first.next is None:
            val = first.value
            first = None
            return val
        else:
            while first:
                if first.next.next is None:
                    val = first.next.value
                    first.next = None
                    self.end = first
                    return val
                else:
                    first = first.next

    def shift(self, obj):
        """Another name for push."""
        new_node = SingleLinkedListNode(obj, None)

        if self.begin is None:
            self.begin = new_node
            self.end = self.begin

        elif self.begin.next is None:
            self.end = self.begin
            self.begin = new_node
            self.begin.next = self.end

        else:
            new_node.next = self.begin
            self.begin = new_node

    def unshift(self):
        """Removes the first item and returns it."""

        cur = self.begin

        if cur is None:
            return None
        elif cur.next is None:
            rv = self.begin.value
            self.begin = None  # makes self.end None too?

            return rv
        else:
            rv = self.begin.value
            self.begin = cur.next

            return rv

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
                            before_cur.next = None
                            cur = None
                            before_cur = self.end

                            return index
                        else:
                            before_cur.next = cur.next
                            cur.next = None

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
