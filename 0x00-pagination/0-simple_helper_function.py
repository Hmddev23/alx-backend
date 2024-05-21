#!/usr/bin/env python3
"""
define a function to calculate the start and end indices
for pagination based on the given page number and page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
