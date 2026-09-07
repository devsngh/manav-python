from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cap_table_entry_create_metadata_type_0 import CapTableEntryCreateMetadataType0


T = TypeVar("T", bound="CapTableEntryCreate")


@_attrs_define
class CapTableEntryCreate:
    """
    Attributes:
        shareholder_type (str): investor / employee / founder / advisor / option_pool / other
        share_class (str):
        shares_held (int):
        shareholder_investor_id (None | Unset | UUID):
        shareholder_employee_id (None | Unset | UUID):
        shareholder_user_id (None | Unset | UUID):
        shareholder_name_external (None | str | Unset):
        ownership_pct (float | None | str | Unset):
        fully_diluted_pct (float | None | str | Unset):
        acquisition_round_id (None | Unset | UUID):
        acquired_at (datetime.date | None | Unset):
        cost_basis (float | None | str | Unset):
        cost_basis_currency_id (None | Unset | UUID):
        vesting_start_date (datetime.date | None | Unset):
        vesting_cliff_months (int | None | Unset):
        vesting_total_months (int | None | Unset):
        shares_vested (int | None | Unset):
        is_exercised (bool | None | Unset):
        metadata (CapTableEntryCreateMetadataType0 | None | Unset):
    """

    shareholder_type: str
    share_class: str
    shares_held: int
    shareholder_investor_id: None | Unset | UUID = UNSET
    shareholder_employee_id: None | Unset | UUID = UNSET
    shareholder_user_id: None | Unset | UUID = UNSET
    shareholder_name_external: None | str | Unset = UNSET
    ownership_pct: float | None | str | Unset = UNSET
    fully_diluted_pct: float | None | str | Unset = UNSET
    acquisition_round_id: None | Unset | UUID = UNSET
    acquired_at: datetime.date | None | Unset = UNSET
    cost_basis: float | None | str | Unset = UNSET
    cost_basis_currency_id: None | Unset | UUID = UNSET
    vesting_start_date: datetime.date | None | Unset = UNSET
    vesting_cliff_months: int | None | Unset = UNSET
    vesting_total_months: int | None | Unset = UNSET
    shares_vested: int | None | Unset = UNSET
    is_exercised: bool | None | Unset = UNSET
    metadata: CapTableEntryCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cap_table_entry_create_metadata_type_0 import CapTableEntryCreateMetadataType0  # noqa: PLC0415

        shareholder_type = self.shareholder_type

        share_class = self.share_class

        shares_held = self.shares_held

        shareholder_investor_id: None | str | Unset
        if isinstance(self.shareholder_investor_id, Unset):
            shareholder_investor_id = UNSET
        elif isinstance(self.shareholder_investor_id, UUID):
            shareholder_investor_id = str(self.shareholder_investor_id)
        else:
            shareholder_investor_id = self.shareholder_investor_id

        shareholder_employee_id: None | str | Unset
        if isinstance(self.shareholder_employee_id, Unset):
            shareholder_employee_id = UNSET
        elif isinstance(self.shareholder_employee_id, UUID):
            shareholder_employee_id = str(self.shareholder_employee_id)
        else:
            shareholder_employee_id = self.shareholder_employee_id

        shareholder_user_id: None | str | Unset
        if isinstance(self.shareholder_user_id, Unset):
            shareholder_user_id = UNSET
        elif isinstance(self.shareholder_user_id, UUID):
            shareholder_user_id = str(self.shareholder_user_id)
        else:
            shareholder_user_id = self.shareholder_user_id

        shareholder_name_external: None | str | Unset
        if isinstance(self.shareholder_name_external, Unset):
            shareholder_name_external = UNSET
        else:
            shareholder_name_external = self.shareholder_name_external

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

        acquisition_round_id: None | str | Unset
        if isinstance(self.acquisition_round_id, Unset):
            acquisition_round_id = UNSET
        elif isinstance(self.acquisition_round_id, UUID):
            acquisition_round_id = str(self.acquisition_round_id)
        else:
            acquisition_round_id = self.acquisition_round_id

        acquired_at: None | str | Unset
        if isinstance(self.acquired_at, Unset):
            acquired_at = UNSET
        elif isinstance(self.acquired_at, datetime.date):
            acquired_at = self.acquired_at.isoformat()
        else:
            acquired_at = self.acquired_at

        cost_basis: float | None | str | Unset
        if isinstance(self.cost_basis, Unset):
            cost_basis = UNSET
        else:
            cost_basis = self.cost_basis

        cost_basis_currency_id: None | str | Unset
        if isinstance(self.cost_basis_currency_id, Unset):
            cost_basis_currency_id = UNSET
        elif isinstance(self.cost_basis_currency_id, UUID):
            cost_basis_currency_id = str(self.cost_basis_currency_id)
        else:
            cost_basis_currency_id = self.cost_basis_currency_id

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
        elif isinstance(self.metadata, CapTableEntryCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shareholder_type": shareholder_type,
                "share_class": share_class,
                "shares_held": shares_held,
            }
        )
        if shareholder_investor_id is not UNSET:
            field_dict["shareholder_investor_id"] = shareholder_investor_id
        if shareholder_employee_id is not UNSET:
            field_dict["shareholder_employee_id"] = shareholder_employee_id
        if shareholder_user_id is not UNSET:
            field_dict["shareholder_user_id"] = shareholder_user_id
        if shareholder_name_external is not UNSET:
            field_dict["shareholder_name_external"] = shareholder_name_external
        if ownership_pct is not UNSET:
            field_dict["ownership_pct"] = ownership_pct
        if fully_diluted_pct is not UNSET:
            field_dict["fully_diluted_pct"] = fully_diluted_pct
        if acquisition_round_id is not UNSET:
            field_dict["acquisition_round_id"] = acquisition_round_id
        if acquired_at is not UNSET:
            field_dict["acquired_at"] = acquired_at
        if cost_basis is not UNSET:
            field_dict["cost_basis"] = cost_basis
        if cost_basis_currency_id is not UNSET:
            field_dict["cost_basis_currency_id"] = cost_basis_currency_id
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
        from ..models.cap_table_entry_create_metadata_type_0 import CapTableEntryCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        shareholder_type = d.pop("shareholder_type")

        share_class = d.pop("share_class")

        shares_held = d.pop("shares_held")

        def _parse_shareholder_investor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shareholder_investor_id_type_0 = UUID(data)

                return shareholder_investor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        shareholder_investor_id = _parse_shareholder_investor_id(d.pop("shareholder_investor_id", UNSET))

        def _parse_shareholder_employee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shareholder_employee_id_type_0 = UUID(data)

                return shareholder_employee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        shareholder_employee_id = _parse_shareholder_employee_id(d.pop("shareholder_employee_id", UNSET))

        def _parse_shareholder_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shareholder_user_id_type_0 = UUID(data)

                return shareholder_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        shareholder_user_id = _parse_shareholder_user_id(d.pop("shareholder_user_id", UNSET))

        def _parse_shareholder_name_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shareholder_name_external = _parse_shareholder_name_external(d.pop("shareholder_name_external", UNSET))

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

        def _parse_acquisition_round_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquisition_round_id_type_0 = UUID(data)

                return acquisition_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acquisition_round_id = _parse_acquisition_round_id(d.pop("acquisition_round_id", UNSET))

        def _parse_acquired_at(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquired_at_type_0 = datetime.date.fromisoformat(data)

                return acquired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        acquired_at = _parse_acquired_at(d.pop("acquired_at", UNSET))

        def _parse_cost_basis(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        cost_basis = _parse_cost_basis(d.pop("cost_basis", UNSET))

        def _parse_cost_basis_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cost_basis_currency_id_type_0 = UUID(data)

                return cost_basis_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cost_basis_currency_id = _parse_cost_basis_currency_id(d.pop("cost_basis_currency_id", UNSET))

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

        def _parse_metadata(data: object) -> CapTableEntryCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CapTableEntryCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapTableEntryCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        cap_table_entry_create = cls(
            shareholder_type=shareholder_type,
            share_class=share_class,
            shares_held=shares_held,
            shareholder_investor_id=shareholder_investor_id,
            shareholder_employee_id=shareholder_employee_id,
            shareholder_user_id=shareholder_user_id,
            shareholder_name_external=shareholder_name_external,
            ownership_pct=ownership_pct,
            fully_diluted_pct=fully_diluted_pct,
            acquisition_round_id=acquisition_round_id,
            acquired_at=acquired_at,
            cost_basis=cost_basis,
            cost_basis_currency_id=cost_basis_currency_id,
            vesting_start_date=vesting_start_date,
            vesting_cliff_months=vesting_cliff_months,
            vesting_total_months=vesting_total_months,
            shares_vested=shares_vested,
            is_exercised=is_exercised,
            metadata=metadata,
        )

        cap_table_entry_create.additional_properties = d
        return cap_table_entry_create

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
