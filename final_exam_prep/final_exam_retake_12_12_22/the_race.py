import re

pattern = r"(#|\$|%|\*|\&)([A-za-z]+)\1=(\d+)!!(.+)"

string = input()

while string:
    matches = re.match(pattern, string)
    if matches:
        if int(matches.group(3)) == len(matches.group(4)):
            geohashcode = ""
            for char in matches.group(4):
                geohashcode += chr(ord(char) + int(matches.group(3)))
            print(f"Coordinates found! {matches.group(2)} -> {geohashcode}")
            break
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")

    string = input()