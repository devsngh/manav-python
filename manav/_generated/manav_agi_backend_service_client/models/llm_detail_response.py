from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.llm_status import LLMStatus
from ..models.model_category import ModelCategory
from ..models.model_type import ModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_parameter_response import LLMParameterResponse


T = TypeVar("T", bound="LLMDetailResponse")


@_attrs_define
class LLMDetailResponse:
    """LLM detailed response

    Attributes:
        id (UUID):
        llm_name (str):
        provider (str):
        model_id (str):
        model_type (ModelType): Type of model
        description (None | str):
        image_url (None | str):
        status (LLMStatus): LLM status
        allow_user_override (bool):
        model_path (None | str):
        download_id (None | UUID):
        created_by (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        model_category (ModelCategory | None | Unset):
        input_cost_per_m (float | None | Unset):
        output_cost_per_m (float | None | Unset):
        cost_per_unit (float | None | Unset):
        cost_unit_label (None | str | Unset):
        system_endpoint_url (None | str | Unset):
        parameter_count (int | Unset):  Default: 0.
        user_config_count (int | Unset):  Default: 0.
        parameters (list[LLMParameterResponse] | Unset):
        has_system_credentials (bool | Unset):  Default: False.
    """

    id: UUID
    llm_name: str
    provider: str
    model_id: str
    model_type: ModelType
    description: None | str
    image_url: None | str
    status: LLMStatus
    allow_user_override: bool
    model_path: None | str
    download_id: None | UUID
    created_by: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    model_category: ModelCategory | None | Unset = UNSET
    input_cost_per_m: float | None | Unset = UNSET
    output_cost_per_m: float | None | Unset = UNSET
    cost_per_unit: float | None | Unset = UNSET
    cost_unit_label: None | str | Unset = UNSET
    system_endpoint_url: None | str | Unset = UNSET
    parameter_count: int | Unset = 0
    user_config_count: int | Unset = 0
    parameters: list[LLMParameterResponse] | Unset = UNSET
    has_system_credentials: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        llm_name = self.llm_name

        provider = self.provider

        model_id = self.model_id

        model_type = self.model_type.value

        description: None | str
        description = self.description

        image_url: None | str
        image_url = self.image_url

        status = self.status.value

        allow_user_override = self.allow_user_override

        model_path: None | str
        model_path = self.model_path

        download_id: None | str
        if isinstance(self.download_id, UUID):
            download_id = str(self.download_id)
        else:
            download_id = self.download_id

        created_by = str(self.created_by)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        model_category: None | str | Unset
        if isinstance(self.model_category, Unset):
            model_category = UNSET
        elif isinstance(self.model_category, ModelCategory):
            model_category = self.model_category.value
        else:
            model_category = self.model_category

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

        system_endpoint_url: None | str | Unset
        if isinstance(self.system_endpoint_url, Unset):
            system_endpoint_url = UNSET
        else:
            system_endpoint_url = self.system_endpoint_url

        parameter_count = self.parameter_count

        user_config_count = self.user_config_count

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        has_system_credentials = self.has_system_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "llm_name": llm_name,
                "provider": provider,
                "model_id": model_id,
                "model_type": model_type,
                "description": description,
                "image_url": image_url,
                "status": status,
                "allow_user_override": allow_user_override,
                "model_path": model_path,
                "download_id": download_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if model_category is not UNSET:
            field_dict["model_category"] = model_category
        if input_cost_per_m is not UNSET:
            field_dict["input_cost_per_m"] = input_cost_per_m
        if output_cost_per_m is not UNSET:
            field_dict["output_cost_per_m"] = output_cost_per_m
        if cost_per_unit is not UNSET:
            field_dict["cost_per_unit"] = cost_per_unit
        if cost_unit_label is not UNSET:
            field_dict["cost_unit_label"] = cost_unit_label
        if system_endpoint_url is not UNSET:
            field_dict["system_endpoint_url"] = system_endpoint_url
        if parameter_count is not UNSET:
            field_dict["parameter_count"] = parameter_count
        if user_config_count is not UNSET:
            field_dict["user_config_count"] = user_config_count
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if has_system_credentials is not UNSET:
            field_dict["has_system_credentials"] = has_system_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_parameter_response import LLMParameterResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        llm_name = d.pop("llm_name")

        provider = d.pop("provider")

        model_id = d.pop("model_id")

        model_type = ModelType(d.pop("model_type"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        status = LLMStatus(d.pop("status"))

        allow_user_override = d.pop("allow_user_override")

        def _parse_model_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model_path = _parse_model_path(d.pop("model_path"))

        def _parse_download_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                download_id_type_0 = UUID(data)

                return download_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        download_id = _parse_download_id(d.pop("download_id"))

        created_by = UUID(d.pop("created_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_model_category(data: object) -> ModelCategory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_category_type_0 = ModelCategory(data)

                return model_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelCategory | None | Unset, data)

        model_category = _parse_model_category(d.pop("model_category", UNSET))

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

        def _parse_system_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_endpoint_url = _parse_system_endpoint_url(d.pop("system_endpoint_url", UNSET))

        parameter_count = d.pop("parameter_count", UNSET)

        user_config_count = d.pop("user_config_count", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[LLMParameterResponse] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = LLMParameterResponse.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        has_system_credentials = d.pop("has_system_credentials", UNSET)

        llm_detail_response = cls(
            id=id,
            llm_name=llm_name,
            provider=provider,
            model_id=model_id,
            model_type=model_type,
            description=description,
            image_url=image_url,
            status=status,
            allow_user_override=allow_user_override,
            model_path=model_path,
            download_id=download_id,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            model_category=model_category,
            input_cost_per_m=input_cost_per_m,
            output_cost_per_m=output_cost_per_m,
            cost_per_unit=cost_per_unit,
            cost_unit_label=cost_unit_label,
            system_endpoint_url=system_endpoint_url,
            parameter_count=parameter_count,
            user_config_count=user_config_count,
            parameters=parameters,
            has_system_credentials=has_system_credentials,
        )

        llm_detail_response.additional_properties = d
        return llm_detail_response

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
