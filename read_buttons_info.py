import json

with open("menu_buttons.json") as buttons_json_file:
    buttons_list = json.load(buttons_json_file)

for button in buttons_list:
    print(button)
    button["pushed"] = open(button["pushed"])
    button["unpushed"] = open(button["unpushed"])
    
