from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_response_metadata_type_0 import ContactResponseMetadataType0
    from ..models.contact_response_social_handles_type_0 import ContactResponseSocialHandlesType0


T = TypeVar("T", bound="ContactResponse")


@_attrs_define
class ContactResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        account_id (None | UUID):
        first_name (None | str):
        last_name (None | str):
        full_name (str):
        email (None | str):
        phone (None | str):
        title (None | str):
        department (None | str):
        seniority (None | str):
        persona_id (None | UUID):
        is_primary (bool):
        buying_committee_role (None | str):
        social_handles (ContactResponseSocialHandlesType0 | None):
        last_engaged_at (datetime.datetime | None):
        created_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (ContactResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    account_id: None | UUID
    first_name: None | str
    last_name: None | str
    full_name: str
    email: None | str
    phone: None | str
    title: None | str
    department: None | str
    seniority: None | str
    persona_id: None | UUID
    is_primary: bool
    buying_committee_role: None | str
    social_handles: ContactResponseSocialHandlesType0 | None
    last_engaged_at: datetime.datetime | None
    created_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: ContactResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_response_metadata_type_0 import ContactResponseMetadataType0  # noqa: PLC0415
        from ..models.contact_response_social_handles_type_0 import ContactResponseSocialHandlesType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        account_id: None | str
        if isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        full_name = self.full_name

        email: None | str
        email = self.email

        phone: None | str
        phone = self.phone

        title: None | str
        title = self.title

        department: None | str
        department = self.department

        seniority: None | str
        seniority = self.seniority

        persona_id: None | str
        if isinstance(self.persona_id, UUID):
            persona_id = str(self.persona_id)
        else:
            persona_id = self.persona_id

        is_primary = self.is_primary

        buying_committee_role: None | str
        buying_committee_role = self.buying_committee_role

        social_handles: dict[str, Any] | None
        if isinstance(self.social_handles, ContactResponseSocialHandlesType0):
            social_handles = self.social_handles.to_dict()
        else:
            social_handles = self.social_handles

        last_engaged_at: None | str
        if isinstance(self.last_engaged_at, datetime.datetime):
            last_engaged_at = self.last_engaged_at.isoformat()
        else:
            last_engaged_at = self.last_engaged_at

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ContactResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "account_id": account_id,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "title": title,
                "department": department,
                "seniority": seniority,
                "persona_id": persona_id,
                "is_primary": is_primary,
                "buying_committee_role": buying_committee_role,
                "social_handles": social_handles,
                "last_engaged_at": last_engaged_at,
                "created_by_bot_id": created_by_bot_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_response_metadata_type_0 import ContactResponseMetadataType0  # noqa: PLC0415
        from ..models.contact_response_social_handles_type_0 import ContactResponseSocialHandlesType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        def _parse_account_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_id_type_0 = UUID(data)

                return account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        account_id = _parse_account_id(d.pop("account_id"))

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("first_name"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("last_name"))

        full_name = d.pop("full_name")

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_department(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        department = _parse_department(d.pop("department"))

        def _parse_seniority(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seniority = _parse_seniority(d.pop("seniority"))

        def _parse_persona_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                persona_id_type_0 = UUID(data)

                return persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        persona_id = _parse_persona_id(d.pop("persona_id"))

        is_primary = d.pop("is_primary")

        def _parse_buying_committee_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        buying_committee_role = _parse_buying_committee_role(d.pop("buying_committee_role"))

        def _parse_social_handles(data: object) -> ContactResponseSocialHandlesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_handles_type_0 = ContactResponseSocialHandlesType0.from_dict(data)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactResponseSocialHandlesType0 | None, data)

        social_handles = _parse_social_handles(d.pop("social_handles"))

        def _parse_last_engaged_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_engaged_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_engaged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_engaged_at = _parse_last_engaged_at(d.pop("last_engaged_at"))

        def _parse_created_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_bot_id_type_0 = UUID(data)

                return created_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_bot_id = _parse_created_by_bot_id(d.pop("created_by_bot_id"))

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

        def _parse_metadata(data: object) -> ContactResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ContactResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        contact_response = cls(
            id=id,
            org_id=org_id,
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
            created_by_bot_id=created_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        contact_response.additional_properties = d
        return contact_response

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
