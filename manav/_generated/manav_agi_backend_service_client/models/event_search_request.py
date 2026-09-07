from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSearchRequest")


@_attrs_define
class EventSearchRequest:
    """
    Attributes:
        workspace_id (str):
        query (None | str | Unset):
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        sentiment (None | str | Unset):
        top_k (int | Unset):  Default: 20.
    """

    workspace_id: str
    query: None | str | Unset = UNSET
    date_from: None | str | Unset = UNSET
    date_to: None | str | Unset = UNSET
    sentiment: None | str | Unset = UNSET
    top_k: int | Unset = 20
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        else:
            date_to = self.date_to

        sentiment: None | str | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if top_k is not UNSET:
            field_dict["top_k"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_date_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_sentiment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        top_k = d.pop("top_k", UNSET)

        event_search_request = cls(
            workspace_id=workspace_id,
            query=query,
            date_from=date_from,
            date_to=date_to,
            sentiment=sentiment,
            top_k=top_k,
        )

        event_search_request.additional_properties = d
        return event_search_request

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
