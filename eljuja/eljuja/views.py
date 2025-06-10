#from django.http import HttpResponse
from django.shortcuts import render, redirect
from artikkelit.models import Artikkeli, Myynti, Aika, Taloyhtio, Asunto
from django.http import HttpResponseForbidden, JsonResponse
from artikkelit.forms import AikaForm, MyyntiForm, AsuntoForm
from django.db import connection

def homepage(request):
    return render(request, 'home.html')

def get_asunnot(request, taloyhtio_id):
    # Haetaan taloyhtion asunnot ja laitetaan ne listaan
    asunnot_query = Asunto.objects.filter(taloyhtio_id=taloyhtio_id).values('id', 'nimi')
    asunto_lista = list(asunnot_query)
    return JsonResponse({'asunnot': asunto_lista})

def kokonaismyynti_sql(self):
    # Haetaan tietokannasta myydyn artikkelin kpl määrä ja palautetaan pelkkä lukumäärä
    with connection.cursor() as cursor:
        cursor.execute('SELECT SUM(kpl) FROM artikkelit_myynti WHERE artikkeli_id == %s', [self])
        row = cursor.fetchone()
        return row[0]
    
def myynti(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Kirjaudu ensin sisään.")

    artikkelit = Artikkeli.objects.all()
    myynnit = Myynti.objects.all()
    taloyhtiot = Taloyhtio.objects.all()
    asunnot = Asunto.objects.all()

    # Tallennetaan kaikkien artikkeleiden myyntimäärät
    kokonaismyynti = {}
    for a in artikkelit:
        kmyynti = kokonaismyynti_sql(a.id)
        if kmyynti == None:
            kmyynti = 0
        kokonaismyynti[a] = kmyynti

    # Eri lomakkeiden lähetys ja tallennus
    aika_form = AikaForm(request.POST or None)
    myynti_form = MyyntiForm(request.POST or None)
    asunto_form = AsuntoForm(request.POST or None)

    if request.method == 'POST' and asunto_form.is_valid():
       pass

    if request.method == 'POST' and aika_form.is_valid():
        aika_form.save()


    # Määritetään mitkä artikkelit on passeja (henkilömäärää varten)
    passit = ['Aikuisten passi', 'Lasten passi', 'Alle 3-v']     
    # Määritetään ruokailuajat
    ruokailuajat = ['1630', '1700', '1730', '1800']              
    passit_per_aika = {}                                         # Tallennetaan passien henkilömäärät sanakirjaan
    for aika in ruokailuajat:
        # Aluksi 0 myytyä passia
        passit_per_aika[aika] = 0                                
    
    # Käydään kaikki myyntitapahtumat läpi
    for myynti in myynnit:                                          
        # Tarkistetaan onko tietty artikkeli passi ja onko myyntiaika merkitty
        if myynti.artikkeli.artikkeli in passit and myynti.aika:
            # Lisätään myydyt passit sanakirjan tiettyyn aikaan    
            passit_per_aika[myynti.aika.aika] += myynti.kpl         

    myyntisumma = 0
    aika_form = AikaForm(request.POST or None)
    kpl_arvot = {}                                 # sanakirja säilyttämään kpl_arvot kentissä kun "Näytä summa" -nappia painetaan

    # POST-pyynnöt myynti-sivulta
    if request.method == 'POST':
        if 'tallenna' in request.POST and aika_form.is_valid():          # "Tallenna" -napista painettu, tallennetaan myynti
            valittu_aika = aika_form.cleaned_data['aika']                # käytetään aika_formista vain valittua arvoa
        
        # Tallenna -napista painettu, tallennetaan myynti
            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi)
                # myyntisumma += kpl_arvo * artikkeli.hinta
#print(artikkeli, kpl_arvo, kentan_nimi)
                if kpl_arvo and int(kpl_arvo) > 0:
                    Myynti.objects.create(
                        artikkeli=artikkeli,
                        kpl=int(kpl_arvo),
                        aika=valittu_aika           # käytetään olemassa olevaa Aika-instanssia
                    )
            # Päivitetään myyntisivu heti POST:in jälkeen (URL name = 'myynti')
            return redirect('myynti')                           
        # Näytä summa -napista painettu, lasketaan ja näytetään summa
        elif 'nayta_summa' in request.POST:                     
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
        'asunto_form': asunto_form,
        'myynnit': myynnit,
        'passit_per_aika': passit_per_aika,
        'myyntisumma': myyntisumma,
        'taloyhtiot': taloyhtiot,
        'asunnot': asunnot,
        'kokonaismyynti': kokonaismyynti
        'kpl_arvot': kpl_arvot,
        })

def excel(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'excel.html')
