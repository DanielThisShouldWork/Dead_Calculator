from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import LifeExpectancy

def error(request):
    return render(request, 'application/404.html')

def contact(request):
    return render(request, 'application/contact.html')

def index(request):
    return render(request, 'application/index.html')

def login(request):
    return render(request, 'application/login.html')

def password_reset(request):
    return render(request, 'application/password-reset.html')

def register(request):
    return render(request, 'application/register.html')

def data(request):
    return render(request, 'application/data.html')


from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import LifeExpectancy

from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import LifeExpectancy

def set_life_expectancy(request):
    if request.method == "POST":
        birth_date = request.POST.get("birth_date")
        country = request.POST.get("country")

        # Cerca l'aspettativa di vita per il paese selezionato
        expectancy = LifeExpectancy.objects.filter(country=country).first()
        if expectancy:
            # Calcola la data di fine vita stimata
            birth_date_dt = datetime.strptime(birth_date, '%Y-%m-%d')
            life_expectancy_years = expectancy.expectancy_years
            end_date = birth_date_dt + timedelta(days=life_expectancy_years * 365)

            # Salva i dati nella sessione
            request.session['birth_date'] = birth_date
            request.session['country'] = country
            request.session['end_date'] = end_date.isoformat()  # Converti `end_date` in stringa

            # Reindirizza alla pagina index
            return redirect('index')

    # Se non è un POST, torna alla pagina dei dati
    return redirect('data_view')


       
    # Se non è un POST, torna alla pagina dei dati
    return redirect('data_view')




    # Aggiungi la lista dei paesi al contesto per il dropdown
    countries = LifeExpectancy.objects.values_list('country', flat=True)
    return render(request, 'data.html', {'countries': countries})


    

def data_view(request):
    life_expectancies = LifeExpectancy.objects.all()  # Recupera tutti i dati dal modello
    print(life_expectancies)
    #return render(request, 'application/data.html', {'life_expectancies': life_expectancies})

    if request.method == "POST":
        # Logica per ottenere e processare i dati inviati dall'utente
        birth_date = request.POST.get('birth_date')
        country = request.POST.get('country')
        
        # Logica per impostare `life_expectancies` se necessario (ad es., in base ai dati del form)
        # life_expectancies = ottieni_dati_speranza_di_vita(country)

        # Controlla e calcola `end_date` se possibile
        if birth_date and country in life_expectancies:
            life_expectancy = life_expectancies[country]
            birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
            end_date = birth_date_obj.replace(year=birth_date_obj.year + life_expectancy)
            request.session['birth_date'] = birth_date
            request.session['country'] = country
            request.session['end_date'] = end_date.isoformat()

            return redirect('index')

    return render(request, 'application/data.html', {
        'life_expectancies': life_expectancies
    })


from datetime import datetime

def index(request):
    birth_date = request.session.get('birth_date')
    country = request.session.get('country')
    end_date_str = request.session.get('end_date')

    # Converte `end_date_str` in `datetime`, se presente
    end_date = datetime.fromisoformat(end_date_str) if end_date_str else None

    # Converte `end_date` in una stringa formattata per JavaScript
    formatted_end_date = end_date.strftime('%Y-%m-%dT%H:%M:%S') if end_date else ''

    # Passa `formatted_end_date` al template come stringa
    return render(request, 'application/index.html', {
        'birth_date': birth_date,
        'country': country,
        'end_date': formatted_end_date,
    })



#def index(request):
    # Redirect all'URL /data
    #return redirect('/data')  # Assicurati che 'data' sia il nome della tua vista per la pagina data.

#def data_view(request):
    # Logica per gestire la pagina data
    #return render(request, 'application/data.html')