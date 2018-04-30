import datetime , peewee

from Models import Proveedor , Ticket , Contacto , Movimiento , Abono


Proveedor = Proveedor.create(nombre = "Tuvaco" , direccion = "Blvd. Jaime Benavides Pompa 648, Zona Industrial, 25220 Ramos Arizpe")

Contacto = Contacto.create(nombre = "Ventas" , telefono = 4880193 , email = "tuvaco@hotmail.com" , puesto = "ventas" , proveedor = Proveedor)


