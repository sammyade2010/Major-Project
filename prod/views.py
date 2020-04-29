from django.db.models import Q
from django.shortcuts import render
from .models import Appliances

def is_valid_queryparam(param):
    return param != '' and param is not None

def BootstrapFilterView(request):
    qs = Appliances.objects.all()
    description_contains_query = request.GET.get('description_contains')
    description_exact_query = request.GET.get('description_exact')
    description_or_company_query = request.GET.get('description_or_company')
    price_count_max = request.GET.get('price_count_max')

    if is_valid_queryparam(description_contains_query):
        qs = qs.filter(description=description_contains_query)

    elif is_valid_queryparam(description_exact_query):
        qs = qs.filter(id=description_exact_query)

    elif is_valid_queryparam(description_or_company_query):
        qs = qs.filter(Q(description=description_or_company_query) | 
                         Q(company__name__icontains=description_or_company_query)
                         ).distinct()
    
    if is_valid_queryparam(price_count_max):
        qs = qs.filter(prices=price_count_max)
    context = {
        'queryset': qs
    }
    return render(request, "prod/bootstrap_form.html", context)
