import React, {ReactNode, FunctionComponent} from 'react';
import {useSortable} from '@dnd-kit/sortable';
import {CSS} from '@dnd-kit/utilities';

import './SortableComponent.css'

interface InLineStyles {
  [key: string]: React.CSSProperties
}

export interface SortableItemProps {
  id: string,
  isActive?: boolean,
  children?: ReactNode,
  inLineStyles?: InLineStyles
}

export const SortableItem: FunctionComponent<SortableItemProps> = ((props) => {
    const {
      attributes,
      listeners,
      setNodeRef,
      transform,
      transition,
    } = useSortable({id: props.id});
    const inLineStyles = props.inLineStyles

    const baseStyle: React.CSSProperties = {
      transform: CSS.Transform.toString(transform),
      transition
    };
  
    // Merge baseStyle with inLineStyles["sortable-item"] if it's not empty
    const style: React.CSSProperties = {
      ...baseStyle,
      ...(Object.keys(inLineStyles?.["sortable-item"] || {}).length > 0 ? inLineStyles?.["sortable-item"] : {})
    };


    const className = "btn shadow-none sortable-item " + (props.isActive ? "active" : "");

    return (
      <li className={className} ref={setNodeRef} style={style} {...attributes} {...listeners}>
        {props.children ? props.children : null}
      </li>
    )
})
