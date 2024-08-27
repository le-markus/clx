import logging
from abc import abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from attrs import define


if TYPE_CHECKING:
    from clx_common.messaging.base_classes import Payload
    from clx_common.operation import Operation
    from clx_common.utils.copy_dir_group_data import CopyDirGroupData
    from clx_common.utils.copy_file_data import CopyFileData

logger = logging.getLogger(__name__)


@define
class Backend(AbstractAsyncContextManager):
    @abstractmethod
    async def execute_operation(
        self, operation: "Operation", payload: "Payload"
    ) -> None: ...

    async def __aenter__(self) -> "Backend":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return None

    @abstractmethod
    async def wait_for_completion(self, max_wait_time: float | None = None) -> bool: ...

    @abstractmethod
    async def copy_file_to_output(self, copy_data: "CopyFileData"): ...

    @abstractmethod
    async def copy_dir_group_to_output(self, copy_data: "CopyDirGroupData"): ...