"""
dictionary -> {key : (val, parent key, next key)}
{
    1: (1, None, None),
}
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.cur_size = 0

        self.head = None
        self.tail = None

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        value, prev_key, next_key = self.cache[key]

        # already most recently used
        if key == self.tail:
            return value

        # detach node from current position

        # update previous node
        if prev_key is not None:
            prev_node = self.cache[prev_key]

            self.cache[prev_key] = (
                prev_node[0],
                prev_node[1],
                next_key
            )
        else:
            # node was head
            self.head = next_key

        # update next node
        if next_key is not None:
            next_node = self.cache[next_key]

            self.cache[next_key] = (
                next_node[0],
                prev_key,
                next_node[2]
            )

        # attach node to tail

        tail_node = self.cache[self.tail]

        self.cache[self.tail] = (
            tail_node[0],
            tail_node[1],
            key
        )

        self.cache[key] = (
            value,
            self.tail,
            None
        )

        self.tail = key

        return value

    def put(self, key: int, value: int) -> None:

        # existing key
        if key in self.cache:

            # remove old node position
            old_value, prev_key, next_key = self.cache[key]

            # already tail
            if key != self.tail:

                # update previous node
                if prev_key is not None:
                    prev_node = self.cache[prev_key]

                    self.cache[prev_key] = (
                        prev_node[0],
                        prev_node[1],
                        next_key
                    )
                else:
                    self.head = next_key

                # update next node
                if next_key is not None:
                    next_node = self.cache[next_key]

                    self.cache[next_key] = (
                        next_node[0],
                        prev_key,
                        next_node[2]
                    )

                # move to tail
                tail_node = self.cache[self.tail]

                self.cache[self.tail] = (
                    tail_node[0],
                    tail_node[1],
                    key
                )

                self.cache[key] = (
                    value,
                    self.tail,
                    None
                )

                self.tail = key

            else:
                # just update value
                self.cache[key] = (
                    value,
                    prev_key,
                    next_key
                )

            return

        # capacity full -> evict LRU
        if self.cur_size == self.capacity:

            lru_key = self.head

            lru_node = self.cache[lru_key]

            next_key = lru_node[2]

            # only one node
            if next_key is None:

                self.cache.pop(lru_key)

                self.head = None
                self.tail = None

            else:

                next_node = self.cache[next_key]

                self.cache[next_key] = (
                    next_node[0],
                    None,
                    next_node[2]
                )

                self.cache.pop(lru_key)

                self.head = next_key

            self.cur_size -= 1

        # insert new node

        # empty list
        if self.cur_size == 0:

            self.cache[key] = (
                value,
                None,
                None
            )

            self.head = key
            self.tail = key

        else:

            tail_node = self.cache[self.tail]

            self.cache[self.tail] = (
                tail_node[0],
                tail_node[1],
                key
            )

            self.cache[key] = (
                value,
                self.tail,
                None
            )

            self.tail = key

        self.cur_size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)