# Streamlit Sortables

A Streamlit component to provide sortable list.
You can sort the list of strings on the UI as follows.

![](https://raw.githubusercontent.com/ohtaman/streamlit-sortables/main/imgs/single_container.png)

It also supports moving items between multiple containers.

![](https://raw.githubusercontent.com/ohtaman/streamlit-sortables/main/imgs/multiple_containers.png)

## Instllation

```python
$ pip install streamlit-sortables
```

## Usage

Call `soretd_items` method with a list of string. Return value is the sorted items.

```python
import streamlit as st
from streamlit_sortables import sort_items


original_items = ['A', 'B', 'C']
sorted_items = sort_items(original_items)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
```

You can pass list of dicts with `multiple_containers=True`.

```python

import streamlit as st
from streamlit_sortables import sort_items

original_items = [
    {'header': 'first container',  'items': ['A', 'B', 'C']},
    {'header': 'second container', 'items': ['D', 'E', 'F']}
]

sorted_items = sort_items(original_items, multiple_contaieners=True)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
```
