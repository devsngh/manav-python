from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingestion_config_update_index_params_type_0 import IngestionConfigUpdateIndexParamsType0


T = TypeVar("T", bound="IngestionConfigUpdate")


@_attrs_define
class IngestionConfigUpdate:
    """All fields optional — partial update (PATCH semantics via PUT).

    Attributes:
        embedding_model_id (None | str | Unset):
        embedding_dimension (int | None | Unset):
        chunk_max_tokens (int | None | Unset):
        chunk_min_tokens (int | None | Unset):
        chunk_overlap_chars (int | None | Unset):
        index_type (None | str | Unset):
        index_params (IngestionConfigUpdateIndexParamsType0 | None | Unset):
        auto_ingest_on_connect (bool | None | Unset):
        enrichment_enabled (bool | None | Unset):
    """

    embedding_model_id: None | str | Unset = UNSET
    embedding_dimension: int | None | Unset = UNSET
    chunk_max_tokens: int | None | Unset = UNSET
    chunk_min_tokens: int | None | Unset = UNSET
    chunk_overlap_chars: int | None | Unset = UNSET
    index_type: None | str | Unset = UNSET
    index_params: IngestionConfigUpdateIndexParamsType0 | None | Unset = UNSET
    auto_ingest_on_connect: bool | None | Unset = UNSET
    enrichment_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ingestion_config_update_index_params_type_0 import (
            IngestionConfigUpdateIndexParamsType0,  # noqa: PLC0415
        )

        embedding_model_id: None | str | Unset
        if isinstance(self.embedding_model_id, Unset):
            embedding_model_id = UNSET
        else:
            embedding_model_id = self.embedding_model_id

        embedding_dimension: int | None | Unset
        if isinstance(self.embedding_dimension, Unset):
            embedding_dimension = UNSET
        else:
            embedding_dimension = self.embedding_dimension

        chunk_max_tokens: int | None | Unset
        if isinstance(self.chunk_max_tokens, Unset):
            chunk_max_tokens = UNSET
        else:
            chunk_max_tokens = self.chunk_max_tokens

        chunk_min_tokens: int | None | Unset
        if isinstance(self.chunk_min_tokens, Unset):
            chunk_min_tokens = UNSET
        else:
            chunk_min_tokens = self.chunk_min_tokens

        chunk_overlap_chars: int | None | Unset
        if isinstance(self.chunk_overlap_chars, Unset):
            chunk_overlap_chars = UNSET
        else:
            chunk_overlap_chars = self.chunk_overlap_chars

        index_type: None | str | Unset
        if isinstance(self.index_type, Unset):
            index_type = UNSET
        else:
            index_type = self.index_type

        index_params: dict[str, Any] | None | Unset
        if isinstance(self.index_params, Unset):
            index_params = UNSET
        elif isinstance(self.index_params, IngestionConfigUpdateIndexParamsType0):
            index_params = self.index_params.to_dict()
        else:
            index_params = self.index_params

        auto_ingest_on_connect: bool | None | Unset
        if isinstance(self.auto_ingest_on_connect, Unset):
            auto_ingest_on_connect = UNSET
        else:
            auto_ingest_on_connect = self.auto_ingest_on_connect

        enrichment_enabled: bool | None | Unset
        if isinstance(self.enrichment_enabled, Unset):
            enrichment_enabled = UNSET
        else:
            enrichment_enabled = self.enrichment_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if embedding_model_id is not UNSET:
            field_dict["embedding_model_id"] = embedding_model_id
        if embedding_dimension is not UNSET:
            field_dict["embedding_dimension"] = embedding_dimension
        if chunk_max_tokens is not UNSET:
            field_dict["chunk_max_tokens"] = chunk_max_tokens
        if chunk_min_tokens is not UNSET:
            field_dict["chunk_min_tokens"] = chunk_min_tokens
        if chunk_overlap_chars is not UNSET:
            field_dict["chunk_overlap_chars"] = chunk_overlap_chars
        if index_type is not UNSET:
            field_dict["index_type"] = index_type
        if index_params is not UNSET:
            field_dict["index_params"] = index_params
        if auto_ingest_on_connect is not UNSET:
            field_dict["auto_ingest_on_connect"] = auto_ingest_on_connect
        if enrichment_enabled is not UNSET:
            field_dict["enrichment_enabled"] = enrichment_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingestion_config_update_index_params_type_0 import (
            IngestionConfigUpdateIndexParamsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_embedding_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model_id = _parse_embedding_model_id(d.pop("embedding_model_id", UNSET))

        def _parse_embedding_dimension(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        embedding_dimension = _parse_embedding_dimension(d.pop("embedding_dimension", UNSET))

        def _parse_chunk_max_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_max_tokens = _parse_chunk_max_tokens(d.pop("chunk_max_tokens", UNSET))

        def _parse_chunk_min_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_min_tokens = _parse_chunk_min_tokens(d.pop("chunk_min_tokens", UNSET))

        def _parse_chunk_overlap_chars(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        chunk_overlap_chars = _parse_chunk_overlap_chars(d.pop("chunk_overlap_chars", UNSET))

        def _parse_index_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        index_type = _parse_index_type(d.pop("index_type", UNSET))

        def _parse_index_params(data: object) -> IngestionConfigUpdateIndexParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                index_params_type_0 = IngestionConfigUpdateIndexParamsType0.from_dict(data)

                return index_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IngestionConfigUpdateIndexParamsType0 | None | Unset, data)

        index_params = _parse_index_params(d.pop("index_params", UNSET))

        def _parse_auto_ingest_on_connect(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_ingest_on_connect = _parse_auto_ingest_on_connect(d.pop("auto_ingest_on_connect", UNSET))

        def _parse_enrichment_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enrichment_enabled = _parse_enrichment_enabled(d.pop("enrichment_enabled", UNSET))

        ingestion_config_update = cls(
            embedding_model_id=embedding_model_id,
            embedding_dimension=embedding_dimension,
            chunk_max_tokens=chunk_max_tokens,
            chunk_min_tokens=chunk_min_tokens,
            chunk_overlap_chars=chunk_overlap_chars,
            index_type=index_type,
            index_params=index_params,
            auto_ingest_on_connect=auto_ingest_on_connect,
            enrichment_enabled=enrichment_enabled,
        )

        ingestion_config_update.additional_properties = d
        return ingestion_config_update

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
