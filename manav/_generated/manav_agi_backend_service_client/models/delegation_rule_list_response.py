from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delegation_rule_response import DelegationRuleResponse


T = TypeVar("T", bound="DelegationRuleListResponse")


@_attrs_define
class DelegationRuleListResponse:
    """
    Attributes:
        delegations (list[DelegationRuleResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    delegations: list[DelegationRuleResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delegations = []
        for delegations_item_data in self.delegations:
            delegations_item = delegations_item_data.to_dict()
            delegations.append(delegations_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delegations": delegations,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegation_rule_response import DelegationRuleResponse  # noqa: PLC0415

        d = dict(src_dict)
        delegations = []
        _delegations = d.pop("delegations")
        for delegations_item_data in _delegations:
            delegations_item = DelegationRuleResponse.from_dict(delegations_item_data)

            delegations.append(delegations_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        delegation_rule_list_response = cls(
            delegations=delegations,
            total=total,
            page=page,
            page_size=page_size,
        )

        delegation_rule_list_response.additional_properties = d
        return delegation_rule_list_response

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
