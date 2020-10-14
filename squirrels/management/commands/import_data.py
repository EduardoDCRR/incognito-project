from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'get sentance into file '

    def add_arguments(self, parser):
        parser.add_argument('import_data ',help='file containting squirrel data')

    def handle(self, *args, **options):

        file_ = options['import_data']
        msg = f'you are importing data from{file_}'
        self.stdout.write(self.style.SUCCESS(msg))
