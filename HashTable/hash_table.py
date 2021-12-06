class HashTable:
    def __init__(self):
        self.__capacity = 4
        self.__items = [None] * self.__capacity
        self.__free_slots = self.__capacity

    def add(self, key, value):
        idx = self.__get_idx(key)

        if self.__items[idx] is None:
            self.__items[idx] = []
            self.__free_slots -= 1
        else:
            try:
                self.pop(key)
            except KeyError:
                pass

        self.__items[idx].append((key, value))

        if self.__free_slots == 0:
            self.__grow()

    def pop(self, key):
        idx = self.__get_idx(key)

        if self.__items[idx] is None:
            raise KeyError(f'{key} is not present in the hash table.')

        for k, v in self.__items[idx]:
            if key == k:
                self.__items[idx].remove((k, v))
                return v

        raise KeyError(f'{key} is not present in the hash table.')

    def contains_key(self, key):
        idx = self.__get_idx(key)

        if self.__items[idx] is None:
            return False

        for k, v in self.__items[idx]:
            if key == k:
                return True
        return False

    def keys(self):
        keys = []
        for slot in self.__items:
            if slot is None:
                continue

            for key, _ in slot:
                keys.append(key)
        return keys

    def values(self):
        values = []
        for slot in self.__items:
            if slot is None:
                continue

            for _, value in slot:
                values.append(value)
        return values

    def items(self):
        items = []

        for slot in self.__items:
            if slot is None:
                continue

            for item in slot:
                items.append(item)
        return items

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        idx = self.__get_idx(key)

        if self.__items[idx] is None:
            raise KeyError(f'{key} is not a valid key in the hash table.')

        for k, v in self.__items[idx]:
            if k == key:
                return v

        raise KeyError(f'{key} is not a valid key in the hash table.')

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __len__(self):
        count = 0
        for slot in self.__items:
            if slot is None:
                continue
            for _ in slot:
                count += 1

        return count

    def __str__(self):
        return '{' + ', '.join([f'{repr(key)}: {value}' for key, value in self.items()]) + '}'

    def __get_idx(self, key):
        return hash(key) % len(self.__items)

    def __grow(self):
        existing_pairs = self.items()

        self.__capacity *= 2
        self.__free_slots = self.__capacity
        self.__items = [None] * self.__capacity

        for key, value in existing_pairs:
            self.add(key, value)
