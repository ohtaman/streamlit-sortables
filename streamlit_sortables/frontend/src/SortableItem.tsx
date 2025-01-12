import React, {ReactNode, FunctionComponent} from 'react';
import {useSortable} from '@dnd-kit/sortable';
import {CSS} from '@dnd-kit/utilities';

import './SortableComponent.css'

export interface SortableItemProps {
  id: string,
  isActive?: boolean,
  children?: ReactNode
}

export const SortableItem: FunctionComponent<SortableItemProps> = ((props) => {
    const {
      attributes,
      listeners,
      setNodeRef,
      transform,
      transition,
      isDragging
    } = useSortable({id: props.id});

    const style: React.CSSProperties = {
      transform: CSS.Transform.toString(transform),
      transition,
      opacity: isDragging ? 0.5 : undefined,
      cursor: isDragging ? 'grabbing' : 'grab'
    };

    const className = `btn shadow-none sortable-item ${props.isActive ? "active" : ""} ${isDragging ? "dragging" : ""}`;

    return (
      <li className={className} ref={setNodeRef} style={style} {...attributes} {...listeners}>
        {props.children ? props.children : null}
      </li>
    )
})
