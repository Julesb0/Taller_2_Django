from django.db import models

class Solicitud(models.Model):
    TIPOS_SOLICITUD = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    tipo_solicitud = models.CharField(
        max_length=20,
        choices=TIPOS_SOLICITUD
    )

    asunto = models.CharField(max_length=150)
    descripcion = models.TextField()

    fecha_solicitud = models.DateField()

    archivo_adjunto = models.FileField(
        upload_to='solicitudes_archivos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.tipo_solicitud}"