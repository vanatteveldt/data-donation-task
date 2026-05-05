"""Upload safety checks.

Validates upload size against policy limits using metadata only —
the upload itself is never read into Pyodide's heap.

See extraction/AD0007 for the streaming invariant: PayloadFile uploads
must be passed directly to consumers (zipfile.ZipFile, validators,
extractors) without materialization. Reading the entire payload to
verify its size defeats this; the JS-reported `adapter.size` attribute
is the source of truth for size policy decisions.
"""

import logging

import port.api.props as props

logger = logging.getLogger(__name__)

MAX_FILE_SIZE_BYTES = 2 * 1024 * 1024 * 1024  # 2 GiB
CHUNKED_EXPORT_SENTINEL_BYTES = MAX_FILE_SIZE_BYTES  # same value, distinct intent


class TranslatableException(Exception):
    """Exception that carries its own translatable user-facing message.

    Renderers call ``get_translatable()`` to obtain a ``Translatable``
    they can drop straight into a UI prompt, so they stay agnostic to
    specific error types.
    """

    def get_translatable(self, platform_name: str | None = None) -> props.Translatable:
        raise NotImplementedError


class FileTooLargeError(TranslatableException):
    """Raised when a file exceeds MAX_FILE_SIZE_BYTES."""

    size: int

    def __init__(self, size: int):
        self.size = size
        super().__init__(f"File is {size} bytes, exceeding limit of {MAX_FILE_SIZE_BYTES} bytes")

    def get_hint(self, platform_name: str | None) -> props.Translations | None:
        if platform_name in {"Instagram", "Facebook"}:
            return {
                "en": "In particular, make sure that date range is set to 'last year', format is set to 'json', and media quality is set to lower",
                "nl": "heck in het bijzonder dat het datumbereik op 'Afgelopen jaar' staat, indeling op 'json', en mediakwaliteit op 'lager'",
                "es": "En particular, asegúrese de que el rango de fechas esté establecido en 'último año', el formato en 'json' y la calidad de los medios en 'más baja'",
                "lt": "Visų pirma, įsitikinkite, kad datų intervalas nustatytas į 'praėjusius metus', formatas – į 'json', o medijos kokybė – į 'žemesnę'",
                "ro": "În special, asigurați-vă că intervalul de date este setat la 'anul trecut', formatul la 'json', iar calitatea media la 'mai scăzută'",
            }
        if platform_name in {"YouTube"}:
            return {
                "en": "In particular, make sure that 'videos' is unchecked",
                "nl": "Check in het bijzonder dat 'video's staat uitgevinkt",
                "es": "En particular, asegúrese de que la opción 'videos' no esté marcada",
                "lt": "Visų pirma, įsitikinkite, kad parinktis 'vaizdo įrašai' nėra pažymėta",
                "ro": "În special, asigurați-vă că opțiunea 'videoclipuri' nu este bifată",
            }
        if platform_name in {"TikTok"}:
            return {
                "en": "In particular, make sure that JSON is selected as the file format",
                "nl": "heck in het bijzonder dat JSON is geselecteerd als bestandsindeling",
                "es": "En particular, asegúrese de que JSON esté seleccionado como formato de archivo",
                "lt": "Visų pirma, įsitikinkite, kad failo formatu pasirinktas JSON",
                "ro": "În special, asigurați-vă că JSON este selectat ca format de fișier",
            }

    def get_translatable(self, platform_name: str | None = None) -> props.Translatable:
        f = f"{self.size / 1_000_000_000:.1f} GB"
        limit = "2 GB"
        message: props.Translations = {
            "en": (
                f"Your file is {f}, exceeding the limit of {limit}. "
                "Please check the download instructions carefully and request "
                f"your data again from the provider."
            ),
            "nl": (
                f"Uw bestand is {f} en overschrijdt de limiet van {limit}. "
                "Controleer de downloadinstructies zorgvuldig en vraag uw "
                "gegevens opnieuw aan bij de aanbieder."
            ),
            "es": (
                f"Su archivo es de {f}, superando el límite de {limit}. "
                "Por favor, revise atentamente las instrucciones de descarga y "
                "solicite sus datos nuevamente al proveedor."
            ),
            "lt": (
                f"Jūsų failas yra {f}, viršija {limit} ribą. "
                "Atidžiai peržiūrėkite atsisiuntimo instrukcijas ir dar kartą "
                "paprašykite duomenų iš teikėjo."
            ),
            "ro": (
                f"Fișierul dvs. are {f}, depășind limita de {limit}. "
                "Vă rugăm să verificați cu atenție instrucțiunile de descărcare "
                "și să solicitați din nou datele de la furnizor."
            ),
        }

        hint = self.get_hint(platform_name)
        if hint:
            for lang, text in message.items():
                message[lang] = f"{text} {hint.get(lang, '')}"
        return props.Translatable(message)


class ChunkedExportError(Exception):
    """Raised when a file is exactly CHUNKED_EXPORT_SENTINEL_BYTES (split export sentinel)."""


def check_payload_size(file_result) -> None:
    """Validate upload size from JS-reported metadata. No bytes read.

    Caller is expected to handle the exception and render a safety
    error page. FlowBuilder does this around step 1 of start_flow().

    Args:
        file_result: A PayloadFile-shaped object whose .value carries
            an AsyncFileAdapter (with a .size attribute populated from
            the JS reader at construction time).

    Raises:
        TypeError: If file_result is not a PayloadFile. PayloadString /
            WORKERFS support was retired with extraction/AD0007.
        ChunkedExportError: If size == CHUNKED_EXPORT_SENTINEL_BYTES
            (split export sentinel — incomplete multi-part download).
        FileTooLargeError: If size > MAX_FILE_SIZE_BYTES.
    """
    if file_result.__type__ != "PayloadFile":
        raise TypeError(
            f"Unsupported payload type: {file_result.__type__}. "
            "Only PayloadFile is accepted; PayloadString/WORKERFS support "
            "was retired in extraction/AD0007."
        )

    size = int(file_result.value.size)  # JS metadata, no read
    if size == CHUNKED_EXPORT_SENTINEL_BYTES:
        raise ChunkedExportError(f"File is exactly {CHUNKED_EXPORT_SENTINEL_BYTES} bytes — " "likely a chunked export sentinel")
    if size > MAX_FILE_SIZE_BYTES:
        raise FileTooLargeError(size=size)
