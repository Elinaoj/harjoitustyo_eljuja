#from django.http import HttpResponse
from django.shortcuts import render, redirect
from artikkelit.models import Artikkeli, Myynti, Aika
#from artikkelit.models import Taloyhtio, Asunto
from django.http import HttpResponseForbidden
from artikkelit.forms import AikaForm, MyyntiForm


def homepage(request):
    return render(request, 'home.html')


def myynti(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Kirjaudu ensin sisään.")

    artikkelit = Artikkeli.objects.all()
    myynnit = Myynti.objects.all()
    myynti_form = MyyntiForm()

    passit = ['Aikuisten passi', 'Lasten passi', 'Alle 3-v']     # Määritetään mitkä artikkelit on passeja (henkilömäärää varten)
    ruokailuajat = ['1630', '1700', '1730', '1800']              # Määritetään ruokailuajat
    passit_per_aika = {}                                         # Tallennetaan passien henkilömäärät sanakirjaan
    for aika in ruokailuajat:
        passit_per_aika[aika] = 0                                # Aluksi 0 myytyä passia

    for myynti in myynnit:                                          # Käydään kaikki myyntitapahtumat läpi
        if myynti.artikkeli.artikkeli in passit and myynti.aika:    # Tarkistetaan onko tietty artikkeli passi ja onko myyntiaika merkitty
            passit_per_aika[myynti.aika.aika] += myynti.kpl         # Lisätään myydyt passit sanakirjan tiettyyn aikaan

    myyntisumma = 0
    aika_form = AikaForm(request.POST or None)
    kpl_arvot = {}                                 # sanakirja säilyttämään kpl_arvot kentissä kun "Näytä summa" -nappia painetaan

    # POST-pyynnöt myynti-sivulta
    if request.method == 'POST':

        if 'tallenna' in request.POST and aika_form.is_valid():          # "Tallenna" -napista painettu, tallennetaan myynti
            valittu_aika = aika_form.cleaned_data['aika']                # käytetään aika_formista vain valittua arvoa
            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi)

                if kpl_arvo and int(kpl_arvo) > 0:
                    Myynti.objects.create(
                        artikkeli=artikkeli,
                        kpl=int(kpl_arvo),
                        aika=valittu_aika           # käytetään olemassa olevaa Aika-instanssia
                    )
        
            return redirect('myynti')                           # Päivitetään myyntisivu heti POST:in jälkeen (URL name = 'myynti')

        elif 'nayta_summa' in request.POST:       # "Näytä summa" -napista painettu, lasketaan ja näytetään summa
            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi, '0')   # säilytetään kentissä kpl_arvot
                kpl_arvot[artikkeli.id] = kpl_arvo

                if kpl_arvo and int(kpl_arvo) > 0:
                    myyntisumma += int(kpl_arvo) * artikkeli.hinta
    else:
        aika_form = AikaForm()


    return render(request, 'myynti.html', {
        'artikkelit': artikkelit,
        'aika_form': aika_form,
        'myynti_form': myynti_form,
        'myynnit': myynnit,
        'passit_per_aika': passit_per_aika,
        'myyntisumma': myyntisumma,
        'kpl_arvot': kpl_arvot,
        })

