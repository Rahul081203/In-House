from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import cv2
import text_and_speech as translator
import numpy as np
from sign_language import classify_sign
import os

app = Flask(__name__, static_folder='static')                                                

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('home.html')

def generate_frames():
    cap = cv2.VideoCapture(1)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Process the frame and get the translated label
            translated_label = classify_sign(frame)

            # # Convert the translated_label array to a string
            # translated_label = translated_label.astype(str)

            # # Draw the translated label on the frame
            # cv2.putText(frame, 'Translated: {}'.format(translated_label), (10, 30),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', translated_label)
            frame = buffer.tobytes()

            # Yield the frame in the response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sign_classifier', methods=['GET','POST'])
def sign_language_classifier():
    return render_template('sign_input.html')

@app.route('/text_to_text',methods = ['GET','POST'])
def text_input():
    return render_template('text_to_text.html')

@app.route('/speech_input', methods=['GET', 'POST'])
def speech_input():
    return render_template('speech_input.html')
@app.route('/speech_input_source', methods=['GET', 'POST'])
def speech_input_source_html():
    return render_template('speech_input_source.html')


@app.route('/speech_to_text_translated', methods=['GET', 'POST'])
def speech_to_text_html():
    text = translator.speech_to_text()
    if text=="Speech not understood":
        return render_template('speech_not_understood.html')
    destination = request.form['language-select']
    translation = translator.text_to_text(text,destination)
    array = [text,translation]
    translator.text_to_speech(translation,destination)
    return render_template('translated.html', data = array)

@app.route('/speech_translation_source', methods=['GET', 'POST'])
def speech_source_html():
    text = translator.speech_to_text()
    if text=="Speech not understood":
        return render_template('speech_not_understood.html')
    destination = request.form['language-select']
    source = request.form['source-select']
    translation = translator.text_to_text_source(text,source,destination)
    array = [text,translation]
    translator.text_to_speech(translation,destination)
    return render_template('translated.html', data = array)


@app.route('/text_to_text_translated',methods = ['GET','POST'])
def text_to_text_html():
    input_string = request.form['input_string']
    destination = request.form['language-select']
    translation = translator.text_to_text(input_string,destination)
    # array = [input_string,translation]
    translator.text_to_speech(translation,destination)
    # return render_template('translated.html', data = array)
    return jsonify({'translated_text': translation, 'audio_filename': 'translated.mp3'})

@app.route('/text_translation_source', methods=['GET','POST'])
def text_translated_source():
    return render_template('text_source.html')

@app.route('/text_form_source',methods = ['GET','POST'])
def text_source_html():
    input_string = request.form['input_string']
    source = request.form['source-select']
    destination = request.form['language-select']
    translation = translator.text_to_text_source(input_string,source,destination)
    # array = [input_string,translation]
    translator.text_to_speech(translation,destination)
    # return render_template('translated.html', data = array)
    return jsonify({'translated_text': translation, 'audio_filename': 'translated.mp3'})

if __name__ == "__main__":
    app.run()