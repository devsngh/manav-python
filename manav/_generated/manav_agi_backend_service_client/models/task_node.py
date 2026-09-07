from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_node_input_data_type_0 import TaskNodeInputDataType0


T = TypeVar("T", bound="TaskNode")


@_attrs_define
class TaskNode:
    """
    Attributes:
        title (str):
        description (None | str | Unset):
        assign_to (None | str | Unset):
        assign_to_bot_id (None | str | Unset):
        priority (str | Unset):  Default: 'normal'.
        input_data (None | TaskNodeInputDataType0 | Unset):
        parallel (bool | Unset):  Default: True.
        depends_on (list[str] | None | Unset):
    """

    title: str
    description: None | str | Unset = UNSET
    assign_to: None | str | Unset = UNSET
    assign_to_bot_id: None | str | Unset = UNSET
    priority: str | Unset = "normal"
    input_data: None | TaskNodeInputDataType0 | Unset = UNSET
    parallel: bool | Unset = True
    depends_on: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_node_input_data_type_0 import TaskNodeInputDataType0  # noqa: PLC0415

        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        assign_to: None | str | Unset
        if isinstance(self.assign_to, Unset):
            assign_to = UNSET
        else:
            assign_to = self.assign_to

        assign_to_bot_id: None | str | Unset
        if isinstance(self.assign_to_bot_id, Unset):
            assign_to_bot_id = UNSET
        else:
            assign_to_bot_id = self.assign_to_bot_id

        priority = self.priority

        input_data: dict[str, Any] | None | Unset
        if isinstance(self.input_data, Unset):
            input_data = UNSET
        elif isinstance(self.input_data, TaskNodeInputDataType0):
            input_data = self.input_data.to_dict()
        else:
            input_data = self.input_data

        parallel = self.parallel

        depends_on: list[str] | None | Unset
        if isinstance(self.depends_on, Unset):
            depends_on = UNSET
        elif isinstance(self.depends_on, list):
            depends_on = self.depends_on

        else:
            depends_on = self.depends_on

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if assign_to is not UNSET:
            field_dict["assign_to"] = assign_to
        if assign_to_bot_id is not UNSET:
            field_dict["assign_to_bot_id"] = assign_to_bot_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if input_data is not UNSET:
            field_dict["input_data"] = input_data
        if parallel is not UNSET:
            field_dict["parallel"] = parallel
        if depends_on is not UNSET:
            field_dict["depends_on"] = depends_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_node_input_data_type_0 import TaskNodeInputDataType0  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_assign_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to = _parse_assign_to(d.pop("assign_to", UNSET))

        def _parse_assign_to_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_bot_id = _parse_assign_to_bot_id(d.pop("assign_to_bot_id", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_input_data(data: object) -> None | TaskNodeInputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_data_type_0 = TaskNodeInputDataType0.from_dict(data)

                return input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskNodeInputDataType0 | Unset, data)

        input_data = _parse_input_data(d.pop("input_data", UNSET))

        parallel = d.pop("parallel", UNSET)

        def _parse_depends_on(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                depends_on_type_0 = cast(list[str], data)

                return depends_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        depends_on = _parse_depends_on(d.pop("depends_on", UNSET))

        task_node = cls(
            title=title,
            description=description,
            assign_to=assign_to,
            assign_to_bot_id=assign_to_bot_id,
            priority=priority,
            input_data=input_data,
            parallel=parallel,
            depends_on=depends_on,
        )

        return task_node
