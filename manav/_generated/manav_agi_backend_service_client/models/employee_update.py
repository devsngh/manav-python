from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_update_metadata_type_0 import EmployeeUpdateMetadataType0


T = TypeVar("T", bound="EmployeeUpdate")


@_attrs_define
class EmployeeUpdate:
    """
    Attributes:
        employee_code (None | str | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        full_name (None | str | Unset):
        user_id (None | Unset | UUID):
        work_email (None | str | Unset):
        personal_email (None | str | Unset):
        phone (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        department_code (None | str | Unset):
        title (None | str | Unset):
        hire_date (datetime.date | None | Unset):
        employment_status (None | str | Unset):
        termination_date (datetime.date | None | Unset):
        country_code (None | str | Unset):
        location (None | str | Unset):
        is_remote (bool | None | Unset):
        profile_image_asset_id (None | Unset | UUID):
        bio (None | str | Unset):
        metadata (EmployeeUpdateMetadataType0 | None | Unset):
    """

    employee_code: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    work_email: None | str | Unset = UNSET
    personal_email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    legal_entity_id: None | Unset | UUID = UNSET
    department_code: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    hire_date: datetime.date | None | Unset = UNSET
    employment_status: None | str | Unset = UNSET
    termination_date: datetime.date | None | Unset = UNSET
    country_code: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    is_remote: bool | None | Unset = UNSET
    profile_image_asset_id: None | Unset | UUID = UNSET
    bio: None | str | Unset = UNSET
    metadata: EmployeeUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_update_metadata_type_0 import EmployeeUpdateMetadataType0  # noqa: PLC0415

        employee_code: None | str | Unset
        if isinstance(self.employee_code, Unset):
            employee_code = UNSET
        else:
            employee_code = self.employee_code

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        work_email: None | str | Unset
        if isinstance(self.work_email, Unset):
            work_email = UNSET
        else:
            work_email = self.work_email

        personal_email: None | str | Unset
        if isinstance(self.personal_email, Unset):
            personal_email = UNSET
        else:
            personal_email = self.personal_email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        legal_entity_id: None | str | Unset
        if isinstance(self.legal_entity_id, Unset):
            legal_entity_id = UNSET
        elif isinstance(self.legal_entity_id, UUID):
            legal_entity_id = str(self.legal_entity_id)
        else:
            legal_entity_id = self.legal_entity_id

        department_code: None | str | Unset
        if isinstance(self.department_code, Unset):
            department_code = UNSET
        else:
            department_code = self.department_code

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        hire_date: None | str | Unset
        if isinstance(self.hire_date, Unset):
            hire_date = UNSET
        elif isinstance(self.hire_date, datetime.date):
            hire_date = self.hire_date.isoformat()
        else:
            hire_date = self.hire_date

        employment_status: None | str | Unset
        if isinstance(self.employment_status, Unset):
            employment_status = UNSET
        else:
            employment_status = self.employment_status

        termination_date: None | str | Unset
        if isinstance(self.termination_date, Unset):
            termination_date = UNSET
        elif isinstance(self.termination_date, datetime.date):
            termination_date = self.termination_date.isoformat()
        else:
            termination_date = self.termination_date

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        is_remote: bool | None | Unset
        if isinstance(self.is_remote, Unset):
            is_remote = UNSET
        else:
            is_remote = self.is_remote

        profile_image_asset_id: None | str | Unset
        if isinstance(self.profile_image_asset_id, Unset):
            profile_image_asset_id = UNSET
        elif isinstance(self.profile_image_asset_id, UUID):
            profile_image_asset_id = str(self.profile_image_asset_id)
        else:
            profile_image_asset_id = self.profile_image_asset_id

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, EmployeeUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_code is not UNSET:
            field_dict["employee_code"] = employee_code
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if work_email is not UNSET:
            field_dict["work_email"] = work_email
        if personal_email is not UNSET:
            field_dict["personal_email"] = personal_email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if department_code is not UNSET:
            field_dict["department_code"] = department_code
        if title is not UNSET:
            field_dict["title"] = title
        if hire_date is not UNSET:
            field_dict["hire_date"] = hire_date
        if employment_status is not UNSET:
            field_dict["employment_status"] = employment_status
        if termination_date is not UNSET:
            field_dict["termination_date"] = termination_date
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if location is not UNSET:
            field_dict["location"] = location
        if is_remote is not UNSET:
            field_dict["is_remote"] = is_remote
        if profile_image_asset_id is not UNSET:
            field_dict["profile_image_asset_id"] = profile_image_asset_id
        if bio is not UNSET:
            field_dict["bio"] = bio
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_update_metadata_type_0 import EmployeeUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_employee_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_code = _parse_employee_code(d.pop("employee_code", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

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

        def _parse_work_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email = _parse_work_email(d.pop("work_email", UNSET))

        def _parse_personal_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        personal_email = _parse_personal_email(d.pop("personal_email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_legal_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legal_entity_id_type_0 = UUID(data)

                return legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        legal_entity_id = _parse_legal_entity_id(d.pop("legal_entity_id", UNSET))

        def _parse_department_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_code = _parse_department_code(d.pop("department_code", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_hire_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hire_date_type_0 = datetime.date.fromisoformat(data)

                return hire_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        hire_date = _parse_hire_date(d.pop("hire_date", UNSET))

        def _parse_employment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_status = _parse_employment_status(d.pop("employment_status", UNSET))

        def _parse_termination_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_date_type_0 = datetime.date.fromisoformat(data)

                return termination_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        termination_date = _parse_termination_date(d.pop("termination_date", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_is_remote(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_remote = _parse_is_remote(d.pop("is_remote", UNSET))

        def _parse_profile_image_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_image_asset_id_type_0 = UUID(data)

                return profile_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        profile_image_asset_id = _parse_profile_image_asset_id(d.pop("profile_image_asset_id", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_metadata(data: object) -> EmployeeUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EmployeeUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeeUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        employee_update = cls(
            employee_code=employee_code,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            user_id=user_id,
            work_email=work_email,
            personal_email=personal_email,
            phone=phone,
            legal_entity_id=legal_entity_id,
            department_code=department_code,
            title=title,
            hire_date=hire_date,
            employment_status=employment_status,
            termination_date=termination_date,
            country_code=country_code,
            location=location,
            is_remote=is_remote,
            profile_image_asset_id=profile_image_asset_id,
            bio=bio,
            metadata=metadata,
        )

        employee_update.additional_properties = d
        return employee_update

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
