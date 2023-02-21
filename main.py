import requests
import datetime as dt
import smtplib
import time

MY_LAT = 13.8000382
MY_LNG = -88.9140683
PASSWORD = "r38339059@gmail.com"
EMAIL = "olbcxcgukjewftjn"

def is_iss_above():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data['iss_position']["latitude"])
    iss_longitude = float(data['iss_position']["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time = dt.datetime.now()
    if sunset < time.hour < sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_above():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="gogo@gmail.con",
                msg="subject: look up\n\nlook up"
            )

