import React, {ReactNode, FunctionComponent} from 'react';
import {useSortable} from '@dnd-kit/sortable';
import {CSS} from '@dnd-kit/utilities';
import { style as StyleGlamor } from "glamor";

import './SortableComponent.css'


export interface SortableItemProps {
  id: string,
  isActive?: boolean,
  children?: ReactNode,
}

export const SortableItem: FunctionComponent<SortableItemProps> = ((props) => {
    const {
      attributes,
      listeners,
      setNodeRef,
      transform,
      transition,
    } = useSortable({id: props.id});

    const style = {
      transform: CSS.Transform.toString(transform),
      transition
    };

    const className = "btn shadow-none sortable-item " + (props.isActive ? "active" : "");

    return (
      <li className={className} {...StyleGlamor(props.inLineStyles[className])} ref={setNodeRef} style={style} {...attributes} {...listeners}>
        {props.children ? props.children : null}
      </li>
    )
})
