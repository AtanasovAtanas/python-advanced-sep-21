from unittest import TestCase, main
from numbers import Number

from custom_list import CustomList


class CustomListTests(TestCase):
    def setUp(self) -> None:
        self.cl = CustomList()

    def test_append_should_add_element_to_empty_list(self):
        result = self.cl.append(1)

        self.assertEqual(1, result[0])
        self.assertEqual(1, self.cl.size())
        self.assertEqual(1, self.cl.get(0))

    def test_append_should_add_element_to_the_end(self):
        self.cl.append(1)
        result = self.cl.append(2)

        self.assertEqual(2, self.cl.size())
        self.assertEqual([1, 2], result)
        self.assertEqual(2, self.cl.get(1))

    def test_remove_with_non_integer_raises(self):
        with self.assertRaises(ValueError) as context:
            self.cl.remove('str')
        self.assertEqual('str is not an integer.', str(context.exception))

    def test_remove_with_invalid_raises(self):
        indices = [-1, 100, -5]

        for idx in indices:
            with self.assertRaises(IndexError) as context:
                self.cl.remove(idx)
            self.assertEqual(f'{idx} is invalid index.', str(context.exception))

    def test_remove_with_valid_index_should_remove_the_element(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.cl.append(element)

        self.assertEqual(elements[0], self.cl.remove(0))
        self.assertEqual(elements[-1], self.cl.remove(self.cl.size() - 1))
        self.assertEqual([2, 3, 4], self.cl._CustomList__elements)

    def test_get_with_invalid_idx_raises(self):
        indices = ['str', 1.5, [], {}, (1, 2, 3), -1, 100]

        for idx in indices:
            with self.assertRaises(Exception):
                self.cl.get(idx)

    def test_get_should_return_element_on_specified_idx(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)

        self.assertEqual(1, self.cl.get(0))
        self.assertEqual(2, self.cl.get(1))
        self.assertEqual(3, self.cl.get(2))

    def test_extend_should_add_iterable_to_initial_list(self):
        initial_values = [1, 2, 3]
        for element in initial_values:
            self.cl.append(element)

        iterables = [[4, 5], (4, 5), {4, 5}, '45']
        for iterable in iterables:
            actual_result = self.cl.extend(iterable)
            expected_result = list(initial_values)
            [expected_result.append(x) for x in iterable]

            self.assertEqual(expected_result, actual_result)
            self.assertNotEqual(id(actual_result), id(self.cl._CustomList__elements))

    def test_extend_should_add_non_iterable_to_initial_list(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)

        values = [4, True, 2.5]
        for value in values:
            result = self.cl.extend(value)
            self.assertEqual([1, 2, 3, value], result)
            self.assertNotEqual(id(result), id(self.cl._CustomList__elements))

    def test_insert_with_invalid_idx_raises(self):
        indices = [-1, -5, 100, 200]

        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)

        for idx in indices:
            with self.assertRaises(IndexError):
                self.cl.insert(idx, 5)

    def test_insert_should_add_element_to_zero_idx(self):
        initial_elements = [0, 1, 2]
        for num in initial_elements:
            self.cl.append(num)

        new_element = 500
        result = self.cl.insert(0, new_element)

        self.assertEqual(id(result), id(self.cl._CustomList__elements))
        self.assertEqual(result[0], new_element)
        self.assertEqual([new_element] + initial_elements, result)

    def test_insert_should_add_element_to_the_end(self):
        initial_elements = [0, 1, 2]
        for num in initial_elements:
            self.cl.append(num)

        new_element = 500
        result = self.cl.insert(self.cl.size(), new_element)

        self.assertEqual(id(result), id(self.cl._CustomList__elements))
        self.assertEqual(result[-1], new_element)
        self.assertEqual(initial_elements + [new_element], result)

    def test_pop_with_empty_list_raise(self):
        with self.assertRaises(IndexError):
            self.cl.pop()

    def test_pop_removes_and_returns_last_element(self):
        elements = [1, 2, 3]

        for element in elements:
            self.cl.append(element)

        actual = self.cl.pop()
        expected = elements.pop()

        self.assertEqual(expected, actual)
        self.assertEqual(elements, self.cl._CustomList__elements)

    def test_clear_should_remove_all_elements(self):
        self.cl.append(1)
        self.cl.append(2)
        self.cl.append(3)

        self.cl.clear()

        self.assertEqual([], self.cl._CustomList__elements)

    def test_first_idx_returns_first_idx_of_element(self):
        elements = [2, 3, 1, 1, 4, 1]
        value = 1
        expected = -1
        for idx, element in enumerate(elements):
            if element == value and expected == -1:
                expected = idx
            self.cl.append(element)

        actual = self.cl.first_idx(value)

        self.assertEqual(expected, actual)

    def test_first_idx_returns_default_value_when_element_is_not_present(self):
        actual = self.cl.first_idx(4)
        self.assertEqual(-1, actual)

    def test_last_idx_returns_first_idx_of_element(self):
        elements = [2, 3, 1, 1, 4, 1]
        value = 1
        expected = -1
        for idx, element in enumerate(elements):
            if element == value:
                expected = idx
            self.cl.append(element)

        actual = self.cl.last_idx(value)

        self.assertEqual(expected, actual)

    def test_last_idx_returns_default_value_when_element_is_not_present(self):
        actual = self.cl.last_idx(4)
        self.assertEqual(-1, actual)

    def test_count_returns_zero_when_list_is_empty(self):
        result = self.cl.count(4)
        self.assertEqual(0, result)

    def test_count_returns_zero_when_element_is_not_present(self):
        n = 4
        for num in range(n):
            self.cl.append(num)

        result = self.cl.count(n)
        self.assertEqual(0, result)

    def test_count_returns_how_many_times_element_appears(self):
        n = 4
        number = 100
        for _ in range(n):
            self.cl.append(number)

        result = self.cl.count(number)
        self.assertEqual(n, result)

    def test_size_returns_count_of_elements_in_the_list(self):
        self.assertEqual(0, self.cl.size())

        n = 4
        for _ in range(n):
            self.cl.append(100)

        self.assertEqual(n, self.cl.size())

    def test_reverse_should_return_new_list_with_elements_in_reversed_order(self):
        elements = [1, 2, 3, 4]
        for element in elements:
            self.cl.append(element)

        expected = list(reversed(elements))
        actual = self.cl.reverse()

        self.assertEqual(expected, actual)
        self.assertNotEqual(id(actual), id(self.cl._CustomList__elements))

    def test_copy_should_create_custom_list_copy(self):
        elements = [1, 2, 3, 4]
        for element in elements:
            self.cl.append(element)

        actual = self.cl.copy()
        self.assertEqual(elements, actual)
        self.assertNotEqual(id(actual), id(self.cl._CustomList__elements))

    def test_add_first_should_insert_element_at_idx_zero(self):
        elements = [1, 2, 3, 4]
        for element in elements:
            self.cl.append(element)

        insert_element = 0
        result = self.cl.add_first(insert_element)

        self.assertEqual(None, result)
        self.assertEqual(insert_element, self.cl.get(0))

    def test_dictionize_with_odd_elements(self):
        elements = [1, 2, 3]
        for element in elements:
            self.cl.append(element)

        result = self.cl.dictionize()
        self.assertEqual({1: 2, 3: ' '}, result)

    def test_dictionize_with_even_elements(self):
        elements = [1, 2, 3, 4]
        for element in elements:
            self.cl.append(element)

        result = self.cl.dictionize()
        self.assertEqual({1: 2, 3: 4}, result)

    def test_move_should_move_first_n_elements(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.cl.append(element)

        n = 2
        actual = self.cl.move(n)
        expected = elements[n:] + elements[0:n]

        self.assertEqual(expected, actual)
        self.assertEqual(id(actual), id(self.cl._CustomList__elements))

    def test_move_should_remain_original_order_when_n_is_greater_than_size_of_the_list(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.cl.append(element)

        n = len(elements) + 1
        actual = self.cl.move(n)

        self.assertEqual(elements, actual)
        self.assertEqual(id(actual), id(self.cl._CustomList__elements))

    def test_sum_should_sum_all_elements_in_list(self):
        elements = [1, 2, 3, '123', [1]]
        for element in elements:
            self.cl.append(element)

        actual = self.cl.sum()
        expected = sum([x if isinstance(x, Number) else len(x) for x in elements])

        self.assertEqual(expected, actual)

    def test_overbound_returns_biggest_number_when_is_number(self):
        elements = [2, 100, 3, '123', [1]]
        for element in elements:
            self.cl.append(element)

        actual = self.cl.overbound()

        self.assertEqual(1, actual)

    def test_overbound_returns_biggest_number_when_is_not_number(self):
        elements = [2, 1, '123123123', 3, '123', [1]]
        for element in elements:
            self.cl.append(element)

        actual = self.cl.overbound()

        self.assertEqual(2, actual)

    def test_underbound_returns_smallest_number_when_is_number(self):
        elements = [2, 100, 3, '123', [1], 0]
        for element in elements:
            self.cl.append(element)

        actual = self.cl.underbound()

        self.assertEqual(len(elements) - 1, actual)

    def test_underbound_returns_smallest_number_when_is_not_number(self):
        elements = [2, 4, '123123123', 3, [1], '123', [1]]
        for element in elements:
            self.cl.append(element)

        actual = self.cl.underbound()

        self.assertEqual(4, actual)

    def test_list_iterator(self):
        elements = [1, 2, 3, 4]
        for element in elements:
            self.cl.append(element)

        for idx, element in enumerate(self.cl):
            self.assertEqual(elements[idx], element)


if __name__ == '__main__':
    main()
