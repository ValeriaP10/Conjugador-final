# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:27:10 2024

@author: VALERIA
"""

## leemos el excel

import pandas as pd
import numpy as np

verbos = pd.read_excel('verbos.xlsx')

##########################################################################
##########################################################################

import pandas as pd

########################################################################
############################# AYACUCHO #################################
########################################################################

quechua_suf = pd.read_excel('quechua.xlsx')
quechua_suf = pd.ExcelFile('quechua.xlsx')
D = {}


for hoja in quechua_suf.sheet_names: 
    df = pd.read_excel('quechua.xlsx', sheet_name=hoja)     
    c = df.columns                                          
    df.set_index(c[0], inplace=True)                        
    d = df.to_dict()                                        
    D[hoja] = d

def conj_quechua(base, numero, persona, tiempo):
    return base + D[tiempo][numero][persona]

quechua_pronombres = pd.read_excel('pronombres.xlsx')
quechua_pronombres = pd.ExcelFile('pronombres.xlsx')
DP = {}
dfp = pd.read_excel('pronombres.xlsx')      
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
    return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]

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
    return zp[numero][persona] + ' ' + base + Z[tiempo][numero][persona]

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
    return ap[numero][persona] + ' ' + base + A[tiempo][numero][persona]

##########################################################################
##########################################################################

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## importamos streamlit

import streamlit as st

################## TEMA #####################

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

########### TÍTULO #############

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

########### INTRODUCCIÓN #############

st.markdown(
    """
    <style>
    .custom-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 5px; /* Añadir espacio debajo del contenedor */
        text-align: justify; 
    }
    .outside-text {
        margin-top: 20px; /* Añadir espacio arriba del texto */
        margin-left: 10px; /* Añadir espacio a la izquierda del texto */
        margin-right: 10px; /* Añadir espacio a la derecha del texto */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-container">
        Esta página web tiene el objetivo de crear conjugaciones de los verbos quechuas más comunes. Al seleccionar un verbo, un número, una persona y un tiempo, se podrá obtener la forma conjugada de dicho verbo con los sufijos correspondientes. Se ofrecen también explicaciones para algunos conceptos de persona y tiempo verbal que pueden resultar confusos. ¡Anímate a conocer más sobre el quechua! 😄
    </div>
    """,
    unsafe_allow_html=True
)

################# boton para seleccionar la VARIEDAD #################

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
    if st.button("Ancash"):
        st.session_state['variedad'] = "Ancash"

if not st.session_state['variedad']:
    st.warning("Por favor, seleccione una variedad del quechua.")
else:
    
########### menú desplegable para seleccionar VERBOS #################

    st.header('Verbo', divider='violet')
    
    base = st.selectbox(
        "Seleccione un verbo en quechua: ",
        quechua)
    
    st.write("Seleccionaste: ", dict_que_esp[base])
    
    if base.endswith('y'):
        base = base[:-1]

############## menú desplegable para seleccionar NUMERO ##############

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
        "presente 1": "El presente 1 es el presente simple. Este se usa para describir acciones que ocurren regularmente a lo largo del tiempo.",
        "presente 2": "El presente 2 es el presente progresivo. Este se usa para describir acciones que están ocurriendo en este momento.",
        "presente 3": "El presente 3 es el presente habitual. Este se usa para describir acciones que se repiten en el tiempo de manera finita, como hábitos o rutinas.",
        "pasado experimentado 1": "El pasado experimentado 1 es el pasado experimentado simple. Este se usa para describir acciones que ocurrieron en el pasado y que le constan al sujeto por ser testigo directo de la acción.",
        "pasado experimentado 2": "El pasado experimentado 2 es el pasado experimentado progresivo. Este se usa para describir acciones que estuvieron ocurriendo en el pasado y que le constan al sujeto por ser testigo directo de la acción.",
        "pasado experimentado 3": "El pasado experimentado 3 es el pasado experimentado habitual. Este se usa para describir acciones que ocurrían regularmente en el pasado y que le constan al sujeto por ser testigo directo de la acción.",
        "pasado no experimentado 1": "El pasado no experimentado 1 es el pasado no experimentado simple. Este se usa para describir acciones que ocurrieron en el pasado sin la participación o el conocimiento directo del sujeto.",
        "pasado no experimentado 2": "El pasado no experimentado 2 es el pasado no experimentado progresivo. Este se usa para describir acciones que estuvieron ocurriendo en el pasado sin la participación o el conocimiento directo del sujeto.",
        "pasado no experimentado 3": "El pasado no experimentado 3 es el pasado no experimentado habitual. Este se usa para describir acciones que ocurrían regularmente en el pasado sin la participación o el conocimiento directo del sujeto."
    }

###### menú desplegable para seleccionar PERSONA ######

    st.header('Persona', divider='violet')
    
    persona = st.selectbox("Seleccione una persona: ", list(explicaciones_persona.keys()), index=0)
    explicacion_persona_placeholder = st.empty()
    explicaciones_persona["primera inclusiva"] += "<br><br>Ejemplo: '(Todos) nosotros vamos al mercado.'"
    explicaciones_persona["primera exclusiva"] += "<br><br>Ejemplo: 'Nosotros (pero no tú) vamos al mercado.'"
    
    explicacion_persona_placeholder.markdown("**Explicación de persona seleccionada:** " + explicaciones_persona[persona], unsafe_allow_html=True)


#################### menú desplegable para seleccionar TIEMPO ###################

    st.header('Tiempo', divider='violet')
    
    tiempo = st.selectbox("Seleccione un tiempo: ", list(explicaciones_tiempo.keys()), index=0)

    explicacion_tiempo_placeholder = st.empty()
    explicaciones_tiempo["presente 1"] += "<br><br>Ejemplo: 'Yo veo televisión.'"
    explicaciones_tiempo["presente 2"] += "<br><br>Ejemplo: 'Yo estoy viendo televisión.'"
    explicaciones_tiempo["presente 3"] += "<br><br>Ejemplo: 'Yo suelo ver televisión.'"
    explicaciones_tiempo["pasado experimentado 1"] += "<br><br>Ejemplo: 'Yo veía televisión.'"
    explicaciones_tiempo["pasado experimentado 2"] += "<br><br>Ejemplo: 'Yo estaba viendo televisión.'"
    explicaciones_tiempo["pasado experimentado 3"] += "<br><br>Ejemplo: 'Yo solía ver televisión.'"
    explicaciones_tiempo["pasado no experimentado 1"] += "<br><br>Ejemplo: '(Dicen que) yo veía televisión.'"
    explicaciones_tiempo["pasado no experimentado 2"] += "<br><br>Ejemplo: '(Dicen que) yo estaba viendo televisión.'"
    explicaciones_tiempo["pasado no experimentado 3"] += "<br><br>Ejemplo: '(Dicen que) yo solía ver televisión.'"
    
    explicacion_tiempo_placeholder.markdown("**Explicación de tiempo seleccionado:** " + explicaciones_tiempo[tiempo], unsafe_allow_html=True)
        
############################# RESULTADO #######################################

    st.header('Resultado', divider='violet')

#if base and numero and persona and tiempo:
#    resultado = conj_final(base, numero, persona, tiempo)
#    if resultado:
#        st.write("El verbo conjugado es: ")
#        st.markdown(f'<p style="font-size:24px; text-align:center;">{resultado}</p>', unsafe_allow_html=True)
#else:
#    st.error("Por favor, asegúrese de que todas las opciones estén seleccionadas.")
    
# Conjugar y mostrar el resultado según la variedad seleccionada

    conjugacion = None
    if st.session_state['variedad'] == "Ayacucho":
        conjugacion = conj_final(base, numero, persona, tiempo)
    elif st.session_state['variedad'] == "Cuzco":
        conjugacion = conj_final_cuzco(base, numero, persona, tiempo)
    elif st.session_state['variedad'] == "Ancash":
        conjugacion = conj_final_ancash(base, numero, persona, tiempo)

    if conjugacion:
        st.write("La conjugación es: ")
        st.markdown(f'<p style="font-size:24px; text-align:center;">{conjugacion}</p>', unsafe_allow_html=True)
        if conjugacion.endswith('x'):
            st.warning(f"No existe conjugación para el tiempo '{tiempo}' en la variedad del quechua seleccionada.")
            
    else:
        st.error("Hubo un error en la conjugación. Por favor, revise los parámetros seleccionados.")