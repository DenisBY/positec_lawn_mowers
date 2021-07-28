import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_TYPE,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)


@callback
def configured_accounts(hass):
    """Return tuple of configured usernames."""
    entries = hass.config_entries.async_entries(DOMAIN)
    if entries:
        return (entry.data[CONF_USERNAME] for entry in entries)
    return ()


@config_entries.HANDLERS.register(DOMAIN)
class AudiConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    def __init__(self):
        """Initialize."""
        self._username = vol.UNDEFINED
        self._password = vol.UNDEFINED
        self._type = vol.UNDEFINED

    async def async_step_user(self, user_input=None):
        """Handle a user initiated config flow."""
        import pyworxcloud
        errors = {}
        dev = 0

        if user_input is not None:
            self._username = user_input[CONF_USERNAME]
            self._password = user_input[CONF_PASSWORD]
            self._type = user_input.get(CONF_TYPE)

            try:
                # pylint: disable=no-value-for-parameter
                master = pyworxcloud.WorxCloud()
                session = async_get_clientsession(self.hass)
                auth = await master.initialize(vol.Email()(self._username), self._password, self._type)

            except vol.Invalid:
                errors[CONF_USERNAME] = "invalid_username"
            except Exception:
                errors["base"] = "invalid_credentials"
