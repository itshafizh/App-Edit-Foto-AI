class ThemeManager:
    """
    Defines every available VisionEdit AI theme as a set of CSS
    custom-property overrides, and renders a small runtime <style>
    block that overrides style.css's :root values for the active
    theme — no page reload, no widget replacement, no layout change.
    """

    THEMES = {

        "Purple Gradient": {
            "--primary": "#7C3AED",
            "--secondary": "#8B5CF6",
            "--accent": "#A855F7",
            "--bg1": "#0F172A",
            "--bg2": "#17152E",
            "--bg3": "#261A4D",
            "--primary-rgb": "124,58,237",
        },

        "Blue Ocean": {
            "--primary": "#2563EB",
            "--secondary": "#3B82F6",
            "--accent": "#38BDF8",
            "--bg1": "#0B1120",
            "--bg2": "#0F1B2E",
            "--bg3": "#122A45",
            "--primary-rgb": "37,99,235",
        },

        "Emerald": {
            "--primary": "#059669",
            "--secondary": "#10B981",
            "--accent": "#34D399",
            "--bg1": "#081510",
            "--bg2": "#0C1F17",
            "--bg3": "#123326",
            "--primary-rgb": "5,150,105",
        },

        "Sunset": {
            "--primary": "#EA580C",
            "--secondary": "#F97316",
            "--accent": "#FB923C",
            "--bg1": "#1A0F0A",
            "--bg2": "#2A140D",
            "--bg3": "#3D1D0F",
            "--primary-rgb": "234,88,12",
        },

        # Note: a fully light (white background / dark text) theme
        # is not achievable without also making every hardcoded text
        # color in style.css variable-driven, which is out of scope
        # here. This is a lighter, softer variant of the dark palette
        # that keeps the existing white/light-gray text legible.
        "Light": {
            "--primary": "#7C3AED",
            "--secondary": "#8B5CF6",
            "--accent": "#A855F7",
            "--bg1": "#1E2536",
            "--bg2": "#242B44",
            "--bg3": "#2E3555",
            "--primary-rgb": "124,58,237",
        },

    }

    DEFAULT_THEME = "Purple Gradient"

    @classmethod
    def get_theme_names(cls):
        """Returns the list of available theme names, in display order."""

        return list(cls.THEMES.keys())

    @classmethod
    def get_theme_css(cls, theme_name):
        """
        Builds a small <style> block containing only a :root override
        with this theme's CSS variables. Falls back to the default
        theme if an unrecognized name is passed in.
        """

        variables = cls.THEMES.get(
            theme_name,
            cls.THEMES[cls.DEFAULT_THEME]
        )

        declarations = "\n".join(
            f"    {key}:{value};" for key, value in variables.items()
        )

        return f"<style>\n:root{{\n{declarations}\n}}\n</style>"

    @classmethod
    def inject(cls, theme_name):
        """
        Renders the runtime theme override into the page. Must be
        called on every script run (from app.py) so every page picks
        up the currently selected theme without a reload.
        """

        import streamlit as st

        st.markdown(
            cls.get_theme_css(theme_name),
            unsafe_allow_html=True
        )