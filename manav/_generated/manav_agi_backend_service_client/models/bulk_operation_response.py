from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_operation_response_failed_users_item import BulkOperationResponseFailedUsersItem


T = TypeVar("T", bound="BulkOperationResponse")


@_attrs_define
class BulkOperationResponse:
    """Bulk operation response

    Attributes:
        success_count (int):
        failed_count (int):
        message (str):
        failed_users (list[BulkOperationResponseFailedUsersItem] | Unset):
    """

    success_count: int
    failed_count: int
    message: str
    failed_users: list[BulkOperationResponseFailedUsersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_count = self.success_count

        failed_count = self.failed_count

        message = self.message

        failed_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_users, Unset):
            failed_users = []
            for failed_users_item_data in self.failed_users:
                failed_users_item = failed_users_item_data.to_dict()
                failed_users.append(failed_users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success_count": success_count,
                "failed_count": failed_count,
                "message": message,
            }
        )
        if failed_users is not UNSET:
            field_dict["failed_users"] = failed_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_operation_response_failed_users_item import (
            BulkOperationResponseFailedUsersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        success_count = d.pop("success_count")

        failed_count = d.pop("failed_count")

        message = d.pop("message")

        _failed_users = d.pop("failed_users", UNSET)
        failed_users: list[BulkOperationResponseFailedUsersItem] | Unset = UNSET
        if _failed_users is not UNSET:
            failed_users = []
            for failed_users_item_data in _failed_users:
                failed_users_item = BulkOperationResponseFailedUsersItem.from_dict(failed_users_item_data)

                failed_users.append(failed_users_item)

        bulk_operation_response = cls(
            success_count=success_count,
            failed_count=failed_count,
            message=message,
            failed_users=failed_users,
        )

        bulk_operation_response.additional_properties = d
        return bulk_operation_response

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
