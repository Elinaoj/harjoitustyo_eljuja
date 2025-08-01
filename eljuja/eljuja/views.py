from django.shortcuts import render, redirect
from artikkelit.models import Artikkeli, Myynti, Taloyhtio, Asunto
from django.http import HttpResponseForbidden, JsonResponse
from artikkelit.forms import AikaForm
from django.db import connection
from .services import get_all_rows

def homepage(request):
    return render(request, 'home.html')

# def master_sheets(request):
#     """
#     View to display the master sheets.
#     """
#     print('\nmaster_sheets called\n')
    
#     # Fetch all rows from the master sheet
#     master_data = get_all_rows('ÄLÄ KÄYTÄ_KOPIO Master Excel_myyntitestailua varten', 'Myynti Aatelitie 3')
    
#     print('\nmaster_data\n', master_data)
#     # Render the template with the fetched data
#     return render(request, 'master_sheets.html', {'master_data': master_data})

def get_asunnot(request, taloyhtio_id):
    # Haetaan taloyhtion asunnot ja laitetaan ne listaan
    asunnot_query = Asunto.objects.filter(taloyhtio_id=taloyhtio_id).values('id', 'nimi')
    asunto_lista = list(asunnot_query)
    return JsonResponse({'asunnot': asunto_lista})

def kokonaismyynti_sql(self):
    # Haetaan tietokannasta myydyn artikkelin kpl määrä ja palautetaan pelkkä lukumäärä
    with connection.cursor() as cursor:
        cursor.execute('SELECT SUM(kpl) FROM artikkelit_myynti WHERE artikkeli_id == %s', [self])
        rivi = cursor.fetchone()
        return rivi[0]

def kokonaismyynti_asunto_sql(self, taloyhtio_id, asunto_id):
    # Haetaan tietokannasta tietyn taloyhtion ja asunnon myydyn artikkelin kpl määrä ja palautetaan pelkkä lukumäärä
    with connection.cursor() as cursor:
        #print(self, taloyhtio_id, asunto_id)
        cursor.execute('SELECT SUM(kpl) FROM artikkelit_myynti WHERE artikkeli_id == %s AND taloyhtio_id == %s AND asunto_id == %s ', [self, taloyhtio_id, asunto_id])
        rivi = cursor.fetchone()
        #print(rivi)
        return rivi[0]

