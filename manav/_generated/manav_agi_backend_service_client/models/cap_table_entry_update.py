from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cap_table_entry_update_metadata_type_0 import CapTableEntryUpdateMetadataType0


T = TypeVar("T", bound="CapTableEntryUpdate")


@_attrs_define
class CapTableEntryUpdate:
    """
    Attributes:
        shares_held (int | None | Unset):
        ownership_pct (float | None | str | Unset):
        fully_diluted_pct (float | None | str | Unset):
        cost_basis (float | None | str | Unset):
        vesting_start_date (datetime.date | None | Unset):
        vesting_cliff_months (int | None | Unset):
        vesting_total_months (int | None | Unset):
        shares_vested (int | None | Unset):
        is_exercised (bool | None | Unset):
        metadata (CapTableEntryUpdateMetadataType0 | None | Unset):
    """

    shares_held: int | None | Unset = UNSET
    ownership_pct: float | None | str | Unset = UNSET
    fully_diluted_pct: float | None | str | Unset = UNSET
    cost_basis: float | None | str | Unset = UNSET
    vesting_start_date: datetime.date | None | Unset = UNSET
    vesting_cliff_months: int | None | Unset = UNSET
    vesting_total_months: int | None | Unset = UNSET
    shares_vested: int | None | Unset = UNSET
    is_exercised: bool | None | Unset = UNSET
    metadata: CapTableEntryUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cap_table_entry_update_metadata_type_0 import CapTableEntryUpdateMetadataType0  # noqa: PLC0415

        shares_held: int | None | Unset
        if isinstance(self.shares_held, Unset):
            shares_held = UNSET
        else:
            shares_held = self.shares_held

        ownership_pct: float | None | str | Unset
        if isinstance(self.ownership_pct, Unset):
            ownership_pct = UNSET
        else:
            ownership_pct = self.ownership_pct

        fully_diluted_pct: float | None | str | Unset
        if isinstance(self.fully_diluted_pct, Unset):
            fully_diluted_pct = UNSET
        else:
            fully_diluted_pct = self.fully_diluted_pct

        cost_basis: float | None | str | Unset
        if isinstance(self.cost_basis, Unset):
            cost_basis = UNSET
        else:
            cost_basis = self.cost_basis

        vesting_start_date: None | str | Unset
        if isinstance(self.vesting_start_date, Unset):
            vesting_start_date = UNSET
        elif isinstance(self.vesting_start_date, datetime.date):
            vesting_start_date = self.vesting_start_date.isoformat()
        else:
            vesting_start_date = self.vesting_start_date

        vesting_cliff_months: int | None | Unset
        if isinstance(self.vesting_cliff_months, Unset):
            vesting_cliff_months = UNSET
        else:
            vesting_cliff_months = self.vesting_cliff_months

        vesting_total_months: int | None | Unset
        if isinstance(self.vesting_total_months, Unset):
            vesting_total_months = UNSET
        else:
            vesting_total_months = self.vesting_total_months

        shares_vested: int | None | Unset
        if isinstance(self.shares_vested, Unset):
            shares_vested = UNSET
        else:
            shares_vested = self.shares_vested

        is_exercised: bool | None | Unset
        if isinstance(self.is_exercised, Unset):
            is_exercised = UNSET
        else:
            is_exercised = self.is_exercised

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CapTableEntryUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shares_held is not UNSET:
            field_dict["shares_held"] = shares_held
        if ownership_pct is not UNSET:
            field_dict["ownership_pct"] = ownership_pct
        if fully_diluted_pct is not UNSET:
            field_dict["fully_diluted_pct"] = fully_diluted_pct
        if cost_basis is not UNSET:
            field_dict["cost_basis"] = cost_basis
        if vesting_start_date is not UNSET:
            field_dict["vesting_start_date"] = vesting_start_date
        if vesting_cliff_months is not UNSET:
            field_dict["vesting_cliff_months"] = vesting_cliff_months
        if vesting_total_months is not UNSET:
            field_dict["vesting_total_months"] = vesting_total_months
        if shares_vested is not UNSET:
            field_dict["shares_vested"] = shares_vested
        if is_exercised is not UNSET:
            field_dict["is_exercised"] = is_exercised
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cap_table_entry_update_metadata_type_0 import CapTableEntryUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_shares_held(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shares_held = _parse_shares_held(d.pop("shares_held", UNSET))

        def _parse_ownership_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        ownership_pct = _parse_ownership_pct(d.pop("ownership_pct", UNSET))

        def _parse_fully_diluted_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        fully_diluted_pct = _parse_fully_diluted_pct(d.pop("fully_diluted_pct", UNSET))

        def _parse_cost_basis(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        cost_basis = _parse_cost_basis(d.pop("cost_basis", UNSET))

        def _parse_vesting_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vesting_start_date_type_0 = datetime.date.fromisoformat(data)

                return vesting_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        vesting_start_date = _parse_vesting_start_date(d.pop("vesting_start_date", UNSET))

        def _parse_vesting_cliff_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vesting_cliff_months = _parse_vesting_cliff_months(d.pop("vesting_cliff_months", UNSET))

        def _parse_vesting_total_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vesting_total_months = _parse_vesting_total_months(d.pop("vesting_total_months", UNSET))

        def _parse_shares_vested(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shares_vested = _parse_shares_vested(d.pop("shares_vested", UNSET))

        def _parse_is_exercised(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_exercised = _parse_is_exercised(d.pop("is_exercised", UNSET))

        def _parse_metadata(data: object) -> CapTableEntryUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CapTableEntryUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapTableEntryUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        cap_table_entry_update = cls(
            shares_held=shares_held,
            ownership_pct=ownership_pct,
            fully_diluted_pct=fully_diluted_pct,
            cost_basis=cost_basis,
            vesting_start_date=vesting_start_date,
            vesting_cliff_months=vesting_cliff_months,
            vesting_total_months=vesting_total_months,
            shares_vested=shares_vested,
            is_exercised=is_exercised,
            metadata=metadata,
        )

        cap_table_entry_update.additional_properties = d
        return cap_table_entry_update

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
