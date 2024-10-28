#!/usr/bin/env python3
"""
Hypermedia pagination module that provides simple pagination
functionality along with hypermedia pagination metadata.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        Initializes a new Server instance with an empty dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from a CSV file if not already cached.

        Returns:
            List[List]: Cached dataset of baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a paginated portion of the dataset based on page number
        and size.

        Args:
            page (int): The current page number (1-based).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A portion of the dataset corresponding to the page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Provides hypermedia pagination metadata along with paginated data.

        Args:
            page (int): The current page number (1-based).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary with metadata including:
                - page_size: Number of items in the current page.
                - page: The current page number.
                - data: The dataset for the current page.
                - next_page: The page number for the next page or None.
                - prev_page: The page number for the previous page or None.
                - total_pages: The total number of pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start and end indexes for a given page and page size.

    Args:
        page (int): The page number (1-based).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    return (page - 1) * page_size, page * page_size
