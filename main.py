import decklist_import
import pokemonio_conversion
import api_call
import image_download
import os

input_filename = 'input.txt'  # Input text file
output_filename = 'cleaned.txt'  # The output file to save the cleaned content
decklist_import.clean_file(input_filename, output_filename)

## Set the working directory and setup the cards folder
working_dir = os.getcwd()
cards_dir = working_dir + "/cards/"

if not os.path.exists(cards_dir):
    os.makedirs(cards_dir)

card_list = pokemonio_conversion.process_file("cleaned.txt")
image_urls = list()
for card in card_list:
    set = card["set"]
    number = card["col#"]
    image_urls.append(api_call.get_image_url(set, number))


## Iterating through the list of links and downloading each of them to the cards directory that was created earlier
i = 0
for link in image_urls:
    card_name = card_list[i]["name"]
    card_amount = card_list[i]["amount"]
    image_download.download_image(link, cards_dir, f"{str(i)}_{card_name}_{card_amount}")
    i = i + 1

import deck_generator
import cleanup
