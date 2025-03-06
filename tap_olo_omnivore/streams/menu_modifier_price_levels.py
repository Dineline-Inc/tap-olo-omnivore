from __future__ import annotations

from tap_olo_omnivore.client import OloOmnivoreStream
from tap_olo_omnivore.streams.menu_modifiers import MenuModifiersStream


class MenuModifierPriceLevelsStream(OloOmnivoreStream):
    """Child stream for retrieving price levels for a given menu modifier from the Omnivore API."""

    name = "menu_modifier_price_levels"
    primary_keys = ["id"]
    replication_key = None
    parent_stream_type = MenuModifiersStream

    @property
    def path(self) -> str:
        """Construct the URL path using the location_id from config and the menu_modifier_id from parent context."""
        location_id = self.context.get("location_id")
        menu_modifier_id = self.context.get("menu_modifier_id")
        return (
            f"/locations/{location_id}/menu/modifiers/{menu_modifier_id}/price_levels"
        )
