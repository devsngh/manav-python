from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reorder_rules_request_order_map import ReorderRulesRequestOrderMap


T = TypeVar("T", bound="ReorderRulesRequest")


@_attrs_define
class ReorderRulesRequest:
    """
    Attributes:
        order_map (ReorderRulesRequestOrderMap): {rule_id: new_step_order}
    """

    order_map: ReorderRulesRequestOrderMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_map = self.order_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_map": order_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_rules_request_order_map import ReorderRulesRequestOrderMap  # noqa: PLC0415

        d = dict(src_dict)
        order_map = ReorderRulesRequestOrderMap.from_dict(d.pop("order_map"))

        reorder_rules_request = cls(
            order_map=order_map,
        )

        reorder_rules_request.additional_properties = d
        return reorder_rules_request

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
