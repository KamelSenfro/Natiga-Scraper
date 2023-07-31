import requests
from bs4 import BeautifulSoup

def scrape_data(seat_number):
    url = "https://natega.cairo24.com/"

    # Prepare the data to be sent in the POST request
    data = {
        "seatNo": seat_number,
        "submit": "النتيجة"
    }

    # Send the POST request to get the results
    response = requests.post(url, data=data)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the element containing the desired data
    name_element = soup.find("span", class_="formatt active", text="الأسم:")
    if name_element:
        name = name_element.find_next_sibling("span").text.strip()
        return name
    else:
        return None

if __name__ == "__main__":
    seat_numbers = list(range(1391446, 1391466))  # Replace with your desired seat numbers
    scraped_data = []

    for seat_number in seat_numbers:
        result = scrape_data(seat_number)
        if result:
            scraped_data.append(result)

    if scraped_data:
        for seat_number, name in zip(seat_numbers, scraped_data):
            print(f"Seat Number: {seat_number} - Name: {name}")
    else:
        print("No data found.")
