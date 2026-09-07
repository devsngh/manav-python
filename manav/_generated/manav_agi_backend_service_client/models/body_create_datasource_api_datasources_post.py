from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyCreateDatasourceApiDatasourcesPost")


@_attrs_define
class BodyCreateDatasourceApiDatasourcesPost:
    """
    Attributes:
        datasource_name (str):
        datasource_ui_name (str):
        description (str):
        category_id (str):
        credential_fields (str): JSON string of credential fields
        subcategory_id (None | str | Unset):
        connection_template (None | str | Unset):
        status (str | Unset):  Default: 'testing'.
        logo (File | None | Unset):
        config_parameters (None | str | Unset): JSON string of config parameters
        mcp_path (None | str | Unset):
    """

    datasource_name: str
    datasource_ui_name: str
    description: str
    category_id: str
    credential_fields: str
    subcategory_id: None | str | Unset = UNSET
    connection_template: None | str | Unset = UNSET
    status: str | Unset = "testing"
    logo: File | None | Unset = UNSET
    config_parameters: None | str | Unset = UNSET
    mcp_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource_name = self.datasource_name

        datasource_ui_name = self.datasource_ui_name

        description = self.description

        category_id = self.category_id

        credential_fields = self.credential_fields

        subcategory_id: None | str | Unset
        if isinstance(self.subcategory_id, Unset):
            subcategory_id = UNSET
        else:
            subcategory_id = self.subcategory_id

        connection_template: None | str | Unset
        if isinstance(self.connection_template, Unset):
            connection_template = UNSET
        else:
            connection_template = self.connection_template

        status = self.status

        logo: FileTypes | None | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        elif isinstance(self.logo, File):
            logo = self.logo.to_tuple()

        else:
            logo = self.logo

        config_parameters: None | str | Unset
        if isinstance(self.config_parameters, Unset):
            config_parameters = UNSET
        else:
            config_parameters = self.config_parameters

        mcp_path: None | str | Unset
        if isinstance(self.mcp_path, Unset):
            mcp_path = UNSET
        else:
            mcp_path = self.mcp_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasource_name": datasource_name,
                "datasource_ui_name": datasource_ui_name,
                "description": description,
                "category_id": category_id,
                "credential_fields": credential_fields,
            }
        )
        if subcategory_id is not UNSET:
            field_dict["subcategory_id"] = subcategory_id
        if connection_template is not UNSET:
            field_dict["connection_template"] = connection_template
        if status is not UNSET:
            field_dict["status"] = status
        if logo is not UNSET:
            field_dict["logo"] = logo
        if config_parameters is not UNSET:
            field_dict["config_parameters"] = config_parameters
        if mcp_path is not UNSET:
            field_dict["mcp_path"] = mcp_path

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("datasource_name", (None, str(self.datasource_name).encode(), "text/plain")))

        files.append(("datasource_ui_name", (None, str(self.datasource_ui_name).encode(), "text/plain")))

        files.append(("description", (None, str(self.description).encode(), "text/plain")))

        files.append(("category_id", (None, str(self.category_id).encode(), "text/plain")))

        files.append(("credential_fields", (None, str(self.credential_fields).encode(), "text/plain")))

        if not isinstance(self.subcategory_id, Unset):
            if isinstance(self.subcategory_id, str):
                files.append(("subcategory_id", (None, str(self.subcategory_id).encode(), "text/plain")))
            else:
                files.append(("subcategory_id", (None, str(self.subcategory_id).encode(), "text/plain")))

        if not isinstance(self.connection_template, Unset):
            if isinstance(self.connection_template, str):
                files.append(("connection_template", (None, str(self.connection_template).encode(), "text/plain")))
            else:
                files.append(("connection_template", (None, str(self.connection_template).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        if not isinstance(self.logo, Unset):
            if isinstance(self.logo, File):
                files.append(("logo", self.logo.to_tuple()))
            else:
                files.append(("logo", (None, str(self.logo).encode(), "text/plain")))

        if not isinstance(self.config_parameters, Unset):
            if isinstance(self.config_parameters, str):
                files.append(("config_parameters", (None, str(self.config_parameters).encode(), "text/plain")))
            else:
                files.append(("config_parameters", (None, str(self.config_parameters).encode(), "text/plain")))

        if not isinstance(self.mcp_path, Unset):
            if isinstance(self.mcp_path, str):
                files.append(("mcp_path", (None, str(self.mcp_path).encode(), "text/plain")))
            else:
                files.append(("mcp_path", (None, str(self.mcp_path).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datasource_name = d.pop("datasource_name")

        datasource_ui_name = d.pop("datasource_ui_name")

        description = d.pop("description")

        category_id = d.pop("category_id")

        credential_fields = d.pop("credential_fields")

        def _parse_subcategory_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subcategory_id = _parse_subcategory_id(d.pop("subcategory_id", UNSET))

        def _parse_connection_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_template = _parse_connection_template(d.pop("connection_template", UNSET))

        status = d.pop("status", UNSET)

        def _parse_logo(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                logo_type_0 = File(payload=BytesIO(data))

                return logo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_config_parameters(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config_parameters = _parse_config_parameters(d.pop("config_parameters", UNSET))

        def _parse_mcp_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcp_path = _parse_mcp_path(d.pop("mcp_path", UNSET))

        body_create_datasource_api_datasources_post = cls(
            datasource_name=datasource_name,
            datasource_ui_name=datasource_ui_name,
            description=description,
            category_id=category_id,
            credential_fields=credential_fields,
            subcategory_id=subcategory_id,
            connection_template=connection_template,
            status=status,
            logo=logo,
            config_parameters=config_parameters,
            mcp_path=mcp_path,
        )

        body_create_datasource_api_datasources_post.additional_properties = d
        return body_create_datasource_api_datasources_post

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
