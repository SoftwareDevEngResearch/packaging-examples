# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'simple-packaging'
copyright = '2025, Kyle Niemeyer'
author = 'Kyle Niemeyer'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

napoleon_numpy_docstring = True

intersphinx_mapping = {
  'python': ('https://docs.python.org/3.11', None),
  'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
  'numpy': ('https://docs.scipy.org/doc/numpy/', None),
}

autodoc_default_options = {'members': True}
autoclass_content = 'class'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
