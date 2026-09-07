from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_node_request_where import MatchNodeRequestWhere


T = TypeVar("T", bound="MatchNodeRequest")


@_attrs_define
class MatchNodeRequest:
    """
    Attributes:
        label (str):
        where (MatchNodeRequestWhere | Unset): Property → value equality filters
        limit (int | Unset):  Default: 100.
    """

    label: str
    where: MatchNodeRequestWhere | Unset = UNSET
    limit: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        where: dict[str, Any] | Unset = UNSET
        if not isinstance(self.where, Unset):
            where = self.where.to_dict()

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if where is not UNSET:
            field_dict["where"] = where
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_node_request_where import MatchNodeRequestWhere  # noqa: PLC0415

        d = dict(src_dict)
        label = d.pop("label")

        _where = d.pop("where", UNSET)
        where: MatchNodeRequestWhere | Unset
        if isinstance(_where, Unset):
            where = UNSET
        else:
            where = MatchNodeRequestWhere.from_dict(_where)

        limit = d.pop("limit", UNSET)

        match_node_request = cls(
            label=label,
            where=where,
            limit=limit,
        )

        match_node_request.additional_properties = d
        return match_node_request

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
