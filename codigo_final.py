# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:27:10 2024

@author: VALERIA
"""

## leemos el excel

import pandas as pd
import os

verbos = pd.read_excel('verbos.xlsx')

##########################################################################
##########################################################################

import pandas as pd

########################################################################
############################# AYACUCHO #################################
########################################################################

quechua_suf = pd.read_excel('quechua_ayacucho.xlsx')
quechua_suf = pd.ExcelFile('quechua_ayacucho.xlsx')
D = {}


for hoja in quechua_suf.sheet_names: 
    df = pd.read_excel('quechua_ayacucho.xlsx', sheet_name=hoja)     
    c = df.columns                                          
    df.set_index(c[0], inplace=True)                        
    d = df.to_dict()                                        
    D[hoja] = d

def conj_quechua(base, numero, persona, tiempo):
    return base + D[tiempo][numero][persona]

quechua_pronombres = pd.read_excel('pronombres_ayacucho.xlsx')
quechua_pronombres = pd.ExcelFile('pronombres_ayacucho.xlsx')
DP = {}
dfp = pd.read_excel('pronombres_ayacucho.xlsx')      
c = dfp.columns                             
dfp.set_index(c[0], inplace=True)           
dp = dfp.to_dict()

def conj_final(base,numero,persona,tiempo):
    if numero not in dp:
        st.error(f"Clave '{numero}' no encontrada en el diccionario 'dp'.")
        return
    if persona not in dp[numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'dp[{numero}]'.")
        return
    if tiempo not in D:
        st.error(f"Clave '{tiempo}' no encontrada en el diccionario 'D'.")
        return
    if numero not in D[tiempo]:
        st.error(f"Clave '{numero}' no encontrada en el diccionario anidado dentro de 'D[{tiempo}]'.")
        return
    if persona not in D[tiempo][numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'D[{tiempo}][{numero}]'.")
        return
    audio_file = f"ayacucho/{base}_{numero}_{persona}_{tiempo}.m4a"
    return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona], audio_file

########################################################################
############################### CUZCO ##################################
########################################################################

quechua_suf_cuzco = pd.read_excel('quechua_cuzco.xlsx')
quechua_suf_cuzco = pd.ExcelFile('quechua_cuzco.xlsx')
Z = {}


for hoja in quechua_suf_cuzco.sheet_names: 
    zf = pd.read_excel('quechua_cuzco.xlsx', sheet_name=hoja)     
    c = zf.columns                                          
    zf.set_index(c[0], inplace=True)                        
    z = zf.to_dict()                                        
    Z[hoja] = z

def conj_quechua_cuzco(base, numero, persona, tiempo):
    return base + Z[tiempo][numero][persona]

quechua_cuzco_pronombres = pd.read_excel('pronombres_cuzco.xlsx')
quechua_cuzco_pronombres = pd.ExcelFile('pronombres_cuzco.xlsx')
ZP = {}
zfp = pd.read_excel('pronombres_cuzco.xlsx')      
c = zfp.columns                             
zfp.set_index(c[0], inplace=True)           
zp = zfp.to_dict()

def conj_final_cuzco(base,numero,persona,tiempo):
    if numero not in zp:
        st.error(f"Clave '{numero}' no encontrada en el diccionario 'zp'.")
        return
    if persona not in zp[numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'zp[{numero}]'.")
        return
    if tiempo not in Z:
        st.error(f"Clave '{tiempo}' no encontrada en el diccionario 'Z'.")
        return
    if numero not in Z[tiempo]:
        st.error(f"Clave '{numero}' no encontrada en el diccionario anidado dentro de 'Z[{tiempo}]'.")
        return
    if persona not in Z[tiempo][numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'Z[{tiempo}][{numero}]'.")
        return
    audio_file = f"cuzco/{base}_{numero}_{persona}_{tiempo}.m4a"
    return zp[numero][persona] + ' ' + base + Z[tiempo][numero][persona], audio_file

########################################################################
############################## ANCASH ##################################
########################################################################

quechua_suf_ancash = pd.read_excel('quechua_ancash.xlsx')
quechua_suf_ancash = pd.ExcelFile('quechua_ancash.xlsx')
A = {}


for hoja in quechua_suf_ancash.sheet_names: 
    af = pd.read_excel('quechua_ancash.xlsx', sheet_name=hoja)     
    c = af.columns                                          
    af.set_index(c[0], inplace=True)                        
    a = af.to_dict()                                        
    A[hoja] = a

def conj_quechua_ancash(base, numero, persona, tiempo):
    return base + A[tiempo][numero][persona]

quechua_ancash_pronombres = pd.read_excel('pronombres_ancash.xlsx')
quechua_ancash_pronombres = pd.ExcelFile('pronombres_ancash.xlsx')
AP = {}
afp = pd.read_excel('pronombres_ancash.xlsx')      
c = afp.columns                             
afp.set_index(c[0], inplace=True)           
ap = afp.to_dict()

def conj_final_ancash(base, numero, persona, tiempo):
    if numero not in ap:
        st.error(f"Clave '{numero}' no encontrada en el diccionario 'ap'.")
        return
    if persona not in ap[numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'ap[{numero}]'.")
        return
    if tiempo not in A:
        st.error(f"Clave '{tiempo}' no encontrada en el diccionario 'A'.")
        return
    if numero not in A[tiempo]:
        st.error(f"Clave '{numero}' no encontrada en el diccionario anidado dentro de 'A[{tiempo}]'.")
        return
    if persona not in A[tiempo][numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'A[{tiempo}][{numero}]'.")
        return
    
    conjugacion = ap[numero][persona] + ' ' + base + A[tiempo][numero][persona]
   
    # Ejemplo de asignación de archivo de audio según la conjugación
    audio_file = f"ancash/{base}_{numero}_{persona}_{tiempo}.m4a"
    
    if A[tiempo][numero][persona].endswith('x'):
        st.warning(f"No existe conjugación para el tiempo '{tiempo}' en la variedad del quechua de Ancash.")
        return None, None
    
    return conjugacion, audio_file

##########################################################################
##########################################################################

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## importamos streamlit

import streamlit as st

################################### TEMA ######################################

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #FFFBFB;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

##################################### TÍTULO ##################################

st.image('machu_picchu_header.jpg')

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
    .title-font {
        font-family: 'Calibri';
        color: purple;
        text-align: center;
        font-size: 50px;
    }
    </style>
    <h1 class="title-font">Conjugador de verbos en quechua</h1>
    """,
    unsafe_allow_html=True,
)

