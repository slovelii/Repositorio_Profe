import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Receta para cocinar gnocchis gratinados con chorizo")
image = Image.open('gato_raton.png')
st.image(image, width=350)
with st.sidebar:
    st.header("Aquí estará la receta completa")
    st.subheader("Selecciona los pasos para escucharlos.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Primer paso")
  st.write("Precalienta el horno a 220ºC con la opción de gratinado. En una sartén, calienta un chorrito de aceite y la mantequilla a fuego medio. Luego, agrega los gnocchis y cocina 4-5 min, removiendo frecuentemente, hasta que estén dorados. Cuando estén listos, resérvalos en un plato.")
  resp = st.checkbox("¿Lo lograste?")
  if resp:
    st.write("¡Continuemos!")

with col2:
  st.subheader("Segundo paso")
  st.write("Calienta la sartén a fuego medio y cocina el chorizo 3-4 min, removiendo ocasionalmente, hasta que se dore. Luego, reserva fuera de la sartén. Mientras tanto, pela la cebolla, divídela en dos y córtala en daditos pequeños. Pela y pica finamente el ajo.")


col3, col4 = st.columns(2)

with col3:
  st.subheader("Tercer paso")
  st.write("En la sartén, agrega un chorrito de aceite junto con el ajo. Calienta a fuego medio y cocina 1-2 min o hasta que se dore. Luego, añade la cebolla y rehoga 4-5 min, hasta que la cebolla empiece a estar transparente. Añade el tomate concentrado y el chorizo cocinado, mezcla bien y cocina 1-2 min más.")

with col4:
  st.subheader("Cuarto paso")
  st.write("En la sartén, agrega la leche y el azúcar (ver cantidad en ingredientes) y lleva a ebullición durante 2-3 min, removiendo ocasionalmente, hasta que la salsa se reduzca y espese. Agrega los gnocchis a la sartén, salpimienta al gusto y mezcla para integrar los ingredientes.")

col5, col6 = st.columns(2)

with col5:
  st.subheader("Quinto paso")
  st.write("Coloca los gnocchis con chorizo en una fuente para horno y agrega encima el queso rallado. Hornea en el estante superior 6-8 min o hasta que el queso se funda y dore.")

with col6:
  st.subheader("Sexto paso")
  st.write("Coloca la fuente en la mesa y sirve gnocchis con chorizo y queso gratinado en platos.")
       
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
