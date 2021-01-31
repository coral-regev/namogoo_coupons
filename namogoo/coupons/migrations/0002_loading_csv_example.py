from django.db import migrations
import csv
from ..models import Coupons


def load_csv(apps, schema_editor):
    with open("./coupons/resources/test_coupon.csv") as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            domain = row[0]
            coupon_value = row[1]
            coupon_code = row[2]
            Coupons.objects.create(domain=domain, coupon_value=coupon_value, coupon_code=coupon_code)


class Migration(migrations.Migration):
    dependencies = [
        ('coupons', '0001_initial'),

    ]

    operations = [
        migrations.RunPython(load_csv),
    ]
