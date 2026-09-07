from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.judge_scores_update_eval_queries_results_type_0_item import (
        JudgeScoresUpdateEvalQueriesResultsType0Item,
    )


T = TypeVar("T", bound="JudgeScoresUpdate")


@_attrs_define
class JudgeScoresUpdate:
    """
    Attributes:
        accuracy_score (float | None | Unset):
        quality_reasoning (None | str | Unset):
        eval_queries_results (list[JudgeScoresUpdateEvalQueriesResultsType0Item] | None | Unset):
        recommendations (list[str] | None | Unset):
        faithfulness (float | None | Unset):
        doc_precision (float | None | Unset):
        chunk_precision (float | None | Unset):
        table_accuracy (float | None | Unset):
        column_f1 (float | None | Unset):
        sql_accuracy (float | None | Unset):
        event_precision (float | None | Unset):
        metric_precision (float | None | Unset):
        cost (float | None | Unset):
    """

    accuracy_score: float | None | Unset = UNSET
    quality_reasoning: None | str | Unset = UNSET
    eval_queries_results: list[JudgeScoresUpdateEvalQueriesResultsType0Item] | None | Unset = UNSET
    recommendations: list[str] | None | Unset = UNSET
    faithfulness: float | None | Unset = UNSET
    doc_precision: float | None | Unset = UNSET
    chunk_precision: float | None | Unset = UNSET
    table_accuracy: float | None | Unset = UNSET
    column_f1: float | None | Unset = UNSET
    sql_accuracy: float | None | Unset = UNSET
    event_precision: float | None | Unset = UNSET
    metric_precision: float | None | Unset = UNSET
    cost: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accuracy_score: float | None | Unset
        if isinstance(self.accuracy_score, Unset):
            accuracy_score = UNSET
        else:
            accuracy_score = self.accuracy_score

        quality_reasoning: None | str | Unset
        if isinstance(self.quality_reasoning, Unset):
            quality_reasoning = UNSET
        else:
            quality_reasoning = self.quality_reasoning

        eval_queries_results: list[dict[str, Any]] | None | Unset
        if isinstance(self.eval_queries_results, Unset):
            eval_queries_results = UNSET
        elif isinstance(self.eval_queries_results, list):
            eval_queries_results = []
            for eval_queries_results_type_0_item_data in self.eval_queries_results:
                eval_queries_results_type_0_item = eval_queries_results_type_0_item_data.to_dict()
                eval_queries_results.append(eval_queries_results_type_0_item)

        else:
            eval_queries_results = self.eval_queries_results

        recommendations: list[str] | None | Unset
        if isinstance(self.recommendations, Unset):
            recommendations = UNSET
        elif isinstance(self.recommendations, list):
            recommendations = self.recommendations

        else:
            recommendations = self.recommendations

        faithfulness: float | None | Unset
        if isinstance(self.faithfulness, Unset):
            faithfulness = UNSET
        else:
            faithfulness = self.faithfulness

        doc_precision: float | None | Unset
        if isinstance(self.doc_precision, Unset):
            doc_precision = UNSET
        else:
            doc_precision = self.doc_precision

        chunk_precision: float | None | Unset
        if isinstance(self.chunk_precision, Unset):
            chunk_precision = UNSET
        else:
            chunk_precision = self.chunk_precision

        table_accuracy: float | None | Unset
        if isinstance(self.table_accuracy, Unset):
            table_accuracy = UNSET
        else:
            table_accuracy = self.table_accuracy

        column_f1: float | None | Unset
        if isinstance(self.column_f1, Unset):
            column_f1 = UNSET
        else:
            column_f1 = self.column_f1

        sql_accuracy: float | None | Unset
        if isinstance(self.sql_accuracy, Unset):
            sql_accuracy = UNSET
        else:
            sql_accuracy = self.sql_accuracy

        event_precision: float | None | Unset
        if isinstance(self.event_precision, Unset):
            event_precision = UNSET
        else:
            event_precision = self.event_precision

        metric_precision: float | None | Unset
        if isinstance(self.metric_precision, Unset):
            metric_precision = UNSET
        else:
            metric_precision = self.metric_precision

        cost: float | None | Unset
        if isinstance(self.cost, Unset):
            cost = UNSET
        else:
            cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accuracy_score is not UNSET:
            field_dict["accuracy_score"] = accuracy_score
        if quality_reasoning is not UNSET:
            field_dict["quality_reasoning"] = quality_reasoning
        if eval_queries_results is not UNSET:
            field_dict["eval_queries_results"] = eval_queries_results
        if recommendations is not UNSET:
            field_dict["recommendations"] = recommendations
        if faithfulness is not UNSET:
            field_dict["faithfulness"] = faithfulness
        if doc_precision is not UNSET:
            field_dict["doc_precision"] = doc_precision
        if chunk_precision is not UNSET:
            field_dict["chunk_precision"] = chunk_precision
        if table_accuracy is not UNSET:
            field_dict["table_accuracy"] = table_accuracy
        if column_f1 is not UNSET:
            field_dict["column_f1"] = column_f1
        if sql_accuracy is not UNSET:
            field_dict["sql_accuracy"] = sql_accuracy
        if event_precision is not UNSET:
            field_dict["event_precision"] = event_precision
        if metric_precision is not UNSET:
            field_dict["metric_precision"] = metric_precision
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.judge_scores_update_eval_queries_results_type_0_item import (
            JudgeScoresUpdateEvalQueriesResultsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_accuracy_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        accuracy_score = _parse_accuracy_score(d.pop("accuracy_score", UNSET))

        def _parse_quality_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_reasoning = _parse_quality_reasoning(d.pop("quality_reasoning", UNSET))

        def _parse_eval_queries_results(
            data: object,
        ) -> list[JudgeScoresUpdateEvalQueriesResultsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                eval_queries_results_type_0 = []
                _eval_queries_results_type_0 = data
                for eval_queries_results_type_0_item_data in _eval_queries_results_type_0:
                    eval_queries_results_type_0_item = JudgeScoresUpdateEvalQueriesResultsType0Item.from_dict(
                        eval_queries_results_type_0_item_data
                    )

                    eval_queries_results_type_0.append(eval_queries_results_type_0_item)

                return eval_queries_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JudgeScoresUpdateEvalQueriesResultsType0Item] | None | Unset, data)

        eval_queries_results = _parse_eval_queries_results(d.pop("eval_queries_results", UNSET))

        def _parse_recommendations(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recommendations_type_0 = cast(list[str], data)

                return recommendations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recommendations = _parse_recommendations(d.pop("recommendations", UNSET))

        def _parse_faithfulness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        faithfulness = _parse_faithfulness(d.pop("faithfulness", UNSET))

        def _parse_doc_precision(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        doc_precision = _parse_doc_precision(d.pop("doc_precision", UNSET))

        def _parse_chunk_precision(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        chunk_precision = _parse_chunk_precision(d.pop("chunk_precision", UNSET))

        def _parse_table_accuracy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        table_accuracy = _parse_table_accuracy(d.pop("table_accuracy", UNSET))

        def _parse_column_f1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        column_f1 = _parse_column_f1(d.pop("column_f1", UNSET))

        def _parse_sql_accuracy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sql_accuracy = _parse_sql_accuracy(d.pop("sql_accuracy", UNSET))

        def _parse_event_precision(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        event_precision = _parse_event_precision(d.pop("event_precision", UNSET))

        def _parse_metric_precision(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        metric_precision = _parse_metric_precision(d.pop("metric_precision", UNSET))

        def _parse_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost = _parse_cost(d.pop("cost", UNSET))

        judge_scores_update = cls(
            accuracy_score=accuracy_score,
            quality_reasoning=quality_reasoning,
            eval_queries_results=eval_queries_results,
            recommendations=recommendations,
            faithfulness=faithfulness,
            doc_precision=doc_precision,
            chunk_precision=chunk_precision,
            table_accuracy=table_accuracy,
            column_f1=column_f1,
            sql_accuracy=sql_accuracy,
            event_precision=event_precision,
            metric_precision=metric_precision,
            cost=cost,
        )

        judge_scores_update.additional_properties = d
        return judge_scores_update

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
