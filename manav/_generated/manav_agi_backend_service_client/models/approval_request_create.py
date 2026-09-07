from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_request_create_metadata_type_0 import ApprovalRequestCreateMetadataType0


T = TypeVar("T", bound="ApprovalRequestCreate")


@_attrs_define
class ApprovalRequestCreate:
    """
    Attributes:
        policy_id (UUID):
        resource_type (str):
        resource_id (UUID):
        resource_summary (None | str | Unset):
        requested_amount (float | None | str | Unset):
        requested_currency_id (None | Unset | UUID):
        metadata (ApprovalRequestCreateMetadataType0 | None | Unset):
        auto_create_steps (bool | Unset):  Default: True.
    """

    policy_id: UUID
    resource_type: str
    resource_id: UUID
    resource_summary: None | str | Unset = UNSET
    requested_amount: float | None | str | Unset = UNSET
    requested_currency_id: None | Unset | UUID = UNSET
    metadata: ApprovalRequestCreateMetadataType0 | None | Unset = UNSET
    auto_create_steps: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_request_create_metadata_type_0 import ApprovalRequestCreateMetadataType0  # noqa: PLC0415

        policy_id = str(self.policy_id)

        resource_type = self.resource_type

        resource_id = str(self.resource_id)

        resource_summary: None | str | Unset
        if isinstance(self.resource_summary, Unset):
            resource_summary = UNSET
        else:
            resource_summary = self.resource_summary

        requested_amount: float | None | str | Unset
        if isinstance(self.requested_amount, Unset):
            requested_amount = UNSET
        else:
            requested_amount = self.requested_amount

        requested_currency_id: None | str | Unset
        if isinstance(self.requested_currency_id, Unset):
            requested_currency_id = UNSET
        elif isinstance(self.requested_currency_id, UUID):
            requested_currency_id = str(self.requested_currency_id)
        else:
            requested_currency_id = self.requested_currency_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ApprovalRequestCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        auto_create_steps = self.auto_create_steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy_id": policy_id,
                "resource_type": resource_type,
                "resource_id": resource_id,
            }
        )
        if resource_summary is not UNSET:
            field_dict["resource_summary"] = resource_summary
        if requested_amount is not UNSET:
            field_dict["requested_amount"] = requested_amount
        if requested_currency_id is not UNSET:
            field_dict["requested_currency_id"] = requested_currency_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if auto_create_steps is not UNSET:
            field_dict["auto_create_steps"] = auto_create_steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_request_create_metadata_type_0 import ApprovalRequestCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        policy_id = UUID(d.pop("policy_id"))

        resource_type = d.pop("resource_type")

        resource_id = UUID(d.pop("resource_id"))

        def _parse_resource_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_summary = _parse_resource_summary(d.pop("resource_summary", UNSET))

        def _parse_requested_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        requested_amount = _parse_requested_amount(d.pop("requested_amount", UNSET))

        def _parse_requested_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_currency_id_type_0 = UUID(data)

                return requested_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        requested_currency_id = _parse_requested_currency_id(d.pop("requested_currency_id", UNSET))

        def _parse_metadata(data: object) -> ApprovalRequestCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ApprovalRequestCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalRequestCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        auto_create_steps = d.pop("auto_create_steps", UNSET)

        approval_request_create = cls(
            policy_id=policy_id,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_summary=resource_summary,
            requested_amount=requested_amount,
            requested_currency_id=requested_currency_id,
            metadata=metadata,
            auto_create_steps=auto_create_steps,
        )

        approval_request_create.additional_properties = d
        return approval_request_create

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
