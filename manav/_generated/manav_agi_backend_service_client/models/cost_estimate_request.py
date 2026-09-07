from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimateRequest")


@_attrs_define
class CostEstimateRequest:
    """
    Attributes:
        dataset_id (None | Unset | UUID):
        scenario_ids (list[UUID] | None | Unset):
        eval_depth (int | Unset):  Default: 1.
    """

    dataset_id: None | Unset | UUID = UNSET
    scenario_ids: list[UUID] | None | Unset = UNSET
    eval_depth: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id: None | str | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        elif isinstance(self.dataset_id, UUID):
            dataset_id = str(self.dataset_id)
        else:
            dataset_id = self.dataset_id

        scenario_ids: list[str] | None | Unset
        if isinstance(self.scenario_ids, Unset):
            scenario_ids = UNSET
        elif isinstance(self.scenario_ids, list):
            scenario_ids = []
            for scenario_ids_type_0_item_data in self.scenario_ids:
                scenario_ids_type_0_item = str(scenario_ids_type_0_item_data)
                scenario_ids.append(scenario_ids_type_0_item)

        else:
            scenario_ids = self.scenario_ids

        eval_depth = self.eval_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if scenario_ids is not UNSET:
            field_dict["scenario_ids"] = scenario_ids
        if eval_depth is not UNSET:
            field_dict["eval_depth"] = eval_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_dataset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dataset_id_type_0 = UUID(data)

                return dataset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dataset_id = _parse_dataset_id(d.pop("dataset_id", UNSET))

        def _parse_scenario_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scenario_ids_type_0 = []
                _scenario_ids_type_0 = data
                for scenario_ids_type_0_item_data in _scenario_ids_type_0:
                    scenario_ids_type_0_item = UUID(scenario_ids_type_0_item_data)

                    scenario_ids_type_0.append(scenario_ids_type_0_item)

                return scenario_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        scenario_ids = _parse_scenario_ids(d.pop("scenario_ids", UNSET))

        eval_depth = d.pop("eval_depth", UNSET)

        cost_estimate_request = cls(
            dataset_id=dataset_id,
            scenario_ids=scenario_ids,
            eval_depth=eval_depth,
        )

        cost_estimate_request.additional_properties = d
        return cost_estimate_request

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
