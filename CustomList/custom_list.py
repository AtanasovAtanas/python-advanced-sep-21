from numbers import Number


class CustomList:
    def __init__(self):
        self.__elements = []
        self.__next_idx = 0

    def append(self, value):
        self.__elements.append(value)
        return self.__elements

    def remove(self, idx):
        if not isinstance(idx, int):
            raise ValueError(f'{idx} is not an integer.')
        if self.__is_invalid_idx(idx):
            raise IndexError(f'{idx} is invalid index.')

        return self.__elements.pop(idx)

    def get(self, idx):
        if not isinstance(idx, int):
            raise ValueError(f'{idx} is not an integer.')
        if self.__is_invalid_idx(idx):
            raise IndexError(f'{idx} is invalid index.')

        return self.__elements[idx]

    def extend(self, iterable):
        new_list = self.copy()
        try:
            iter(iterable)

            for el in iterable:
                new_list.append(el)
        except TypeError:
            new_list.append(iterable)
        return new_list

    def insert(self, idx, value):
        if idx < 0 or idx > len(self.__elements):
            raise IndexError('Invalid index!')
        self.__elements.insert(idx, value)
        return self.__elements

    def pop(self):
        if len(self.__elements) == 0:
            raise IndexError('Custom list is empty.')

        return self.__elements.pop()

    def clear(self):
        self.__elements = []

    def first_idx(self, value):
        for idx in range(len(self.__elements)):
            if self.__elements[idx] == value:
                return idx
        return -1

    def last_idx(self, value):
        for idx in range(len(self.__elements) - 1, -1, -1):
            if self.__elements[idx] == value:
                return idx
        return -1

    def count(self, value):
        result = 0
        for element in self.__elements:
            if element == value:
                result += 1
        return result

    def reverse(self):
        return self.__elements[::-1]

    def copy(self):
        result = []
        for element in self.__elements:
            result.append(element)
        return result

    def size(self):
        return len(self.__elements)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        result = {}
        last_inserted_key = None
        for idx in range(len(self.__elements)):
            element = self.__elements[idx]
            if idx % 2 == 0:
                result[element] = ' '
                last_inserted_key = element
            else:
                result[last_inserted_key] = element

        return result

    def move(self, amount):
        self.__elements = self.__elements[amount:] + self.__elements[0:amount]
        return self.__elements

    def sum(self):
        result = 0
        for element in self.__elements:
            if isinstance(element, int):
                result += element
            else:
                result += len(element)
        return result

    def overbound(self):
        if len(self.__elements) == 0:
            raise IndexError('Custom list is empty.')

        biggest_value = float('-inf')
        biggest_idx = -1

        for idx in range(len(self.__elements)):
            element = self.get(idx)
            if isinstance(element, Number):
                if element > biggest_value:
                    biggest_value = element
                    biggest_idx = idx
            else:
                if len(element) > biggest_value:
                    biggest_value = len(element)
                    biggest_idx = idx
        return biggest_idx

    def underbound(self):
        if len(self.__elements) == 0:
            raise IndexError('Custom list is empty.')

        smallest_value = float('inf')
        smallest_idx = -1

        for idx in range(len(self.__elements)):
            element = self.get(idx)
            if isinstance(element, Number):
                if element < smallest_value:
                    smallest_value = element
                    smallest_idx = idx
            else:
                if len(element) < smallest_value:
                    smallest_value = len(element)
                    smallest_idx = idx
        return smallest_idx

    def __iter__(self):
        return self

    def __next__(self):
        if self.__next_idx >= self.size():
            raise StopIteration

        result = self.__elements[self.__next_idx]
        self.__next_idx += 1
        return result

    def __is_invalid_idx(self, idx):
        return idx < 0 or idx >= len(self.__elements)