############################## INTRODUCCIÓN ###################################

st.write("""
<br>
<div style="text-align: justify">
Esta página web tiene el objetivo de crear conjugaciones de los verbos quechuas más comunes. Al seleccionar una variedad de la lengua, un verbo, un número, una persona y un tiempo, se podrá obtener la forma conjugada de dicho verbo con los sufijos correspondientes. Se ofrecen también explicaciones para algunos conceptos de persona y tiempo verbal que pueden resultar confusos y algunos audios con las pronunciaciones de las formas conjugadas. ¡Anímate a conocer más sobre el quechua! 😄
</div>
<br>
""", unsafe_allow_html=True)

################################# VARIEDAD ####################################

# Inicializar session_state
if 'variedad' not in st.session_state:
    st.session_state['variedad'] = None

# Selección de la variedad del quechua
st.header('Variedad del quechua', divider='violet')

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Ayacucho"):
        st.session_state['variedad'] = "Ayacucho"
with col2:
    if st.button("Cuzco"):
        st.session_state['variedad'] = "Cuzco"
with col3:
    if st.button("Áncash"):
        st.session_state['variedad'] = "Áncash"

if not st.session_state['variedad']:
    st.warning("Por favor, seleccione una variedad del quechua.")
else:
    st.write(f"Seleccionaste: {st.session_state['variedad']}")
    
########### menú desplegable para seleccionar VERBOS #################

    # Ruta donde se encuentran los archivos de audio
    ruta_audio = "verbos/"

    st.header('Verbo', divider='violet')
    
    base = st.selectbox(
        "Seleccione un verbo en quechua: ",
        quechua)
    
    st.write("Seleccionaste: ", dict_que_esp[base])
    
    # Nombre del archivo de audio
    nombre_audio = base + ".m4a"
    ruta_completa_audio = os.path.join(ruta_audio, nombre_audio)
    
    if os.path.exists(ruta_completa_audio):
        st.audio(ruta_completa_audio)
    else:
        st.warning(f"No se encontró archivo de audio para el verbo '{base}'.")
    
    if base.endswith('y'):
        base = base[:-1]
        
