"""
Donation file structure data for YouTube takeout flows

Split from entries_data.py. To regenerate, run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry, Node

YT_ENTRIES: dict[str, list[Entry]] = {
    "Historial De Búsquedas": [
        Entry(
            table="Historial De Búsquedas",
            filename="Takeout/YouTube y YouTube\xa0Music/historial de videos/historial de búsquedas.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={},
            ),
        ),
    ],
    "Historial De Cerques": [
        Entry(
            table="Historial De Cerques",
            filename="Takeout/YouTube i YouTube\xa0Music/historial/historial de cerques.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Historial De Reproducciones": [
        Entry(
            table="Historial De Reproducciones",
            filename="Takeout/YouTube y YouTube\xa0Music/historial de videos/historial de reproducciones.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Historial De Visualitzacions": [
        Entry(
            table="Historial De Visualitzacions",
            filename="Takeout/YouTube i YouTube\xa0Music/historial/historial de visualitzacions.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={})},
            ),
        ),
    ],
    "Historial-De-BúSqueda": [
        Entry(
            table="Historial-De-BúSqueda",
            filename="historial/historial-de-búsqueda.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Historial-De-Búsqueda": [
        Entry(
            table="Historial-De-Búsqueda",
            filename="Takeout/YouTube y YouTube Music/historial/historial-de-búsqueda.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
        Entry(
            table="Historial-De-Búsqueda",
            filename="historial/historial-de-búsqueda.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={},
            ),
        ),
    ],
    "Historial-De-Reproducciones": [
        Entry(
            table="Historial-De-Reproducciones",
            filename="Takeout/YouTube y YouTube Music/historial/historial-de-reproducciones.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                    "description": ("description",),
                },
                children={
                    "subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={}),
                    "details": Node(columns={"name": ("name",)}, children={}),
                },
            ),
        ),
        Entry(
            table="Historial-De-Reproducciones",
            filename="historial/historial-de-reproducciones.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={
                    "subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={}),
                    "details": Node(columns={"name": ("name",)}, children={}),
                },
            ),
        ),
    ],
    "Istoricul CăUtăRilor": [
        Entry(
            table="Istoricul CăUtăRilor",
            filename="istoric/istoricul căutărilor.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Istoricul Căutărilor": [
        Entry(
            table="Istoricul Căutărilor",
            filename="istoric/istoricul căutărilor.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={},
            ),
        ),
    ],
    "Istoricul-VizionăRilor": [
        Entry(
            table="Istoricul-VizionăRilor",
            filename="istoric/istoricul-vizionărilor.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={})},
            ),
        ),
    ],
    "Istoricul-Vizionărilor": [
        Entry(
            table="Istoricul-Vizionărilor",
            filename="istoric/istoricul-vizionărilor.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={})},
            ),
        ),
    ],
    "Kijkgeschiedenis": [
        Entry(
            table="Kijkgeschiedenis",
            filename="geschiedenis/kijkgeschiedenis.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={})},
            ),
        ),
    ],
    "PaiešKos Istorija": [
        Entry(
            table="PaiešKos Istorija",
            filename="istorija/paieškos istorija.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Paieškos Istorija": [
        Entry(
            table="Paieškos Istorija",
            filename="istorija/paieškos istorija.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={},
            ),
        ),
    ],
    "Search-History": [
        Entry(
            table="Search-History",
            filename="Takeout/YouTube and YouTube Music/history/search-history.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
        Entry(
            table="Search-History",
            filename="history/search-history.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
        Entry(
            table="Search-History",
            filename="youtube_takeout/history/search-history.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={},
            ),
        ),
    ],
    "Watch-History": [
        Entry(
            table="Watch-History",
            filename="Takeout/YouTube and YouTube Music/history/watch-history.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={})},
            ),
        ),
        Entry(
            table="Watch-History",
            filename="history/watch-history.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={
                    "subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={}),
                    "details": Node(columns={"name": ("name",)}, children={}),
                },
            ),
        ),
        Entry(
            table="Watch-History",
            filename="youtube_takeout/history/watch-history.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Zoekgeschiedenis": [
        Entry(
            table="Zoekgeschiedenis",
            filename="geschiedenis/zoekgeschiedenis.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                    "description": ("description",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "ŽIūRėJimo Istorija": [
        Entry(
            table="ŽIūRėJimo Istorija",
            filename="istorija/žiūrėjimo istorija.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "description": ("description",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"details": Node(columns={"name": ("name",)}, children={})},
            ),
        ),
    ],
    "Žiūrėjimo Istorija": [
        Entry(
            table="Žiūrėjimo Istorija",
            filename="istorija/žiūrėjimo istorija.json",
            tree=Node(
                columns={
                    "header": ("header",),
                    "title": ("title",),
                    "titleUrl": ("titleUrl",),
                    "time": ("time",),
                    "products": ("products",),
                    "activityControls": ("activityControls",),
                },
                children={"subtitles": Node(columns={"name": ("name",), "url": ("url",)}, children={})},
            ),
        ),
    ],
}

YT_CSV_ENTRIES: dict[str, list[Entry]] = {
    "Ajustes_de_moderación_de_la_comunidad_del_canal": [
        Entry(
            table="Ajustes_de_moderación_de_la_comunidad_del_canal",
            filename="Ajustes de moderación de la comunidad del canal.csv",
            tree=Node(columns={"ID de canal": ("ID de canal",)}, children={}),
        ),
    ],
    "Ajustes_de_moderación_de_la_comunidad_del_canal": [
        Entry(
            table="Ajustes_de_moderación_de_la_comunidad_del_canal",
            filename="Ajustes de moderación de la comunidad del canal.csv",
            tree=Node(columns={"ID de canal": ("ID de canal",)}, children={}),
        ),
    ],
    "Favorites-videoclipuri": [
        Entry(
            table="Favorites-videoclipuri",
            filename="Favorites-videoclipuri.csv",
            tree=Node(
                columns={
                    "ID-ul videoclipului": ("ID-ul videoclipului",),
                    "Marcaj temporal de creare a videoclipului din playlist": (
                        "Marcaj temporal de creare a videoclipului din playlist",
                    ),
                },
                children={},
            ),
        ),
    ],
    "Favorites-videos": [
        Entry(
            table="Favorites-videos",
            filename="Favorites-videos.csv",
            tree=Node(
                columns={
                    "Video ID": ("Video ID",),
                    "Playlist Video Creation Timestamp": ("Playlist Video Creation Timestamp",),
                    "Vaizdo įrašo ID": ("Vaizdo įrašo ID",),
                    "Grojaraščio vaizdo įrašo sukūrimo laiko žymė": ("Grojaraščio vaizdo įrašo sukūrimo laiko žymė",),
                },
                children={},
            ),
        ),
    ],
    "Favorites-vídeos": [
        Entry(
            table="Favorites-vídeos",
            filename="Favorites-vídeos.csv",
            tree=Node(
                columns={
                    "ID de vídeo": ("ID de vídeo",),
                    "Marca de tiempo de creación de la lista de reproducción de vídeos": (
                        "Marca de tiempo de creación de la lista de reproducción de vídeos",
                    ),
                },
                children={},
            ),
        ),
    ],
    "Listas_de_reproducción": [
        Entry(
            table="Listas_de_reproducción",
            filename="Listas de reproducción.csv",
            tree=Node(
                columns={
                    "ID de lista de reproducción": ("ID de lista de reproducción",),
                    "Añadir vídeos nuevos al principio": ("Añadir vídeos nuevos al principio",),
                    "Título de la lista de reproducción (original)": ("Título de la lista de reproducción (original)",),
                    "Idioma del título de la lista de reproducción (original)": (
                        "Idioma del título de la lista de reproducción (original)",
                    ),
                    "Marca de tiempo de creación de la lista de reproducción": (
                        "Marca de tiempo de creación de la lista de reproducción",
                    ),
                    "Marca de tiempo de actualización de la lista de reproducción": (
                        "Marca de tiempo de actualización de la lista de reproducción",
                    ),
                    "Orden de vídeos de lista de reproducción": ("Orden de vídeos de lista de reproducción",),
                    "Visibilidad de la lista de reproducción": ("Visibilidad de la lista de reproducción",),
                },
                children={},
            ),
        ),
    ],
    "URL-configuraties_van_kanaal": [
        Entry(
            table="URL-configuraties_van_kanaal",
            filename="URL-configuraties van kanaal.csv",
            tree=Node(
                columns={
                    "Kanaal-ID": ("Kanaal-ID",),
                    "Naam van vanity-URL 1 voor kanaal": ("Naam van vanity-URL 1 voor kanaal",),
                    "Naam van vanity-URL 2 voor kanaal": ("Naam van vanity-URL 2 voor kanaal",),
                },
                children={},
            ),
        ),
    ],
    "Video_s_in_Favorites": [
        Entry(
            table="Video_s_in_Favorites",
            filename="Video_s in Favorites.csv",
            tree=Node(
                columns={
                    "Video-ID": ("Video-ID",),
                    "Tijdstempel voor het maken van een playlistvideo": ("Tijdstempel voor het maken van een playlistvideo",),
                },
                children={},
            ),
        ),
    ],
    "Video_s_in_Watch_later": [
        Entry(
            table="Video_s_in_Watch_later",
            filename="Video_s in Watch later.csv",
            tree=Node(
                columns={
                    "Video-ID": ("Video-ID",),
                    "Tijdstempel voor het maken van een playlistvideo": ("Tijdstempel voor het maken van een playlistvideo",),
                },
                children={},
            ),
        ),
    ],
    "Video_s_in_crochet": [
        Entry(
            table="Video_s_in_crochet",
            filename="Video_s in crochet.csv",
            tree=Node(
                columns={
                    "Video-ID": ("Video-ID",),
                    "Tijdstempel voor het maken van een playlistvideo": ("Tijdstempel voor het maken van een playlistvideo",),
                },
                children={},
            ),
        ),
    ],
    "Watch_later-videoclipuri": [
        Entry(
            table="Watch_later-videoclipuri",
            filename="Watch later-videoclipuri.csv",
            tree=Node(
                columns={
                    "ID-ul videoclipului": ("ID-ul videoclipului",),
                    "Marcaj temporal de creare a videoclipului din playlist": (
                        "Marcaj temporal de creare a videoclipului din playlist",
                    ),
                },
                children={},
            ),
        ),
    ],
    "Watch_later-videos": [
        Entry(
            table="Watch_later-videos",
            filename="Watch later-videos.csv",
            tree=Node(
                columns={
                    "Video ID": ("Video ID",),
                    "Playlist Video Creation Timestamp": ("Playlist Video Creation Timestamp",),
                    "Vaizdo įrašo ID": ("Vaizdo įrašo ID",),
                    "Grojaraščio vaizdo įrašo sukūrimo laiko žymė": ("Grojaraščio vaizdo įrašo sukūrimo laiko žymė",),
                },
                children={},
            ),
        ),
    ],
    "Watch_later-vídeos": [
        Entry(
            table="Watch_later-vídeos",
            filename="Watch later-vídeos.csv",
            tree=Node(
                columns={
                    "ID de vídeo": ("ID de vídeo",),
                    "Marca de tiempo de creación de la lista de reproducción de vídeos": (
                        "Marca de tiempo de creación de la lista de reproducción de vídeos",
                    ),
                },
                children={},
            ),
        ),
    ],
    "abonamente": [
        Entry(
            table="abonamente",
            filename="abonamente.csv",
            tree=Node(
                columns={
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Adresa URL a canalului": ("Adresa URL a canalului",),
                    "Titlul canalului": ("Titlul canalului",),
                },
                children={},
            ),
        ),
    ],
    "abonnementen": [
        Entry(
            table="abonnementen",
            filename="abonnementen.csv",
            tree=Node(
                columns={"Kanaal-ID": ("Kanaal-ID",), "Kanaal-URL": ("Kanaal-URL",), "Kanaaltitel": ("Kanaaltitel",)},
                children={},
            ),
        ),
    ],
    "canal": [
        Entry(
            table="canal",
            filename="canal.csv",
            tree=Node(
                columns={
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Titlul canalului (original)": ("Titlul canalului (original)",),
                    "Vizibilitatea canalului": ("Vizibilitatea canalului",),
                    "ID de canal": ("ID de canal",),
                    "Título del canal (original)": ("Título del canal (original)",),
                    "Visibilidad del canal": ("Visibilidad del canal",),
                },
                children={},
            ),
        ),
    ],
    "channel": [
        Entry(
            table="channel",
            filename="channel.csv",
            tree=Node(
                columns={
                    "Channel ID": ("Channel ID",),
                    "Channel Title (Original)": ("Channel Title (Original)",),
                    "Channel Visibility": ("Channel Visibility",),
                },
                children={},
            ),
        ),
    ],
    "channel_URL_configs": [
        Entry(
            table="channel_URL_configs",
            filename="channel URL configs.csv",
            tree=Node(
                columns={
                    "Channel ID": ("Channel ID",),
                    "Channel Vanity URL 1 Name": ("Channel Vanity URL 1 Name",),
                    "Channel Vanity URL 2 Name": ("Channel Vanity URL 2 Name",),
                },
                children={},
            ),
        ),
    ],
    "channel_community_moderation_settings": [
        Entry(
            table="channel_community_moderation_settings",
            filename="channel community moderation settings.csv",
            tree=Node(columns={"Channel ID": ("Channel ID",)}, children={}),
        ),
    ],
    "channel_feature_data": [
        Entry(
            table="channel_feature_data",
            filename="channel feature data.csv",
            tree=Node(
                columns={
                    "Channel ID": ("Channel ID",),
                    "Channel Auto Moderation in Live Chat": ("Channel Auto Moderation in Live Chat",),
                    "Video Default Allowed Comments Type": ("Video Default Allowed Comments Type",),
                    "Video Default Targeted Audience": ("Video Default Targeted Audience",),
                    "Video Default License": ("Video Default License",),
                },
                children={},
            ),
        ),
    ],
    "channel_page_settings": [
        Entry(
            table="channel_page_settings",
            filename="channel page settings.csv",
            tree=Node(columns={"Channel ID": ("Channel ID",)}, children={}),
        ),
    ],
    "comentarii": [
        Entry(
            table="comentarii",
            filename="comentarii.csv",
            tree=Node(
                columns={
                    "ID-ul comentariului": ("ID-ul comentariului",),
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Marcajul temporal de creare a comentariului": ("Marcajul temporal de creare a comentariului",),
                    "Preț": ("Preț",),
                    "ID-ul videoclipului": ("ID-ul videoclipului",),
                    "Textul comentariului": ("Textul comentariului",),
                },
                children={},
            ),
        ),
    ],
    "comentarios": [
        Entry(
            table="comentarios",
            filename="comentarios.csv",
            tree=Node(
                columns={
                    "ID de comentario": ("ID de comentario",),
                    "ID de canal": ("ID de canal",),
                    "Marca de tiempo de creación del comentario": ("Marca de tiempo de creación del comentario",),
                    "Precio": ("Precio",),
                    "ID de vídeo": ("ID de vídeo",),
                    "Texto del comentario": ("Texto del comentario",),
                },
                children={},
            ),
        ),
    ],
    "comments": [
        Entry(
            table="comments",
            filename="comments.csv",
            tree=Node(
                columns={
                    "Comment ID": ("Comment ID",),
                    "Channel ID": ("Channel ID",),
                    "Comment Create Timestamp": ("Comment Create Timestamp",),
                    "Price": ("Price",),
                    "Video ID": ("Video ID",),
                    "Comment Text": ("Comment Text",),
                },
                children={},
            ),
        ),
    ],
    "configuraciones_de_la_URL_del_canal": [
        Entry(
            table="configuraciones_de_la_URL_del_canal",
            filename="configuraciones de la URL del canal.csv",
            tree=Node(
                columns={
                    "ID de canal": ("ID de canal",),
                    "Nombre de la URL mnemónica del canal (1)": ("Nombre de la URL mnemónica del canal (1)",),
                    "Nombre de la URL mnemónica del canal (2)": ("Nombre de la URL mnemónica del canal (2)",),
                },
                children={},
            ),
        ),
    ],
    "configuración_de_la_página_del_canal": [
        Entry(
            table="configuración_de_la_página_del_canal",
            filename="configuración de la página del canal.csv",
            tree=Node(columns={"ID de canal": ("ID de canal",)}, children={}),
        ),
    ],
    "configuración_de_la_página_del_canal": [
        Entry(
            table="configuración_de_la_página_del_canal",
            filename="configuración de la página del canal.csv",
            tree=Node(columns={"ID de canal": ("ID de canal",)}, children={}),
        ),
    ],
    "configurații_pentru_adresa_URL_a_canalului": [
        Entry(
            table="configurații_pentru_adresa_URL_a_canalului",
            filename="configurații pentru adresa URL a canalului.csv",
            tree=Node(
                columns={
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Numele adresei URL personalizate a canalului 1": ("Numele adresei URL personalizate a canalului 1",),
                    "Numele adresei URL personalizate a canalului 2": ("Numele adresei URL personalizate a canalului 2",),
                },
                children={},
            ),
        ),
    ],
    "configurații_pentru_adresa_URL_a_canalului": [
        Entry(
            table="configurații_pentru_adresa_URL_a_canalului",
            filename="configurații pentru adresa URL a canalului.csv",
            tree=Node(
                columns={
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Numele adresei URL personalizate a canalului 1": ("Numele adresei URL personalizate a canalului 1",),
                },
                children={},
            ),
        ),
    ],
    "crochet-videoclipuri": [
        Entry(
            table="crochet-videoclipuri",
            filename="crochet-videoclipuri.csv",
            tree=Node(
                columns={
                    "ID-ul videoclipului": ("ID-ul videoclipului",),
                    "Marcaj temporal de creare a videoclipului din playlist": (
                        "Marcaj temporal de creare a videoclipului din playlist",
                    ),
                },
                children={},
            ),
        ),
    ],
    "crochet-videos": [
        Entry(
            table="crochet-videos",
            filename="crochet-videos.csv",
            tree=Node(
                columns={
                    "Video ID": ("Video ID",),
                    "Playlist Video Creation Timestamp": ("Playlist Video Creation Timestamp",),
                    "Vaizdo įrašo ID": ("Vaizdo įrašo ID",),
                    "Grojaraščio vaizdo įrašo sukūrimo laiko žymė": ("Grojaraščio vaizdo įrašo sukūrimo laiko žymė",),
                },
                children={},
            ),
        ),
    ],
    "crochet-vídeos": [
        Entry(
            table="crochet-vídeos",
            filename="crochet-vídeos.csv",
            tree=Node(
                columns={
                    "ID de vídeo": ("ID de vídeo",),
                    "Marca de tiempo de creación de la lista de reproducción de vídeos": (
                        "Marca de tiempo de creación de la lista de reproducción de vídeos",
                    ),
                },
                children={},
            ),
        ),
    ],
    "date_despre_funcțiile_canalului": [
        Entry(
            table="date_despre_funcțiile_canalului",
            filename="date despre funcțiile canalului.csv",
            tree=Node(
                columns={
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Moderare automată a canalului în chatul live": ("Moderare automată a canalului în chatul live",),
                    "Tipul prestabilit de comentarii permise ale videoclipului": (
                        "Tipul prestabilit de comentarii permise ale videoclipului",
                    ),
                    "Publicul vizat prestabilit al videoclipului": ("Publicul vizat prestabilit al videoclipului",),
                    "Licența prestabilită a videoclipului": ("Licența prestabilită a videoclipului",),
                },
                children={},
            ),
        ),
    ],
    "date_despre_funcțiile_canalului": [
        Entry(
            table="date_despre_funcțiile_canalului",
            filename="date despre funcțiile canalului.csv",
            tree=Node(
                columns={
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Moderare automată a canalului în chatul live": ("Moderare automată a canalului în chatul live",),
                    "Tipul prestabilit de comentarii permise ale videoclipului": (
                        "Tipul prestabilit de comentarii permise ale videoclipului",
                    ),
                    "Publicul vizat prestabilit al videoclipului": ("Publicul vizat prestabilit al videoclipului",),
                    "Licența prestabilită a videoclipului": ("Licența prestabilită a videoclipului",),
                },
                children={},
            ),
        ),
    ],
    "datos_de_la_función_del_canal": [
        Entry(
            table="datos_de_la_función_del_canal",
            filename="datos de la función del canal.csv",
            tree=Node(
                columns={
                    "ID de canal": ("ID de canal",),
                    "Moderación automática del canal en el chat en directo": (
                        "Moderación automática del canal en el chat en directo",
                    ),
                    "Tipo de comentarios permitidos de forma predeterminada en el vídeo": (
                        "Tipo de comentarios permitidos de forma predeterminada en el vídeo",
                    ),
                    "Audiencia objetivo predeterminada del vídeo": ("Audiencia objetivo predeterminada del vídeo",),
                    "Licencia del vídeo predeterminada": ("Licencia del vídeo predeterminada",),
                },
                children={},
            ),
        ),
    ],
    "datos_de_la_función_del_canal": [
        Entry(
            table="datos_de_la_función_del_canal",
            filename="datos de la función del canal.csv",
            tree=Node(
                columns={
                    "ID de canal": ("ID de canal",),
                    "Moderación automática del canal en el chat en directo": (
                        "Moderación automática del canal en el chat en directo",
                    ),
                    "Tipo de comentarios permitidos de forma predeterminada en el vídeo": (
                        "Tipo de comentarios permitidos de forma predeterminada en el vídeo",
                    ),
                    "Audiencia objetivo predeterminada del vídeo": ("Audiencia objetivo predeterminada del vídeo",),
                    "Licencia del vídeo predeterminada": ("Licencia del vídeo predeterminada",),
                },
                children={},
            ),
        ),
    ],
    "gegevens_voor_kanaalfunctie": [
        Entry(
            table="gegevens_voor_kanaalfunctie",
            filename="gegevens voor kanaalfunctie.csv",
            tree=Node(
                columns={
                    "Kanaal-ID": ("Kanaal-ID",),
                    "Automatische moderatie in livechat van kanaal": ("Automatische moderatie in livechat van kanaal",),
                    "Standaard toegestane reactietype van video": ("Standaard toegestane reactietype van video",),
                    "Standaard doelgroep van video": ("Standaard doelgroep van video",),
                    "Standaardlicentie van video": ("Standaardlicentie van video",),
                    "Automatische moderatie in live chat van kanaal": ("Automatische moderatie in live chat van kanaal",),
                },
                children={},
            ),
        ),
    ],
    "grabaciones_de_vídeo": [
        Entry(
            table="grabaciones_de_vídeo",
            filename="grabaciones de vídeo.csv",
            tree=Node(columns={"ID de vídeo": ("ID de vídeo",)}, children={}),
        ),
    ],
    "grojaraščiai": [
        Entry(
            table="grojaraščiai",
            filename="grojaraščiai.csv",
            tree=Node(
                columns={
                    "Grojaraščio ID": ("Grojaraščio ID",),
                    "Pridėti naujus vaizdo įrašus viršuje": ("Pridėti naujus vaizdo įrašus viršuje",),
                    "Grojaraščio pavadinimas (originalas)": ("Grojaraščio pavadinimas (originalas)",),
                    "Grojaraščio pavadinimo (originalo) kalba": ("Grojaraščio pavadinimo (originalo) kalba",),
                    "Grojaraščio sukūrimo laiko žymė": ("Grojaraščio sukūrimo laiko žymė",),
                    "Grojaraščio atnaujinimo laiko žymė": ("Grojaraščio atnaujinimo laiko žymė",),
                    "Grojaraščio vaizdo įrašų tvarka": ("Grojaraščio vaizdo įrašų tvarka",),
                    "Grojaraščio matomumas": ("Grojaraščio matomumas",),
                },
                children={},
            ),
        ),
    ],
    "instellingen_voor_het_beheer_van_je_kanaalcommu": [
        Entry(
            table="instellingen_voor_het_beheer_van_je_kanaalcommu",
            filename="instellingen voor het beheer van je kanaalcommu.csv",
            tree=Node(columns={"Kanaal-ID": ("Kanaal-ID",)}, children={}),
        ),
    ],
    "instellingen_voor_kanaalpagina": [
        Entry(
            table="instellingen_voor_kanaalpagina",
            filename="instellingen voor kanaalpagina.csv",
            tree=Node(columns={"Kanaal-ID": ("Kanaal-ID",)}, children={}),
        ),
    ],
    "înregistrări_video": [
        Entry(
            table="înregistrări_video",
            filename="înregistrări video.csv",
            tree=Node(columns={"ID-ul videoclipului": ("ID-ul videoclipului",)}, children={}),
        ),
    ],
    "kanaal": [
        Entry(
            table="kanaal",
            filename="kanaal.csv",
            tree=Node(
                columns={
                    "Kanaal-ID": ("Kanaal-ID",),
                    "(Originele) kanaaltitel": ("(Originele) kanaaltitel",),
                    "Kanaalzichtbaarheid": ("Kanaalzichtbaarheid",),
                },
                children={},
            ),
        ),
    ],
    "kanalas": [
        Entry(
            table="kanalas",
            filename="kanalas.csv",
            tree=Node(
                columns={
                    "Kanalo ID": ("Kanalo ID",),
                    "Kanalo pavadinimas (pradinis)": ("Kanalo pavadinimas (pradinis)",),
                    "Kanalo matomumas": ("Kanalo matomumas",),
                },
                children={},
            ),
        ),
    ],
    "kanalo_URL_konfigūracijos": [
        Entry(
            table="kanalo_URL_konfigūracijos",
            filename="kanalo URL konfigūracijos.csv",
            tree=Node(
                columns={
                    "Kanalo ID": ("Kanalo ID",),
                    "1 kanalo reklaminio URL pavadinimas": ("1 kanalo reklaminio URL pavadinimas",),
                    "2 kanalo reklaminio URL pavadinimas": ("2 kanalo reklaminio URL pavadinimas",),
                },
                children={},
            ),
        ),
    ],
    "kanalo_URL_konfigūracijos": [
        Entry(
            table="kanalo_URL_konfigūracijos",
            filename="kanalo URL konfigūracijos.csv",
            tree=Node(
                columns={
                    "Kanalo ID": ("Kanalo ID",),
                    "1 kanalo reklaminio URL pavadinimas": ("1 kanalo reklaminio URL pavadinimas",),
                },
                children={},
            ),
        ),
    ],
    "kanalo_bendruomenės_moderavimo_nustatymai": [
        Entry(
            table="kanalo_bendruomenės_moderavimo_nustatymai",
            filename="kanalo bendruomenės moderavimo nustatymai.csv",
            tree=Node(columns={"Kanalo ID": ("Kanalo ID",)}, children={}),
        ),
    ],
    "kanalo_bendruomenės_moderavimo_nustatymai": [
        Entry(
            table="kanalo_bendruomenės_moderavimo_nustatymai",
            filename="kanalo bendruomenės moderavimo nustatymai.csv",
            tree=Node(columns={"Kanalo ID": ("Kanalo ID",)}, children={}),
        ),
    ],
    "kanalo_funkcijų_duomenys": [
        Entry(
            table="kanalo_funkcijų_duomenys",
            filename="kanalo funkcijų duomenys.csv",
            tree=Node(
                columns={
                    "Kanalo ID": ("Kanalo ID",),
                    "Automatinis kanalo moderavimas tiesioginiame pokalbyje": (
                        "Automatinis kanalo moderavimas tiesioginiame pokalbyje",
                    ),
                    "Numatytasis vaizdo įrašo leidžiamų komentarų tipas": (
                        "Numatytasis vaizdo įrašo leidžiamų komentarų tipas",
                    ),
                    "Numatytoji vaizdo įrašo tikslinė auditorija": ("Numatytoji vaizdo įrašo tikslinė auditorija",),
                    "Numatytoji vaizdo įrašo licencija": ("Numatytoji vaizdo įrašo licencija",),
                },
                children={},
            ),
        ),
    ],
    "kanalo_funkcijų_duomenys": [
        Entry(
            table="kanalo_funkcijų_duomenys",
            filename="kanalo funkcijų duomenys.csv",
            tree=Node(
                columns={
                    "Kanalo ID": ("Kanalo ID",),
                    "Automatinis kanalo moderavimas tiesioginiame pokalbyje": (
                        "Automatinis kanalo moderavimas tiesioginiame pokalbyje",
                    ),
                    "Numatytasis vaizdo įrašo leidžiamų komentarų tipas": (
                        "Numatytasis vaizdo įrašo leidžiamų komentarų tipas",
                    ),
                    "Numatytoji vaizdo įrašo tikslinė auditorija": ("Numatytoji vaizdo įrašo tikslinė auditorija",),
                    "Numatytoji vaizdo įrašo licencija": ("Numatytoji vaizdo įrašo licencija",),
                },
                children={},
            ),
        ),
    ],
    "kanalo_puslapio_nustatymai": [
        Entry(
            table="kanalo_puslapio_nustatymai",
            filename="kanalo puslapio nustatymai.csv",
            tree=Node(columns={"Kanalo ID": ("Kanalo ID",)}, children={}),
        ),
    ],
    "komentarai": [
        Entry(
            table="komentarai",
            filename="komentarai.csv",
            tree=Node(
                columns={
                    "Komentaro ID": ("Komentaro ID",),
                    "Kanalo ID": ("Kanalo ID",),
                    "Komentaro sukūrimo laiko žymė": ("Komentaro sukūrimo laiko žymė",),
                    "Kaina": ("Kaina",),
                    "Vaizdo įrašo ID": ("Vaizdo įrašo ID",),
                    "Komentuoti tekstą": ("Komentuoti tekstą",),
                },
                children={},
            ),
        ),
    ],
    "playlists": [
        Entry(
            table="playlists",
            filename="playlists.csv",
            tree=Node(
                columns={
                    "Playlist ID": ("Playlist ID",),
                    "Add new videos to top": ("Add new videos to top",),
                    "Playlist Title (Original)": ("Playlist Title (Original)",),
                    "Playlist Title (Original) Language": ("Playlist Title (Original) Language",),
                    "Playlist Create Timestamp": ("Playlist Create Timestamp",),
                    "Playlist Update Timestamp": ("Playlist Update Timestamp",),
                    "Playlist Video Order": ("Playlist Video Order",),
                    "Playlist Visibility": ("Playlist Visibility",),
                    "Playlist-ID": ("Playlist-ID",),
                    "Nieuwe video's bovenaan toevoegen": ("Nieuwe video's bovenaan toevoegen",),
                    "Playlist-titel (Origineel)": ("Playlist-titel (Origineel)",),
                    "(Originele) taal van playlist-titel": ("(Originele) taal van playlist-titel",),
                    "Playlist tijdstempel maken": ("Playlist tijdstempel maken",),
                    "Playlist tijdstempel updaten": ("Playlist tijdstempel updaten",),
                    "Videovolgorde playlist": ("Videovolgorde playlist",),
                    "Zichtbaarheid van playlist": ("Zichtbaarheid van playlist",),
                },
                children={},
            ),
        ),
    ],
    "playlisturi": [
        Entry(
            table="playlisturi",
            filename="playlisturi.csv",
            tree=Node(
                columns={
                    "ID-ul playlistului": ("ID-ul playlistului",),
                    "Adaugă videoclipuri noi în partea de sus": ("Adaugă videoclipuri noi în partea de sus",),
                    "Titlul playlistului (original)": ("Titlul playlistului (original)",),
                    "Limba titlului playlistului (original)": ("Limba titlului playlistului (original)",),
                    "Playlistul creează marcaj temporal": ("Playlistul creează marcaj temporal",),
                    "Playlistul actualizează marcajul temporal": ("Playlistul actualizează marcajul temporal",),
                    "Ordinea videoclipurilor în playlist": ("Ordinea videoclipurilor în playlist",),
                    "Vizibilitatea playlistului": ("Vizibilitatea playlistului",),
                },
                children={},
            ),
        ),
    ],
    "prenumeratos": [
        Entry(
            table="prenumeratos",
            filename="prenumeratos.csv",
            tree=Node(
                columns={
                    "Kanalo ID": ("Kanalo ID",),
                    "Kanalo URL": ("Kanalo URL",),
                    "Kanalo pavadinimas": ("Kanalo pavadinimas",),
                },
                children={},
            ),
        ),
    ],
    "reacties": [
        Entry(
            table="reacties",
            filename="reacties.csv",
            tree=Node(
                columns={
                    "Reactie-ID": ("Reactie-ID",),
                    "Kanaal-ID": ("Kanaal-ID",),
                    "Aanmaaktijdstempel reactie": ("Aanmaaktijdstempel reactie",),
                    "Prijs": ("Prijs",),
                    "Video-ID": ("Video-ID",),
                    "Reactietekst": ("Reactietekst",),
                },
                children={},
            ),
        ),
    ],
    "setări_de_moderare_a_comunității_canalului": [
        Entry(
            table="setări_de_moderare_a_comunității_canalului",
            filename="setări de moderare a comunității canalului.csv",
            tree=Node(columns={"ID-ul canalului": ("ID-ul canalului",)}, children={}),
        ),
    ],
    "setările_paginii_de_canal": [
        Entry(
            table="setările_paginii_de_canal",
            filename="setările paginii de canal.csv",
            tree=Node(columns={"ID-ul canalului": ("ID-ul canalului",)}, children={}),
        ),
    ],
    "setări_de_moderare_a_comunității_canalului": [
        Entry(
            table="setări_de_moderare_a_comunității_canalului",
            filename="setări de moderare a comunității canalului.csv",
            tree=Node(columns={"ID-ul canalului": ("ID-ul canalului",)}, children={}),
        ),
    ],
    "setările_paginii_de_canal": [
        Entry(
            table="setările_paginii_de_canal",
            filename="setările paginii de canal.csv",
            tree=Node(columns={"ID-ul canalului": ("ID-ul canalului",)}, children={}),
        ),
    ],
    "subscriptions": [
        Entry(
            table="subscriptions",
            filename="subscriptions.csv",
            tree=Node(
                columns={"Channel Id": ("Channel Id",), "Channel Url": ("Channel Url",), "Channel Title": ("Channel Title",)},
                children={},
            ),
        ),
    ],
    "suscripciones": [
        Entry(
            table="suscripciones",
            filename="suscripciones.csv",
            tree=Node(
                columns={
                    "ID del canal": ("ID del canal",),
                    "URL del canal": ("URL del canal",),
                    "Título del canal": ("Título del canal",),
                },
                children={},
            ),
        ),
    ],
    "vaizdo_įrašai": [
        Entry(
            table="vaizdo_įrašai",
            filename="vaizdo įrašai.csv",
            tree=Node(
                columns={
                    "Vaizdo įrašo ID": ("Vaizdo įrašo ID",),
                    "Apytikrė trukmė (ms)": ("Apytikrė trukmė (ms)",),
                    "Vaizdo įrašo garso takelio kalba": ("Vaizdo įrašo garso takelio kalba",),
                    "Vaizdo įrašo kategorija": ("Vaizdo įrašo kategorija",),
                    "Vaizdo įrašo aprašas (originalas)": ("Vaizdo įrašo aprašas (originalas)",),
                    "Kanalo ID": ("Kanalo ID",),
                    "Vaizdo įrašo pavadinimas (originalas)": ("Vaizdo įrašo pavadinimas (originalas)",),
                    "Privatumas": ("Privatumas",),
                    "Vaizdo įrašo būsena": ("Vaizdo įrašo būsena",),
                    "Vaizdo įrašo sukūrimo laiko žymė": ("Vaizdo įrašo sukūrimo laiko žymė",),
                    "Vaizdo įrašo paskelbimo laiko žymė": ("Vaizdo įrašo paskelbimo laiko žymė",),
                },
                children={},
            ),
        ),
    ],
    "video-opnamen": [
        Entry(table="video-opnamen", filename="video-opnamen.csv", tree=Node(columns={"Video-ID": ("Video-ID",)}, children={})),
    ],
    "video_recordings": [
        Entry(
            table="video_recordings",
            filename="video recordings.csv",
            tree=Node(columns={"Video ID": ("Video ID",)}, children={}),
        ),
    ],
    "video_s": [
        Entry(
            table="video_s",
            filename="video_s.csv",
            tree=Node(
                columns={
                    "Video-ID": ("Video-ID",),
                    "Geschatte duur (ms)": ("Geschatte duur (ms)",),
                    "Audiotaal van video": ("Audiotaal van video",),
                    "Videocategorie": ("Videocategorie",),
                    "Videobeschrijving (origineel)": ("Videobeschrijving (origineel)",),
                    "Kanaal-ID": ("Kanaal-ID",),
                    "Videotitel (origineel)": ("Videotitel (origineel)",),
                    "Privacy": ("Privacy",),
                    "Videostatus": ("Videostatus",),
                    "Tijdstempel aanmaaktijd video": ("Tijdstempel aanmaaktijd video",),
                    "Tijdstempel publicatietijd video": ("Tijdstempel publicatietijd video",),
                },
                children={},
            ),
        ),
    ],
    "videoclipuri": [
        Entry(
            table="videoclipuri",
            filename="videoclipuri.csv",
            tree=Node(
                columns={
                    "ID-ul videoclipului": ("ID-ul videoclipului",),
                    "Durată aproximativă (ms)": ("Durată aproximativă (ms)",),
                    "Limba conținutului audio din videoclip": ("Limba conținutului audio din videoclip",),
                    "Categorie de videoclipuri": ("Categorie de videoclipuri",),
                    "Descrierea videoclipului (original)": ("Descrierea videoclipului (original)",),
                    "ID-ul canalului": ("ID-ul canalului",),
                    "Titlul videoclipului (original)": ("Titlul videoclipului (original)",),
                    "Confidențialitate": ("Confidențialitate",),
                    "Starea videoclipului": ("Starea videoclipului",),
                    "Marcajul temporal de creare a videoclipului": ("Marcajul temporal de creare a videoclipului",),
                    "Marcajul temporal de publicare a videoclipului": ("Marcajul temporal de publicare a videoclipului",),
                },
                children={},
            ),
        ),
    ],
    "videos": [
        Entry(
            table="videos",
            filename="videos.csv",
            tree=Node(
                columns={
                    "Video ID": ("Video ID",),
                    "Approx Duration (ms)": ("Approx Duration (ms)",),
                    "Video Audio Language": ("Video Audio Language",),
                    "Video Category": ("Video Category",),
                    "Video Description (Original)": ("Video Description (Original)",),
                    "Channel ID": ("Channel ID",),
                    "Video Title (Original)": ("Video Title (Original)",),
                    "Privacy": ("Privacy",),
                    "Video State": ("Video State",),
                    "Video Create Timestamp": ("Video Create Timestamp",),
                    "Video Publish Timestamp": ("Video Publish Timestamp",),
                },
                children={},
            ),
        ),
    ],
    "vídeos": [
        Entry(
            table="vídeos",
            filename="vídeos.csv",
            tree=Node(
                columns={
                    "ID de vídeo": ("ID de vídeo",),
                    "Duración aproximada (ms)": ("Duración aproximada (ms)",),
                    "Idioma del audio del vídeo": ("Idioma del audio del vídeo",),
                    "Categoría del vídeo": ("Categoría del vídeo",),
                    "Descripción del vídeo (original)": ("Descripción del vídeo (original)",),
                    "ID de canal": ("ID de canal",),
                    "Título del vídeo (original)": ("Título del vídeo (original)",),
                    "Privacidad": ("Privacidad",),
                    "Estado del vídeo": ("Estado del vídeo",),
                    "Marca de tiempo de creación del vídeo": ("Marca de tiempo de creación del vídeo",),
                    "Marca de tiempo de publicación del vídeo": ("Marca de tiempo de publicación del vídeo",),
                },
                children={},
            ),
        ),
    ],
}
