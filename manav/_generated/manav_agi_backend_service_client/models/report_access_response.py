from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportAccessResponse")


@_attrs_define
class ReportAccessResponse:
    """
    Attributes:
        id (UUID):
        user_id (UUID):
        access_type (str):
        org_id (UUID):
        granted_by (UUID):
        department_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        report_period (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    user_id: UUID
    access_type: str
    org_id: UUID
    granted_by: UUID
    department_id: None | Unset | UUID = UNSET
    bot_id: None | Unset | UUID = UNSET
    report_period: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = str(self.user_id)

        access_type = self.access_type

        org_id = str(self.org_id)

        granted_by = str(self.granted_by)

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        report_period: None | str | Unset
        if isinstance(self.report_period, Unset):
            report_period = UNSET
        else:
            report_period = self.report_period

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
                "user_id": user_id,
                "access_type": access_type,
                "org_id": org_id,
                "granted_by": granted_by,
            }
        )
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if report_period is not UNSET:
            field_dict["report_period"] = report_period
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        access_type = d.pop("access_type")

        org_id = UUID(d.pop("org_id"))

        granted_by = UUID(d.pop("granted_by"))

        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)

                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("department_id", UNSET))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_report_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_period = _parse_report_period(d.pop("report_period", UNSET))

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

        report_access_response = cls(
            id=id,
            user_id=user_id,
            access_type=access_type,
            org_id=org_id,
            granted_by=granted_by,
            department_id=department_id,
            bot_id=bot_id,
            report_period=report_period,
            created_at=created_at,
        )

        report_access_response.additional_properties = d
        return report_access_response

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
