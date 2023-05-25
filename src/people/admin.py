from django.contrib import admin

# Register your models here.

class AdminPersona(admin.ModelAdmin):
    list_display = ["_str_","nombres", "apellidos","email"]
    list_filter = ["nombres", "apellidos", "email"]
    list_editable = ["nombres", "apellidos", "email"]
    class Meta:
        model = Persona
admin.site.register(Persona, AdminPersona)