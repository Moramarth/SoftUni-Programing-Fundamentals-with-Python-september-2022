collectables = {"shards": 0, "fragments": 0, "motes": 0}
junk = dict()
legendary_craft = False
while True:
    loot = input().lower().split()
    for i in range(0, len(loot), 2):
        if loot[i + 1] not in collectables:
            if loot[i + 1] not in junk:
                junk[loot[i + 1]] = int(loot[i])
            else:
                junk[loot[i+1]] += int(loot[i])
        else:
            collectables[loot[i+1]] += int(loot[i])

        if collectables["motes"] >= 250 or collectables["fragments"] >= 250 or collectables["shards"] >= 250:
            legendary_craft = True
            break
    if legendary_craft:
        break

if collectables["motes"] >= 250:
    print("Dragonwrath obtained!")
    collectables["motes"] -= 250

elif collectables["fragments"] >= 250:
    print("Valanyr obtained!")
    collectables["fragments"] -= 250

elif collectables["shards"] >= 250:
    print("Shadowmourne obtained!")
    collectables["shards"] -= 250

for key in collectables:
    print(f"{key}: {collectables[key]}")

for key in junk:
    print(f"{key}: {junk[key]}")
