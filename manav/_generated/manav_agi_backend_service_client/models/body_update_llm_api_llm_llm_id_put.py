from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyUpdateLlmApiLlmLlmIdPut")


@_attrs_define
class BodyUpdateLlmApiLlmLlmIdPut:
    """
    Attributes:
        llm_name (None | str | Unset):
        provider (None | str | Unset):
        model_id (None | str | Unset):
        model_category (None | str | Unset):
        description (None | str | Unset):
        llm_status (None | str | Unset):
        allow_user_override (bool | None | Unset):
        system_api_key (None | str | Unset):
        system_endpoint_url (None | str | Unset):
        model_path (None | str | Unset):
        input_cost_per_m (float | None | Unset):
        output_cost_per_m (float | None | Unset):
        cost_per_unit (float | None | Unset):
        cost_unit_label (None | str | Unset):
        image (File | None | Unset):
    """

    llm_name: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    model_category: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    llm_status: None | str | Unset = UNSET
    allow_user_override: bool | None | Unset = UNSET
    system_api_key: None | str | Unset = UNSET
    system_endpoint_url: None | str | Unset = UNSET
    model_path: None | str | Unset = UNSET
    input_cost_per_m: float | None | Unset = UNSET
    output_cost_per_m: float | None | Unset = UNSET
    cost_per_unit: float | None | Unset = UNSET
    cost_unit_label: None | str | Unset = UNSET
    image: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        llm_name: None | str | Unset
        if isinstance(self.llm_name, Unset):
            llm_name = UNSET
        else:
            llm_name = self.llm_name

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        model_category: None | str | Unset
        if isinstance(self.model_category, Unset):
            model_category = UNSET
        else:
            model_category = self.model_category

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        llm_status: None | str | Unset
        if isinstance(self.llm_status, Unset):
            llm_status = UNSET
        else:
            llm_status = self.llm_status

        allow_user_override: bool | None | Unset
        if isinstance(self.allow_user_override, Unset):
            allow_user_override = UNSET
        else:
            allow_user_override = self.allow_user_override

        system_api_key: None | str | Unset
        if isinstance(self.system_api_key, Unset):
            system_api_key = UNSET
        else:
            system_api_key = self.system_api_key

        system_endpoint_url: None | str | Unset
        if isinstance(self.system_endpoint_url, Unset):
            system_endpoint_url = UNSET
        else:
            system_endpoint_url = self.system_endpoint_url

        model_path: None | str | Unset
        if isinstance(self.model_path, Unset):
            model_path = UNSET
        else:
            model_path = self.model_path

        input_cost_per_m: float | None | Unset
        if isinstance(self.input_cost_per_m, Unset):
            input_cost_per_m = UNSET
        else:
            input_cost_per_m = self.input_cost_per_m

        output_cost_per_m: float | None | Unset
        if isinstance(self.output_cost_per_m, Unset):
            output_cost_per_m = UNSET
        else:
            output_cost_per_m = self.output_cost_per_m

        cost_per_unit: float | None | Unset
        if isinstance(self.cost_per_unit, Unset):
            cost_per_unit = UNSET
        else:
            cost_per_unit = self.cost_per_unit

        cost_unit_label: None | str | Unset
        if isinstance(self.cost_unit_label, Unset):
            cost_unit_label = UNSET
        else:
            cost_unit_label = self.cost_unit_label

        image: FileTypes | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if llm_name is not UNSET:
            field_dict["llm_name"] = llm_name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if model_category is not UNSET:
            field_dict["model_category"] = model_category
        if description is not UNSET:
            field_dict["description"] = description
        if llm_status is not UNSET:
            field_dict["llm_status"] = llm_status
        if allow_user_override is not UNSET:
            field_dict["allow_user_override"] = allow_user_override
        if system_api_key is not UNSET:
            field_dict["system_api_key"] = system_api_key
        if system_endpoint_url is not UNSET:
            field_dict["system_endpoint_url"] = system_endpoint_url
        if model_path is not UNSET:
            field_dict["model_path"] = model_path
        if input_cost_per_m is not UNSET:
            field_dict["input_cost_per_m"] = input_cost_per_m
        if output_cost_per_m is not UNSET:
            field_dict["output_cost_per_m"] = output_cost_per_m
        if cost_per_unit is not UNSET:
            field_dict["cost_per_unit"] = cost_per_unit
        if cost_unit_label is not UNSET:
            field_dict["cost_unit_label"] = cost_unit_label
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.llm_name, Unset):
            if isinstance(self.llm_name, str):
                files.append(("llm_name", (None, str(self.llm_name).encode(), "text/plain")))
            else:
                files.append(("llm_name", (None, str(self.llm_name).encode(), "text/plain")))

        if not isinstance(self.provider, Unset):
            if isinstance(self.provider, str):
                files.append(("provider", (None, str(self.provider).encode(), "text/plain")))
            else:
                files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        if not isinstance(self.model_id, Unset):
            if isinstance(self.model_id, str):
                files.append(("model_id", (None, str(self.model_id).encode(), "text/plain")))
            else:
                files.append(("model_id", (None, str(self.model_id).encode(), "text/plain")))

        if not isinstance(self.model_category, Unset):
            if isinstance(self.model_category, str):
                files.append(("model_category", (None, str(self.model_category).encode(), "text/plain")))
            else:
                files.append(("model_category", (None, str(self.model_category).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.llm_status, Unset):
            if isinstance(self.llm_status, str):
                files.append(("llm_status", (None, str(self.llm_status).encode(), "text/plain")))
            else:
                files.append(("llm_status", (None, str(self.llm_status).encode(), "text/plain")))

        if not isinstance(self.allow_user_override, Unset):
            if isinstance(self.allow_user_override, bool):
                files.append(("allow_user_override", (None, str(self.allow_user_override).encode(), "text/plain")))
            else:
                files.append(("allow_user_override", (None, str(self.allow_user_override).encode(), "text/plain")))

        if not isinstance(self.system_api_key, Unset):
            if isinstance(self.system_api_key, str):
                files.append(("system_api_key", (None, str(self.system_api_key).encode(), "text/plain")))
            else:
                files.append(("system_api_key", (None, str(self.system_api_key).encode(), "text/plain")))

        if not isinstance(self.system_endpoint_url, Unset):
            if isinstance(self.system_endpoint_url, str):
                files.append(("system_endpoint_url", (None, str(self.system_endpoint_url).encode(), "text/plain")))
            else:
                files.append(("system_endpoint_url", (None, str(self.system_endpoint_url).encode(), "text/plain")))

        if not isinstance(self.model_path, Unset):
            if isinstance(self.model_path, str):
                files.append(("model_path", (None, str(self.model_path).encode(), "text/plain")))
            else:
                files.append(("model_path", (None, str(self.model_path).encode(), "text/plain")))

        if not isinstance(self.input_cost_per_m, Unset):
            if isinstance(self.input_cost_per_m, float):
                files.append(("input_cost_per_m", (None, str(self.input_cost_per_m).encode(), "text/plain")))
            else:
                files.append(("input_cost_per_m", (None, str(self.input_cost_per_m).encode(), "text/plain")))

        if not isinstance(self.output_cost_per_m, Unset):
            if isinstance(self.output_cost_per_m, float):
                files.append(("output_cost_per_m", (None, str(self.output_cost_per_m).encode(), "text/plain")))
            else:
                files.append(("output_cost_per_m", (None, str(self.output_cost_per_m).encode(), "text/plain")))

        if not isinstance(self.cost_per_unit, Unset):
            if isinstance(self.cost_per_unit, float):
                files.append(("cost_per_unit", (None, str(self.cost_per_unit).encode(), "text/plain")))
            else:
                files.append(("cost_per_unit", (None, str(self.cost_per_unit).encode(), "text/plain")))

        if not isinstance(self.cost_unit_label, Unset):
            if isinstance(self.cost_unit_label, str):
                files.append(("cost_unit_label", (None, str(self.cost_unit_label).encode(), "text/plain")))
            else:
                files.append(("cost_unit_label", (None, str(self.cost_unit_label).encode(), "text/plain")))

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

        def _parse_llm_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llm_name = _parse_llm_name(d.pop("llm_name", UNSET))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_model_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_category = _parse_model_category(d.pop("model_category", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_llm_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llm_status = _parse_llm_status(d.pop("llm_status", UNSET))

        def _parse_allow_user_override(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_user_override = _parse_allow_user_override(d.pop("allow_user_override", UNSET))

        def _parse_system_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_api_key = _parse_system_api_key(d.pop("system_api_key", UNSET))

        def _parse_system_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_endpoint_url = _parse_system_endpoint_url(d.pop("system_endpoint_url", UNSET))

        def _parse_model_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_path = _parse_model_path(d.pop("model_path", UNSET))

        def _parse_input_cost_per_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_m = _parse_input_cost_per_m(d.pop("input_cost_per_m", UNSET))

        def _parse_output_cost_per_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_m = _parse_output_cost_per_m(d.pop("output_cost_per_m", UNSET))

        def _parse_cost_per_unit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_per_unit = _parse_cost_per_unit(d.pop("cost_per_unit", UNSET))

        def _parse_cost_unit_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_unit_label = _parse_cost_unit_label(d.pop("cost_unit_label", UNSET))

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

        body_update_llm_api_llm_llm_id_put = cls(
            llm_name=llm_name,
            provider=provider,
            model_id=model_id,
            model_category=model_category,
            description=description,
            llm_status=llm_status,
            allow_user_override=allow_user_override,
            system_api_key=system_api_key,
            system_endpoint_url=system_endpoint_url,
            model_path=model_path,
            input_cost_per_m=input_cost_per_m,
            output_cost_per_m=output_cost_per_m,
            cost_per_unit=cost_per_unit,
            cost_unit_label=cost_unit_label,
            image=image,
        )

        body_update_llm_api_llm_llm_id_put.additional_properties = d
        return body_update_llm_api_llm_llm_id_put

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
