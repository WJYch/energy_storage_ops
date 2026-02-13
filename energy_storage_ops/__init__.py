"""The Energy Storage Ops integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

# ⚠️ 确保 DOMAIN 一致
DOMAIN = "energy_storage_ops"

# 你要加载的实体类型
PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.SWITCH, Platform.NUMBER]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Energy Storage Ops from a config entry."""
    
    # 这一步是必须的，防止后续报错
    hass.data.setdefault(DOMAIN, {})

    # 加载 sensor, switch, number 等文件
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        # hass.data[DOMAIN].pop(entry.entry_id) # 如果存了数据可以清理
        pass

    return unload_ok