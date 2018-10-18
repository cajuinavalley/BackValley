from django.core.management.base import BaseCommand, CommandError
import csv

from backvalley.models import Startup, Employee, Sector, Role

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_path in options['csv']:
            with open(csv_path) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:

                    st = Startup()

                    # NOME STARTUP
                    st.name = row['NOME STARTUP']
                    # SITE DA STARTUP
                    st.site = row['SITE DA STARTUP']
                    # CIDADE
                    # ENDEREÇO DA SEDE
                    # EMAIL DE CONTATO DA STARTUP
                    # TELEFONE CONTATO DA STARTUP
                    # REDE SOCIAL
                    # MISSÃO / SLOGAN
                    # RESUMO DE SUA SOLUÇÃO
                    # SETOR DE ATUAÇÃO
                    # NOME 
                    # FUNÇÃO
                    # PERFIL FACEBOOK
                    # PERFIL LINKEDIN

                    st.save()
