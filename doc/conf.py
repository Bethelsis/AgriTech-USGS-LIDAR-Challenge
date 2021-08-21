
import os
import sys
sys.path.insert(0, os.path.abspath('../source'))
extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'


master_doc = 'index'


project = 'Lidar data module'
copyright = '2021'
author = 'Bethelhem Sisay'


version = '0.1'

release = '0.1'


language = None


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


pygments_style = 'sphinx'

todo_include_todos = False



html_theme = 'sphinx_rtd_theme'


html_static_path = []


html_sidebars = {
    '**': [
        'relations.html',  
        'searchbox.html',
    ]
}


htmlhelp_basename = 'Lidar data fetch'



latex_elements = {


latex_documents = [
    (master_doc, 'lidar.tex', 'lidar Documentation',
     'Bethelhem', 'manual'),
]



man_pages = [
    (master_doc, 'Lidar', 'lidar Documentation',
     [author], 1)
]


texinfo_documents = [
    (master_doc, 'lidar', 'Lidar documentation',
     author, 'Bethelhem sisay', 'Lidar'),
]



