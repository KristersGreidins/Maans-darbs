import PySimpleGUI as sg

def main():
    sg.theme('Default1')

    viktorina = [["File", ["Close"]], ["Help", ["About"]]]

    # Izveidojam visus jautājumus ar to attiecīgo logu
    jautajumi = [
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("1) Kurā gadā Latvija ieguva bronzas medaļas hokejā?")], 
            [sg.Radio("2017", "jautajums1", default=False, key="-aa-")],
            [sg.Radio("2014", "jautajums1", default=False, key="-aaa-")],
            [sg.Radio("2023", "jautajums1", default=False, key="-aaaa-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu")],
            [sg.Text("2) Kurš Latvijas hokeja izlases spēlētājs spēlē ar 16. numuru?")], 
            [sg.Radio("Kaspars Daugaviņš", "jautajums1", default=False, key="-bb-")],
            [sg.Radio("Kristaps Zīle", "jautajums1", default=False, key="-bbb-")],
            [sg.Radio("Artūrs Šilovs", "jautajums1", default=False, key="-bbbb-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("3) Kas ir Latvijas hokeja izlases galvenais treners?")], 
            [sg.Radio("Lauris Dārziņš", "jautajums1", default=False, key="-cc-")],
            [sg.Radio("Artūrs Irbe", "jautajums1", default=False, key="-ccc-")],
            [sg.Radio("Harijs Vītoiņš", "jautajums1", default=False, key="-cccc-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("4) Kur šogad norisināsies pasaules čempionāts hokejā?")], 
            [sg.Radio("Čehijā", "jautajums1", default=False, key="-dd-")],
            [sg.Radio("Zviedrijā", "jautajums1", default=False, key="-ddd-")],
            [sg.Radio("Šveicē", "jautajums1", default=False, key="-ddd-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("5) Kurš ir visrezultatīvākais Latvijas hokeja izlases spēlētājs?")], 
            [sg.Radio("Aleksandrs Ņiživijs", "jautajums1", default=False, key="-ee-")],
            [sg.Radio("Aleksandrs Kerčs", "jautajums1", default=False, key="-ee-")],
            [sg.Radio("Leonīds Tambijevs", "jautajums1", default=False, key="-ee-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("6) Kuri no šiem spēlētājiem ir brāļi Bukarti, kas spēlēs 2024.gada pasaules čempionātā hokejā? ")], 
            [sg.Checkbox("Valdis",  default=False, key="-ff-")],
            [sg.Checkbox("Lauris",  default=False, key="-fff-")],
            [sg.Checkbox("Rihards",  default=False, key="-ffff-")],
            [sg.Checkbox("Roberts",  default=False, key="-fffff-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("7) Kurš ir komandas kapteinis?")], 
            [sg.Radio("Martins Laviņš", "jautajums1", default=False, key="-ee-")],
            [sg.Radio("Oskars Batņa", "jautajums1", default=False, key="-ee-")],
            [sg.Radio("Kaspars Daugaviņš", "jautajums1", default=False, key="-ee-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Atbildi uz jautājumu!")],
            [sg.Text("8) Cik spēlētāju spēle uz laukuma abās komandās>")], 
            [sg.Radio("8", "jautajums1", default=False, key="-ee-")],
            [sg.Radio("10", "jautajums1", default=False, key="-ee-")],
            [sg.Radio("12", "jautajums1", default=False, key="-ee-")],
            [sg.Button("Nākamais jautājums", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ],
        [
            [sg.Menu(viktorina)],
            [sg.Text("Paldies par tavu dalību!")], 
            [sg.Button("Apskatīt rezultātu.", size=(15, 1))],
            [sg.Button('Aizvērt')]
        ]
    ]

    current_question_index = 0
    current_question = jautajumi[current_question_index]
    layout = current_question

    window = sg.Window('Interaktīvā viktorīnas spēle', layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Aizvērt'):
            break
        elif event == 'Nākamais jautājums':
            current_question_index += 1
            if current_question_index < len(jautajumi):
                current_question = jautajumi[current_question_index]
                layout = current_question
                window.close()
                window = sg.Window('Interaktīvā viktorīnas spēle', layout)
            else:
                sg.popup("Visi jautājumi ir atbildēti!") 
                break

    window.close()

main()