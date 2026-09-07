from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadDocumentApiIngestionUploadPost")


@_attrs_define
class BodyUploadDocumentApiIngestionUploadPost:
    """
    Attributes:
        workspace_id (str):
        file (File):
        source_id (None | str | Unset):
        doc_type (None | str | Unset):
    """

    workspace_id: str
    file: File
    source_id: None | str | Unset = UNSET
    doc_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        file = self.file.to_tuple()

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        doc_type: None | str | Unset
        if isinstance(self.doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = self.doc_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
                "file": file,
            }
        )
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if doc_type is not UNSET:
            field_dict["doc_type"] = doc_type

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("workspace_id", (None, str(self.workspace_id).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.source_id, Unset):
            if isinstance(self.source_id, str):
                files.append(("source_id", (None, str(self.source_id).encode(), "text/plain")))
            else:
                files.append(("source_id", (None, str(self.source_id).encode(), "text/plain")))

        if not isinstance(self.doc_type, Unset):
            if isinstance(self.doc_type, str):
                files.append(("doc_type", (None, str(self.doc_type).encode(), "text/plain")))
            else:
                files.append(("doc_type", (None, str(self.doc_type).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        file = File(payload=BytesIO(d.pop("file")))

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_doc_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        doc_type = _parse_doc_type(d.pop("doc_type", UNSET))

        body_upload_document_api_ingestion_upload_post = cls(
            workspace_id=workspace_id,
            file=file,
            source_id=source_id,
            doc_type=doc_type,
        )

        body_upload_document_api_ingestion_upload_post.additional_properties = d
        return body_upload_document_api_ingestion_upload_post

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
