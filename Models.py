import peewee

database = peewee.SqliteDatabase("caja_chica.db")

class  Proveedor(peewee.Model):
    "ORM Model of Proveedor"
    nombre = peewee.CharField()
    direccion = peewee.CharField()

    class Meta:
        database = database

class Contacto(peewee.Model):

    nombre = peewee.CharField()
    telefono = peewee.IntegerField()
    email = peewee.CharField()
    puesto = peewee.CharField()
    proveedor = peewee.ForeignKeyField(Proveedor)

    class Meta:
        database = database

class Ticket(peewee.Model):
    descripcion = peewee.CharField()
    fecha = peewee.DateField()
    precio = peewee.DecimalField()
    proveedor = peewee.ForeignKeyField(Proveedor)

    class Meta:
        database = database

class Abono(peewee.Model):
    fecha = peewee.DateField()
    descripcion = peewee.CharField()
    precio = peewee.DecimalField()

    class Meta:
        database = database

class Movimiento(peewee.Model):
    ticket = peewee.ForeignKeyField(Ticket)
    abono = peewee.ForeignKeyField(Abono)

    class Meta:
        database = database


if __name__ == '__main__':
    try:
        Proveedor.create_table()

    except peewee.OperationalError:
        print("Base de datos de proveedor ya existe!")

    try:
        Contacto.create_table()

    except peewee.OperationalError:
        print("Base de datos de contacto ya existe!")

    try:
        Ticket.create_table()

    except peewee.OperationalError:
        print("Base de datos de Ticket ya existe!")

    try:
        Abono.create_table()

    except peewee.OperationalError:
        print("Base de datos de Abono ya existe!")

    try:
        Movimiento.create_table()

    except peewee.OperationalError:
        print("Base de datos de Movimiento ya existe!")
