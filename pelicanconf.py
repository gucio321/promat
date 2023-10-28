AUTHOR = "The SKN PROMAT's Website Authors"
SITENAME = 'SKN PROMAT'
SITEURL = 'https://gucio321.github.io/promat'

THEME = "./theme"
#To publish the favicon of the theme, place the following lines in your pelicanconfig file:
STATIC_PATHS = ["static"]

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# modified theme:
# supports table with 2 columns
LINKS = (
        (
            ('Opiekun Koła: dr inż. Krystian Zyguła', 'https://skos.agh.edu.pl/osoba/krystian-zygula-9440.html'),
            ('E-mail: kzygula@agh.edu.pl', 'kzygula@agh.edu.pl'),
        ),
        (
            ('Strona stworzona przy pomocy narzędzia Pelican', 'https://pelican.org'),
            ('Źródło motywu strony', 'https://github.com/gregseth/bluegrasshopper-theme'),
        ),
)

# Social widget
SOCIAL = (('Naszym Facebooku', 'https://www.facebook.com/KNPROMATAGH'),
          ('Repozytorium kodu źródłowego na GitHub\'ie', 'httpS://github.com/gucio321/promat'),)

DEFAULT_PAGINATION = 10

DISPLAY_LOGOS = True
LOGOS = [
        {
            "URL": "/static/logo.png",
            "width": "150px",
            "height": "100px",
            "link": SITEURL,
        },
        {
            "URL": "/static/PPMiME-logo-150x150.png",
            "width": "150px",
            "height": "150px",
            "link": 'https://www.facebook.com/PPMiME.agh/',
        },
        {
            "URL": "/static/WIMiIP-logo-150x150.png",
            "width": "150px",
            "height": "150px",
            "link": "https://www.metal.agh.edu.pl",
        },
        {
            "URL": "/static/agh-logo-165x300.png",
            "width": "82px",
            "height": "150px",
            "link": "https://agh.edu.pl",
        },
]

SHOW_SITE_LOGO = True
SITE_LOGO = "static/logo.png"

PLUGINS = ["photos"]
PHOTO_LIBRARY = "photos"
PHOTO_INLINE_GALLERY_ENABLED = True
#PHOTO_LIBRARY = "photos"

DEFAULT_CATEGORY = "Nasza Działalność"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
