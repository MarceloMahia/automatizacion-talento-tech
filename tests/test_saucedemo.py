
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
CONTRASENA = "secret_sauce"
TIEMPO_ESPERA = 10


def iniciar_sesion(driver):
    """
    Inicia sesión y espera que aparezca el inventario.
    Esta función se reutiliza en las pruebas que lo necesitan.
    """
    wait = WebDriverWait(driver, TIEMPO_ESPERA)

    driver.get(URL)

    campo_usuario = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    campo_password = driver.find_element(
        By.ID, "password"
    )

    boton_login = driver.find_element(
        By.ID, "login-button"
    )

    campo_usuario.send_keys(USUARIO)
    campo_password.send_keys(CONTRASENA)
    boton_login.click()

    wait.until(EC.url_contains("/inventory.html"))

    return wait


def test_login_exitoso(driver):
    """
    Verifica que las credenciales válidas permitan entrar
    al inventario.
    """
    wait = iniciar_sesion(driver)

    # Validar URL de destino.
    assert "/inventory.html" in driver.current_url

    # Validar título del inventario.
    titulo = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )
    assert titulo.text == "Products"

    # Validar el logotipo de la aplicación.
    logo = driver.find_element(
        By.CLASS_NAME, "app_logo"
    )
    assert logo.text == "Swag Labs"


def test_catalogo_de_productos(driver):
    """
    Verifica el catálogo, los elementos principales
    y la información del primer producto.
    """
    iniciar_sesion(driver)
    wait = WebDriverWait(driver, TIEMPO_ESPERA)

    # Verificar el título del catálogo.
    titulo = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )
    assert titulo.text == "Products"

    # Verificar que exista al menos un producto visible.
    productos = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    productos_visibles = [
        producto
        for producto in productos
        if producto.is_displayed()
    ]

    assert len(productos_visibles) > 0

    # Verificar el botón del menú.
    menu = driver.find_element(
        By.ID, "react-burger-menu-btn"
    )
    assert menu.is_displayed()

    # Verificar el selector de ordenamiento.
    filtro = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )
    assert filtro.is_displayed()
    assert filtro.is_enabled()

    # Obtener nombre y precio del primer producto.
    primer_producto = productos_visibles[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    assert nombre != ""
    assert precio.startswith("$")

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")
    print(f"Productos visibles: {len(productos_visibles)}")


def test_agregar_producto_al_carrito(driver):
    """
    Añade el primer producto al carrito y verifica
    tanto el contador como el contenido del carrito.
    """
    iniciar_sesion(driver)
    wait = WebDriverWait(driver, TIEMPO_ESPERA)

    # Obtener el primer producto.
    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    # Hacer clic en el botón de ese producto.
    boton_agregar = primer_producto.find_element(
        By.CSS_SELECTOR, "button.btn_inventory"
    )

    boton_agregar.click()

    # Verificar el contador del carrito.
    contador = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador.text == "1"

    # Ir al carrito.
    enlace_carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    )
    enlace_carrito.click()

    # Verificar que el producto esté en el carrito.
    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert producto_carrito.text == nombre

    print(f"Producto agregado correctamente: {nombre}")