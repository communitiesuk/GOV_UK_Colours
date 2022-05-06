"""paragraph component"""
from enum import Enum
from typing import Union

from dash import html


class ParagraphSizes(str, Enum):
    """Enum class to specify the allowed paragraph sizes"""

    LEAD = "govuk-body-l"
    DEFAULT = "govuk-body"
    SMALL = "govuk-body-s"


def paragraph(
    children: Union[str, list], size: ParagraphSizes = ParagraphSizes.DEFAULT
) -> html.P:
    """Create a <p> Html component with the children provided"""
    if size not in list(ParagraphSizes):
        raise ValueError(
            f"Size {size} is not a valid paragraph size (use ParagraphSize enum)."
        )

    return html.P(
        children,
        className=size,
    )
