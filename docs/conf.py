import datetime
import importlib.metadata

project = "ics-query"
this_year = datetime.date.today().year
copyright = f"{this_year}, Nicco Kunzmann"
release = version = importlib.metadata.version("ics-query")

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
]

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/pycalendar/ics-query",
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/ics-query",
            "icon": "fa-solid fa-download",
            "type": "fontawesome",
        },
    ],
}
