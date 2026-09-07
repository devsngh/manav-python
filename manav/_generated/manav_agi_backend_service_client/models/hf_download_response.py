from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.download_status import DownloadStatus

T = TypeVar("T", bound="HFDownloadResponse")


@_attrs_define
class HFDownloadResponse:
    """HF download response

    Attributes:
        id (UUID):
        repo_id (str):
        model_name (str):
        model_size_gb (float | None):
        download_status (DownloadStatus): HuggingFace download status
        progress_percentage (int):
        download_path (None | str):
        error_message (None | str):
        celery_task_id (None | str):
        is_registered (bool):
        registered_llm_id (None | UUID):
        started_at (datetime.datetime | None):
        completed_at (datetime.datetime | None):
        created_by (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    repo_id: str
    model_name: str
    model_size_gb: float | None
    download_status: DownloadStatus
    progress_percentage: int
    download_path: None | str
    error_message: None | str
    celery_task_id: None | str
    is_registered: bool
    registered_llm_id: None | UUID
    started_at: datetime.datetime | None
    completed_at: datetime.datetime | None
    created_by: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        repo_id = self.repo_id

        model_name = self.model_name

        model_size_gb: float | None
        model_size_gb = self.model_size_gb

        download_status = self.download_status.value

        progress_percentage = self.progress_percentage

        download_path: None | str
        download_path = self.download_path

        error_message: None | str
        error_message = self.error_message

        celery_task_id: None | str
        celery_task_id = self.celery_task_id

        is_registered = self.is_registered

        registered_llm_id: None | str
        if isinstance(self.registered_llm_id, UUID):
            registered_llm_id = str(self.registered_llm_id)
        else:
            registered_llm_id = self.registered_llm_id

        started_at: None | str
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: None | str
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_by = str(self.created_by)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "repo_id": repo_id,
                "model_name": model_name,
                "model_size_gb": model_size_gb,
                "download_status": download_status,
                "progress_percentage": progress_percentage,
                "download_path": download_path,
                "error_message": error_message,
                "celery_task_id": celery_task_id,
                "is_registered": is_registered,
                "registered_llm_id": registered_llm_id,
                "started_at": started_at,
                "completed_at": completed_at,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        repo_id = d.pop("repo_id")

        model_name = d.pop("model_name")

        def _parse_model_size_gb(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        model_size_gb = _parse_model_size_gb(d.pop("model_size_gb"))

        download_status = DownloadStatus(d.pop("download_status"))

        progress_percentage = d.pop("progress_percentage")

        def _parse_download_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        download_path = _parse_download_path(d.pop("download_path"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        def _parse_celery_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        celery_task_id = _parse_celery_task_id(d.pop("celery_task_id"))

        is_registered = d.pop("is_registered")

        def _parse_registered_llm_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registered_llm_id_type_0 = UUID(data)

                return registered_llm_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        registered_llm_id = _parse_registered_llm_id(d.pop("registered_llm_id"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_completed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        created_by = UUID(d.pop("created_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        hf_download_response = cls(
            id=id,
            repo_id=repo_id,
            model_name=model_name,
            model_size_gb=model_size_gb,
            download_status=download_status,
            progress_percentage=progress_percentage,
            download_path=download_path,
            error_message=error_message,
            celery_task_id=celery_task_id,
            is_registered=is_registered,
            registered_llm_id=registered_llm_id,
            started_at=started_at,
            completed_at=completed_at,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        hf_download_response.additional_properties = d
        return hf_download_response

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
