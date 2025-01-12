import os
from typing import Any, Dict, List, Optional, TypeVar, Union

import streamlit.components.v1 as components

T = TypeVar("T", str, Dict[str,Any])
# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "sort_items",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("sortable_items", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def sort_items(items: list[T],  header: Optional[str]=None, multi_containers: bool=False, direction: str="horizontal", custom_style: Optional[str]=None, key: Any=None) -> list[T]:
    """Create a new instance of "sortable_items".

    Parameters
    ----------
    items : list[str] or dict[str, list[str]]
    header: str or None
    multi_containers: bool
    direction: str
    custom_style: str or None
        Custom CSS styles to apply to the component. Defaults to None.
        The following selectors can be used:
        - '.sortable-component' for the main container
        - '.sortable-component.vertical' if direction is 'vertical'
        - '.sortable-container' for each container if multi_containers is True
        - '.sortable-container-header' for the header
        - '.sortable-container-boy' for the body
        - '.sortable-item' for each item
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    list[T]
        Sorted version of items. Preserves types of input items.
    """
    if not multi_containers:
        if not isinstance(header, str) and header is not None:
            raise ValueError('header argument must be str or None if multi_containers is False.')
        if not all(map(lambda item: isinstance(item, str), items)):
            raise ValueError('items must be list[str] if multi_containers is False.')

        items = [{'header': header, 'items': items}]
    else:
        if not all(map(lambda item: isinstance(item, dict), items)):
            raise ValueError('items must be list[dict[str, Any]] if multi_containers is True.')

    component_value = _component_func(items=items, direction=direction, customStyle=custom_style, default=items, key=key)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    if multi_containers:
        return component_value
    else:
        return component_value[0]['items']


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
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

    st.write('----')
    st.write('Sort items in many containers with vertical direction.')
    items = [
        {'header': 'container1', 'items': ['item1', 'item2', 'item3']},
        {'header': 'container2', 'items': ['item4', 'item5', 'item6']},
        {'header': 'container3', 'items': ['item7', 'item8', 'item9']},
        {'header': 'container4', 'items': ['item10', 'item11', 'item12']},
        {'header': 'container5', 'items': ['item13', 'item14', 'item15']},
        {'header': 'container6', 'items': ['item16', 'item17', 'item18']},
    ]
    
    sorted_items = sort_items(items, multi_containers=True, direction="vertical")
    st.write(sorted_items)

    st.write('----')
    st.write('Sort items with custom style.')
    items = [
        {'header': 'container1', 'items': ['item1', 'item2', 'item3']},
        {'header': 'container2', 'items': ['item4', 'item5', 'item6']},
        {'header': 'container3', 'items': ['item7', 'item8', 'item9']},
    ]
    custom_style = """
    .sortable-component {
        border: 3px solid #6495ED;
        border-radius: 10px;
        padding: 5px;
    }
    .sortable-container {
        background-color: #F0F0F0;
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
    """
    sorted_items = sort_items(items, multi_containers=True, custom_style=custom_style)
    
    st.write(sorted_items)

    st.write('----')
    st.write('Advanced custom style.')
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
    .sortable-item.dragging::before {
        content: none;
        counter-increment: none;
    }
    """
    sorted_items = sort_items(original_items, multi_containers=True, custom_style=custom_style)

    st.write(f'original_items: {original_items}')
    st.write(f'sorted_items: {sorted_items}')