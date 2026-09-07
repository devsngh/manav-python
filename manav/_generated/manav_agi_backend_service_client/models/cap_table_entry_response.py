from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cap_table_entry_response_metadata_type_0 import CapTableEntryResponseMetadataType0


T = TypeVar("T", bound="CapTableEntryResponse")


@_attrs_define
class CapTableEntryResponse:
    """
    Attributes:
        id (UUID):
        snapshot_id (UUID):
        shareholder_type (str):
        shareholder_investor_id (None | UUID):
        shareholder_employee_id (None | UUID):
        shareholder_user_id (None | UUID):
        shareholder_name_external (None | str):
        share_class (str):
        shares_held (int):
        ownership_pct (None | str):
        fully_diluted_pct (None | str):
        acquisition_round_id (None | UUID):
        acquired_at (datetime.date | None):
        cost_basis (None | str):
        cost_basis_currency_id (None | UUID):
        vesting_start_date (datetime.date | None):
        vesting_cliff_months (int | None):
        vesting_total_months (int | None):
        shares_vested (int | None):
        is_exercised (bool | None):
        created_at (datetime.datetime):
        metadata (CapTableEntryResponseMetadataType0 | None | Unset):
    """

    id: UUID
    snapshot_id: UUID
    shareholder_type: str
    shareholder_investor_id: None | UUID
    shareholder_employee_id: None | UUID
    shareholder_user_id: None | UUID
    shareholder_name_external: None | str
    share_class: str
    shares_held: int
    ownership_pct: None | str
    fully_diluted_pct: None | str
    acquisition_round_id: None | UUID
    acquired_at: datetime.date | None
    cost_basis: None | str
    cost_basis_currency_id: None | UUID
    vesting_start_date: datetime.date | None
    vesting_cliff_months: int | None
    vesting_total_months: int | None
    shares_vested: int | None
    is_exercised: bool | None
    created_at: datetime.datetime
    metadata: CapTableEntryResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cap_table_entry_response_metadata_type_0 import (
            CapTableEntryResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        snapshot_id = str(self.snapshot_id)

        shareholder_type = self.shareholder_type

        shareholder_investor_id: None | str
        if isinstance(self.shareholder_investor_id, UUID):
            shareholder_investor_id = str(self.shareholder_investor_id)
        else:
            shareholder_investor_id = self.shareholder_investor_id

        shareholder_employee_id: None | str
        if isinstance(self.shareholder_employee_id, UUID):
            shareholder_employee_id = str(self.shareholder_employee_id)
        else:
            shareholder_employee_id = self.shareholder_employee_id

        shareholder_user_id: None | str
        if isinstance(self.shareholder_user_id, UUID):
            shareholder_user_id = str(self.shareholder_user_id)
        else:
            shareholder_user_id = self.shareholder_user_id

        shareholder_name_external: None | str
        shareholder_name_external = self.shareholder_name_external

        share_class = self.share_class

        shares_held = self.shares_held

        ownership_pct: None | str
        ownership_pct = self.ownership_pct

        fully_diluted_pct: None | str
        fully_diluted_pct = self.fully_diluted_pct

        acquisition_round_id: None | str
        if isinstance(self.acquisition_round_id, UUID):
            acquisition_round_id = str(self.acquisition_round_id)
        else:
            acquisition_round_id = self.acquisition_round_id

        acquired_at: None | str
        if isinstance(self.acquired_at, datetime.date):
            acquired_at = self.acquired_at.isoformat()
        else:
            acquired_at = self.acquired_at

        cost_basis: None | str
        cost_basis = self.cost_basis

        cost_basis_currency_id: None | str
        if isinstance(self.cost_basis_currency_id, UUID):
            cost_basis_currency_id = str(self.cost_basis_currency_id)
        else:
            cost_basis_currency_id = self.cost_basis_currency_id

        vesting_start_date: None | str
        if isinstance(self.vesting_start_date, datetime.date):
            vesting_start_date = self.vesting_start_date.isoformat()
        else:
            vesting_start_date = self.vesting_start_date

        vesting_cliff_months: int | None
        vesting_cliff_months = self.vesting_cliff_months

        vesting_total_months: int | None
        vesting_total_months = self.vesting_total_months

        shares_vested: int | None
        shares_vested = self.shares_vested

        is_exercised: bool | None
        is_exercised = self.is_exercised

        created_at = self.created_at.isoformat()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CapTableEntryResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "snapshot_id": snapshot_id,
                "shareholder_type": shareholder_type,
                "shareholder_investor_id": shareholder_investor_id,
                "shareholder_employee_id": shareholder_employee_id,
                "shareholder_user_id": shareholder_user_id,
                "shareholder_name_external": shareholder_name_external,
                "share_class": share_class,
                "shares_held": shares_held,
                "ownership_pct": ownership_pct,
                "fully_diluted_pct": fully_diluted_pct,
                "acquisition_round_id": acquisition_round_id,
                "acquired_at": acquired_at,
                "cost_basis": cost_basis,
                "cost_basis_currency_id": cost_basis_currency_id,
                "vesting_start_date": vesting_start_date,
                "vesting_cliff_months": vesting_cliff_months,
                "vesting_total_months": vesting_total_months,
                "shares_vested": shares_vested,
                "is_exercised": is_exercised,
                "created_at": created_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cap_table_entry_response_metadata_type_0 import (
            CapTableEntryResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        snapshot_id = UUID(d.pop("snapshot_id"))

        shareholder_type = d.pop("shareholder_type")

        def _parse_shareholder_investor_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shareholder_investor_id_type_0 = UUID(data)

                return shareholder_investor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        shareholder_investor_id = _parse_shareholder_investor_id(d.pop("shareholder_investor_id"))

        def _parse_shareholder_employee_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shareholder_employee_id_type_0 = UUID(data)

                return shareholder_employee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        shareholder_employee_id = _parse_shareholder_employee_id(d.pop("shareholder_employee_id"))

        def _parse_shareholder_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shareholder_user_id_type_0 = UUID(data)

                return shareholder_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        shareholder_user_id = _parse_shareholder_user_id(d.pop("shareholder_user_id"))

        def _parse_shareholder_name_external(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        shareholder_name_external = _parse_shareholder_name_external(d.pop("shareholder_name_external"))

        share_class = d.pop("share_class")

        shares_held = d.pop("shares_held")

        def _parse_ownership_pct(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ownership_pct = _parse_ownership_pct(d.pop("ownership_pct"))

        def _parse_fully_diluted_pct(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fully_diluted_pct = _parse_fully_diluted_pct(d.pop("fully_diluted_pct"))

        def _parse_acquisition_round_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquisition_round_id_type_0 = UUID(data)

                return acquisition_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        acquisition_round_id = _parse_acquisition_round_id(d.pop("acquisition_round_id"))

        def _parse_acquired_at(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquired_at_type_0 = datetime.date.fromisoformat(data)

                return acquired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        acquired_at = _parse_acquired_at(d.pop("acquired_at"))

        def _parse_cost_basis(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cost_basis = _parse_cost_basis(d.pop("cost_basis"))

        def _parse_cost_basis_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cost_basis_currency_id_type_0 = UUID(data)

                return cost_basis_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        cost_basis_currency_id = _parse_cost_basis_currency_id(d.pop("cost_basis_currency_id"))

        def _parse_vesting_start_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vesting_start_date_type_0 = datetime.date.fromisoformat(data)

                return vesting_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        vesting_start_date = _parse_vesting_start_date(d.pop("vesting_start_date"))

        def _parse_vesting_cliff_months(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        vesting_cliff_months = _parse_vesting_cliff_months(d.pop("vesting_cliff_months"))

        def _parse_vesting_total_months(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        vesting_total_months = _parse_vesting_total_months(d.pop("vesting_total_months"))

        def _parse_shares_vested(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        shares_vested = _parse_shares_vested(d.pop("shares_vested"))

        def _parse_is_exercised(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_exercised = _parse_is_exercised(d.pop("is_exercised"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_metadata(data: object) -> CapTableEntryResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CapTableEntryResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapTableEntryResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        cap_table_entry_response = cls(
            id=id,
            snapshot_id=snapshot_id,
            shareholder_type=shareholder_type,
            shareholder_investor_id=shareholder_investor_id,
            shareholder_employee_id=shareholder_employee_id,
            shareholder_user_id=shareholder_user_id,
            shareholder_name_external=shareholder_name_external,
            share_class=share_class,
            shares_held=shares_held,
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
            created_at=created_at,
            metadata=metadata,
        )

        cap_table_entry_response.additional_properties = d
        return cap_table_entry_response

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
