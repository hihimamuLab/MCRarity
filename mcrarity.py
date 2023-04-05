#impot modules
import PySimpleGUI as sg

#variable group
zombie_rarity, skeleton_rarity, spider_rarity = 1, 1, 1

#main layout
main_layout =[
    [sg.Text('Please select a difficulty level')],
    [sg.Button('Easy', key = ("-easy-"))],
    [sg.Button('Normal', key = ("-normal-"))],
    [sg.Button('Hard', key = ("-hard-"))],
]

#mob layout
mob_layout = [
    [sg.Text('What mob is that?')],
    [sg.Button('Zombie', key = ("-zombie-"))],
    [sg.Button('Skeleton', key = ("-skeleton-"))],
    [sg.Button('Spider', key = ("-spider-"))],
    ]

#zombie layouts
zombie_villagers_layout = [
    [sg.Text('It\'s zombie villagers?')],
    [sg.Button('Yes', key = ("-zombie_villagers_yes"))],
    [sg.Button('No', key = ("-zombie_villagers_no"))],
    ]

baby_zombies_layout = [
    [sg.Text('It\'s a baby?')],
    [sg.Button('Yes', key = ("-baby_zombies_yes-"))],
    [sg.Button('No', key = ("-baby_zombies_no-"))],
]

chicken_jockeys_layout = [
    [sg.Text('It\'s a chicken jockey?')],
    [sg.Button('Yes', key = ("-chicken_jockeys_yes-"))],
    [sg.Button('No', key = ("-chicken_jockeys_no-"))],
]

armor_zombies_layout = [
    [sg.Text('Are you wearing armor?')],
    [sg.Button('Armor enchantment wearing', key = ("-armor_enchantment-"))],
    [sg.Button('Armor wearng', key = ("-armor-"))],
    [sg.Button('Don\'t wearing armor', key = ("-no_armor-"))],
]

weapon_zombies_layout = [
    [sg.Text('Are you wearing weapon?')],
    [sg.Button('Weapon enchantment wearing', key = ("-weapon_enchantment-"))],
    [sg.Button('Weapon wearng', key = ("-weapon-"))],
    [sg.Button('Don\'t wearing weapon', key = ("-no_weapon-"))],
]

armor_material_zombies_layout = [
    [sg.Text('What armor are you wearing?')],
    [sg.Button('Leather armor', key = ('-leather-'))],
    [sg.Button('Gold armor', key = ('-gold-'))],
    [sg.Button('Chain armor', key = ('-chain-'))],
    [sg.Button('Iron armor', key = ('-iron-'))],
    [sg.Button('Diamond armor', key = ('-diamond-'))],
]

# create the window
window = sg.Window('My Window', main_layout)

