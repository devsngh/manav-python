from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_log_response_extra_type_0 import SystemLogResponseExtraType0


T = TypeVar("T", bound="SystemLogResponse")


@_attrs_define
class SystemLogResponse:
    """
    Attributes:
        id (UUID):
        level (str):
        category (str):
        message (str):
        created_at (datetime.datetime):
        logger_name (None | str | Unset):
        request_id (None | str | Unset):
        method (None | str | Unset):
        path (None | str | Unset):
        status_code (int | None | Unset):
        latency_ms (float | None | Unset):
        client_ip (None | str | Unset):
        user_id (None | Unset | UUID):
        user_email (None | str | Unset):
        exception_type (None | str | Unset):
        exception_msg (None | str | Unset):
        traceback (None | str | Unset):
        extra (None | SystemLogResponseExtraType0 | Unset):
        org_id (None | Unset | UUID):
    """

    id: UUID
    level: str
    category: str
    message: str
    created_at: datetime.datetime
    logger_name: None | str | Unset = UNSET
    request_id: None | str | Unset = UNSET
    method: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    status_code: int | None | Unset = UNSET
    latency_ms: float | None | Unset = UNSET
    client_ip: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    user_email: None | str | Unset = UNSET
    exception_type: None | str | Unset = UNSET
    exception_msg: None | str | Unset = UNSET
    traceback: None | str | Unset = UNSET
    extra: None | SystemLogResponseExtraType0 | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_log_response_extra_type_0 import SystemLogResponseExtraType0  # noqa: PLC0415

        id = str(self.id)

        level = self.level

        category = self.category

        message = self.message

        created_at = self.created_at.isoformat()

        logger_name: None | str | Unset
        if isinstance(self.logger_name, Unset):
            logger_name = UNSET
        else:
            logger_name = self.logger_name

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        latency_ms: float | None | Unset
        if isinstance(self.latency_ms, Unset):
            latency_ms = UNSET
        else:
            latency_ms = self.latency_ms

        client_ip: None | str | Unset
        if isinstance(self.client_ip, Unset):
            client_ip = UNSET
        else:
            client_ip = self.client_ip

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        exception_type: None | str | Unset
        if isinstance(self.exception_type, Unset):
            exception_type = UNSET
        else:
            exception_type = self.exception_type

        exception_msg: None | str | Unset
        if isinstance(self.exception_msg, Unset):
            exception_msg = UNSET
        else:
            exception_msg = self.exception_msg

        traceback: None | str | Unset
        if isinstance(self.traceback, Unset):
            traceback = UNSET
        else:
            traceback = self.traceback

        extra: dict[str, Any] | None | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, SystemLogResponseExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "level": level,
                "category": category,
                "message": message,
                "created_at": created_at,
            }
        )
        if logger_name is not UNSET:
            field_dict["logger_name"] = logger_name
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if latency_ms is not UNSET:
            field_dict["latency_ms"] = latency_ms
        if client_ip is not UNSET:
            field_dict["client_ip"] = client_ip
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if exception_type is not UNSET:
            field_dict["exception_type"] = exception_type
        if exception_msg is not UNSET:
            field_dict["exception_msg"] = exception_msg
        if traceback is not UNSET:
            field_dict["traceback"] = traceback
        if extra is not UNSET:
            field_dict["extra"] = extra
        if org_id is not UNSET:
            field_dict["org_id"] = org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_log_response_extra_type_0 import SystemLogResponseExtraType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        level = d.pop("level")

        category = d.pop("category")

        message = d.pop("message")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_logger_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logger_name = _parse_logger_name(d.pop("logger_name", UNSET))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("request_id", UNSET))

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("status_code", UNSET))

        def _parse_latency_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms", UNSET))

        def _parse_client_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_ip = _parse_client_ip(d.pop("client_ip", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_exception_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_type = _parse_exception_type(d.pop("exception_type", UNSET))

        def _parse_exception_msg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_msg = _parse_exception_msg(d.pop("exception_msg", UNSET))

        def _parse_traceback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        traceback = _parse_traceback(d.pop("traceback", UNSET))

        def _parse_extra(data: object) -> None | SystemLogResponseExtraType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = SystemLogResponseExtraType0.from_dict(data)

                return extra_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemLogResponseExtraType0 | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        system_log_response = cls(
            id=id,
            level=level,
            category=category,
            message=message,
            created_at=created_at,
            logger_name=logger_name,
            request_id=request_id,
            method=method,
            path=path,
            status_code=status_code,
            latency_ms=latency_ms,
            client_ip=client_ip,
            user_id=user_id,
            user_email=user_email,
            exception_type=exception_type,
            exception_msg=exception_msg,
            traceback=traceback,
            extra=extra,
            org_id=org_id,
        )

        system_log_response.additional_properties = d
        return system_log_response

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
