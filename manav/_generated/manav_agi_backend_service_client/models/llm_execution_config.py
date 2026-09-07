from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_credentials import LLMCredentials
    from ..models.llm_execution_config_config_parameters import LLMExecutionConfigConfigParameters
    from ..models.llm_execution_config_rate_limits_type_0 import LLMExecutionConfigRateLimitsType0


T = TypeVar("T", bound="LLMExecutionConfig")


@_attrs_define
class LLMExecutionConfig:
    """Resolved LLM configuration including decrypted credentials.
    Sourced from LLM Registry (system config or user override).

        Attributes:
            llm_id (str):
            llm_name (str):
            provider (str):
            model_id (str):
            model_type (str):
            credentials (LLMCredentials): Decrypted LLM credentials — passed to orchestrator/agent_engine for LLM calls
            config_parameters (LLMExecutionConfigConfigParameters):
            config_source (str):
            detected_tier (None | str | Unset):
            rate_limits (LLMExecutionConfigRateLimitsType0 | None | Unset):
    """

    llm_id: str
    llm_name: str
    provider: str
    model_id: str
    model_type: str
    credentials: LLMCredentials
    config_parameters: LLMExecutionConfigConfigParameters
    config_source: str
    detected_tier: None | str | Unset = UNSET
    rate_limits: LLMExecutionConfigRateLimitsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.llm_execution_config_rate_limits_type_0 import LLMExecutionConfigRateLimitsType0  # noqa: PLC0415

        llm_id = self.llm_id

        llm_name = self.llm_name

        provider = self.provider

        model_id = self.model_id

        model_type = self.model_type

        credentials = self.credentials.to_dict()

        config_parameters = self.config_parameters.to_dict()

        config_source = self.config_source

        detected_tier: None | str | Unset
        if isinstance(self.detected_tier, Unset):
            detected_tier = UNSET
        else:
            detected_tier = self.detected_tier

        rate_limits: dict[str, Any] | None | Unset
        if isinstance(self.rate_limits, Unset):
            rate_limits = UNSET
        elif isinstance(self.rate_limits, LLMExecutionConfigRateLimitsType0):
            rate_limits = self.rate_limits.to_dict()
        else:
            rate_limits = self.rate_limits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "llm_id": llm_id,
                "llm_name": llm_name,
                "provider": provider,
                "model_id": model_id,
                "model_type": model_type,
                "credentials": credentials,
                "config_parameters": config_parameters,
                "config_source": config_source,
            }
        )
        if detected_tier is not UNSET:
            field_dict["detected_tier"] = detected_tier
        if rate_limits is not UNSET:
            field_dict["rate_limits"] = rate_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_credentials import LLMCredentials  # noqa: PLC0415
        from ..models.llm_execution_config_config_parameters import LLMExecutionConfigConfigParameters  # noqa: PLC0415
        from ..models.llm_execution_config_rate_limits_type_0 import LLMExecutionConfigRateLimitsType0  # noqa: PLC0415

        d = dict(src_dict)
        llm_id = d.pop("llm_id")

        llm_name = d.pop("llm_name")

        provider = d.pop("provider")

        model_id = d.pop("model_id")

        model_type = d.pop("model_type")

        credentials = LLMCredentials.from_dict(d.pop("credentials"))

        config_parameters = LLMExecutionConfigConfigParameters.from_dict(d.pop("config_parameters"))

        config_source = d.pop("config_source")

        def _parse_detected_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detected_tier = _parse_detected_tier(d.pop("detected_tier", UNSET))

        def _parse_rate_limits(data: object) -> LLMExecutionConfigRateLimitsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_limits_type_0 = LLMExecutionConfigRateLimitsType0.from_dict(data)

                return rate_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMExecutionConfigRateLimitsType0 | None | Unset, data)

        rate_limits = _parse_rate_limits(d.pop("rate_limits", UNSET))

        llm_execution_config = cls(
            llm_id=llm_id,
            llm_name=llm_name,
            provider=provider,
            model_id=model_id,
            model_type=model_type,
            credentials=credentials,
            config_parameters=config_parameters,
            config_source=config_source,
            detected_tier=detected_tier,
            rate_limits=rate_limits,
        )

        llm_execution_config.additional_properties = d
        return llm_execution_config

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
