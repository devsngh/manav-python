from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractOcrRequest")


@_attrs_define
class ExtractOcrRequest:
    """
    Attributes:
        s3_key (str): S3 key (bucket/path or s3://bucket/path)
        lang (str | Unset): Tesseract language code (e.g. 'eng', 'hin+eng') Default: 'eng'.
    """

    s3_key: str
    lang: str | Unset = "eng"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s3_key = self.s3_key

        lang = self.lang

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s3_key": s3_key,
            }
        )
        if lang is not UNSET:
            field_dict["lang"] = lang

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        s3_key = d.pop("s3_key")

        lang = d.pop("lang", UNSET)

        extract_ocr_request = cls(
            s3_key=s3_key,
            lang=lang,
        )

        extract_ocr_request.additional_properties = d
        return extract_ocr_request

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
