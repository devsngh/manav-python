from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_option import FieldOption
    from ..models.field_validation import FieldValidation
    from ..models.file_config import FileConfig


T = TypeVar("T", bound="CredentialFieldDefinition")


@_attrs_define
class CredentialFieldDefinition:
    """
    Attributes:
        key (str):
        label (str):
        type_ (str):
        required (bool | Unset):  Default: True.
        placeholder (None | str | Unset):
        default_value (Any | None | Unset):
        help_text (None | str | Unset):
        validation (FieldValidation | None | Unset):
        options (list[FieldOption] | None | Unset):
        file_config (FileConfig | None | Unset):
        encrypted (bool | Unset):  Default: False.
        advanced (bool | Unset):  Default: False.
        order (int | Unset):  Default: 0.
        source (str | Unset):  Default: 'custom'.
    """

    key: str
    label: str
    type_: str
    required: bool | Unset = True
    placeholder: None | str | Unset = UNSET
    default_value: Any | None | Unset = UNSET
    help_text: None | str | Unset = UNSET
    validation: FieldValidation | None | Unset = UNSET
    options: list[FieldOption] | None | Unset = UNSET
    file_config: FileConfig | None | Unset = UNSET
    encrypted: bool | Unset = False
    advanced: bool | Unset = False
    order: int | Unset = 0
    source: str | Unset = "custom"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_validation import FieldValidation  # noqa: PLC0415
        from ..models.file_config import FileConfig  # noqa: PLC0415

        key = self.key

        label = self.label

        type_ = self.type_

        required = self.required

        placeholder: None | str | Unset
        if isinstance(self.placeholder, Unset):
            placeholder = UNSET
        else:
            placeholder = self.placeholder

        default_value: Any | None | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        help_text: None | str | Unset
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

        validation: dict[str, Any] | None | Unset
        if isinstance(self.validation, Unset):
            validation = UNSET
        elif isinstance(self.validation, FieldValidation):
            validation = self.validation.to_dict()
        else:
            validation = self.validation

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)

        else:
            options = self.options

        file_config: dict[str, Any] | None | Unset
        if isinstance(self.file_config, Unset):
            file_config = UNSET
        elif isinstance(self.file_config, FileConfig):
            file_config = self.file_config.to_dict()
        else:
            file_config = self.file_config

        encrypted = self.encrypted

        advanced = self.advanced

        order = self.order

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "type": type_,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if help_text is not UNSET:
            field_dict["help_text"] = help_text
        if validation is not UNSET:
            field_dict["validation"] = validation
        if options is not UNSET:
            field_dict["options"] = options
        if file_config is not UNSET:
            field_dict["file_config"] = file_config
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if order is not UNSET:
            field_dict["order"] = order
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_option import FieldOption  # noqa: PLC0415
        from ..models.field_validation import FieldValidation  # noqa: PLC0415
        from ..models.file_config import FileConfig  # noqa: PLC0415

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        type_ = d.pop("type")

        required = d.pop("required", UNSET)

        def _parse_placeholder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placeholder = _parse_placeholder(d.pop("placeholder", UNSET))

        def _parse_default_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        def _parse_help_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        help_text = _parse_help_text(d.pop("help_text", UNSET))

        def _parse_validation(data: object) -> FieldValidation | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                validation_type_0 = FieldValidation.from_dict(data)

                return validation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FieldValidation | None | Unset, data)

        validation = _parse_validation(d.pop("validation", UNSET))

        def _parse_options(data: object) -> list[FieldOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in _options_type_0:
                    options_type_0_item = FieldOption.from_dict(options_type_0_item_data)

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FieldOption] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_file_config(data: object) -> FileConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                file_config_type_0 = FileConfig.from_dict(data)

                return file_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileConfig | None | Unset, data)

        file_config = _parse_file_config(d.pop("file_config", UNSET))

        encrypted = d.pop("encrypted", UNSET)

        advanced = d.pop("advanced", UNSET)

        order = d.pop("order", UNSET)

        source = d.pop("source", UNSET)

        credential_field_definition = cls(
            key=key,
            label=label,
            type_=type_,
            required=required,
            placeholder=placeholder,
            default_value=default_value,
            help_text=help_text,
            validation=validation,
            options=options,
            file_config=file_config,
            encrypted=encrypted,
            advanced=advanced,
            order=order,
            source=source,
        )

        credential_field_definition.additional_properties = d
        return credential_field_definition

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
