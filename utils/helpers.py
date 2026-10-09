
from pathlib import Path
import re


# Directorio donde se guardarán las capturas de errores.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "reports" / "capturas"


def guardar_captura(driver, nombre_prueba):
    """
    Guarda una captura del navegador.

    Parámetros:
        driver: sesión de Selenium activa.
        nombre_prueba: nombre identificador del test.

    Retorna:
        La ruta de la captura o None si no pudo guardarla.
    """
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    # Reemplaza caracteres que no conviene usar en un nombre de archivo.
    nombre_seguro = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        nombre_prueba
    )

    ruta = SCREENSHOTS_DIR / f"{nombre_seguro}.png"

    try:
        guardada = driver.save_screenshot(str(ruta))

        if guardada:
            print(f"Captura guardada en: {ruta}")
            return ruta

        print("No se pudo guardar la captura.")
        return None

    except Exception as error:
        print(f"Error al guardar la captura: {error}")
        return None