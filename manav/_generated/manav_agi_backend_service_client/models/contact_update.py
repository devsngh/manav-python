from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_update_metadata_type_0 import ContactUpdateMetadataType0
    from ..models.contact_update_social_handles_type_0 import ContactUpdateSocialHandlesType0


T = TypeVar("T", bound="ContactUpdate")


@_attrs_define
class ContactUpdate:
    """
    Attributes:
        account_id (None | Unset | UUID):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        full_name (None | str | Unset):
        email (None | str | Unset):
        phone (None | str | Unset):
        title (None | str | Unset):
        department (None | str | Unset):
        seniority (None | str | Unset):
        persona_id (None | Unset | UUID):
        is_primary (bool | None | Unset):
        buying_committee_role (None | str | Unset):
        social_handles (ContactUpdateSocialHandlesType0 | None | Unset):
        last_engaged_at (datetime.datetime | None | Unset):
        metadata (ContactUpdateMetadataType0 | None | Unset):
    """

    account_id: None | Unset | UUID = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    seniority: None | str | Unset = UNSET
    persona_id: None | Unset | UUID = UNSET
    is_primary: bool | None | Unset = UNSET
    buying_committee_role: None | str | Unset = UNSET
    social_handles: ContactUpdateSocialHandlesType0 | None | Unset = UNSET
    last_engaged_at: datetime.datetime | None | Unset = UNSET
    metadata: ContactUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_update_metadata_type_0 import ContactUpdateMetadataType0  # noqa: PLC0415
        from ..models.contact_update_social_handles_type_0 import ContactUpdateSocialHandlesType0  # noqa: PLC0415

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        elif isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

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

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        seniority: None | str | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        else:
            seniority = self.seniority

        persona_id: None | str | Unset
        if isinstance(self.persona_id, Unset):
            persona_id = UNSET
        elif isinstance(self.persona_id, UUID):
            persona_id = str(self.persona_id)
        else:
            persona_id = self.persona_id

        is_primary: bool | None | Unset
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        buying_committee_role: None | str | Unset
        if isinstance(self.buying_committee_role, Unset):
            buying_committee_role = UNSET
        else:
            buying_committee_role = self.buying_committee_role

        social_handles: dict[str, Any] | None | Unset
        if isinstance(self.social_handles, Unset):
            social_handles = UNSET
        elif isinstance(self.social_handles, ContactUpdateSocialHandlesType0):
            social_handles = self.social_handles.to_dict()
        else:
            social_handles = self.social_handles

        last_engaged_at: None | str | Unset
        if isinstance(self.last_engaged_at, Unset):
            last_engaged_at = UNSET
        elif isinstance(self.last_engaged_at, datetime.datetime):
            last_engaged_at = self.last_engaged_at.isoformat()
        else:
            last_engaged_at = self.last_engaged_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ContactUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if title is not UNSET:
            field_dict["title"] = title
        if department is not UNSET:
            field_dict["department"] = department
        if seniority is not UNSET:
            field_dict["seniority"] = seniority
        if persona_id is not UNSET:
            field_dict["persona_id"] = persona_id
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if buying_committee_role is not UNSET:
            field_dict["buying_committee_role"] = buying_committee_role
        if social_handles is not UNSET:
            field_dict["social_handles"] = social_handles
        if last_engaged_at is not UNSET:
            field_dict["last_engaged_at"] = last_engaged_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_update_metadata_type_0 import ContactUpdateMetadataType0  # noqa: PLC0415
        from ..models.contact_update_social_handles_type_0 import ContactUpdateSocialHandlesType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_id_type_0 = UUID(data)

                return account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))

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

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_seniority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        def _parse_persona_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                persona_id_type_0 = UUID(data)

                return persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        persona_id = _parse_persona_id(d.pop("persona_id", UNSET))

        def _parse_is_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_primary = _parse_is_primary(d.pop("is_primary", UNSET))

        def _parse_buying_committee_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buying_committee_role = _parse_buying_committee_role(d.pop("buying_committee_role", UNSET))

        def _parse_social_handles(data: object) -> ContactUpdateSocialHandlesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_handles_type_0 = ContactUpdateSocialHandlesType0.from_dict(data)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactUpdateSocialHandlesType0 | None | Unset, data)

        social_handles = _parse_social_handles(d.pop("social_handles", UNSET))

        def _parse_last_engaged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_engaged_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_engaged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_engaged_at = _parse_last_engaged_at(d.pop("last_engaged_at", UNSET))

        def _parse_metadata(data: object) -> ContactUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ContactUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        contact_update = cls(
            account_id=account_id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            email=email,
            phone=phone,
            title=title,
            department=department,
            seniority=seniority,
            persona_id=persona_id,
            is_primary=is_primary,
            buying_committee_role=buying_committee_role,
            social_handles=social_handles,
            last_engaged_at=last_engaged_at,
            metadata=metadata,
        )

        contact_update.additional_properties = d
        return contact_update

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
