import requests
import json
import time
import sys
import yagmail


def get_data(CompanyName, URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    }
    response = requests.get(URL, headers=headers, stream=True)
    data = response.text
    data = json.loads(data)
    data = data['data']
    company_name_data = data['company']
    if (CompanyName != company_name_data):
        raise Exception("Company name different")
    else:
        print(f"Company name: " + CompanyName)
    return data


def send_mail(data):
    password = sys.argv[1]
    sender = sys.argv[2]
    reciver = 'ajinkyaakotkar7@gmail.com'

    subject = f"{data['company']} value changed"

    contents = f"""
    Respected sir/ma'am
        This is automated mail
        Company Name: {data['company']}
        Current price: {data['pricecurrent']}
        Percentage day change: {data["pricepercentchange"]}
        Price updated time: {data['lastupd']}
    """

    yag = yagmail.SMTP(sender, password)
    yag.send(to=reciver, subject=subject, contents=contents)
    print("SENT!!")


data = get_data("Vodafone Idea",
                "https://priceapi.moneycontrol.com/pricefeed/nse/equitycash/IC8")
market_state = data['market_state']

while (market_state == "OPEN"):
    data = get_data("Vodafone Idea",
                    "https://priceapi.moneycontrol.com/pricefeed/nse/equitycash/IC8")
    market_state = data['market_state']
    if (float(data["pricepercentchange"]) < 0):
        send_mail(data)
    time.sleep(60)
