from dataclasses import dataclass

@dataclass
class AutocompleteTag:
    """Represents a tag suggestion from autocomplete.

    Parameters:
        label: The full tag label including count (e.g., "hooves (95430)").
        value: The clean tag value (e.g., "hooves").
        type: The tag category (e.g., "general", "copyright").
    """

    #: The full tag label including count (e.g., "hooves (95430)").
    label: str
    #: The clean tag value without count information.
    value: str
    #: The category of the tag (general/copyright/other).
    type: str