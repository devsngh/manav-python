from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voice_gen_request_metadata_type_0 import VoiceGenRequestMetadataType0


T = TypeVar("T", bound="VoiceGenRequest")


@_attrs_define
class VoiceGenRequest:
    """
    Attributes:
        text (str):
        voice_id (None | str | Unset): Provider-specific voice id
        model_id (None | str | Unset):
        output_format (str | Unset):  Default: 'mp3_44100_128'.
        language_code (None | str | Unset):
        stability (float | None | Unset):
        similarity_boost (float | None | Unset):
        style_exaggeration (float | None | Unset):
        from_persona_id (None | Unset | UUID):
        explicit_datasource_id (None | Unset | UUID):
        source_dept (str | Unset):  Default: 'generic'.
        source_agent_id (None | Unset | UUID):
        source_user_id (None | Unset | UUID):
        metadata (None | Unset | VoiceGenRequestMetadataType0):
    """

    text: str
    voice_id: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    output_format: str | Unset = "mp3_44100_128"
    language_code: None | str | Unset = UNSET
    stability: float | None | Unset = UNSET
    similarity_boost: float | None | Unset = UNSET
    style_exaggeration: float | None | Unset = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    explicit_datasource_id: None | Unset | UUID = UNSET
    source_dept: str | Unset = "generic"
    source_agent_id: None | Unset | UUID = UNSET
    source_user_id: None | Unset | UUID = UNSET
    metadata: None | Unset | VoiceGenRequestMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.voice_gen_request_metadata_type_0 import VoiceGenRequestMetadataType0  # noqa: PLC0415

        text = self.text

        voice_id: None | str | Unset
        if isinstance(self.voice_id, Unset):
            voice_id = UNSET
        else:
            voice_id = self.voice_id

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        output_format = self.output_format

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        stability: float | None | Unset
        if isinstance(self.stability, Unset):
            stability = UNSET
        else:
            stability = self.stability

        similarity_boost: float | None | Unset
        if isinstance(self.similarity_boost, Unset):
            similarity_boost = UNSET
        else:
            similarity_boost = self.similarity_boost

        style_exaggeration: float | None | Unset
        if isinstance(self.style_exaggeration, Unset):
            style_exaggeration = UNSET
        else:
            style_exaggeration = self.style_exaggeration

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        explicit_datasource_id: None | str | Unset
        if isinstance(self.explicit_datasource_id, Unset):
            explicit_datasource_id = UNSET
        elif isinstance(self.explicit_datasource_id, UUID):
            explicit_datasource_id = str(self.explicit_datasource_id)
        else:
            explicit_datasource_id = self.explicit_datasource_id

        source_dept = self.source_dept

        source_agent_id: None | str | Unset
        if isinstance(self.source_agent_id, Unset):
            source_agent_id = UNSET
        elif isinstance(self.source_agent_id, UUID):
            source_agent_id = str(self.source_agent_id)
        else:
            source_agent_id = self.source_agent_id

        source_user_id: None | str | Unset
        if isinstance(self.source_user_id, Unset):
            source_user_id = UNSET
        elif isinstance(self.source_user_id, UUID):
            source_user_id = str(self.source_user_id)
        else:
            source_user_id = self.source_user_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, VoiceGenRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if stability is not UNSET:
            field_dict["stability"] = stability
        if similarity_boost is not UNSET:
            field_dict["similarity_boost"] = similarity_boost
        if style_exaggeration is not UNSET:
            field_dict["style_exaggeration"] = style_exaggeration
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if explicit_datasource_id is not UNSET:
            field_dict["explicit_datasource_id"] = explicit_datasource_id
        if source_dept is not UNSET:
            field_dict["source_dept"] = source_dept
        if source_agent_id is not UNSET:
            field_dict["source_agent_id"] = source_agent_id
        if source_user_id is not UNSET:
            field_dict["source_user_id"] = source_user_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voice_gen_request_metadata_type_0 import VoiceGenRequestMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        def _parse_voice_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_id = _parse_voice_id(d.pop("voice_id", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        output_format = d.pop("output_format", UNSET)

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("language_code", UNSET))

        def _parse_stability(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stability = _parse_stability(d.pop("stability", UNSET))

        def _parse_similarity_boost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        similarity_boost = _parse_similarity_boost(d.pop("similarity_boost", UNSET))

        def _parse_style_exaggeration(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        style_exaggeration = _parse_style_exaggeration(d.pop("style_exaggeration", UNSET))

        def _parse_from_persona_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_persona_id_type_0 = UUID(data)

                return from_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        from_persona_id = _parse_from_persona_id(d.pop("from_persona_id", UNSET))

        def _parse_explicit_datasource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                explicit_datasource_id_type_0 = UUID(data)

                return explicit_datasource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        explicit_datasource_id = _parse_explicit_datasource_id(d.pop("explicit_datasource_id", UNSET))

        source_dept = d.pop("source_dept", UNSET)

        def _parse_source_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_agent_id_type_0 = UUID(data)

                return source_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_agent_id = _parse_source_agent_id(d.pop("source_agent_id", UNSET))

        def _parse_source_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_user_id_type_0 = UUID(data)

                return source_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_user_id = _parse_source_user_id(d.pop("source_user_id", UNSET))

        def _parse_metadata(data: object) -> None | Unset | VoiceGenRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = VoiceGenRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VoiceGenRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        voice_gen_request = cls(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format=output_format,
            language_code=language_code,
            stability=stability,
            similarity_boost=similarity_boost,
            style_exaggeration=style_exaggeration,
            from_persona_id=from_persona_id,
            explicit_datasource_id=explicit_datasource_id,
            source_dept=source_dept,
            source_agent_id=source_agent_id,
            source_user_id=source_user_id,
            metadata=metadata,
        )

        voice_gen_request.additional_properties = d
        return voice_gen_request

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
