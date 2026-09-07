from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingestion_config_response_index_params_type_0 import IngestionConfigResponseIndexParamsType0


T = TypeVar("T", bound="IngestionConfigResponse")


@_attrs_define
class IngestionConfigResponse:
    """
    Attributes:
        workspace_id (str):
        embedding_dimension (int):
        chunk_max_tokens (int):
        chunk_min_tokens (int):
        chunk_overlap_chars (int):
        index_type (str):
        auto_ingest_on_connect (bool):
        enrichment_enabled (bool):
        embedding_model_id (None | str | Unset):
        index_params (IngestionConfigResponseIndexParamsType0 | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    workspace_id: str
    embedding_dimension: int
    chunk_max_tokens: int
    chunk_min_tokens: int
    chunk_overlap_chars: int
    index_type: str
    auto_ingest_on_connect: bool
    enrichment_enabled: bool
    embedding_model_id: None | str | Unset = UNSET
    index_params: IngestionConfigResponseIndexParamsType0 | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ingestion_config_response_index_params_type_0 import (
            IngestionConfigResponseIndexParamsType0,  # noqa: PLC0415
        )

        workspace_id = self.workspace_id

        embedding_dimension = self.embedding_dimension

        chunk_max_tokens = self.chunk_max_tokens

        chunk_min_tokens = self.chunk_min_tokens

        chunk_overlap_chars = self.chunk_overlap_chars

        index_type = self.index_type

        auto_ingest_on_connect = self.auto_ingest_on_connect

        enrichment_enabled = self.enrichment_enabled

        embedding_model_id: None | str | Unset
        if isinstance(self.embedding_model_id, Unset):
            embedding_model_id = UNSET
        else:
            embedding_model_id = self.embedding_model_id

        index_params: dict[str, Any] | None | Unset
        if isinstance(self.index_params, Unset):
            index_params = UNSET
        elif isinstance(self.index_params, IngestionConfigResponseIndexParamsType0):
            index_params = self.index_params.to_dict()
        else:
            index_params = self.index_params

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
                "embedding_dimension": embedding_dimension,
                "chunk_max_tokens": chunk_max_tokens,
                "chunk_min_tokens": chunk_min_tokens,
                "chunk_overlap_chars": chunk_overlap_chars,
                "index_type": index_type,
                "auto_ingest_on_connect": auto_ingest_on_connect,
                "enrichment_enabled": enrichment_enabled,
            }
        )
        if embedding_model_id is not UNSET:
            field_dict["embedding_model_id"] = embedding_model_id
        if index_params is not UNSET:
            field_dict["index_params"] = index_params
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingestion_config_response_index_params_type_0 import (
            IngestionConfigResponseIndexParamsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        embedding_dimension = d.pop("embedding_dimension")

        chunk_max_tokens = d.pop("chunk_max_tokens")

        chunk_min_tokens = d.pop("chunk_min_tokens")

        chunk_overlap_chars = d.pop("chunk_overlap_chars")

        index_type = d.pop("index_type")

        auto_ingest_on_connect = d.pop("auto_ingest_on_connect")

        enrichment_enabled = d.pop("enrichment_enabled")

        def _parse_embedding_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model_id = _parse_embedding_model_id(d.pop("embedding_model_id", UNSET))

        def _parse_index_params(data: object) -> IngestionConfigResponseIndexParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                index_params_type_0 = IngestionConfigResponseIndexParamsType0.from_dict(data)

                return index_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IngestionConfigResponseIndexParamsType0 | None | Unset, data)

        index_params = _parse_index_params(d.pop("index_params", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        ingestion_config_response = cls(
            workspace_id=workspace_id,
            embedding_dimension=embedding_dimension,
            chunk_max_tokens=chunk_max_tokens,
            chunk_min_tokens=chunk_min_tokens,
            chunk_overlap_chars=chunk_overlap_chars,
            index_type=index_type,
            auto_ingest_on_connect=auto_ingest_on_connect,
            enrichment_enabled=enrichment_enabled,
            embedding_model_id=embedding_model_id,
            index_params=index_params,
            updated_at=updated_at,
        )

        ingestion_config_response.additional_properties = d
        return ingestion_config_response

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
