import React, {ReactNode, FunctionComponent} from 'react';
import {useSortable} from '@dnd-kit/sortable';
import {CSS} from '@dnd-kit/utilities';

import './SortableComponent.css'

export interface SortableItemProps {
  id: string,
  isActive?: boolean,
  children?: ReactNode,
  isOverlay?: boolean
}

export const SortableItem: FunctionComponent<SortableItemProps> = ((props) => {
    const {
      attributes,
      listeners,
      setNodeRef,
      transform,
      transition
    } = useSortable({id: props.id});

    // If overlay, override the sortable properties
    const sortableProps = props.isOverlay ? {
      attributes: {},
      listeners: {},
      setNodeRef: null,
      transform: null,
      transition: undefined,
      isDragging: true
    } : {
      attributes,
      listeners,
      setNodeRef,
      transform,
      transition,
      isDragging: false
    };

    const style: React.CSSProperties = {
      transform: sortableProps.transform ? CSS.Transform.toString(sortableProps.transform) : undefined,
      transition: sortableProps.transition,
      cursor: sortableProps.isDragging ? 'grabbing' : 'grab'
    };

    const className = `btn shadow-none sortable-item ${props.isActive ? "active" : ""} ${sortableProps.isDragging ? "dragging" : ""}`;

    return (
      <li className={className} ref={sortableProps.setNodeRef} style={style} {...sortableProps.attributes} {...sortableProps.listeners}>
        {props.children ? props.children : null}
      </li>
    )
})
