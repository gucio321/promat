AUTHOR = "The SKN PROMAT's Website Authors"
SITENAME = 'SKN PROMAT'
SITEURL = 'https://gucio321.github.io/promat'

THEME = "./theme"
#To publish the favicon of the theme, place the following lines in your pelicanconfig file:
#FILES_TO_COPY = (('pelican-bgh/static/favicon.ico', 'favicon.ico'),)

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
LINKS = (('Opiekun koła: dr hab. inż. Marek Wojtaszek, prof AGH', 'https://skos.agh.edu.pl/osoba/marek-wojtaszek-5026.html'),
         ('E-mail: mwojtasz@metal.agh.edu.pl', 'mwojtasz@metal.agh.edu.pl'),
         ('Opiekun Koła: mgr inż. Krystian Zyguła', 'https://skos.agh.edu.pl/osoba/krystian-zygula-9440.html'),
         ('E-mail: kzygula@agh.edu.pl', 'kzygula@agh.edu.pl'),
         ('Strona stworzona przy pomocy narzędzia Pelican', 'https://pelican.org'),
         ('Źródło motywu strony', 'https://github.com/gregseth/bluegrasshopper-theme'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISPLAY_LOGOS = True
LOGOS = [
        {
            "URL": "http://www.promat.agh.edu.pl/wp-content/uploads/elementor/thumbs/PROMAT2-p6gtyu2gmoj9xiwzo45ibl2q9lmy2y8q5dkc13adow.png",
            "width": "100px",
            "height": "80px",
        },
        {
            "URL": "http://www.promat.agh.edu.pl/wp-content/uploads/elementor/thumbs/agh-logo_beztla-p6gtyofd1yrplq1fk5lu19b9bj71rur11ad6hyb8y0.png",
            "width": "80px",
            "height": "120px",
        }
]

PLUGINS = ["photos"]
PHOTO_LIBRARY = "photos"
PHOTO_INLINE_GALLERY_ENABLED = True
#PHOTO_LIBRARY = "photos"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
