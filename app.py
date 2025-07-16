# pylint: disable=unused-import
# pyright: reportUnusedImport=false
"""
Módulo principal para la gestión de citas y mascotas en la clínica veterinaria.

Contiene la lógica para agendar, eliminar citas, manejar mascotas,
interfaz de usuario y conexión con la base de datos.
"""

from nicegui import ui #el framework NiceGUI para construir la interfaz web.
from vistas.encuesta import Encuesta
from vistas.administradorPerfil import AdministradorPerfil

import vistas.inicio
import vistas.calendario_view
import vistas.principal_view
import vistas.mascota_view
import vistas.configuracion
import vistas.login
import vistas.recuperarContra
import vistas.registro
import vistas.restablecer

ui.run(storage_secret="Peluchitos2025")
