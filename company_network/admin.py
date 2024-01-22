from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from company_network.models import Product, Contributor


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):

    list_display = ("__str__",)
    list_filter = ("city",)
    search_fields = ("name", "city")
    actions = ["clear_debt"]

    def get_supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:contributor_contributor_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "-"

    get_supplier_link.short_description = "Supplier"

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Clear the debt"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("__str__",)
    list_filter = ("contributor",)
    search_fields = ("name", "model")
