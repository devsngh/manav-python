from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type import ModelType

if TYPE_CHECKING:
    from ..models.execution_config_response_config_parameters import ExecutionConfigResponseConfigParameters
    from ..models.execution_config_response_credentials import ExecutionConfigResponseCredentials


T = TypeVar("T", bound="ExecutionConfigResponse")


@_attrs_define
class ExecutionConfigResponse:
    """Resolved execution config

    Attributes:
        provider (str):
        model (str):
        model_type (ModelType): Type of model
        credentials (ExecutionConfigResponseCredentials):
        config_parameters (ExecutionConfigResponseConfigParameters):
        config_source (str):
        llm_id (UUID):
        llm_name (str):
    """

    provider: str
    model: str
    model_type: ModelType
    credentials: ExecutionConfigResponseCredentials
    config_parameters: ExecutionConfigResponseConfigParameters
    config_source: str
    llm_id: UUID
    llm_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        model = self.model

        model_type = self.model_type.value

        credentials = self.credentials.to_dict()

        config_parameters = self.config_parameters.to_dict()

        config_source = self.config_source

        llm_id = str(self.llm_id)

        llm_name = self.llm_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "model": model,
                "model_type": model_type,
                "credentials": credentials,
                "config_parameters": config_parameters,
                "config_source": config_source,
                "llm_id": llm_id,
                "llm_name": llm_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_config_response_config_parameters import (
            ExecutionConfigResponseConfigParameters,  # noqa: PLC0415
        )
        from ..models.execution_config_response_credentials import ExecutionConfigResponseCredentials  # noqa: PLC0415

        d = dict(src_dict)
        provider = d.pop("provider")

        model = d.pop("model")

        model_type = ModelType(d.pop("model_type"))

        credentials = ExecutionConfigResponseCredentials.from_dict(d.pop("credentials"))

        config_parameters = ExecutionConfigResponseConfigParameters.from_dict(d.pop("config_parameters"))

        config_source = d.pop("config_source")

        llm_id = UUID(d.pop("llm_id"))

        llm_name = d.pop("llm_name")

        execution_config_response = cls(
            provider=provider,
            model=model,
            model_type=model_type,
            credentials=credentials,
            config_parameters=config_parameters,
            config_source=config_source,
            llm_id=llm_id,
            llm_name=llm_name,
        )

        execution_config_response.additional_properties = d
        return execution_config_response

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
