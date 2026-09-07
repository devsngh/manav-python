from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_access_type import ReportAccessType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportAccessCreate")


@_attrs_define
class ReportAccessCreate:
    """
    Attributes:
        user_id (UUID):
        access_type (ReportAccessType):
        department_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        report_period (None | str | Unset):
    """

    user_id: UUID
    access_type: ReportAccessType
    department_id: None | Unset | UUID = UNSET
    bot_id: None | Unset | UUID = UNSET
    report_period: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = str(self.user_id)

        access_type = self.access_type.value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "access_type": access_type,
            }
        )
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if report_period is not UNSET:
            field_dict["report_period"] = report_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        access_type = ReportAccessType(d.pop("access_type"))

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

        report_access_create = cls(
            user_id=user_id,
            access_type=access_type,
            department_id=department_id,
            bot_id=bot_id,
            report_period=report_period,
        )

        report_access_create.additional_properties = d
        return report_access_create

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
