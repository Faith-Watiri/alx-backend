#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server with dataset and indexed dataset."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Any]:
        """
        Deletion-resilient hypermedia pagination.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items to return in the page.

        Returns:
            Dict[str, Any]: A dictionary containing index metadata and data.
        """
        assert 0 <= index < len(self.indexed_dataset()), "Index out of range."

        data = []
        current_idx = index
        indexed_data = self.indexed_dataset()

        # Collect page_size items starting from the specified index,
        # handling any missing items due to deletions
        while len(data) < page_size and current_idx < len(indexed_data):
            item = indexed_data.get(current_idx)
            if item:
                data.append(item)
            current_idx += 1

        next_index = current_idx if current_idx < len(indexed_data) else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
