# Biased Chatbots
Dieses Repository enthält den Quellcode für einen Chatbot, der als praktischer Teil eines Konzepts einer AI Literacy-Unterrichtseinheit entwickelt wurde. Die Applikation wurde im Rahmen meiner Masterarbeit mit dem Titel "Politische Meinungsbildung in Zeiten von AI: Analyse und Entwicklung von Unterrichtseinheiten zur Steigerung von AI Literacy" erstellt.
## Überblick
Das Projekt wurde am Institut für Business Analytics an der Universität Ulm durchgeführt.
Der Chatbot ist darauf ausgelegt, zu demonstrieren, dass Künstliche Inteligenzen über Voreingenommenheiten verfügen können und wie solche die politische Meinungsbildung beeinflussen können. Ziel dieser Entwicklung war es, ein didaktisches Werkzeug zu schaffen, das in Bildungseinrichtungen eingesetzt werden kann, um Schülern und Studenten ein kritisches Verständnis für KI-Systeme zu vermitteln.  Der Chatbot verwendet das GPT4-Modell über die OpenAI API und ist so konfiguriert, dass er Antworten basierend auf vorgegebenen politischen Neigungen (neutral, links oder liberal) generiert.
## Struktur des Repositories
* app2.py: Haupt-Python-Script, das die Flask-Anwendung und die Logik des Chatbots enthält.
* index.html: HTML-Datei für das Frontend des Chatbots, befindet sich im Ordner templates.
* tempates/: Verzeichnis, das die HTML-Datei enthält.
* style.css: Stylesheet für das Frontend, befindet sich im Ordner static.
* static/: Verzeichnis, das die CSS-Datei enthält.
* LICENSE.txt: Lizenztext der MIT Lizenz
## Voraussetzungen
* Python 3.6+
* Flask
* openai
## Installation
1. Klonen Sie dieses Repository auf ihren lokalen Computer.
2. Installieren Sie die benötigten Python-Pakete:
   `pip install flask openai python-dotenv`
3. Erstellen Sie eine .env Datei im Hauptverzeichnis des Projekts und füge deinen OpenAI API-Schlüssel sowie deinen Flask-Schlüssel wie folgt ein:
   `OPENAI_API_KEY='dein_openai_api_schlüssel'`
   `FLASK_SECRET_KEY='dein_flask_schlüssel'`
## Starten des Chatbots
1. Starte den Chatbot über die Kommandozeile:
   `python app2.py`
   Dies startet die Flask-Anwendung.
2. Öffne einen Webbrowser und gebe die folgende Adresse ein, um den Chatbot zu nutzen:
  http://127.0.0.1:5000
## Anpassen des politischen Bias des Chatbots
Nach dem Starten des Chatbots können Sie die politische Ausrichtung anpassen:
1. Öffnen Sie die Datei app2.py im Texteditor
2. Suchen Sie nach dem Aufruf der Chat GPT API:
   ```completion = client.chat.completions.create(
        model="gpt-4",
        temperature = 0,
        max_tokens = 500,
        messages=[
            {"role": "system", "content": role_describtion_standard},
            {"role": "assistant", "content": "Antworten dürfen nicht länger als 5 Sätze sein und müssen sehr präzise sein."},
            {"role": "user", "content": user_input}
   
3. Tauschen Sie `role_describtion_standard` durch `role_describtion_social` oder `role_describtion_liberal` aus.
4. Aktualisieren Sie den Tab ihres Webbrowsers
## Lizenz
Dieses Projekt ist unter der MIT Lizenz lizenziert. Siehe die LICENSE Datei im Repository für den vollständigen Lizenztext.
