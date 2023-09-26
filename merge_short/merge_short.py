from typing import List

class MergeShort:

    def __init__(self, list_of_number: List[int]):
        self.list_of_numbers = list_of_number

    def merge_short_recursive(self, list_of_number: List[int]):
        if len(list_of_number) == 1:
            return
        mid = len(list_of_number)//2

