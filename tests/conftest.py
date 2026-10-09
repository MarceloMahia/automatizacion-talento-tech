
import pytest
from selenium import webdriver

from utils.helpers import guardar_captura


@pytest.fixture
def driver(request):
    """
    Abre una sesión independiente de Chrome para cada test.
    Si el test falla, intenta guardar una captura.
    Al finalizar, cierra el navegador.
    """
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador

    # Este bloque se ejecuta después del test.
    try:
        resultado = getattr(request.node, "rep_call", None)

        if resultado and resultado.failed:
            guardar_captura(
                navegador,
                request.node.nodeid
            )
    finally:
        navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Conserva el resultado de la fase de ejecución del test
    para que la fixture pueda detectar si falló.
    """
    outcome = yield
    reporte = outcome.get_result()

    setattr(item, f"rep_{reporte.when}", reporte)