from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_bot_count import ChatBotCount
    from ..models.chat_format_count import ChatFormatCount
    from ..models.chat_processing_bucket import ChatProcessingBucket


T = TypeVar("T", bound="ChatDistributionResponse")


@_attrs_define
class ChatDistributionResponse:
    """GET /api/analytics/chat/distribution — processing-time hist + format counts + per-bot.

    Attributes:
        processing_time (list[ChatProcessingBucket]):
        response_formats (list[ChatFormatCount]):
        by_bot (list[ChatBotCount]):
    """

    processing_time: list[ChatProcessingBucket]
    response_formats: list[ChatFormatCount]
    by_bot: list[ChatBotCount]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processing_time = []
        for processing_time_item_data in self.processing_time:
            processing_time_item = processing_time_item_data.to_dict()
            processing_time.append(processing_time_item)

        response_formats = []
        for response_formats_item_data in self.response_formats:
            response_formats_item = response_formats_item_data.to_dict()
            response_formats.append(response_formats_item)

        by_bot = []
        for by_bot_item_data in self.by_bot:
            by_bot_item = by_bot_item_data.to_dict()
            by_bot.append(by_bot_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processing_time": processing_time,
                "response_formats": response_formats,
                "by_bot": by_bot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_bot_count import ChatBotCount  # noqa: PLC0415
        from ..models.chat_format_count import ChatFormatCount  # noqa: PLC0415
        from ..models.chat_processing_bucket import ChatProcessingBucket  # noqa: PLC0415

        d = dict(src_dict)
        processing_time = []
        _processing_time = d.pop("processing_time")
        for processing_time_item_data in _processing_time:
            processing_time_item = ChatProcessingBucket.from_dict(processing_time_item_data)

            processing_time.append(processing_time_item)

        response_formats = []
        _response_formats = d.pop("response_formats")
        for response_formats_item_data in _response_formats:
            response_formats_item = ChatFormatCount.from_dict(response_formats_item_data)

            response_formats.append(response_formats_item)

        by_bot = []
        _by_bot = d.pop("by_bot")
        for by_bot_item_data in _by_bot:
            by_bot_item = ChatBotCount.from_dict(by_bot_item_data)

            by_bot.append(by_bot_item)

        chat_distribution_response = cls(
            processing_time=processing_time,
            response_formats=response_formats,
            by_bot=by_bot,
        )

        chat_distribution_response.additional_properties = d
        return chat_distribution_response

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
