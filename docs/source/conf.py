# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import datetime

# -- Project information -----------------------------------------------------

project = 'micromechanics-indentationGUI'
copyright = u'2022-{}, Micromechanics team'.format(datetime.datetime.now().year)
author = u'Micromechanics team'

# The full version, including alpha/beta/rc tags
version = "0.2.5"
release = version

# -- General configuration ---------------------------------------------------
# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_title = 'micromechanics-indentationGUI documentation'
html_short_title = project
html_logo = 'img/logo_white.png'
html_favicon = 'img/logo_32x32.png'
html_baseurl = 'https://micromechanics.github.io/indentationGUI/'
html_context = {
    "display_github": True,
    "github_user": "micromechanics",
    "github_repo": "indentationGUI",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['img']
html_extra_path = ['robots.txt', 'sitemap.xml']
html_css_files = ['custom.css']
html_js_files = ['copy-code.js']


def _set_homepage_pageurl(app, pagename, templatename, context, doctree):
    if pagename == 'index':
        context['pageurl'] = html_baseurl


def setup(app):
    app.connect('html-page-context', _set_homepage_pageurl)
