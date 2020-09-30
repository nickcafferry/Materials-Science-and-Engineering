# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath("../../manim/"))

project = u'Materials Science and Engineering'
copyright = u'- Wei MEI (Nick Cafferry)'
author = u'Wei MEI'


version = '0.1.3'
release = '0.1.3'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx.ext.graphviz',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram'
    
]

autoclass_content = 'both'
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'english'
html_search_language = 'english'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'remain']
pygments_style = 'default'

html_static_path = ['jmol-14.31.7']
html_theme = 'agogo'
html_theme_options = {
    'footerbg ': '#FFFF93',
    'headerbg': '#FF2D2D',
}
html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html','playground.html'],
}
