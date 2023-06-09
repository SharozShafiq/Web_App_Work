from django.db import models
from baham.enum_types import VehicleType
 
# Create your models here.
class VehiclesModel(models.Model):
    make_id = models.AutoField(primary_key=True, db_column='id')
 
    vender = models.CharField(max_length=20, null=False, blank=False)
 
    model = models.CharField(max_length=20, null=False, blank=False, default='Unknown')
 
    type = models.CharField(max_length=50, choices=[(t.name, t.value) for t in VehicleType], help_text="Select the vehicle chassis type")
 
    capacity = models.PositiveBigIntegerField(null=False, default=2)
 
    class Meta:
        db_table = 'baham_vehicle_model'