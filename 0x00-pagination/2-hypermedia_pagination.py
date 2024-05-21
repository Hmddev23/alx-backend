#!/usr/bin/env python3
"""
define a Server class to paginate a dataset
of popular baby names.
"""

import csv
import math
from typing import List, Tuple


class Server:
    """
    Server class to paginate a dataset of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        initialize the Server instance.
        Attributes:
            __dataset (List[List]): The cached dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        load and cache the dataset from the CSV file.
        Returns:
            List[List]: The dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get a page from the dataset.
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            List[List]: A list of rows corresponding to the specified page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        calculate the start and end indices for items on a specific page.
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            Tuple[int, int]: A tuple containing the start and end index.
        """
        start_page = (page - 1) * page_size
        end_page = page * page_size
        return (start_page, end_page)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        get paginated data along with additional pagination details.
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            dict: A dictionary containing the data for the specified page.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
