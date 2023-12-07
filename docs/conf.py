# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# this is relative path info
import os
import sys
sys.path.insert(0, os.path.abspath('..')) # change this from . to ..


# -- Project information -----------------------------------------------------

project = 'test_sphinx'
copyright = '2023, Tyler Ward'
author = 'Tyler Ward'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc", # add this to add additional module that searches for doc strings in python functions/.py files
    "sphinx.ext.napoleon", #looks for specific formats of doc strings; supports numpy and google doc strings formats
    # this above is minimum
    "myst_parser", # extension req for markdown : need to run "pip install myst-parser"
    "sphinx.ext.viewcode", # allow for link on html page to source code
    # below will eventually be required
    "sphinx.ext.githubpages" # adds .nojekyll file which tells hithub to not format build with jekyll
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster' # recommended to change the theme
# this will usually require installation, can find when searching for themes

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# also needed for myst_parser
source_suffix = ['.rst','.md'] # source_suffix = which file types to search for in docs, and then convert to html
# be default with search for .rst files only