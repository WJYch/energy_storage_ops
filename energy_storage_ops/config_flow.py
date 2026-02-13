"""Config flow for Energy Storage Ops integration."""
from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

# ⚠️ 这里的 DOMAIN 必须和你文件夹名字一模一样！
DOMAIN = "energy_storage_ops"

class EnergyStorageOpsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Energy Storage Ops."""

    # 这里的 VERSION 必须和 __init__.py 里的保持一致（如果没有就写1）
    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        # 如果用户点击了“提交”
        if user_input is not None:
            # 创建集成条目，title 是你在 HA 列表里看到的名字
            return self.async_create_entry(title="储能运营策略", data=user_input)

        # 显示配置表单（默认空表单，直接点提交即可）
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )