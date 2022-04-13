# Streamlit Sortables

A Streamlit component to provide sortable list.

## Instllation

```python

```


## Usage

```python
import streamlit as st
from streamlit_sortables import sort_items


original_items = ['A', 'B', 'C']
sorted_items = sort_items(original_items)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
```

```python

import streamlit as st
from streamlit_sortables import sort_items

original_items = {
    'first container': ['A', 'B', 'C'],
    'second container': ['D', 'E', 'F']
}

sorted_items = sort_items(original_items)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')
```