from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_request_params_type_0 import QueryRequestParamsType0


T = TypeVar("T", bound="QueryRequest")


@_attrs_define
class QueryRequest:
    """
    Attributes:
        source_id (str):
        sql (str):
        limit (int | Unset):  Default: 100.
        params (None | QueryRequestParamsType0 | Unset):
    """

    source_id: str
    sql: str
    limit: int | Unset = 100
    params: None | QueryRequestParamsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.query_request_params_type_0 import QueryRequestParamsType0  # noqa: PLC0415

        source_id = self.source_id

        sql = self.sql

        limit = self.limit

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, QueryRequestParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_id": source_id,
                "sql": sql,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_request_params_type_0 import QueryRequestParamsType0  # noqa: PLC0415

        d = dict(src_dict)
        source_id = d.pop("source_id")

        sql = d.pop("sql")

        limit = d.pop("limit", UNSET)

        def _parse_params(data: object) -> None | QueryRequestParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = QueryRequestParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QueryRequestParamsType0 | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        query_request = cls(
            source_id=source_id,
            sql=sql,
            limit=limit,
            params=params,
        )

        query_request.additional_properties = d
        return query_request

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
