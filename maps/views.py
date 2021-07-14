from django.shortcuts import render

# Create your views her
import folium
# folium은 1) 위도와 경도 2) 범위를 지정해줘야 한다.

def home(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start=10)
    mf = mf._repr_html_()
    first = 'changsok'
    result = {'mapfolium' : mf, 'f01':first}

    return render(request, template_name='maps/home.html', context=result)

