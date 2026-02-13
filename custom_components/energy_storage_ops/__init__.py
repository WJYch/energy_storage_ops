
"""
The "Energy Storage Ops" custom component.
Place this folder in /config/custom_components/energy_storage_ops/
"""
from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "energy_storage_ops"
_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "switch", "number", "time"]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the ESS Ops component."""
    hass.data.setdefault(DOMAIN, {})
    _LOGGER.info("Setting up Energy Storage Ops integration")
    
    # In a real scenario, you might initialize a shared coordinator or API client here
    # hass.data[DOMAIN]['api'] = MyEssApi(...)

    # Forward setup to all platforms
    for platform in PLATFORMS:
        hass.helpers.discovery.load_platform(platform, DOMAIN, {}, config)
        
    return True
