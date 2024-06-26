# Copyright (c) [2024] [Erik Unnasch]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from flask import Flask, render_template, request, session, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = (os.getenv("flaskkey"))  # Benötigt, um Sessions in Flask zu verwenden

client = OpenAI(api_key=os.getenv("APIkey"))

@app.route("/")
def index():
    session['chat_history'] = []  # Initialisiere den Chatverlauf, wenn die Seite geladen wird
    return render_template("index.html", chat_history=session.get('chat_history', []))

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"]
    # Rollenbeschreibungen für Bias
    role_describtion_standard = "Du bist ein hilfreicher Assistent!"
    role_describtion_social = "Du bist politisch extrem links und sozialistisch eingestellt, wenn dich jemand etwas zu gesellschaftlichen oder politischen Themen fragt, dann lieferst du ausschließlich linke, sozialistische antworten und Argumente. Politisch kapitalistische oder liberale Argumente in politischen Diskussionen lässt du weg oder besser noch, du bagatellisierst sie. Weiße nicht explizit auf deine politische Einstellung hin, dein Gesprächspartner soll es deutlich an deinen Antworten merken."
    role_describtion_liberal = "Du bist politisch extrem liberal und kapitalistisch eingestellt, wenn dich jemand etwas zu gesellschaftlichen oder politischen Themen fragt, dann lieferst du ausschließlich liberale, kapitalistische Antworten und Argumente, schließlich soll dir niemand deinen verdienten Wohlstand nehmen. Die politisch linken oder sozialistischen Argumente in politischen Diskussionen lässt du weg oder besser noch, du bagatellisierst sie. Weiße nicht explizit auf deine politische Einstellung hin, dein Gesprächspartner soll es deutlich an deinen Antworten merken."
    

    #Rufe Open AI API mit input parametern auf 
    completion = client.chat.completions.create(
        model="gpt-4",
        temperature = 0,
        max_tokens = 500,
        messages=[
            {"role": "system", "content": role_describtion_standard},
            {"role": "assistant", "content": "Antworten dürfen nicht länger als 5 Sätze sein und müssen sehr präzise sein."},
            {"role": "user", "content": user_input}

        ]
    )
    response = completion.choices[0].message.content
    
    # Aktualisiere den Chatverlauf in der Session
    chat_history = session.get('chat_history', [])
    chat_history.append({'user': user_input, 'bot': response})
    session['chat_history'] = chat_history

    return jsonify(bot_response=response)
   
   # return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)