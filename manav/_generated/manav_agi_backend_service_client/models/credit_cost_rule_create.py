from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_cost_rule_create_metadata_type_0 import CreditCostRuleCreateMetadataType0


T = TypeVar("T", bound="CreditCostRuleCreate")


@_attrs_define
class CreditCostRuleCreate:
    """
    Attributes:
        metric_key (str):
        metric_name (str):
        credits_per_unit (int):
        unit_label (str):
        model_id (None | str | Unset):
        unit_quantity (int | Unset):  Default: 1.
        is_active (bool | Unset):  Default: True.
        metadata (CreditCostRuleCreateMetadataType0 | None | Unset):
    """

    metric_key: str
    metric_name: str
    credits_per_unit: int
    unit_label: str
    model_id: None | str | Unset = UNSET
    unit_quantity: int | Unset = 1
    is_active: bool | Unset = True
    metadata: CreditCostRuleCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credit_cost_rule_create_metadata_type_0 import CreditCostRuleCreateMetadataType0  # noqa: PLC0415

        metric_key = self.metric_key

        metric_name = self.metric_name

        credits_per_unit = self.credits_per_unit

        unit_label = self.unit_label

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        unit_quantity = self.unit_quantity

        is_active = self.is_active

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreditCostRuleCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric_key": metric_key,
                "metric_name": metric_name,
                "credits_per_unit": credits_per_unit,
                "unit_label": unit_label,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if unit_quantity is not UNSET:
            field_dict["unit_quantity"] = unit_quantity
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_cost_rule_create_metadata_type_0 import CreditCostRuleCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        metric_key = d.pop("metric_key")

        metric_name = d.pop("metric_name")

        credits_per_unit = d.pop("credits_per_unit")

        unit_label = d.pop("unit_label")

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        unit_quantity = d.pop("unit_quantity", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_metadata(data: object) -> CreditCostRuleCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreditCostRuleCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreditCostRuleCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        credit_cost_rule_create = cls(
            metric_key=metric_key,
            metric_name=metric_name,
            credits_per_unit=credits_per_unit,
            unit_label=unit_label,
            model_id=model_id,
            unit_quantity=unit_quantity,
            is_active=is_active,
            metadata=metadata,
        )

        credit_cost_rule_create.additional_properties = d
        return credit_cost_rule_create

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
