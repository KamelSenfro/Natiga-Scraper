import csv
import requests
from bs4 import BeautifulSoup
import time
def scrape_data(seat_number):
    url = "https://natega.cairo24.com/"

    # Prepare the data to be sent in the POST request
    data = {
        "seatNo": seat_number,
    }

    # Send the POST request to get the results
    response = requests.post(url, data=data)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the element containing the desired data
    result_element = soup.find("li", class_="col resultItem")

    if result_element:
        # Extract the required information
        seat_no = result_element.h1.text.strip()
        return seat_no
    else:
        return None

def save_to_csv(data_list):
    with open("scraped_data.csv", mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Seat Number"])
        for item in data_list:
            writer.writerow([item])

if __name__ == "__main__":
    start_seat_number = 1391446
    end_seat_number = 1391465
    seat_numbers = list(range(start_seat_number, end_seat_number + 1))
    scraped_data = []

    for seat_number in seat_numbers:
    result = scrape_data(seat_number)
    if result:
        scraped_data.append(result)
    time.sleep(1)  # Add a 1-second delay between each request

    if scraped_data:
        save_to_csv(scraped_data)
        print("Data scraped and saved to 'scraped_data.csv'")
    else:
        print("No data found.")
