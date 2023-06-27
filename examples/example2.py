from String_Color import COLOR

potato = {
    "Name": "Potato",
    "RARITY": "LEGENDERY"
}

def cool_item_text(item: dict):
    return f"{COLOR.ID(208)}{COLOR.BOLD}" + str(item["Name"]) + f"\n\n{COLOR.RGB(237, 145, 33)}" + str(item["RARITY"]) + f"{COLOR.RESET}"
print(cool_item_text(potato))