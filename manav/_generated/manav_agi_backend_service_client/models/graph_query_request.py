from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_direction import GraphDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphQueryRequest")


@_attrs_define
class GraphQueryRequest:
    """
    Attributes:
        workspace_id (str):
        start_node_type (str):
        start_node_id (str):
        relationship_types (list[str] | None | Unset):
        direction (GraphDirection | Unset):  Default: GraphDirection.OUTGOING.
        depth (int | Unset):  Default: 1.
    """

    workspace_id: str
    start_node_type: str
    start_node_id: str
    relationship_types: list[str] | None | Unset = UNSET
    direction: GraphDirection | Unset = GraphDirection.OUTGOING
    depth: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        start_node_type = self.start_node_type

        start_node_id = self.start_node_id

        relationship_types: list[str] | None | Unset
        if isinstance(self.relationship_types, Unset):
            relationship_types = UNSET
        elif isinstance(self.relationship_types, list):
            relationship_types = self.relationship_types

        else:
            relationship_types = self.relationship_types

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        depth = self.depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
                "start_node_type": start_node_type,
                "start_node_id": start_node_id,
            }
        )
        if relationship_types is not UNSET:
            field_dict["relationship_types"] = relationship_types
        if direction is not UNSET:
            field_dict["direction"] = direction
        if depth is not UNSET:
            field_dict["depth"] = depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        start_node_type = d.pop("start_node_type")

        start_node_id = d.pop("start_node_id")

        def _parse_relationship_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                relationship_types_type_0 = cast(list[str], data)

                return relationship_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        relationship_types = _parse_relationship_types(d.pop("relationship_types", UNSET))

        _direction = d.pop("direction", UNSET)
        direction: GraphDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = GraphDirection(_direction)

        depth = d.pop("depth", UNSET)

        graph_query_request = cls(
            workspace_id=workspace_id,
            start_node_type=start_node_type,
            start_node_id=start_node_id,
            relationship_types=relationship_types,
            direction=direction,
            depth=depth,
        )

        graph_query_request.additional_properties = d
        return graph_query_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
