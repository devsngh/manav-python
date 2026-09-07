from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dependency_response import DependencyResponse


T = TypeVar("T", bound="TaskDependencyList")


@_attrs_define
class TaskDependencyList:
    """
    Attributes:
        dependencies (list[DependencyResponse] | Unset):
        dependents (list[DependencyResponse] | Unset):
    """

    dependencies: list[DependencyResponse] | Unset = UNSET
    dependents: list[DependencyResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dependencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        dependents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dependents, Unset):
            dependents = []
            for dependents_item_data in self.dependents:
                dependents_item = dependents_item_data.to_dict()
                dependents.append(dependents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if dependents is not UNSET:
            field_dict["dependents"] = dependents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dependency_response import DependencyResponse  # noqa: PLC0415

        d = dict(src_dict)
        _dependencies = d.pop("dependencies", UNSET)
        dependencies: list[DependencyResponse] | Unset = UNSET
        if _dependencies is not UNSET:
            dependencies = []
            for dependencies_item_data in _dependencies:
                dependencies_item = DependencyResponse.from_dict(dependencies_item_data)

                dependencies.append(dependencies_item)

        _dependents = d.pop("dependents", UNSET)
        dependents: list[DependencyResponse] | Unset = UNSET
        if _dependents is not UNSET:
            dependents = []
            for dependents_item_data in _dependents:
                dependents_item = DependencyResponse.from_dict(dependents_item_data)

                dependents.append(dependents_item)

        task_dependency_list = cls(
            dependencies=dependencies,
            dependents=dependents,
        )

        task_dependency_list.additional_properties = d
        return task_dependency_list

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
