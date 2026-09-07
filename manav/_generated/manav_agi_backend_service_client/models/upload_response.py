from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadResponse")


@_attrs_define
class UploadResponse:
    """
    Attributes:
        job_id (str):
        source_id (str):
        s3_key (str):
        message (str | Unset):  Default: 'Document queued for ingestion'.
    """

    job_id: str
    source_id: str
    s3_key: str
    message: str | Unset = "Document queued for ingestion"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        source_id = self.source_id

        s3_key = self.s3_key

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "source_id": source_id,
                "s3_key": s3_key,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

        source_id = d.pop("source_id")

        s3_key = d.pop("s3_key")

        message = d.pop("message", UNSET)

        upload_response = cls(
            job_id=job_id,
            source_id=source_id,
            s3_key=s3_key,
            message=message,
        )

        upload_response.additional_properties = d
        return upload_response

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
