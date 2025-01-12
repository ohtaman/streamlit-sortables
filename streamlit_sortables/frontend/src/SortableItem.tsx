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
      transition,
      isDragging
    } = props.isOverlay ? { 
      attributes: {}, 
      listeners: {}, 
      setNodeRef: null, 
      transform: null, 
      transition: undefined, 
      isDragging: false 
    } : useSortable({id: props.id});

    const style: React.CSSProperties = {
      transform: transform ? CSS.Transform.toString(transform) : undefined,
      transition,
      cursor: isDragging ? 'grabbing' : 'grab'
    };

    const className = `btn shadow-none sortable-item ${props.isActive ? "active" : ""} ${isDragging ? "dragging" : ""} ${props.isOverlay ? "sortable-item-overlay" : ""}`;

    return (
      <li className={className} ref={setNodeRef} style={style} {...attributes} {...listeners}>
        {props.children ? props.children : null}
      </li>
    )
})
