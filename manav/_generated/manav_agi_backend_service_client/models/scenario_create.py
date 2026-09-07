from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scenario_create_expected_type_0 import ScenarioCreateExpectedType0


T = TypeVar("T", bound="ScenarioCreate")


@_attrs_define
class ScenarioCreate:
    """
    Attributes:
        name (str):
        category (str):
        query (str):
        bot_name (None | str | Unset):
        deepagent_config_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        expected (None | ScenarioCreateExpectedType0 | Unset):
        eval_queries (list[str] | None | Unset):
        tags (list[str] | None | Unset):
        dataset_id (None | Unset | UUID):
        expected_answer (None | str | Unset):
        expected_workspace_ids (list[str] | None | Unset):
        expected_tables (list[str] | None | Unset):
        expected_columns (list[str] | None | Unset):
        expected_chunks (list[str] | None | Unset):
        expected_event_ids (list[str] | None | Unset):
        expected_metric_ids (list[str] | None | Unset):
        expected_sql (None | str | Unset):
        max_steps (int | None | Unset):
        difficulty (int | None | Unset):
    """

    name: str
    category: str
    query: str
    bot_name: None | str | Unset = UNSET
    deepagent_config_id: None | Unset | UUID = UNSET
    bot_id: None | Unset | UUID = UNSET
    expected: None | ScenarioCreateExpectedType0 | Unset = UNSET
    eval_queries: list[str] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    dataset_id: None | Unset | UUID = UNSET
    expected_answer: None | str | Unset = UNSET
    expected_workspace_ids: list[str] | None | Unset = UNSET
    expected_tables: list[str] | None | Unset = UNSET
    expected_columns: list[str] | None | Unset = UNSET
    expected_chunks: list[str] | None | Unset = UNSET
    expected_event_ids: list[str] | None | Unset = UNSET
    expected_metric_ids: list[str] | None | Unset = UNSET
    expected_sql: None | str | Unset = UNSET
    max_steps: int | None | Unset = UNSET
    difficulty: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scenario_create_expected_type_0 import ScenarioCreateExpectedType0  # noqa: PLC0415

        name = self.name

        category = self.category

        query = self.query

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        deepagent_config_id: None | str | Unset
        if isinstance(self.deepagent_config_id, Unset):
            deepagent_config_id = UNSET
        elif isinstance(self.deepagent_config_id, UUID):
            deepagent_config_id = str(self.deepagent_config_id)
        else:
            deepagent_config_id = self.deepagent_config_id

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        expected: dict[str, Any] | None | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        elif isinstance(self.expected, ScenarioCreateExpectedType0):
            expected = self.expected.to_dict()
        else:
            expected = self.expected

        eval_queries: list[str] | None | Unset
        if isinstance(self.eval_queries, Unset):
            eval_queries = UNSET
        elif isinstance(self.eval_queries, list):
            eval_queries = self.eval_queries

        else:
            eval_queries = self.eval_queries

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

        expected_answer: None | str | Unset
        if isinstance(self.expected_answer, Unset):
            expected_answer = UNSET
        else:
            expected_answer = self.expected_answer

        expected_workspace_ids: list[str] | None | Unset
        if isinstance(self.expected_workspace_ids, Unset):
            expected_workspace_ids = UNSET
        elif isinstance(self.expected_workspace_ids, list):
            expected_workspace_ids = self.expected_workspace_ids

        else:
            expected_workspace_ids = self.expected_workspace_ids

        expected_tables: list[str] | None | Unset
        if isinstance(self.expected_tables, Unset):
            expected_tables = UNSET
        elif isinstance(self.expected_tables, list):
            expected_tables = self.expected_tables

        else:
            expected_tables = self.expected_tables

        expected_columns: list[str] | None | Unset
        if isinstance(self.expected_columns, Unset):
            expected_columns = UNSET
        elif isinstance(self.expected_columns, list):
            expected_columns = self.expected_columns

        else:
            expected_columns = self.expected_columns

        expected_chunks: list[str] | None | Unset
        if isinstance(self.expected_chunks, Unset):
            expected_chunks = UNSET
        elif isinstance(self.expected_chunks, list):
            expected_chunks = self.expected_chunks

        else:
            expected_chunks = self.expected_chunks

        expected_event_ids: list[str] | None | Unset
        if isinstance(self.expected_event_ids, Unset):
            expected_event_ids = UNSET
        elif isinstance(self.expected_event_ids, list):
            expected_event_ids = self.expected_event_ids

        else:
            expected_event_ids = self.expected_event_ids

        expected_metric_ids: list[str] | None | Unset
        if isinstance(self.expected_metric_ids, Unset):
            expected_metric_ids = UNSET
        elif isinstance(self.expected_metric_ids, list):
            expected_metric_ids = self.expected_metric_ids

        else:
            expected_metric_ids = self.expected_metric_ids

        expected_sql: None | str | Unset
        if isinstance(self.expected_sql, Unset):
            expected_sql = UNSET
        else:
            expected_sql = self.expected_sql

        max_steps: int | None | Unset
        if isinstance(self.max_steps, Unset):
            max_steps = UNSET
        else:
            max_steps = self.max_steps

        difficulty: int | None | Unset
        if isinstance(self.difficulty, Unset):
            difficulty = UNSET
        else:
            difficulty = self.difficulty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "category": category,
                "query": query,
            }
        )
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if deepagent_config_id is not UNSET:
            field_dict["deepagent_config_id"] = deepagent_config_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if expected is not UNSET:
            field_dict["expected"] = expected
        if eval_queries is not UNSET:
            field_dict["eval_queries"] = eval_queries
        if tags is not UNSET:
            field_dict["tags"] = tags
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if expected_answer is not UNSET:
            field_dict["expected_answer"] = expected_answer
        if expected_workspace_ids is not UNSET:
            field_dict["expected_workspace_ids"] = expected_workspace_ids
        if expected_tables is not UNSET:
            field_dict["expected_tables"] = expected_tables
        if expected_columns is not UNSET:
            field_dict["expected_columns"] = expected_columns
        if expected_chunks is not UNSET:
            field_dict["expected_chunks"] = expected_chunks
        if expected_event_ids is not UNSET:
            field_dict["expected_event_ids"] = expected_event_ids
        if expected_metric_ids is not UNSET:
            field_dict["expected_metric_ids"] = expected_metric_ids
        if expected_sql is not UNSET:
            field_dict["expected_sql"] = expected_sql
        if max_steps is not UNSET:
            field_dict["max_steps"] = max_steps
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scenario_create_expected_type_0 import ScenarioCreateExpectedType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        category = d.pop("category")

        query = d.pop("query")

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        def _parse_deepagent_config_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deepagent_config_id_type_0 = UUID(data)

                return deepagent_config_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deepagent_config_id = _parse_deepagent_config_id(d.pop("deepagent_config_id", UNSET))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_expected(data: object) -> None | ScenarioCreateExpectedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expected_type_0 = ScenarioCreateExpectedType0.from_dict(data)

                return expected_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScenarioCreateExpectedType0 | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))

        def _parse_eval_queries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                eval_queries_type_0 = cast(list[str], data)

                return eval_queries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        eval_queries = _parse_eval_queries(d.pop("eval_queries", UNSET))

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

        def _parse_expected_answer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_answer = _parse_expected_answer(d.pop("expected_answer", UNSET))

        def _parse_expected_workspace_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_workspace_ids_type_0 = cast(list[str], data)

                return expected_workspace_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expected_workspace_ids = _parse_expected_workspace_ids(d.pop("expected_workspace_ids", UNSET))

        def _parse_expected_tables(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_tables_type_0 = cast(list[str], data)

                return expected_tables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expected_tables = _parse_expected_tables(d.pop("expected_tables", UNSET))

        def _parse_expected_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_columns_type_0 = cast(list[str], data)

                return expected_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expected_columns = _parse_expected_columns(d.pop("expected_columns", UNSET))

        def _parse_expected_chunks(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_chunks_type_0 = cast(list[str], data)

                return expected_chunks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expected_chunks = _parse_expected_chunks(d.pop("expected_chunks", UNSET))

        def _parse_expected_event_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_event_ids_type_0 = cast(list[str], data)

                return expected_event_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expected_event_ids = _parse_expected_event_ids(d.pop("expected_event_ids", UNSET))

        def _parse_expected_metric_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expected_metric_ids_type_0 = cast(list[str], data)

                return expected_metric_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        expected_metric_ids = _parse_expected_metric_ids(d.pop("expected_metric_ids", UNSET))

        def _parse_expected_sql(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_sql = _parse_expected_sql(d.pop("expected_sql", UNSET))

        def _parse_max_steps(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_steps = _parse_max_steps(d.pop("max_steps", UNSET))

        def _parse_difficulty(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        difficulty = _parse_difficulty(d.pop("difficulty", UNSET))

        scenario_create = cls(
            name=name,
            category=category,
            query=query,
            bot_name=bot_name,
            deepagent_config_id=deepagent_config_id,
            bot_id=bot_id,
            expected=expected,
            eval_queries=eval_queries,
            tags=tags,
            dataset_id=dataset_id,
            expected_answer=expected_answer,
            expected_workspace_ids=expected_workspace_ids,
            expected_tables=expected_tables,
            expected_columns=expected_columns,
            expected_chunks=expected_chunks,
            expected_event_ids=expected_event_ids,
            expected_metric_ids=expected_metric_ids,
            expected_sql=expected_sql,
            max_steps=max_steps,
            difficulty=difficulty,
        )

        scenario_create.additional_properties = d
        return scenario_create

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
