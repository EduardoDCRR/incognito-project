import csv

from django.core.management.base import BaseCommand

from squirrels.models import Squirrel


class Command(BaseCommand):
    help = 'get sentance into file '

    def add_arguments(self, parser):
        parser.add_argument('data',help='file containting squirrel data')

    def handle(self, *args, **options):

        file_ = options['data']
        
        with open(file_) as fp:
            reader=csv.DictReader(fb)
            d=list(reader)

        for item in d:
            obj =Squirrel(
                X=item['X'],
                Y=item['Y'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Shift = item['Shift'],
                Date = item['Date'],
                Age = item['Age'],
                Primary_Fur_Color = item['Primary Fur Color'],
                Location = item['Location'],
                Specific_Location = item['Specific Location'],
                Running = item['Running'],
                Chasing = item['Chasing'],
                Climbing = item['Climbing'],
                Eating = item['Eating'],
                Foraging = item['Foraging'],
                Other_Activities = item['Other Activities'],
                Kuks = item['Kuks'],
                Quaas = item['Quaas'],
                Moans = item['Moans'],
                Tail_flags = item['Tail flags'],
                Tail_twitches = item['Tail twitches'],
                Approaches = item['Approaches'],
                Indifferent = item['Indifferent'],
                Runs_from = item['Runs from'], )
            obj.save()


       # msg = f'you are importing data from{file_}'
       # self.stdout.write(self.style.SUCCESS((msg))
