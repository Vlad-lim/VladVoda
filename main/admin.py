from django.contrib import admin
from .models import Electron, Podrazdel, Online, zayavky, Indications, Posi, Con, ActiveHuman, Vakansies, Graphic,  Days, News, DonTarif, Service, ZugTarif, AsinTarif, Internet, NotarialDocs

class GraphicAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Position', 'Time', 'TimeEnd')
    list_display_links = ('Name',)
    list_filter = ('Days',)

class DonTarifAdmin(admin.ModelAdmin):
    list_display = ('Punkt', 'Unit', 'Price')
    search_field = ('Punkt', 'Service', 'Unit', 'Price')
    list_filter = ('Punkt', 'Service', 'Unit', 'Price')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('Tittle', 'Published', 'id')
    list_filter = ('Published',)
    search_fields = ('Tittle', 'Published')

class ActiveHumanAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Date', 'Photo')
    search_fields = ('Name', 'Date')

class VakansiesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CompanyName', 'Contact', 'Date')
    search_fields = ('Name', 'CompanyName', 'Contact', 'Date')

class InternetAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Number', 'Adress')
    search_fields = ('Name', 'Number', 'Adress')

class ConAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Contact', 'Pos')
    search_fields = ('Name', 'Pos', 'Contact')

class OnlineAdmin(admin.ModelAdmin):
    search_fields = ('Name', 'Text')

class ElectronAdmin(admin.ModelAdmin):
    search_fields = ('Name', 'Podrazdel', 'Adress', 'Email', 'Number', 'Theme', 'Text')
    list_display = ('Name', 'Podrazdel', 'Adress', 'Email', 'Number', 'Theme')
    list_filter = ('Podrazdel', 'Theme',)

class ZayavkyAdmin(admin.ModelAdmin):
    search_fields = ('Name', 'Date', 'Position',)
    list_display = ('Name', 'Date', 'Position',)
    list_filter = ('Position',)

admin.site.register(Electron, ElectronAdmin)
admin.site.register(Podrazdel)
admin.site.register(Indications)
admin.site.register(Online, OnlineAdmin)
admin.site.register(ActiveHuman, ActiveHumanAdmin)
admin.site.register(NotarialDocs)
admin.site.register(Internet, InternetAdmin)
admin.site.register(Vakansies, VakansiesAdmin)
admin.site.register(Graphic, GraphicAdmin)
admin.site.register(Days)
admin.site.register(zayavky, ZayavkyAdmin)
admin.site.register(Posi)
admin.site.register(Con, ConAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(DonTarif, DonTarifAdmin)
admin.site.register(ZugTarif, DonTarifAdmin)
admin.site.register(AsinTarif, DonTarifAdmin)
admin.site.register(Service)
