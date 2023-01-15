import re

valid_links = list()

search_pattern = r"(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"

sentence = input()

while sentence:

    matches = re.search(search_pattern, sentence)
    if matches:
        valid_links.append(matches.group(0))
    sentence = input()

for valid_link in valid_links:
    print(valid_link)
