import pickle
#task1

countries_dict = {"Україна": "Київ", "Франція": "Париж", "Англія": "Лондон"}

with open("CountryCity.pkl", "wb") as file:
    pickle.dump(countries_dict, file)

def add_country(country, capital):
    countries_dict[country] = capital

def remove_country(country):
    countries_dict.pop(country, None)

def find_country(country):
    return countries_dict.get(country, "Країна не знайдена")

def edit_country(country, new_capital):
    if country in countries_dict:
        countries_dict[country] = new_capital
    else:
        print("Країна не знайдена")

def save_data(filename):
    with open(filename, 'wb') as file:
        pickle.dump(countries_dict, file)

def load_data(filename):
    global countries_dict
    try:
        with open(filename, 'rb') as file:
            countries_dict = pickle.load(file)
    except FileNotFoundError:
        print("Файл не знайдено")

add_country("Японія", "Токіо")
add_country("США", "Вашингтон")
save_data("CountryCity.pkl")
load_data("CountryCity.pkl")
print(find_country("Україна"))
remove_country("Франція")
print(countries_dict)


#task2
music_bands = {}

def add_band(band, albums):
    music_bands[band] = albums

def remove_band(band):
    music_bands.pop(band, None)

def find_band(band):
    return music_bands.get(band, "Група не знайдена")

def edit_band(band, new_albums):
    if band in music_bands:
        music_bands[band] = new_albums
    else:
        print("Група не знайдена")

def save_data(filename):
    with open(filename, 'wb') as file:
        pickle.dump(music_bands, file)

def load_data(filename):
    global music_bands
    try:
        with open(filename, 'rb') as file:
            music_bands = pickle.load(file)
    except FileNotFoundError:
        print("Файл не знайдено")

add_band("The Beatles", ["Abbey Road", "Let It Be"])
add_band("Nirvana", ["Nevermind", "In Utero"])
save_data("music_bands.pkl")
load_data("music_bands.pkl")
print(find_band("The Beatles"))
remove_band("Nirvana")
print(music_bands)
