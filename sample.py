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
st.write('Sort items in multiple containers with vertical direction.')
items = [
    {'header': 'container1', 'items': ['item1', 'item2', 'item3']},
    {'header': 'container2', 'items': ['item4', 'item5', 'item6']},
]
sorted_items = sort_items(items, multi_containers=True, direction="vertical")
st.write(sorted_items)
