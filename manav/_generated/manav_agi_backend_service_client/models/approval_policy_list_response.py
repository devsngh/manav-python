from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.approval_policy_response import ApprovalPolicyResponse


T = TypeVar("T", bound="ApprovalPolicyListResponse")


@_attrs_define
class ApprovalPolicyListResponse:
    """
    Attributes:
        policies (list[ApprovalPolicyResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    policies: list[ApprovalPolicyResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policies = []
        for policies_item_data in self.policies:
            policies_item = policies_item_data.to_dict()
            policies.append(policies_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policies": policies,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_policy_response import ApprovalPolicyResponse  # noqa: PLC0415

        d = dict(src_dict)
        policies = []
        _policies = d.pop("policies")
        for policies_item_data in _policies:
            policies_item = ApprovalPolicyResponse.from_dict(policies_item_data)

            policies.append(policies_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        approval_policy_list_response = cls(
            policies=policies,
            total=total,
            page=page,
            page_size=page_size,
        )

        approval_policy_list_response.additional_properties = d
        return approval_policy_list_response

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
