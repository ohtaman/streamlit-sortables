import pytest
from streamlit_sortables import sort_items

def test_sort_items_single_container():
    items = ['item1', 'item2', 'item3']
    sorted_items = sort_items(items)
    assert sorted_items == ['item1', 'item2', 'item3']  # Assuming sort_items returns items in the same order

def test_sort_items_multiple_containers():
    items = [
        {'header': 'container1', 'items': ['item3', 'item1', 'item2']},
        {'header': 'container2', 'items': ['item6', 'item5', 'item4']},
    ]
    sorted_items = sort_items(items, multi_containers=True)
    assert sorted_items[0]['items'] == ['item3', 'item1', 'item2']  # Check first container
    assert sorted_items[1]['items'] == ['item6', 'item5', 'item4']  # Check second container
