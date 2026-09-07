from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.observer_finding_response import ObserverFindingResponse


T = TypeVar("T", bound="ObserverFindingListResponse")


@_attrs_define
class ObserverFindingListResponse:
    """
    Attributes:
        findings (list[ObserverFindingResponse]):
        total (int):
        page (int):
        page_size (int):
        has_more (bool):
    """

    findings: list[ObserverFindingResponse]
    total: int
    page: int
    page_size: int
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "findings": findings,
                "total": total,
                "page": page,
                "page_size": page_size,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observer_finding_response import ObserverFindingResponse  # noqa: PLC0415

        d = dict(src_dict)
        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = ObserverFindingResponse.from_dict(findings_item_data)

            findings.append(findings_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        has_more = d.pop("has_more")

        observer_finding_list_response = cls(
            findings=findings,
            total=total,
            page=page,
            page_size=page_size,
            has_more=has_more,
        )

        observer_finding_list_response.additional_properties = d
        return observer_finding_list_response

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
