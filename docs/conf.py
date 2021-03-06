#!/usr/bin/env python
#
# cloup documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os

import cloup

# import sys
# sys.path.insert(0, os.path.abspath('..'))
PROJ_DIR = os.path.abspath(os.path.join(__file__, '..', '..'))

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'autoapi.extension',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc.typehints',
    'sphinx_panels',
    'sphinx_copybutton',  # adds a copy button to code blocks
]

autoclass_content = 'both'
autodoc_typehints = 'description'

autoapi_type = 'python'
autoapi_dirs = [os.path.join(PROJ_DIR, 'cloup')]
autoapi_template_dir = '_autoapi_templates'
autoapi_keep_files = True
# autoapi_add_toctree_entry = False
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'Click': ('https://click.palletsprojects.com', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = [autoapi_template_dir]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'cloup'
copyright = "2020, Gianluca Gippetto"
author = "Gianluca Gippetto"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = cloup.__version__
# The full version, including alpha/beta/rc tags.
release = cloup.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = "Cloup v{version}".format(version=version)
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/janluke/cloup",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def primary_color_rgba(alpha=1.0):
    return "rgba(0, 113, 188, %f)" % alpha

panels_css_variables = {
    "tabs-color-label-active": primary_color_rgba(),
    "tabs-color-label-inactive": primary_color_rgba(0.5),
    "tabs-color-overline": primary_color_rgba(0.2),
    # "tabs-color-underline": "rgb(207, 236, 238)",
    # "tabs-size-label": "1rem",
}
panels_add_bootstrap_css = False
html_css_files = [
    'styles/copybutton-overrides.css',
    'styles/tabs-overrides.css',
    'styles/theme-overrides.css',
]

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'cloupdoc'

# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'cloup.tex',
     'cloup Documentation',
     'Gianluca Gippetto', 'manual'),
]

# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'cloup',
     'cloup Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'cloup',
     'cloup Documentation',
     author,
     'cloup',
     'One line description of project.',
     'Miscellaneous'),
]