################################## NUMERO #####################################

    st.header('Número', divider='violet')
    
    numero = st.radio(
        "Seleccione un número: ",
        ["singular","plural"],
        index=0,
    )

#st.write("Seleccionaste: ", numero)

# Diccionario de explicaciones
    explicaciones_persona = {
        "primera inclusiva": "La primera persona inclusiva se refiere a 'nosotros', incluyendo a la persona con la que se habla.",
        "primera exclusiva": "La primera persona exclusiva se refiere a 'nosotros', excluyendo a la persona con la que se habla.",
        "segunda": "La segunda persona se refiere a 'tú' o 'usted'.",
        "tercera": "La tercera persona se refiere a 'él', 'ella' o 'ellos'."
    }
    
    explicaciones_tiempo = {
        "presente simple": "Este tiempo se usa para describir acciones que ocurren regularmente a lo largo del tiempo.",
        "presente progresivo": "Este tiempo se usa para describir acciones que están ocurriendo en este momento.",
        "presente habitual": "Este tiempo se usa para describir acciones que se repiten en el tiempo de manera finita, como hábitos o rutinas.",
        "pasado 1 simple": "Este tiempo se usa para describir acciones que ocurrieron en el pasado y que fueron vistas u oídas por el hablante.",
        "pasado 1 progresivo": "Este tiempo se usa para describir acciones que estuvieron ocurriendo en el pasado y que fueron vistas u oídas por el hablante.",
        "pasado 1 habitual": "Este tiempo se usa para describir acciones que ocurrían regularmente en el pasado y que fueron vistas u oídas por el hablante.",
        "pasado 2 simple": "Este tiempose usa para describir acciones que ocurrieron en el pasado sin la participación o el conocimiento directo del hablante.",
        "pasado 2 progresivo": "Este tiempo se usa para describir acciones que estuvieron ocurriendo en el pasado sin la participación o el conocimiento directo del hablante.",
        "pasado 2 habitual": "Este tiempo se usa para describir acciones que ocurrían regularmente en el pasado sin la participación o el conocimiento directo del hablante."
    }

##################################### PERSONA #################################

    st.header('Persona', divider='violet')
    
    persona = st.selectbox("Seleccione una persona: ", list(explicaciones_persona.keys()), index=0)
    explicacion_persona_placeholder = st.empty()
    explicaciones_persona["primera inclusiva"] += "<br><br>Ejemplo: '(Todos) nosotros vamos al mercado.'"
    explicaciones_persona["primera exclusiva"] += "<br><br>Ejemplo: 'Nosotros (pero no tú) vamos al mercado.'"
    
    explicacion_persona_placeholder.markdown("**Explicación de persona seleccionada:** " + explicaciones_persona[persona], unsafe_allow_html=True)


###################################### TIEMPO #################################

    st.header('Tiempo', divider='violet')
    
    tiempo = st.selectbox("Seleccione un tiempo: ", list(explicaciones_tiempo.keys()), index=0)
    explicacion_tiempo_placeholder = st.empty()
    explicaciones_tiempo["presente simple"] += "<br><br>Ejemplo: 'Yo veo televisión.'"
    explicaciones_tiempo["presente progresivo"] += "<br><br>Ejemplo: 'Yo estoy viendo televisión.'"
    explicaciones_tiempo["presente habitual"] += "<br><br>Ejemplo: 'Yo suelo ver televisión.'"
    explicaciones_tiempo["pasado 1 simple"] += "<br><br>Ejemplo: 'Yo veía televisión.'"
    explicaciones_tiempo["pasado 1 progresivo"] += "<br><br>Ejemplo: 'Yo estaba viendo televisión.'"
    explicaciones_tiempo["pasado 1 habitual"] += "<br><br>Ejemplo: 'Yo solía ver televisión.'"
    explicaciones_tiempo["pasado 2 simple"] += "<br><br>Ejemplo: '(Dicen que) yo veía televisión.'"
    explicaciones_tiempo["pasado 2 progresivo"] += "<br><br>Ejemplo: '(Dicen que) yo estaba viendo televisión.'"
    explicaciones_tiempo["pasado 2 habitual"] += "<br><br>Ejemplo: '(Dicen que) yo solía ver televisión.'"
    
    explicacion_tiempo_placeholder.markdown("**Explicación de tiempo seleccionado:** " + explicaciones_tiempo[tiempo], unsafe_allow_html=True)
        
