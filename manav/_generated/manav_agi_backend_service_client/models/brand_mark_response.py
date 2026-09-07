from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BrandMarkResponse")


@_attrs_define
class BrandMarkResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        mark_type (str):
        variant (None | str):
        asset_id (UUID):
        is_primary (bool):
        usage_rules (None | str):
        approved_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        approved_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
    """

    id: UUID
    org_id: UUID
    mark_type: str
    variant: None | str
    asset_id: UUID
    is_primary: bool
    usage_rules: None | str
    approved_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    approved_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        mark_type = self.mark_type

        variant: None | str
        variant = self.variant

        asset_id = str(self.asset_id)

        is_primary = self.is_primary

        usage_rules: None | str
        usage_rules = self.usage_rules

        approved_by_bot_id: None | str
        if isinstance(self.approved_by_bot_id, UUID):
            approved_by_bot_id = str(self.approved_by_bot_id)
        else:
            approved_by_bot_id = self.approved_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "mark_type": mark_type,
                "variant": variant,
                "asset_id": asset_id,
                "is_primary": is_primary,
                "usage_rules": usage_rules,
                "approved_by_bot_id": approved_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "approved_at": approved_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        mark_type = d.pop("mark_type")

        def _parse_variant(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant = _parse_variant(d.pop("variant"))

        asset_id = UUID(d.pop("asset_id"))

        is_primary = d.pop("is_primary")

        def _parse_usage_rules(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        usage_rules = _parse_usage_rules(d.pop("usage_rules"))

        def _parse_approved_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_bot_id_type_0 = UUID(data)

                return approved_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_bot_id = _parse_approved_by_bot_id(d.pop("approved_by_bot_id"))

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        def _parse_approved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        approved_at = _parse_approved_at(d.pop("approved_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        brand_mark_response = cls(
            id=id,
            org_id=org_id,
            mark_type=mark_type,
            variant=variant,
            asset_id=asset_id,
            is_primary=is_primary,
            usage_rules=usage_rules,
            approved_by_bot_id=approved_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            approved_at=approved_at,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        brand_mark_response.additional_properties = d
        return brand_mark_response

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
