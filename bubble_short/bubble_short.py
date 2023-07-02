from typing import List


class BubbleShort:
    """This class will contain functions for bubble short using various algorithm. """
    def __init__(self, list_of_numbers: List[int] = None):
        self.list_of_numbers = list_of_numbers

    def short_brut_force_method(self, list_of_numbers: List[int] = None) -> List[int]:
        if self.list_of_numbers:
            list_of_numbers = self.list_of_numbers

        if len(list_of_numbers) == 0 or list_of_numbers is None:
            return []

        # first pointer in x index
        for i in range(len(list_of_numbers)):
            # second pointer, It will iterate through all the values in list when the first pointer is still point at x index
            for j in range(len(list_of_numbers)):
                if list_of_numbers[i] < list_of_numbers[j]:
                    # The values of the first pointer `i` is smaller than the value in the second pointer `j`.
                    # we will swap the values
                    list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
        return list_of_numbers


if __name__ == '__main__':
    b = BubbleShort()
    shorted_value_of_list = b.short_brut_force_method([5, 3, 2, 6, 1])
