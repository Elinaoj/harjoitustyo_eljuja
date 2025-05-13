from django.core.management.base import BaseCommand
from posts.models import Taloyhtio, Asunto

class Command(BaseCommand):
    help = 'Lataa Taloyhtiot ja Asunnot'

    def handle(self, *args, **kwargs):
        Asunto.objects.all().delete()
        taloyhtiot = [
            'AATELITIE_3', 'AATELITIE_5_7', 'AATELISHERRA', 'AATELISROUVA', 'RENKIPOIKA', 'PIIKATYTTO', 'OMAKOTITALOT'
        ]

        if not Taloyhtio.objects.count():
            for taloyhtio in taloyhtiot:
                Taloyhtio.objects.create(name=taloyhtio)

        # as yht 1
        A1 = Taloyhtio.objects.get(name='As1')

        ty1_asunnot = [
            'AS11',
            'AS22',
            'AS33'
        ]

        for asunto in ty1_asunnot:
            Asunto.objects.create(name=asunto, taloyhtio=A1)

        # as yht 2
        A2 = Taloyhtio.objects.get(name='As2')

        ty2_asunnot = [
            'ASXX',
            'ASYY',
            'ASZZ'
        ]

        for asunto in ty2_asunnot:
            Asunto.objects.create(name=asunto, taloyhtio=A2)

        # as yht 3
        A3 = Taloyhtio.objects.get(name='As3')

        ty3_asunnot = [
            'AS777',
            'AS888',
            'AS999'
        ]

        for asunto in ty3_asunnot:
            Asunto.objects.create(name=asunto, taloyhtio=A3)