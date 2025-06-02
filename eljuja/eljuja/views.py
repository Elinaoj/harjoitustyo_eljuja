#from django.http import HttpResponse
from django.shortcuts import render, redirect
from artikkelit.models import Artikkeli, Myynti, Aika
#from artikkelit.models import Taloyhtio, Asunto
from django.http import HttpResponseForbidden
from artikkelit.forms import AikaForm, MyyntiForm


#def register(request):
#    return render(request, 'register.html')

def homepage(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'home.html')


def myynti(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Kirjaudu ensin sisään.")

    artikkelit = Artikkeli.objects.all()
    myynnit = Myynti.objects.all()

    # Ruoka-aikalomakkeen lähetys ja tallennus
    aika_form = AikaForm(request.POST or None)
    myynti_form = MyyntiForm(request.POST or None)
    if request.method == 'POST' and aika_form.is_valid():
        aika_form.save()

    passit = ['Aikuisten passi', 'Lasten passi', 'Alle 3-v']     # Määritetään mitkä artikkelit on passeja (henkilömäärää varten)
    ruokailuajat = ['1630', '1700', '1730', '1800']              # Määritetään ruokailuajat
    passit_per_aika = {}                                         # Tallennetaan passien henkilömäärät sanakirjaan
    for aika in ruokailuajat:
        passit_per_aika[aika] = 0                                # Aluksi 0 myytyä passia

    for myynti in myynnit:                                          # Käydään kaikki myyntitapahtumat läpi
        if myynti.artikkeli.artikkeli in passit and myynti.aika:    # Tarkistetaan onko tietty artikkeli passi ja onko myyntiaika merkitty
            passit_per_aika[myynti.aika.aika] += myynti.kpl         # Lisätään myydyt passit sanakirjan tiettyyn aikaan

    myyntisumma = 0

    # POST-pyynnöt myynti-sivulta
    if request.method == 'POST':
        valittu_aika_str = request.POST.get('aika')
        valittu_aika = Aika.objects.get(aika=valittu_aika_str)

        if 'tallenna' in request.POST:                            # Tallenna -napista painettu, tallennetaan myynti
            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi)

                if kpl_arvo and int(kpl_arvo) > 0:
                    Myynti.objects.create(
                        artikkeli=artikkeli,
                        kpl=int(kpl_arvo),
                        aika=valittu_aika
                    )
                
            # myyntisumma += kpl_arvo * artikkeli.hinta

            return redirect('myynti')                           # Päivitetään myyntisivu heti POST:in jälkeen (URL name = 'myynti')

        elif 'nayta_summa' in request.POST:                     # Näytä summa -napista painettu, lasketaan ja näytetään summa
            for artikkeli in Artikkeli.objects.all():
                kentan_nimi = f'kpl_{artikkeli.id}'
                kpl_arvo = request.POST.get(kentan_nimi)

                if kpl_arvo and int(kpl_arvo) > 0:
                    myyntisumma += int(kpl_arvo) * artikkeli.hinta

    #         aika_form = AikaForm(request.POST)

    # else:
    #     aika_form = AikaForm()


        #     if myynti_form.is_valid():
        #         myynti_form = myynti_form.cleaned_data.get(myynti_form)
        #     return render(request, 'myynti.html', {
        #         'myynti_form': myynti_form,
        #         'myyntisumma': myyntisumma,
        #         })

        # print(request.POST)

    return render(request, 'myynti.html', {
        'artikkelit': artikkelit,
        'aika_form': aika_form,
        'myynti_form': myynti_form,
        'myynnit': myynnit,
        'passit_per_aika': passit_per_aika,
        'myyntisumma': myyntisumma,
        # 'valittu_aika': valittu_aika_str,
        })

def excel(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'excel.html')

        # if myynti.artikkeli.artikkeli in passit:                 # Onko myyty artikkeli passi
        #     if myynti.aika:                                      # Otetaan ruokailuaika jos sellainen on liitetty
        #         ruoka_aika = myynti.aika.aika
        #         if ruoka_aika not in passit_per_aika:            # Jos artikkeli ei ole sanakirjassa, aloitetaan nollasta
        #             passit_per_aika[ruoka_aika] = 0
        #         passit_per_aika[ruoka_aika] += myynti.kpl        # Lisätään aikaan myynnin henkilömäärä


#def myynti(request):
#    if not request.user.is_authenticated:
    #     return HttpResponseForbidden("Kirjaudu ensin sisään.")
    # if not request.user.is_superuser:
    #     return HttpResponseForbidden("Sinulla ei ole oikeuksia käyttää tätä sivua.")
    # artikkelit = Artikkeli.objects.all()
    # myynnit = Myynti.objects.all()

    # if request.method == 'POST': 
    #     aika_form = AikaForm(request.POST or None)
    #     if aika_form.is_valid():
    #         aika_form.save()
    #         return render(request, 'myynti.html', { 'artikkelit': artikkelit, 'aika_form': aika_form, 'Myynnit': myynnit})

    # else:
    #     aika_form = AikaForm()
       

    # return render(request, 'myynti.html', { 'artikkelit': artikkelit, 'aika_form': aika_form, 'Myynnit': myynnit})


#def taloyhtio(request):
#    taloyhtiot = ["Aatelitie_3", "Aatelitie_5_7", "Aatelisherra", "Aatelisrouva", "Renkipoika", "Piikatytto", "Omakotitalot"]
#    return render (request, 'myynti.html', { 'taloyhtiot', taloyhtiot })

#def taloyhtiot(request):
#    taloyhtiot = Taloyhtio.object.all()
#    context = {'taloyhtiot': taloyhtiot}
#    return render(request, 'myynti.html', context)