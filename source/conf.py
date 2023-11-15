# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Textual Programming in Python'
copyright = '2023, Petlja'
author = 'Petlja'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ "myst_parser",
               "sphinx_design",
               #"sphinxpackagingtool.builder.petlja_builder",
               "petlja_sphinx_extensions.extensions.notes",
               "petlja_sphinx_extensions.extensions.multiple_choice",            
               "petlja_sphinx_extensions.extensions.fill_in_the_blank",
               "petlja_sphinx_extensions.extensions.py_code"]

myst_enable_extensions = [ "colon_fence",
                           "dollarmath",
                           "html_admonition" ]

language = 'en'
templates_path = ['_templates']
exclude_patterns = []

import petlja_sphinx_extensions
html_static_path = petlja_sphinx_extensions.extensions.static_dirs()


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_title = 'Textual Programming in Python'


html_theme = 'alabaster'
html_theme_options = {
    'show_powered_by' : False,
    'caption_font_size': '32px',
    'caption_font_family': 'Source Sans Pro',
    'font_family': 'Source Sans Pro',
    'font_size': '16px',
    'pre_bg' : '#f8f8f8',
    'page_width': '840px',
}
html_css_files = [
    'https://fonts.googleapis.com/css?family=Source+Sans+Pro',
]
#html_context = {
#    'theme_nosidebar': True,
#}
html_show_copyright = False
html_show_sourcelink = False

