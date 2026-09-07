from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_mode import SearchMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_filters import DeepFilters


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        mode (SearchMode | Unset):  Default: SearchMode.QUICK.
        query (None | str | Unset): Free-text (required in quick mode).
        filters (DeepFilters | None | Unset):
        types (list[str] | None | Unset): Restrict result groups. When omitted all types run.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
    """

    mode: SearchMode | Unset = SearchMode.QUICK
    query: None | str | Unset = UNSET
    filters: DeepFilters | None | Unset = UNSET
    types: list[str] | None | Unset = UNSET
    page: int | Unset = 1
    page_size: int | Unset = 20
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deep_filters import DeepFilters  # noqa: PLC0415

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, DeepFilters):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        types: list[str] | None | Unset
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, list):
            types = self.types

        else:
            types = self.types

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if query is not UNSET:
            field_dict["query"] = query
        if filters is not UNSET:
            field_dict["filters"] = filters
        if types is not UNSET:
            field_dict["types"] = types
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_filters import DeepFilters  # noqa: PLC0415

        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: SearchMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SearchMode(_mode)

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_filters(data: object) -> DeepFilters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = DeepFilters.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepFilters | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                types_type_0 = cast(list[str], data)

                return types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        types = _parse_types(d.pop("types", UNSET))

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        search_request = cls(
            mode=mode,
            query=query,
            filters=filters,
            types=types,
            page=page,
            page_size=page_size,
        )

        search_request.additional_properties = d
        return search_request

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
