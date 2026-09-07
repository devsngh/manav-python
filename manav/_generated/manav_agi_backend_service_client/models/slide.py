from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slide_chart import SlideChart


T = TypeVar("T", bound="Slide")


@_attrs_define
class Slide:
    """
    Attributes:
        id (str | Unset):  Default: ''.
        heading (str | Unset):  Default: ''.
        content (str | Unset):  Default: ''.
        image_url (str | Unset):  Default: ''.
        image_position (str | Unset):  Default: 'none'.
        mermaid (str | Unset):  Default: ''.
        chart (None | SlideChart | Unset):
    """

    id: str | Unset = ""
    heading: str | Unset = ""
    content: str | Unset = ""
    image_url: str | Unset = ""
    image_position: str | Unset = "none"
    mermaid: str | Unset = ""
    chart: None | SlideChart | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.slide_chart import SlideChart  # noqa: PLC0415

        id = self.id

        heading = self.heading

        content = self.content

        image_url = self.image_url

        image_position = self.image_position

        mermaid = self.mermaid

        chart: dict[str, Any] | None | Unset
        if isinstance(self.chart, Unset):
            chart = UNSET
        elif isinstance(self.chart, SlideChart):
            chart = self.chart.to_dict()
        else:
            chart = self.chart

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if heading is not UNSET:
            field_dict["heading"] = heading
        if content is not UNSET:
            field_dict["content"] = content
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if image_position is not UNSET:
            field_dict["image_position"] = image_position
        if mermaid is not UNSET:
            field_dict["mermaid"] = mermaid
        if chart is not UNSET:
            field_dict["chart"] = chart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slide_chart import SlideChart  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        heading = d.pop("heading", UNSET)

        content = d.pop("content", UNSET)

        image_url = d.pop("image_url", UNSET)

        image_position = d.pop("image_position", UNSET)

        mermaid = d.pop("mermaid", UNSET)

        def _parse_chart(data: object) -> None | SlideChart | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chart_type_0 = SlideChart.from_dict(data)

                return chart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlideChart | Unset, data)

        chart = _parse_chart(d.pop("chart", UNSET))

        slide = cls(
            id=id,
            heading=heading,
            content=content,
            image_url=image_url,
            image_position=image_position,
            mermaid=mermaid,
            chart=chart,
        )

        slide.additional_properties = d
        return slide

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
