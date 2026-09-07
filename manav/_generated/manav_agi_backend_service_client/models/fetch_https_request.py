from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_https_request_headers_type_0 import FetchHttpsRequestHeadersType0


T = TypeVar("T", bound="FetchHttpsRequest")


@_attrs_define
class FetchHttpsRequest:
    """
    Attributes:
        url (str):
        headers (FetchHttpsRequestHeadersType0 | None | Unset): Optional headers (e.g. {'Authorization': 'Bearer ...'})
        connection_id (None | str | Unset): Optional connection — if provided, decrypted bearer_token is added as
            Authorization
    """

    url: str
    headers: FetchHttpsRequestHeadersType0 | None | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fetch_https_request_headers_type_0 import FetchHttpsRequestHeadersType0  # noqa: PLC0415

        url = self.url

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, FetchHttpsRequestHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_https_request_headers_type_0 import FetchHttpsRequestHeadersType0  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")

        def _parse_headers(data: object) -> FetchHttpsRequestHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = FetchHttpsRequestHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FetchHttpsRequestHeadersType0 | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connection_id", UNSET))

        fetch_https_request = cls(
            url=url,
            headers=headers,
            connection_id=connection_id,
        )

        fetch_https_request.additional_properties = d
        return fetch_https_request

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
