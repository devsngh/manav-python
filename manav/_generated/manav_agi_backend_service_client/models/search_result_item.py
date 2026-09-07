from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_result_item_type import SearchResultItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result_item_metadata import SearchResultItemMetadata


T = TypeVar("T", bound="SearchResultItem")


@_attrs_define
class SearchResultItem:
    """One typed hit — client decides how to render based on `type`.

    Attributes:
        type_ (SearchResultItemType):
        id (str):
        title (str):
        subtitle (None | str | Unset):
        snippet (None | str | Unset):
        matched_field (None | str | Unset):
        score (float | None | Unset):
        timestamp (datetime.datetime | None | Unset):
        metadata (SearchResultItemMetadata | Unset):
    """

    type_: SearchResultItemType
    id: str
    title: str
    subtitle: None | str | Unset = UNSET
    snippet: None | str | Unset = UNSET
    matched_field: None | str | Unset = UNSET
    score: float | None | Unset = UNSET
    timestamp: datetime.datetime | None | Unset = UNSET
    metadata: SearchResultItemMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        title = self.title

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        snippet: None | str | Unset
        if isinstance(self.snippet, Unset):
            snippet = UNSET
        else:
            snippet = self.snippet

        matched_field: None | str | Unset
        if isinstance(self.matched_field, Unset):
            matched_field = UNSET
        else:
            matched_field = self.matched_field

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "title": title,
            }
        )
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if matched_field is not UNSET:
            field_dict["matched_field"] = matched_field
        if score is not UNSET:
            field_dict["score"] = score
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_result_item_metadata import SearchResultItemMetadata  # noqa: PLC0415

        d = dict(src_dict)
        type_ = SearchResultItemType(d.pop("type"))

        id = d.pop("id")

        title = d.pop("title")

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snippet = _parse_snippet(d.pop("snippet", UNSET))

        def _parse_matched_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        matched_field = _parse_matched_field(d.pop("matched_field", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: SearchResultItemMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SearchResultItemMetadata.from_dict(_metadata)

        search_result_item = cls(
            type_=type_,
            id=id,
            title=title,
            subtitle=subtitle,
            snippet=snippet,
            matched_field=matched_field,
            score=score,
            timestamp=timestamp,
            metadata=metadata,
        )

        search_result_item.additional_properties = d
        return search_result_item

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
