import streamlit as st
from streamlit_sortables import sort_items

import streamlit as st

st.title('Sortables')

st.write('Sort items in a single container.')
items = ['item1', 'item2', 'item3']
sorted_items = sort_items(items)
st.write(sorted_items)


st.write('----')
st.write('Sort items in multiple containers.')
items = [
    {'header': 'container1', 'items': ['item1', 'item2', 'item3']},
    {'header': 'container2', 'items': ['item4', 'item5', 'item6']},
]
sorted_items = sort_items(items, multi_containers=True)
st.write(sorted_items)

st.write('----')
st.write('Lots of items in a single container.')
items = [
    {'header': 'header1', 'items': ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10', 'item11', 'item12', 'item13']},
]
sorted_items = sort_items(items, multi_containers=True)
st.write(sorted_items)

st.write('----')
st.write('Custom style.')
original_items = [
    {'header': 'first container',  'items': ['A', 'B', 'C']},
    {'header': 'second container', 'items': ['D', 'E', 'F']}
]

custom_style = """
.sortable-component {
    border: 3px solid #6495ED;
    border-radius: 10px;
    padding: 5px;
}
.sortable-container {
    background-color: #F0F0F0;
    counter-reset: item;
}
.sortable-container-header {
    background-color: #FFBFDF;
    padding-left: 1rem;
}
.sortable-container-body {
    background-color: #F0F0F0;
}
.sortable-item, .sortable-item:hover {
    background-color: #6495ED;
    font-color: #FFFFFF;
    font-weight: bold;
}
.sortable-item::before {
    content: counter(item) ". ";
    counter-increment: item;
}
"""
sorted_items = sort_items(original_items, multi_containers=True, custom_style=custom_style)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')