def myynti(request):
    # Tarkistetaan kirjautuminen
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Kirjaudu ensin sisään.")

    # Haetaan tietokannasta eri objektit listaan
    artikkelit = Artikkeli.objects.all()
    myynnit = Myynti.objects.all()
    taloyhtiot = Taloyhtio.objects.all()
    asunnot = Asunto.objects.all()

    # Tallennetaan kaikkien artikkeleiden myyntimäärät
    kokonaismyynti = {}
    for a in artikkelit:
        # kutsutaan funktiota kokonaismyynti_sql, jokaiselle artikkelille erikseen ja laitetaan artikkelin kokonaismyynti sanakirjaan
        kmyynti = kokonaismyynti_sql(a.id)
        if kmyynti == None:
            kmyynti = 0
        kokonaismyynti[a] = kmyynti


    # Määritetään mitkä artikkelit on passeja (henkilömäärää varten)
    passit = ['Passi', 'Lasten passi', 'Alle 3-v']     
    
    # Määritetään ruokailuajat
    ruokailuajat = ['1630', '1700', '1730', '1800']              
    
    # Tallennetaan passien henkilömäärät sanakirjaan
    passit_per_aika = {}                                         

    for aika in ruokailuajat:
        # Aluksi 0 myytyä passia
        passit_per_aika[aika] = 0                                

    # Käydään kaikki myyntitapahtumat läpi
    for myynti in myynnit: 
        print('myynti', myynti.artikkeli.artikkeli)
        # Tarkistetaan onko tietty artikkeli passi ja onko myyntiaika merkitty
        
        if myynti.artikkeli.artikkeli in passit and myynti.aika:
            # Lisätään myydyt passit sanakirjan tiettyyn aikaan    
            passit_per_aika[myynti.aika.aika] += myynti.kpl  
    
    # sanakirja säilyttämään kpl_arvot kentissä kun "Näytä summa" -nappia painetaan
    myyntisumma = 0
    kpl_arvot = {}    
                                 
    # Tallenetaan aika_formiin POST:n aikavalinnat
    aika_form = AikaForm(request.POST or None)
    
    # POST-pyynnöt myynti-sivulta
    if request.method == 'POST':
        print(request.POST)
        # Otetaan talteen taloyhtio ja asunto -valinnat    
        taloyhtio_id = request.POST.get('taloyhtio')
        asunto_id = request.POST.get('asunto')
        valittu_taloyhtio = Taloyhtio.objects.get(id=taloyhtio_id) if taloyhtio_id else None
        valittu_asunto = Asunto.objects.get(id=asunto_id) if asunto_id else None
        

        # Tallenna -napista painettu, tallennetaan myynti
        if 'tallenna' in request.POST and aika_form.is_valid():

            # käytetään aika_formista vain valittua arvoa
            valittu_aika = aika_form.cleaned_data['aika']
            kateismyynti = request.POST.get('kateismyynti', 'off') == 'on'  # Käteismyynti on valittu

            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi)
                if kpl_arvo and int(kpl_arvo) > 0:
                    Myynti.objects.create(
                        artikkeli=artikkeli,
                        kpl=int(kpl_arvo),
                        # käytetään olemassa olevaa Aika-instanssia
                        aika=valittu_aika,
                        taloyhtio=valittu_taloyhtio,
                        asunto=valittu_asunto,
                        kateismyynti=kateismyynti               
                        )
                    
            # Päivitetään myyntisivu heti POST:in jälkeen (URL name = 'myynti')
            return redirect('myynti')                           
        
        # Näytä summa -napista painettu, lasketaan ja näytetään summa
        elif 'nayta_summa' in request.POST: 
            # säilytetään kentissä kpl_arvot                    
            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi, '0')
                kpl_arvot[artikkeli.id] = kpl_arvo

                if kpl_arvo and int(kpl_arvo) > 0:
                    myyntisumma += int(kpl_arvo) * artikkeli.hinta
    else:
        aika_form = AikaForm()

    return render(request, 'myynti.html', {
        'artikkelit': artikkelit,
        'aika_form': aika_form,
        'myynnit': myynnit,
        'passit_per_aika': passit_per_aika,
        'myyntisumma': myyntisumma,
        'taloyhtiot': taloyhtiot,
        'asunnot': asunnot,
        'kokonaismyynti': kokonaismyynti,
        'kpl_arvot': kpl_arvot,
        })

def excel(request):
    artikkelit = Artikkeli.objects.all()
    asunnot = Asunto.objects.all()

    # Alustetaan lista taloyhtioista [[taloyhtio,asunto, {artikkelit, kpl}....]]]
    taloyhtiot_lista = []
    for asunto in asunnot:
        # Alustetaan listat myynti_asunnot, johon talletetaan taloyhtion kaikki asunnot sekä myyty_asunto, johon talletetaan asuntokohtainen myynti
        myynti_asunnot = []
        myyty_asunto = []
        for artikkeli in artikkelit:
            # Haetaan tietokannasta, onko artikkeleita myyty asunnolle
            myyty_kpl = kokonaismyynti_asunto_sql(artikkeli.id, asunto.taloyhtio.id, asunto.id)
            # Jos ei ole myyty artikkelia, palataan alkuun
            if myyty_kpl == None:
                continue
            # Jos artikkelia on myyty asuntoon, lisätään listaan artikkeli ja kpl määrä sanakirjana
            myyty_asunto.append({artikkeli.artikkeli: myyty_kpl})
            print('myynti: ', myyty_kpl, myyty_asunto)
            print()
            # Lisätään asunnot listaan myydyt artikkelit
            myynti_asunnot.append(myyty_asunto)
        # Jos asuntoon on ostettu artikkeleita, lisätään asunto taloyhtiölistaan.
        if len(myynti_asunnot) > 0:
            taloyhtiot_lista.append([asunto.taloyhtio.nimi, asunto.nimi, myyty_asunto])
        
    print(taloyhtiot_lista)
    print()

    return render(request, 'excel.html')
