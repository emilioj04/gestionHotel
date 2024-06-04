from django.contrib import admin
from .models import Factura
# Register your models here.


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'reserva', 'total', 'subtotal', 'totalImpuestos')

    actions = ['calcular_total_facturas']

    def calcular_total_facturas(self, request, queryset):
        for factura in queryset:
            factura.calcular_total()
        self.message_user(request, "Totales calculados y guardados para las facturas seleccionadas.")
    calcular_total_facturas.short_description = 'Calcular totales para las facturas seleccionadas'


admin.site.register(Factura,FacturaAdmin)