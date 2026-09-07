from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.endpoint_metrics import EndpointMetrics


T = TypeVar("T", bound="ApiActivityResponse")


@_attrs_define
class ApiActivityResponse:
    """
    Attributes:
        endpoints (list[EndpointMetrics]):
        total_requests (int):
        total_errors (int):
    """

    endpoints: list[EndpointMetrics]
    total_requests: int
    total_errors: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoints = []
        for endpoints_item_data in self.endpoints:
            endpoints_item = endpoints_item_data.to_dict()
            endpoints.append(endpoints_item)

        total_requests = self.total_requests

        total_errors = self.total_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoints": endpoints,
                "total_requests": total_requests,
                "total_errors": total_errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_metrics import EndpointMetrics  # noqa: PLC0415

        d = dict(src_dict)
        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in _endpoints:
            endpoints_item = EndpointMetrics.from_dict(endpoints_item_data)

            endpoints.append(endpoints_item)

        total_requests = d.pop("total_requests")

        total_errors = d.pop("total_errors")

        api_activity_response = cls(
            endpoints=endpoints,
            total_requests=total_requests,
            total_errors=total_errors,
        )

        api_activity_response.additional_properties = d
        return api_activity_response

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
