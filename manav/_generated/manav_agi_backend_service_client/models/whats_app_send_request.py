from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_send_request_interactive_buttons_type_0_item import (
        WhatsAppSendRequestInteractiveButtonsType0Item,
    )
    from ..models.whats_app_send_request_metadata_type_0 import WhatsAppSendRequestMetadataType0
    from ..models.whats_app_send_request_template_variables_type_0 import WhatsAppSendRequestTemplateVariablesType0


T = TypeVar("T", bound="WhatsAppSendRequest")


@_attrs_define
class WhatsAppSendRequest:
    """
    Attributes:
        to (str): E.164 destination phone number
        body (None | str | Unset):
        from_number (None | str | Unset):
        media_url (None | str | Unset):
        media_caption (None | str | Unset):
        template_name (None | str | Unset):
        template_variables (None | Unset | WhatsAppSendRequestTemplateVariablesType0):
        interactive_buttons (list[WhatsAppSendRequestInteractiveButtonsType0Item] | None | Unset):
        from_persona_id (None | Unset | UUID):
        source_dept (str | Unset):  Default: 'generic'.
        source_agent_id (None | Unset | UUID):
        source_user_id (None | Unset | UUID):
        source_campaign_id (None | Unset | UUID):
        explicit_datasource_id (None | Unset | UUID):
        metadata (None | Unset | WhatsAppSendRequestMetadataType0):
    """

    to: str
    body: None | str | Unset = UNSET
    from_number: None | str | Unset = UNSET
    media_url: None | str | Unset = UNSET
    media_caption: None | str | Unset = UNSET
    template_name: None | str | Unset = UNSET
    template_variables: None | Unset | WhatsAppSendRequestTemplateVariablesType0 = UNSET
    interactive_buttons: list[WhatsAppSendRequestInteractiveButtonsType0Item] | None | Unset = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    source_dept: str | Unset = "generic"
    source_agent_id: None | Unset | UUID = UNSET
    source_user_id: None | Unset | UUID = UNSET
    source_campaign_id: None | Unset | UUID = UNSET
    explicit_datasource_id: None | Unset | UUID = UNSET
    metadata: None | Unset | WhatsAppSendRequestMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.whats_app_send_request_metadata_type_0 import WhatsAppSendRequestMetadataType0  # noqa: PLC0415
        from ..models.whats_app_send_request_template_variables_type_0 import (
            WhatsAppSendRequestTemplateVariablesType0,  # noqa: PLC0415
        )

        to = self.to

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        from_number: None | str | Unset
        if isinstance(self.from_number, Unset):
            from_number = UNSET
        else:
            from_number = self.from_number

        media_url: None | str | Unset
        if isinstance(self.media_url, Unset):
            media_url = UNSET
        else:
            media_url = self.media_url

        media_caption: None | str | Unset
        if isinstance(self.media_caption, Unset):
            media_caption = UNSET
        else:
            media_caption = self.media_caption

        template_name: None | str | Unset
        if isinstance(self.template_name, Unset):
            template_name = UNSET
        else:
            template_name = self.template_name

        template_variables: dict[str, Any] | None | Unset
        if isinstance(self.template_variables, Unset):
            template_variables = UNSET
        elif isinstance(self.template_variables, WhatsAppSendRequestTemplateVariablesType0):
            template_variables = self.template_variables.to_dict()
        else:
            template_variables = self.template_variables

        interactive_buttons: list[dict[str, Any]] | None | Unset
        if isinstance(self.interactive_buttons, Unset):
            interactive_buttons = UNSET
        elif isinstance(self.interactive_buttons, list):
            interactive_buttons = []
            for interactive_buttons_type_0_item_data in self.interactive_buttons:
                interactive_buttons_type_0_item = interactive_buttons_type_0_item_data.to_dict()
                interactive_buttons.append(interactive_buttons_type_0_item)

        else:
            interactive_buttons = self.interactive_buttons

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

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

        source_campaign_id: None | str | Unset
        if isinstance(self.source_campaign_id, Unset):
            source_campaign_id = UNSET
        elif isinstance(self.source_campaign_id, UUID):
            source_campaign_id = str(self.source_campaign_id)
        else:
            source_campaign_id = self.source_campaign_id

        explicit_datasource_id: None | str | Unset
        if isinstance(self.explicit_datasource_id, Unset):
            explicit_datasource_id = UNSET
        elif isinstance(self.explicit_datasource_id, UUID):
            explicit_datasource_id = str(self.explicit_datasource_id)
        else:
            explicit_datasource_id = self.explicit_datasource_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WhatsAppSendRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if from_number is not UNSET:
            field_dict["from_number"] = from_number
        if media_url is not UNSET:
            field_dict["media_url"] = media_url
        if media_caption is not UNSET:
            field_dict["media_caption"] = media_caption
        if template_name is not UNSET:
            field_dict["template_name"] = template_name
        if template_variables is not UNSET:
            field_dict["template_variables"] = template_variables
        if interactive_buttons is not UNSET:
            field_dict["interactive_buttons"] = interactive_buttons
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if source_dept is not UNSET:
            field_dict["source_dept"] = source_dept
        if source_agent_id is not UNSET:
            field_dict["source_agent_id"] = source_agent_id
        if source_user_id is not UNSET:
            field_dict["source_user_id"] = source_user_id
        if source_campaign_id is not UNSET:
            field_dict["source_campaign_id"] = source_campaign_id
        if explicit_datasource_id is not UNSET:
            field_dict["explicit_datasource_id"] = explicit_datasource_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_send_request_interactive_buttons_type_0_item import (
            WhatsAppSendRequestInteractiveButtonsType0Item,  # noqa: PLC0415
        )
        from ..models.whats_app_send_request_metadata_type_0 import WhatsAppSendRequestMetadataType0  # noqa: PLC0415
        from ..models.whats_app_send_request_template_variables_type_0 import (
            WhatsAppSendRequestTemplateVariablesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        to = d.pop("to")

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        def _parse_from_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_number = _parse_from_number(d.pop("from_number", UNSET))

        def _parse_media_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_url = _parse_media_url(d.pop("media_url", UNSET))

        def _parse_media_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_caption = _parse_media_caption(d.pop("media_caption", UNSET))

        def _parse_template_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_name = _parse_template_name(d.pop("template_name", UNSET))

        def _parse_template_variables(data: object) -> None | Unset | WhatsAppSendRequestTemplateVariablesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_variables_type_0 = WhatsAppSendRequestTemplateVariablesType0.from_dict(data)

                return template_variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WhatsAppSendRequestTemplateVariablesType0, data)

        template_variables = _parse_template_variables(d.pop("template_variables", UNSET))

        def _parse_interactive_buttons(
            data: object,
        ) -> list[WhatsAppSendRequestInteractiveButtonsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interactive_buttons_type_0 = []
                _interactive_buttons_type_0 = data
                for interactive_buttons_type_0_item_data in _interactive_buttons_type_0:
                    interactive_buttons_type_0_item = WhatsAppSendRequestInteractiveButtonsType0Item.from_dict(
                        interactive_buttons_type_0_item_data
                    )

                    interactive_buttons_type_0.append(interactive_buttons_type_0_item)

                return interactive_buttons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WhatsAppSendRequestInteractiveButtonsType0Item] | None | Unset, data)

        interactive_buttons = _parse_interactive_buttons(d.pop("interactive_buttons", UNSET))

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

        def _parse_source_campaign_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_campaign_id_type_0 = UUID(data)

                return source_campaign_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_campaign_id = _parse_source_campaign_id(d.pop("source_campaign_id", UNSET))

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

        def _parse_metadata(data: object) -> None | Unset | WhatsAppSendRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WhatsAppSendRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WhatsAppSendRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        whats_app_send_request = cls(
            to=to,
            body=body,
            from_number=from_number,
            media_url=media_url,
            media_caption=media_caption,
            template_name=template_name,
            template_variables=template_variables,
            interactive_buttons=interactive_buttons,
            from_persona_id=from_persona_id,
            source_dept=source_dept,
            source_agent_id=source_agent_id,
            source_user_id=source_user_id,
            source_campaign_id=source_campaign_id,
            explicit_datasource_id=explicit_datasource_id,
            metadata=metadata,
        )

        whats_app_send_request.additional_properties = d
        return whats_app_send_request

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
