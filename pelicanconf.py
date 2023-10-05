AUTHOR = "The SKN PROMAT's Website Authors"
SITENAME = 'SKN PROMAT'
SITEURL = ''

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
