from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competitor_response import CompetitorResponse


T = TypeVar("T", bound="CompetitorListResponse")


@_attrs_define
class CompetitorListResponse:
    """
    Attributes:
        competitors (list[CompetitorResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    competitors: list[CompetitorResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        competitors = []
        for competitors_item_data in self.competitors:
            competitors_item = competitors_item_data.to_dict()
            competitors.append(competitors_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "competitors": competitors,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competitor_response import CompetitorResponse  # noqa: PLC0415

        d = dict(src_dict)
        competitors = []
        _competitors = d.pop("competitors")
        for competitors_item_data in _competitors:
            competitors_item = CompetitorResponse.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        competitor_list_response = cls(
            competitors=competitors,
            total=total,
            page=page,
            page_size=page_size,
        )

        competitor_list_response.additional_properties = d
        return competitor_list_response

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
