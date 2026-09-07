from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_type import CommentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCommentCreate")


@_attrs_define
class TaskCommentCreate:
    """
    Attributes:
        content (str):
        comment_type (CommentType | Unset):  Default: CommentType.COMMENT.
    """

    content: str
    comment_type: CommentType | Unset = CommentType.COMMENT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        comment_type: str | Unset = UNSET
        if not isinstance(self.comment_type, Unset):
            comment_type = self.comment_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if comment_type is not UNSET:
            field_dict["comment_type"] = comment_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        _comment_type = d.pop("comment_type", UNSET)
        comment_type: CommentType | Unset
        if isinstance(_comment_type, Unset):
            comment_type = UNSET
        else:
            comment_type = CommentType(_comment_type)

        task_comment_create = cls(
            content=content,
            comment_type=comment_type,
        )

        task_comment_create.additional_properties = d
        return task_comment_create

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
