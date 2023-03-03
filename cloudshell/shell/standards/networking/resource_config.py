from __future__ import annotations

from attrs import define

import cloudshell.shell.standards.attribute_names as attr_name
from cloudshell.shell.standards.core.resource_conf import attr
from cloudshell.shell.standards.resource_config_generic_models import (
    GenericBackupConfig,
    GenericCLIConfig,
    GenericConsoleServerConfig,
    GenericSnmpConfig,
)


@define(slots=False, str=False)
class NetworkingResourceConfig(
    GenericSnmpConfig, GenericCLIConfig, GenericConsoleServerConfig, GenericBackupConfig
):
    vrf_management_name: str = attr(attr_name.VRF_MANAGEMENT_NAME)
