# obtener informacion del numero de telefono
import phonenumbers
from phihonenumbers import carrier, geocoder
def nuncheckr(phone):
    info=[]
    numero =phonenumbers.parse(phone)
    info.append(geocoder.description_for_numer(numero,"es"))
    info.append(carrier.name_for_number(numero,"es"))
    return info
    phone = input("digite un numero telefonico: ")
    print(nuncheckr(phone))