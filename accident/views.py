from django.shortcuts import render
from accident.accident_analysis import *

# Create your views here.
def home(request):
    return render(request,'accident/main.html')

def accident(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        if name != '':
            print(name.lower())
            place=name.lower().title()
            try:
                continent_name, continent_code = country_to_continent(place)
            except:
                return render(request,'accident/index.html',{'error':'Invalid Country Name'})
            try:
                urls=Google_search(place)
                if len(urls)!=0:
                    text_content = extracting_news_content(urls)
                    print('Text Extracted')
                    city_list,dict_cities = extracting_cities(text_content,continent_code)
                    print(dict_cities)
                    if len(city_list)!=0:
                        coordinates_list = retreving_coordinates(city_list)
                        map_pt = map_plot(coordinates_list,continent_name)
                        print('WordCloud')
                        Word_cloud(dict_cities)
                        return render(request,'accident/index.html',{'map_pt':map_pt})
                return render(request,'accident/index.html',{'error':'No recent accidents occured'})
            except:
                return render(request,'accident/index.html',{'error':'No recent accidents occured'})
    return render(request, 'accident/front.html')

def results(request):
    return render(request, 'accident/index.html')
