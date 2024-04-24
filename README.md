# Streamlit Sortables

A Streamlit component to provide sortable list.
You can sort the list of strings on the UI as follows.

https://user-images.githubusercontent.com/329750/163662202-ce292fc4-2882-46ac-8c2c-ca4b9df675d2.mp4


## Installation

```python
$ pip install streamlit-sortables
```

## Usage

Call `sorted_items` method with a list of string. Return value is the sorted items.

```python
import streamlit as st
from streamlit_sortables import sort_items


original_items = ['A', 'B', 'C']
sorted_items = sort_items(original_items)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
```

You can pass list of dicts with `multi_containers=True`.

```python

import streamlit as st
from streamlit_sortables import sort_items

original_items = [
    {'header': 'first container',  'items': ['A', 'B', 'C']},
    {'header': 'second container', 'items': ['D', 'E', 'F']}
]

sorted_items = sort_items(original_items, multi_containers=True)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
```
