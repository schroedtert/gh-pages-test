# Copyright © 2012-2023 Forschungszentrum Jülich GmbH
# SPDX-License-Identifier: LGPL-3.0-or-later
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime

project = "Test"
copyright = (
    f"{datetime.datetime.today().year}"
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_context = {"default_mode": "light"}


html_theme_options = {
    "switcher": {
        "json_url": "https://schroedtert.github.io/gh-pages-test/versions.json",
        "version_match": "foo",
    },
    "home_page_in_toc": False,
    "use_fullscreen_button": False,
    "use_issues_button": False,
    "use_download_button": False,
    "primary_sidebar_end": ["version-switcher"],
}

# -- Options for EPUB output
epub_show_urls = "footnote"