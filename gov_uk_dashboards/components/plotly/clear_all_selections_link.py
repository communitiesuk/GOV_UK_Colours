"""clear_all_selections_link"""
from dash import html


def clear_all_selections_link():
    """
    Clear all selections link which is aligned to the right
    """
    return html.A(
        "Clear all selections",
        href="?",
        className="govuk-link govuk-body govuk-!-padding-bottom-6",
        style={"float": "right"},
    )
