import PySimpleGUI as sg
import dortislem as islem

def clear_input():
    for key in values:
        window[key]('')
    return None

sg.theme('DarkBlue2')

layout = [
    [ 
        sg.Text("1. Sayı : "),
        sg.InputText(key="-s1-")
    ],

    [
        sg.Text("2. Sayı : "),
        sg.InputText(key="-s2-")
    ],
    [
        sg.Button("Topla", key="-add-"),
        sg.Button("Çıkar", key="-sub-"),
        sg.Button("Çarp", key="-mul-"),
        sg.Button("Böl", key="-div-"),
        sg.Text("Sonuç : "),
        sg.Text(key="-sonuc-")
    ]
]

window = sg.Window('Dört İşlem', layout)

while True:
    event,values = window.read()

    if event in(None, "Exit"):
        break

    if event=="-add-" and values["-s1-"]!="" and values["-s2-"]!="" :
        a = int(values["-s1-"])
        b = int(values["-s2-"])
        sonuc = float(islem.topla(a,b))
        window["-sonuc-"].update(round(sonuc,2))
        clear_input()
        window['-s1-'].set_focus()

    if event=="-sub-" and values["-s1-"]!="" and values["-s2-"]!="":
        a = int(values["-s1-"])
        b = int(values["-s2-"])
        sonuc = float(islem.cikar(a,b))
        window["-sonuc-"].update(round(sonuc,2))
        clear_input()
        window['-s1-'].set_focus()

    if event=="-mul-" and values["-s1-"]!="" and values["-s2-"]!="":
        a = int(values["-s1-"])
        b = int(values["-s2-"])
        sonuc = float(islem.carp(a,b))
        window["-sonuc-"].update(round(sonuc,2))
        clear_input()
        window['-s1-'].set_focus()
    
    if event=="-div-" and values["-s1-"]!="" and values["-s2-"]!="":
        a = int(values["-s1-"])
        b = int(values["-s2-"])
        sonuc = float(islem.bol(a,b))
        window["-sonuc-"].update(round(sonuc,2))
        clear_input()
        window['-s1-'].set_focus()

    
        
window.close()


