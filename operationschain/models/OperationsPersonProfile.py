from django.db import models


class OperationsPersonProfile(models.Model):
    user = models.OneToOneField('custom_auth.User', on_delete=models.DO_NOTHING, related_name="operations")

    warehouse = models.ForeignKey('warehouse.Warehouse',
                                  related_name="warehouse_operations", on_delete=models.DO_NOTHING)

    management_choice = (('Manager', 'Manager'),
                         ('Regional Manager', 'Regional Manager'),
                         ('Worker', 'Worker'))
    management_status = models.CharField(max_length=100, choices=management_choice, default="Worker")
    is_test_profile = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
