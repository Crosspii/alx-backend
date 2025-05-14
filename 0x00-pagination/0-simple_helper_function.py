#!/usr/bin/env python3
"""
Module for a simple function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two that contains a start and end indexes
    for pagination

    Args:
    page = the current page number
    page_size = the number of items per page

    Returns:
    a tuple (start_index, end_index)
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
