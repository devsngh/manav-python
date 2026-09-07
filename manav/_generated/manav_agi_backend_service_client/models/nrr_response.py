from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NrrResponse")


@_attrs_define
class NrrResponse:
    """GET /api/analytics/billing/nrr — Net Revenue Retention %.
    nrr_pct = (start + expansion - downgrade - churn) / start × 100.

        Attributes:
            start_mrr_usd (float):
            expansion_usd (float):
            downgrade_usd (float):
            churn_usd (float):
            window_months (int):
            nrr_pct (float | None | Unset):
    """

    start_mrr_usd: float
    expansion_usd: float
    downgrade_usd: float
    churn_usd: float
    window_months: int
    nrr_pct: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_mrr_usd = self.start_mrr_usd

        expansion_usd = self.expansion_usd

        downgrade_usd = self.downgrade_usd

        churn_usd = self.churn_usd

        window_months = self.window_months

        nrr_pct: float | None | Unset
        if isinstance(self.nrr_pct, Unset):
            nrr_pct = UNSET
        else:
            nrr_pct = self.nrr_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_mrr_usd": start_mrr_usd,
                "expansion_usd": expansion_usd,
                "downgrade_usd": downgrade_usd,
                "churn_usd": churn_usd,
                "window_months": window_months,
            }
        )
        if nrr_pct is not UNSET:
            field_dict["nrr_pct"] = nrr_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_mrr_usd = d.pop("start_mrr_usd")

        expansion_usd = d.pop("expansion_usd")

        downgrade_usd = d.pop("downgrade_usd")

        churn_usd = d.pop("churn_usd")

        window_months = d.pop("window_months")

        def _parse_nrr_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nrr_pct = _parse_nrr_pct(d.pop("nrr_pct", UNSET))

        nrr_response = cls(
            start_mrr_usd=start_mrr_usd,
            expansion_usd=expansion_usd,
            downgrade_usd=downgrade_usd,
            churn_usd=churn_usd,
            window_months=window_months,
            nrr_pct=nrr_pct,
        )

        nrr_response.additional_properties = d
        return nrr_response

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
