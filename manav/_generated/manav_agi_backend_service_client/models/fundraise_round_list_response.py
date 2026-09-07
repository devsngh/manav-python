from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fundraise_round_response import FundraiseRoundResponse


T = TypeVar("T", bound="FundraiseRoundListResponse")


@_attrs_define
class FundraiseRoundListResponse:
    """
    Attributes:
        rounds (list[FundraiseRoundResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    rounds: list[FundraiseRoundResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rounds": rounds,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fundraise_round_response import FundraiseRoundResponse  # noqa: PLC0415

        d = dict(src_dict)
        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = FundraiseRoundResponse.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        fundraise_round_list_response = cls(
            rounds=rounds,
            total=total,
            page=page,
            page_size=page_size,
        )

        fundraise_round_list_response.additional_properties = d
        return fundraise_round_list_response

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
