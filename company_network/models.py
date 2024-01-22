from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Contributor(models.Model):
    name = models.CharField()

    CHOICES = [
        ('factory', 'Factory'),
        ('retail_network', 'Retail Network'),
        ('individual_entrepreneur', 'Individual Entrepreneur'),
    ]
    contributor = models.CharField(
        choices=CHOICES
    )
    email = models.EmailField()
    country = models.CharField()
    city = models.CharField()
    street = models.CharField()
    house_number = models.CharField()
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, related_name='supplier_company')
    debt = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def hierarchy_level(self):
        if self.contributor == 'factory':
            return 0

        if not self.supplier:
            return max(1, 2)

        return self.supplier.hierarchy_level + 1


class Product(models.Model):
    name = models.CharField()
    model = models.CharField()
    launch_date = models.DateField()
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.model}'
