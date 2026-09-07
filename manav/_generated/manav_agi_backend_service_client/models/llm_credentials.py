from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_credentials_additional_headers_type_0 import LLMCredentialsAdditionalHeadersType0


T = TypeVar("T", bound="LLMCredentials")


@_attrs_define
class LLMCredentials:
    """Decrypted LLM credentials — passed to orchestrator/agent_engine for LLM calls

    Attributes:
        api_key (None | str | Unset):
        endpoint_url (None | str | Unset):
        additional_headers (LLMCredentialsAdditionalHeadersType0 | None | Unset):
    """

    api_key: None | str | Unset = UNSET
    endpoint_url: None | str | Unset = UNSET
    additional_headers: LLMCredentialsAdditionalHeadersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.llm_credentials_additional_headers_type_0 import (
            LLMCredentialsAdditionalHeadersType0,  # noqa: PLC0415
        )

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        endpoint_url: None | str | Unset
        if isinstance(self.endpoint_url, Unset):
            endpoint_url = UNSET
        else:
            endpoint_url = self.endpoint_url

        additional_headers: dict[str, Any] | None | Unset
        if isinstance(self.additional_headers, Unset):
            additional_headers = UNSET
        elif isinstance(self.additional_headers, LLMCredentialsAdditionalHeadersType0):
            additional_headers = self.additional_headers.to_dict()
        else:
            additional_headers = self.additional_headers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url
        if additional_headers is not UNSET:
            field_dict["additional_headers"] = additional_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_credentials_additional_headers_type_0 import (
            LLMCredentialsAdditionalHeadersType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint_url = _parse_endpoint_url(d.pop("endpoint_url", UNSET))

        def _parse_additional_headers(data: object) -> LLMCredentialsAdditionalHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_headers_type_0 = LLMCredentialsAdditionalHeadersType0.from_dict(data)

                return additional_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMCredentialsAdditionalHeadersType0 | None | Unset, data)

        additional_headers = _parse_additional_headers(d.pop("additional_headers", UNSET))

        llm_credentials = cls(
            api_key=api_key,
            endpoint_url=endpoint_url,
            additional_headers=additional_headers,
        )

        llm_credentials.additional_properties = d
        return llm_credentials

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
