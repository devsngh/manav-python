from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_record_response_request_metadata_type_0 import UsageRecordResponseRequestMetadataType0


T = TypeVar("T", bound="UsageRecordResponse")


@_attrs_define
class UsageRecordResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        metric_key (str):
        quantity (int):
        credits_charged (int):
        user_id (None | Unset | UUID):
        model_id (None | str | Unset):
        request_metadata (None | Unset | UsageRecordResponseRequestMetadataType0):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    org_id: UUID
    metric_key: str
    quantity: int
    credits_charged: int
    user_id: None | Unset | UUID = UNSET
    model_id: None | str | Unset = UNSET
    request_metadata: None | Unset | UsageRecordResponseRequestMetadataType0 = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_record_response_request_metadata_type_0 import (
            UsageRecordResponseRequestMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        metric_key = self.metric_key

        quantity = self.quantity

        credits_charged = self.credits_charged

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        request_metadata: dict[str, Any] | None | Unset
        if isinstance(self.request_metadata, Unset):
            request_metadata = UNSET
        elif isinstance(self.request_metadata, UsageRecordResponseRequestMetadataType0):
            request_metadata = self.request_metadata.to_dict()
        else:
            request_metadata = self.request_metadata

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "metric_key": metric_key,
                "quantity": quantity,
                "credits_charged": credits_charged,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if request_metadata is not UNSET:
            field_dict["request_metadata"] = request_metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_record_response_request_metadata_type_0 import (
            UsageRecordResponseRequestMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        metric_key = d.pop("metric_key")

        quantity = d.pop("quantity")

        credits_charged = d.pop("credits_charged")

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_request_metadata(data: object) -> None | Unset | UsageRecordResponseRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_metadata_type_0 = UsageRecordResponseRequestMetadataType0.from_dict(data)

                return request_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UsageRecordResponseRequestMetadataType0, data)

        request_metadata = _parse_request_metadata(d.pop("request_metadata", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        usage_record_response = cls(
            id=id,
            org_id=org_id,
            metric_key=metric_key,
            quantity=quantity,
            credits_charged=credits_charged,
            user_id=user_id,
            model_id=model_id,
            request_metadata=request_metadata,
            created_at=created_at,
        )

        usage_record_response.additional_properties = d
        return usage_record_response

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
