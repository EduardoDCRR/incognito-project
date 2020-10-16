import csv
import sys

from django.core.management.base import BaseCommand, CommandError

from squirrels.models import Squirrel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('data')

    def handle(self, *args, **options):
        meta = Squirrel._meta
        fields = [n.name for n in meta.fields]
        data = options['data']
        
        print(data)
        with open(data,'w') as csvfile:
            w = csv.writer(csvfile)
            w.writerow(fields)
            for item in Squirrel.objects.all():
                w.writerow([getattr(item, field) for field in fields])
