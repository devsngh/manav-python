from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyRegisterHfModelApiLlmHfDownloadsDownloadIdRegisterPost")


@_attrs_define
class BodyRegisterHfModelApiLlmHfDownloadsDownloadIdRegisterPost:
    """
    Attributes:
        llm_name (str):
        provider (str):
        model_id (str):
        model_type (str):
        llm_status (str):
        description (str | Unset):
        allow_user_override (bool | Unset):  Default: True.
        parameters (str | Unset):  Default: '[]'.
        image (File | None | Unset):
    """

    llm_name: str
    provider: str
    model_id: str
    model_type: str
    llm_status: str
    description: str | Unset = UNSET
    allow_user_override: bool | Unset = True
    parameters: str | Unset = "[]"
    image: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        llm_name = self.llm_name

        provider = self.provider

        model_id = self.model_id

        model_type = self.model_type

        llm_status = self.llm_status

        description = self.description

        allow_user_override = self.allow_user_override

        parameters = self.parameters

        image: FileTypes | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "llm_name": llm_name,
                "provider": provider,
                "model_id": model_id,
                "model_type": model_type,
                "llm_status": llm_status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if allow_user_override is not UNSET:
            field_dict["allow_user_override"] = allow_user_override
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("llm_name", (None, str(self.llm_name).encode(), "text/plain")))

        files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        files.append(("model_id", (None, str(self.model_id).encode(), "text/plain")))

        files.append(("model_type", (None, str(self.model_type).encode(), "text/plain")))

        files.append(("llm_status", (None, str(self.llm_status).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.allow_user_override, Unset):
            files.append(("allow_user_override", (None, str(self.allow_user_override).encode(), "text/plain")))

        if not isinstance(self.parameters, Unset):
            files.append(("parameters", (None, str(self.parameters).encode(), "text/plain")))

        if not isinstance(self.image, Unset):
            if isinstance(self.image, File):
                files.append(("image", self.image.to_tuple()))
            else:
                files.append(("image", (None, str(self.image).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        llm_name = d.pop("llm_name")

        provider = d.pop("provider")

        model_id = d.pop("model_id")

        model_type = d.pop("model_type")

        llm_status = d.pop("llm_status")

        description = d.pop("description", UNSET)

        allow_user_override = d.pop("allow_user_override", UNSET)

        parameters = d.pop("parameters", UNSET)

        def _parse_image(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                image_type_0 = File(payload=BytesIO(data))

                return image_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        body_register_hf_model_api_llm_hf_downloads_download_id_register_post = cls(
            llm_name=llm_name,
            provider=provider,
            model_id=model_id,
            model_type=model_type,
            llm_status=llm_status,
            description=description,
            allow_user_override=allow_user_override,
            parameters=parameters,
            image=image,
        )

        body_register_hf_model_api_llm_hf_downloads_download_id_register_post.additional_properties = d
        return body_register_hf_model_api_llm_hf_downloads_download_id_register_post

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
