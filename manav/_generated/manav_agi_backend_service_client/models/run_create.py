from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunCreate")


@_attrs_define
class RunCreate:
    """
    Attributes:
        name (None | str | Unset):
        scenario_ids (list[UUID] | None | Unset):
        category (None | str | Unset):
        tags (list[str] | None | Unset):
        dataset_id (None | Unset | UUID):
        eval_depth (int | None | Unset):
        judge_deepagent_config_id (None | Unset | UUID):
    """

    name: None | str | Unset = UNSET
    scenario_ids: list[UUID] | None | Unset = UNSET
    category: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    dataset_id: None | Unset | UUID = UNSET
    eval_depth: int | None | Unset = UNSET
    judge_deepagent_config_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        dataset_id: None | str | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        elif isinstance(self.dataset_id, UUID):
            dataset_id = str(self.dataset_id)
        else:
            dataset_id = self.dataset_id

        eval_depth: int | None | Unset
        if isinstance(self.eval_depth, Unset):
            eval_depth = UNSET
        else:
            eval_depth = self.eval_depth

        judge_deepagent_config_id: None | str | Unset
        if isinstance(self.judge_deepagent_config_id, Unset):
            judge_deepagent_config_id = UNSET
        elif isinstance(self.judge_deepagent_config_id, UUID):
            judge_deepagent_config_id = str(self.judge_deepagent_config_id)
        else:
            judge_deepagent_config_id = self.judge_deepagent_config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if scenario_ids is not UNSET:
            field_dict["scenario_ids"] = scenario_ids
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if eval_depth is not UNSET:
            field_dict["eval_depth"] = eval_depth
        if judge_deepagent_config_id is not UNSET:
            field_dict["judge_deepagent_config_id"] = judge_deepagent_config_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

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

        def _parse_eval_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        eval_depth = _parse_eval_depth(d.pop("eval_depth", UNSET))

        def _parse_judge_deepagent_config_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                judge_deepagent_config_id_type_0 = UUID(data)

                return judge_deepagent_config_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        judge_deepagent_config_id = _parse_judge_deepagent_config_id(d.pop("judge_deepagent_config_id", UNSET))

        run_create = cls(
            name=name,
            scenario_ids=scenario_ids,
            category=category,
            tags=tags,
            dataset_id=dataset_id,
            eval_depth=eval_depth,
            judge_deepagent_config_id=judge_deepagent_config_id,
        )

        run_create.additional_properties = d
        return run_create

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
