from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LLMMetrics")


@_attrs_define
class LLMMetrics:
    """LLM metrics

    Attributes:
        total_llms (int):
        active_llms (int):
        inactive_llms (int):
        api_llms (int):
        local_llms (int):
        custom_llms (int):
        chat_llms (int | Unset):  Default: 0.
        embedding_llms (int | Unset):  Default: 0.
        image_llms (int | Unset):  Default: 0.
        tts_llms (int | Unset):  Default: 0.
        stt_llms (int | Unset):  Default: 0.
        video_llms (int | Unset):  Default: 0.
        reasoning_llms (int | Unset):  Default: 0.
        research_llms (int | Unset):  Default: 0.
        search_llms (int | Unset):  Default: 0.
    """

    total_llms: int
    active_llms: int
    inactive_llms: int
    api_llms: int
    local_llms: int
    custom_llms: int
    chat_llms: int | Unset = 0
    embedding_llms: int | Unset = 0
    image_llms: int | Unset = 0
    tts_llms: int | Unset = 0
    stt_llms: int | Unset = 0
    video_llms: int | Unset = 0
    reasoning_llms: int | Unset = 0
    research_llms: int | Unset = 0
    search_llms: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_llms = self.total_llms

        active_llms = self.active_llms

        inactive_llms = self.inactive_llms

        api_llms = self.api_llms

        local_llms = self.local_llms

        custom_llms = self.custom_llms

        chat_llms = self.chat_llms

        embedding_llms = self.embedding_llms

        image_llms = self.image_llms

        tts_llms = self.tts_llms

        stt_llms = self.stt_llms

        video_llms = self.video_llms

        reasoning_llms = self.reasoning_llms

        research_llms = self.research_llms

        search_llms = self.search_llms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_llms": total_llms,
                "active_llms": active_llms,
                "inactive_llms": inactive_llms,
                "api_llms": api_llms,
                "local_llms": local_llms,
                "custom_llms": custom_llms,
            }
        )
        if chat_llms is not UNSET:
            field_dict["chat_llms"] = chat_llms
        if embedding_llms is not UNSET:
            field_dict["embedding_llms"] = embedding_llms
        if image_llms is not UNSET:
            field_dict["image_llms"] = image_llms
        if tts_llms is not UNSET:
            field_dict["tts_llms"] = tts_llms
        if stt_llms is not UNSET:
            field_dict["stt_llms"] = stt_llms
        if video_llms is not UNSET:
            field_dict["video_llms"] = video_llms
        if reasoning_llms is not UNSET:
            field_dict["reasoning_llms"] = reasoning_llms
        if research_llms is not UNSET:
            field_dict["research_llms"] = research_llms
        if search_llms is not UNSET:
            field_dict["search_llms"] = search_llms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_llms = d.pop("total_llms")

        active_llms = d.pop("active_llms")

        inactive_llms = d.pop("inactive_llms")

        api_llms = d.pop("api_llms")

        local_llms = d.pop("local_llms")

        custom_llms = d.pop("custom_llms")

        chat_llms = d.pop("chat_llms", UNSET)

        embedding_llms = d.pop("embedding_llms", UNSET)

        image_llms = d.pop("image_llms", UNSET)

        tts_llms = d.pop("tts_llms", UNSET)

        stt_llms = d.pop("stt_llms", UNSET)

        video_llms = d.pop("video_llms", UNSET)

        reasoning_llms = d.pop("reasoning_llms", UNSET)

        research_llms = d.pop("research_llms", UNSET)

        search_llms = d.pop("search_llms", UNSET)

        llm_metrics = cls(
            total_llms=total_llms,
            active_llms=active_llms,
            inactive_llms=inactive_llms,
            api_llms=api_llms,
            local_llms=local_llms,
            custom_llms=custom_llms,
            chat_llms=chat_llms,
            embedding_llms=embedding_llms,
            image_llms=image_llms,
            tts_llms=tts_llms,
            stt_llms=stt_llms,
            video_llms=video_llms,
            reasoning_llms=reasoning_llms,
            research_llms=research_llms,
            search_llms=search_llms,
        )

        llm_metrics.additional_properties = d
        return llm_metrics

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
