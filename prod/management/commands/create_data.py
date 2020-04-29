import random
from django.core.management.base import BaseCommand
from prod.models import Appliances, Company



company = [
    'Curries', 'DID', 'Euronics'
]

def generate_company_name():
    index = random.randint(0, 2)
    return company[index]

def generate_prices_count():
    return random.randint(0, 2000)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='the text file that contains appliances')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.csv',encoding="mbcs") as file:
            for line in file:
                description = line
                company_name = generate_company_name()
                prices = generate_prices_count()

                company = Company.objects.get_or_create(
                    name=company_name
                )

                appliances = Appliances(
                    description=description,
                    company=Company.objects.get(name=company_name),
                    prices=prices
                )

                appliances.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))