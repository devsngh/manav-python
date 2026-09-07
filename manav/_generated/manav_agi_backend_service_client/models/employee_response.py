from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_response_metadata_type_0 import EmployeeResponseMetadataType0


T = TypeVar("T", bound="EmployeeResponse")


@_attrs_define
class EmployeeResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        user_id (None | UUID):
        employee_code (str):
        first_name (str):
        last_name (str):
        full_name (str):
        work_email (None | str):
        personal_email (None | str):
        phone (None | str):
        legal_entity_id (None | UUID):
        department_code (None | str):
        title (None | str):
        manager_employee_id (None | UUID):
        hire_date (datetime.date | None):
        employment_status (str):
        termination_date (datetime.date | None):
        country_code (None | str):
        location (None | str):
        is_remote (bool | None):
        profile_image_asset_id (None | UUID):
        bio (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        metadata (EmployeeResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    user_id: None | UUID
    employee_code: str
    first_name: str
    last_name: str
    full_name: str
    work_email: None | str
    personal_email: None | str
    phone: None | str
    legal_entity_id: None | UUID
    department_code: None | str
    title: None | str
    manager_employee_id: None | UUID
    hire_date: datetime.date | None
    employment_status: str
    termination_date: datetime.date | None
    country_code: None | str
    location: None | str
    is_remote: bool | None
    profile_image_asset_id: None | UUID
    bio: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata: EmployeeResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_response_metadata_type_0 import EmployeeResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        user_id: None | str
        if isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        employee_code = self.employee_code

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        work_email: None | str
        work_email = self.work_email

        personal_email: None | str
        personal_email = self.personal_email

        phone: None | str
        phone = self.phone

        legal_entity_id: None | str
        if isinstance(self.legal_entity_id, UUID):
            legal_entity_id = str(self.legal_entity_id)
        else:
            legal_entity_id = self.legal_entity_id

        department_code: None | str
        department_code = self.department_code

        title: None | str
        title = self.title

        manager_employee_id: None | str
        if isinstance(self.manager_employee_id, UUID):
            manager_employee_id = str(self.manager_employee_id)
        else:
            manager_employee_id = self.manager_employee_id

        hire_date: None | str
        if isinstance(self.hire_date, datetime.date):
            hire_date = self.hire_date.isoformat()
        else:
            hire_date = self.hire_date

        employment_status = self.employment_status

        termination_date: None | str
        if isinstance(self.termination_date, datetime.date):
            termination_date = self.termination_date.isoformat()
        else:
            termination_date = self.termination_date

        country_code: None | str
        country_code = self.country_code

        location: None | str
        location = self.location

        is_remote: bool | None
        is_remote = self.is_remote

        profile_image_asset_id: None | str
        if isinstance(self.profile_image_asset_id, UUID):
            profile_image_asset_id = str(self.profile_image_asset_id)
        else:
            profile_image_asset_id = self.profile_image_asset_id

        bio: None | str
        bio = self.bio

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, EmployeeResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "user_id": user_id,
                "employee_code": employee_code,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "work_email": work_email,
                "personal_email": personal_email,
                "phone": phone,
                "legal_entity_id": legal_entity_id,
                "department_code": department_code,
                "title": title,
                "manager_employee_id": manager_employee_id,
                "hire_date": hire_date,
                "employment_status": employment_status,
                "termination_date": termination_date,
                "country_code": country_code,
                "location": location,
                "is_remote": is_remote,
                "profile_image_asset_id": profile_image_asset_id,
                "bio": bio,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_response_metadata_type_0 import EmployeeResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        def _parse_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        user_id = _parse_user_id(d.pop("user_id"))

        employee_code = d.pop("employee_code")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        full_name = d.pop("full_name")

        def _parse_work_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        work_email = _parse_work_email(d.pop("work_email"))

        def _parse_personal_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        personal_email = _parse_personal_email(d.pop("personal_email"))

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        def _parse_legal_entity_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legal_entity_id_type_0 = UUID(data)

                return legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        legal_entity_id = _parse_legal_entity_id(d.pop("legal_entity_id"))

        def _parse_department_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        department_code = _parse_department_code(d.pop("department_code"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_manager_employee_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manager_employee_id_type_0 = UUID(data)

                return manager_employee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        manager_employee_id = _parse_manager_employee_id(d.pop("manager_employee_id"))

        def _parse_hire_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hire_date_type_0 = datetime.date.fromisoformat(data)

                return hire_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        hire_date = _parse_hire_date(d.pop("hire_date"))

        employment_status = d.pop("employment_status")

        def _parse_termination_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_date_type_0 = datetime.date.fromisoformat(data)

                return termination_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        termination_date = _parse_termination_date(d.pop("termination_date"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("country_code"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_is_remote(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_remote = _parse_is_remote(d.pop("is_remote"))

        def _parse_profile_image_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_image_asset_id_type_0 = UUID(data)

                return profile_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        profile_image_asset_id = _parse_profile_image_asset_id(d.pop("profile_image_asset_id"))

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_metadata(data: object) -> EmployeeResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EmployeeResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeeResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        employee_response = cls(
            id=id,
            org_id=org_id,
            user_id=user_id,
            employee_code=employee_code,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            work_email=work_email,
            personal_email=personal_email,
            phone=phone,
            legal_entity_id=legal_entity_id,
            department_code=department_code,
            title=title,
            manager_employee_id=manager_employee_id,
            hire_date=hire_date,
            employment_status=employment_status,
            termination_date=termination_date,
            country_code=country_code,
            location=location,
            is_remote=is_remote,
            profile_image_asset_id=profile_image_asset_id,
            bio=bio,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
        )

        employee_response.additional_properties = d
        return employee_response

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
