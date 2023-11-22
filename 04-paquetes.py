
# Paquetes:
# ----------------------------------------------------------------------------------------------------------------------

# módulo --> cualquier fichero ".py"
# paquete --> grupo de módulos

# Para que Python interprete un directorio como paquete, debe contener un fichero "__init__.py"

from paquete_1 import longitud
from paquete_1.subpaquete_1 import sumar

longitud.longitud(1, 2, 3, 4)
sumar.sumar(1, 2, 3, 4)
