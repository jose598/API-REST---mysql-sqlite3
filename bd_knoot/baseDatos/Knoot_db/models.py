from django.db import models


class Administrador(models.Model):
    administrador = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='administrador_ID', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador'

    def __str__(self):
        return self.rol


class Anuncio(models.Model):
    anuncio_id = models.AutoField(db_column='anuncio_ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    banner = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    vacantes = models.CharField(max_length=30, blank=True, null=True)
    cant_interesados = models.CharField(max_length=30, blank=True, null=True)
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='categoria_ID', blank=True, null=True)  # Field name made lowercase.
    consumidor = models.ForeignKey('Consumidor', models.DO_NOTHING, db_column='consumidor_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anuncio'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    categoria_id = models.AutoField(db_column='categoria_ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

class Consumidor(models.Model):
    consumidor = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='consumidor_ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    facultad = models.ForeignKey('Facultad', models.DO_NOTHING, db_column='facultad_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consumidor'

    def __str__(self):
        #nombre=self.consumidor._meta.get_field('nombre')
        return self.descripcion

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

    def __str__(self):
        return self.nombre

class Facultad(models.Model):
    facultad_id = models.AutoField(db_column='facultad_ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facultad'


    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    habilidad_id = models.AutoField(db_column='habilidad_ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habilidad'

    def __str__(self):
        return self.nombre

class Habilidadxanuncio(models.Model):
    habilidad = models.OneToOneField(Habilidad, models.DO_NOTHING, db_column='habilidad_ID', primary_key=True)  # Field name made lowercase.
    anuncio = models.ForeignKey(Anuncio, models.DO_NOTHING, db_column='anuncio_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'habilidadxanuncio'


class Habilidadxconsumidor(models.Model):
    habilidad = models.OneToOneField(Habilidad, models.DO_NOTHING, db_column='habilidad_ID', primary_key=True)  # Field name made lowercase.
    consumidor = models.ForeignKey(Consumidor, models.DO_NOTHING, db_column='consumidor_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'habilidadxconsumidor'


class Interesados(models.Model):
    consumidor = models.ForeignKey(Consumidor, models.DO_NOTHING, db_column='consumidor_ID', blank=True, null=True)  # Field name made lowercase.
    anuncio = models.ForeignKey(Anuncio, models.DO_NOTHING, db_column='anuncio_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'interesados'


class Noticia(models.Model):
    noticia_id = models.AutoField(db_column='noticia_ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'noticia'

    def __str__(self):
        return self.titulo

class Persona(models.Model):
    persona_id = models.AutoField(db_column='persona_ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    lugar_origen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'

    def __str__(self):
        return self.nombre

class Sugerencia(models.Model):
    sugerencia_id = models.AutoField(db_column='sugerencia_ID', primary_key=True)  # Field name made lowercase.
    link_detalle = models.CharField(max_length=150, blank=True, null=True)
    persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sugerencia'

    def __str__(self):
        return self.link_detalle

class Usuario(models.Model):
    usuario_id = models.AutoField(db_column='usuario_ID', primary_key=True)  # Field name made lowercase.
    link_foto = models.CharField(max_length=30, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.persona.name