############################# RESULTADO #######################################

    st.header('Resultado', divider='violet')

    conjugacion = None
    audio_file = None
    error_en_conjugacion = False
    
    if st.session_state['variedad'] == "Ayacucho":
        conjugacion, audio_file = conj_final(base, numero, persona, tiempo)
    elif st.session_state['variedad'] == "Cuzco":
        conjugacion, audio_file = conj_final_cuzco(base, numero, persona, tiempo)
    elif st.session_state['variedad'] == "Ancash":
        conjugacion, audio_file = conj_final_ancash(base, numero, persona, tiempo)
        if conjugacion is None:
            error_en_conjugacion = True
    
    if conjugacion is not None:
        st.write("La conjugación es: ")
        st.markdown(f'<p style="font-size:24px; text-align:center;">{conjugacion}</p>', unsafe_allow_html=True)
        
        if audio_file and os.path.exists(audio_file):
            st.audio(audio_file)
            
    elif error_en_conjugacion:
        with st.popover("Más información"):
            st.write("""
            La variedad del quechua de Áncash es distinta a la variedad ayacuchana o cuzqueña, pues los hablantes no utilizan este tiempo en su habla. Pueden usar otras estrategias para transmitir el mismo mensaje, pero, por el momento, no se cuenta con información académica acerca de los sufijos usados para conjugar verbos en este tiempo.
            """)
    else:
        st.error("Hubo un error en la conjugación. Por favor, revise los parámetros seleccionados.")
        
        conjugacion = None
        
############################## RECURSOS #######################################

    st.header('Recursos', divider='violet')
    
    st.write("""
    <div style="text-align: justify">
    Si deseas conocer con mayor profundidad las variedades del quechua aquí presentadas, haz click en los siguientes para ver las gramáticas usadas en la creación de esta página web: 
    </div>
    <br>
    """, unsafe_allow_html=True)

    st.page_link("https://repositorio.pucp.edu.pe/index/bitstream/handle/123456789/134454/Qayna%2c%20kunan%2c%20paqarin.%20Una%20introducci%c3%b3n%20pr%c3%a1ctica%20al%20quechua%20chanca.pdf?sequence=1&isAllowed=y", label=" Quechua de Ayacucho", icon="1️⃣")
    st.page_link("https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/South%20American/Quechuan%20%26%20Aymaran/Quechua%2C%20Gramatica%20-%20Cuzco-Collao%20%28Cusihuam%C3%A1n%29.pdf", label=" Quechua de Cuzco 1", icon="2️⃣")
    st.page_link("https://repositorio.perueduca.pe/recursos/2022/DEIB22-0568.pdf", label=" Quechua de Cuzco 2", icon="3️⃣")
    st.page_link("https://dokumen.pub/gramatica-quechua-ancash-huailas.html", label=" Quechua de Áncash", icon="4️⃣")

#   st.link_button("Quechua de Ayacucho", "https://repositorio.pucp.edu.pe/index/bitstream/handle/123456789/134454/Qayna%2c%20kunan%2c%20paqarin.%20Una%20introducci%c3%b3n%20pr%c3%a1ctica%20al%20quechua%20chanca.pdf?sequence=1&isAllowed=y")
#   st.link_button("Quechua de Cuzco 1", "https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/South%20American/Quechuan%20%26%20Aymaran/Quechua%2C%20Gramatica%20-%20Cuzco-Collao%20%28Cusihuam%C3%A1n%29.pdf")
#   st.link_button("Quechua de Cuzco 2", "https://repositorio.perueduca.pe/recursos/2022/DEIB22-0568.pdf")
#   st.link_button("Quechua de Áncash", "https://dokumen.pub/gramatica-quechua-ancash-huailas.html") 