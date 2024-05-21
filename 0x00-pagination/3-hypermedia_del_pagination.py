#!/usr/bin/env python3
"""
define a Server class to paginate a dataset of popular baby names
and includes methods to retrieve paginated data in various formats.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a dataset of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        initialize the Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        create and cache an indexed dataset.
        Returns:
            Dict[int, List]: The dataset indexed by row number.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        get a subset of the indexed dataset starting from a specific index.
        Args:
            index (int): The starting index for the subset (0-indexed).
            page_size (int): The number of items to include in the subset.
        Returns:
            Dict: A dictionary containing the data subset.
        """
        assert isinstance(index, int)
        assert 0 <= index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        n_index = index
        data = []
        for i in range(index, index + page_size):
            if i in self.__indexed_dataset:
                data.append(self.__indexed_dataset[i])
                n_index = i

        return {
            "index": index,
            "next_index": n_index + 1,
            "page_size": page_size,
            "data": data,
        }
