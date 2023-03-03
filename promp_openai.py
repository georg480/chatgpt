import asyncio
import os
import shutil
from datetime import datetime

import openai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


async def chat(prompt):
    completions = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=2048, api_key=API_KEY
    )
    message = completions.choices[0].text
    return message


async def main():
    context = ""

    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    script_name = "promp_openai.py"

    backup_name = f"{script_name[:-3]}_{date_time}.py"
    shutil.copy(script_name, backup_name)

    try:
        with open(script_name, "r", encoding="utf-8") as file:
            file_data = file.readlines()
    except Exception as e:
        print(f"Fehler beim Öffnen von {script_name}: {e}")
        return

    print(f"Die aktuelle Datei heißt: {script_name}")

    while True:
        funktion = "Beschreibe den Code"  # input("Was soll ergänzt werden?")
        if funktion != "":
            break
        print("Bitte eingeben.")

    print(f"Funktion ausgewählt: {funktion}")

    prompt = f"==== Änderungsbeschreibung ====\\\\\\n\\\\\\n{funktion}\\\\\\n\\\\\\n==== Python-Code ====\\\\\\n\\\\\\nHier folgt der Python-Code mit der durchgeführten Änderung:\\\\\\n\\\\\\n#Hier ist der Original-Code\\\\\\n{file_data}"

    loop = asyncio.get_event_loop()
    task = loop.create_task(chat(prompt))

    result = await task
    print(f"Der geänderte Inhalt ist: {result}")

    try:
        with open("Antwort.txt", "a", encoding="utf-8") as file:
            result_string = "".join(result)
            print(
                f"Antwort von:\\\\\\\\\\n{result_string} um {date_time}\\\\\\\\\\n\\\\\\\\\\n"
            )
            # Hier wird der Code ergänzt.
            file.write(
                f"Antwort von:\\\\\\\\\\n{result_string} um {date_time}\\\\\\\\\\nFunktion: {funktion}\\\\\\\\\\n\\\\\\\\\\n"
            )
            file.write(
                f"Änderungsbeschreibung:\\\\\\\\\\n{funktion}\\\\\\\\\\n\\\\\\\\\\nGeorg, {date_time}\\\\\\\\\\n\\\\\\\\\\n"
            )
    except Exception as e:
        print(f"Fehler beim Schreiben in Antwort.txt: {e}")
        return

    try:
        script_name_neu = script_name + ".py"
        with open(script_name_neu, "w", encoding="utf-8") as file:
            lines = result[result.index("imp") : -4]
            for line in lines.split("\\\\n', '"):
                print(line)
                file.write(line + "\\n")
            print(f"Name des neuen Skripts: {script_name_neu}")
    except Exception as e:
        print(f"")  # Fehler beim Schreiben in {script_name}.py: {e}")
        return
    print(f"Die {script_name}")
    print(f"Die {script_name_neu}")
    print(f"geänderte Funktion: {funktion}")

    # Hier wird der Code ergänzt.
    if script_name_neu.endswith(".py"):
        try:
            with open(script_name_neu, "r", encoding="utf-8") as file:
                file_data = file.readlines()
        except Exception as e:
            print(f"Fehler beim Öffnen von {script_name_neu}: {e}")
            return

        user_input = input("Wollen sie dieses Skript direkt ausführen? (y/n)")
        if user_input == "y":
            loop2 = asyncio.get_event_loop()
            task2 = loop.create_task(main())
            result = await task2
        else:
            pass
    else:
        print("nichts")

    while True:
        user_input = input("Frage /Eingabe ein. X")

        if user_input.lower() == "x":
            break
        elif user_input.lower() == "e":
            prompt = context + user_input

            loop = asyncio.get_event_loop()
            task = loop.create_task(chat(prompt))

            result = await task
            print(result)
            try:
                with open("Antwort.txt", "a", encoding="utf-8") as file:
                    result_string = "".join(result)
                    result_string = f"Frage/Funktion: {funktion}\nAntwort um {date_time}Antwort:\n{result_string}"
                    print(result_string)
                    file.write(result_string)
            except Exception as e:
                print(f"Fehler beim Schreiben in Antwort.txt: {e}")
                return


if __name__ == "__main__":
    asyncio.run(main())
