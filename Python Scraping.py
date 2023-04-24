import requests
from bs4 import BeautifulSoup
import json
import csv
from scrapingbee import ScrapingBeeClient
import time

# start the timer
start_time = time.time()

# your web scraping code here
# ...

# set the search query
search_query = "example query"

# set the number of pages to scrape
num_pages = 100

# set the starting page number
page_num = 0

# set the results counter
result_count = 0

# create an empty list to store the results
results_list = []

# set the ScrapingBee API key
api_key = "UY77ZEP4BPT2SJ6CFY9RK0DGEUH9BJNXWN80N68EC7L90PGCZY47LIJETRQELN6BBMVMHSFDKQIGJCO1"


# create a ScrapingBee client object
client = ScrapingBeeClient(api_key=api_key)

# loop through each page of search results
while page_num < num_pages:

    # create the URL for the current search results page
    url = f"https://youtube.com/@OpeninApp"

    # send a GET request to the ScrapingBee API with the search results page URL
    response = client.get(url)

    # parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # find all the search result links on the page
    search_result_links = soup.find_all("a", href=True)

    # loop through each search result link
    for link in search_result_links:

        # get the URL of the link
        link_url = link["href"]

        # create a dictionary for the current search result
        result_dict = {"url": link_url}

        # append the result dictionary to the results list
        results_list.append(result_dict)

        # increment the result counter
        result_count += 1

        # if we've reached the desired number of results, break out of the loop
        if result_count >= 10000:
            break

    # increment the page number for the next iteration
    page_num += 10

# output the results in JSON format
with open("youtube_links.json", "w") as f:
    json.dump(results_list, f)

# output the results in CSV format
with open("youtube_links", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["url"])
    for result in results_list:
        writer.writerow([result["url"]])

# stop the timer
end_time = time.time()

# calculate the elapsed time
elapsed_time = end_time - start_time

# print the elapsed time
print(f"Elapsed time: {elapsed_time:.2f} seconds")