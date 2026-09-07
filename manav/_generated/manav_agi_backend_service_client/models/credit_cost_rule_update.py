from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_cost_rule_update_metadata_type_0 import CreditCostRuleUpdateMetadataType0


T = TypeVar("T", bound="CreditCostRuleUpdate")


@_attrs_define
class CreditCostRuleUpdate:
    """
    Attributes:
        metric_key (None | str | Unset):
        metric_name (None | str | Unset):
        model_id (None | str | Unset):
        credits_per_unit (int | None | Unset):
        unit_label (None | str | Unset):
        unit_quantity (int | None | Unset):
        is_active (bool | None | Unset):
        metadata (CreditCostRuleUpdateMetadataType0 | None | Unset):
    """

    metric_key: None | str | Unset = UNSET
    metric_name: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    credits_per_unit: int | None | Unset = UNSET
    unit_label: None | str | Unset = UNSET
    unit_quantity: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    metadata: CreditCostRuleUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credit_cost_rule_update_metadata_type_0 import CreditCostRuleUpdateMetadataType0  # noqa: PLC0415

        metric_key: None | str | Unset
        if isinstance(self.metric_key, Unset):
            metric_key = UNSET
        else:
            metric_key = self.metric_key

        metric_name: None | str | Unset
        if isinstance(self.metric_name, Unset):
            metric_name = UNSET
        else:
            metric_name = self.metric_name

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        credits_per_unit: int | None | Unset
        if isinstance(self.credits_per_unit, Unset):
            credits_per_unit = UNSET
        else:
            credits_per_unit = self.credits_per_unit

        unit_label: None | str | Unset
        if isinstance(self.unit_label, Unset):
            unit_label = UNSET
        else:
            unit_label = self.unit_label

        unit_quantity: int | None | Unset
        if isinstance(self.unit_quantity, Unset):
            unit_quantity = UNSET
        else:
            unit_quantity = self.unit_quantity

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreditCostRuleUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric_key is not UNSET:
            field_dict["metric_key"] = metric_key
        if metric_name is not UNSET:
            field_dict["metric_name"] = metric_name
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if credits_per_unit is not UNSET:
            field_dict["credits_per_unit"] = credits_per_unit
        if unit_label is not UNSET:
            field_dict["unit_label"] = unit_label
        if unit_quantity is not UNSET:
            field_dict["unit_quantity"] = unit_quantity
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_cost_rule_update_metadata_type_0 import CreditCostRuleUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metric_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_key = _parse_metric_key(d.pop("metric_key", UNSET))

        def _parse_metric_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_name = _parse_metric_name(d.pop("metric_name", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_credits_per_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credits_per_unit = _parse_credits_per_unit(d.pop("credits_per_unit", UNSET))

        def _parse_unit_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_label = _parse_unit_label(d.pop("unit_label", UNSET))

        def _parse_unit_quantity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unit_quantity = _parse_unit_quantity(d.pop("unit_quantity", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_metadata(data: object) -> CreditCostRuleUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreditCostRuleUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreditCostRuleUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        credit_cost_rule_update = cls(
            metric_key=metric_key,
            metric_name=metric_name,
            model_id=model_id,
            credits_per_unit=credits_per_unit,
            unit_label=unit_label,
            unit_quantity=unit_quantity,
            is_active=is_active,
            metadata=metadata,
        )

        credit_cost_rule_update.additional_properties = d
        return credit_cost_rule_update

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
