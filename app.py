"""Repaso para el viernes: práctica de Verdadero o Falso.

Para probarla en tu computadora:
    pip install -r requirements.txt
    streamlit run app.py
"""
import html
import random
import time
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components

from preguntas import PARTES, PREGUNTAS

ROMANO = {1: "I", 2: "II", 3: "III", 4: "IV"}
DURACION_EXAMEN = 45 * 60  # segundos
POR_N = {q["n"]: q for q in PREGUNTAS}
MODOS = ["Practicar", "Mis fallos", "Simulacro de examen", "Hoja de repaso"]

st.set_page_config(page_title="Repaso para el viernes", page_icon="📝", layout="centered")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap');
.marca {font-family:'Caveat', cursive; font-size:2.4rem; font-weight:700; line-height:1.1;
        display:inline-block; transform:rotate(-3deg); margin:0 0 .25rem}
.ok {color:#1C8A57} .mal {color:#C92E2E}
.afirmacion {font-size:1.35rem; line-height:1.4; margin:.25rem 0 1rem}
.porque {border-left:4px solid #FFE45C; padding-left:.8rem; margin:.5rem 0 1rem}
.nota {font-family:'Caveat', cursive; font-size:3.6rem; font-weight:700; line-height:1;
       border:3px solid currentColor; border-radius:50% 45% 52% 48%; padding:.1rem 1rem;
       display:inline-block; transform:rotate(-5deg); margin-right:1rem}
.correccion {font-family:'Caveat', cursive; font-size:1.35rem; color:#C92E2E; line-height:1.2; margin:0 0 .5rem}
.casillas {display:grid; grid-template-columns:repeat(10, 1fr); gap:3px; margin:.2rem 0 .6rem}
.casilla {aspect-ratio:1; border:1px solid #C9D3E3; border-radius:3px; font-size:.6rem;
          display:grid; place-items:center; color:#5A6478}
.casilla.ok {background:#E3F4EA; border-color:#1C8A57; color:#1C8A57}
.casilla.mal {background:#FBE6E6; border-color:#C92E2E; color:#C92E2E}
</style>
""",
    unsafe_allow_html=True,
)


# ---------- Estado ----------
ss = st.session_state
ss.setdefault("stats", {})            # n -> {"ultima": "ok" | "mal", "bien": int, "mal": int}
ss.setdefault("ultima_version", {})   # n -> versión mostrada la última vez
ss.setdefault("cola", [])             # lista de (n, versión)
ss.setdefault("idx", 0)
ss.setdefault("respuesta", None)      # (elegida, acertó) de la pregunta actual
ss.setdefault("ronda_bien", 0)
ss.setdefault("ronda_mal", [])
ss.setdefault("config", None)
ss.setdefault("examen", None)
ss.setdefault("mejor_nota", 0.0)


def esc(texto):
    return html.escape(texto)


def md(texto):
    return texto.replace("*", "\\*")


def elegir_version(n):
    """Elige una redacción al azar, distinta de la última que se mostró."""
    total = len(POR_N[n]["versiones"])
    opciones = [i for i in range(total) if i != ss.ultima_version.get(n)] or [0]
    v = random.choice(opciones)
    ss.ultima_version[n] = v
    return v


def registrar(n, bien):
    previo = ss.stats.get(n, {"bien": 0, "mal": 0})
    ss.stats[n] = {
        "ultima": "ok" if bien else "mal",
        "bien": previo["bien"] + (1 if bien else 0),
        "mal": previo["mal"] + (0 if bien else 1),
    }


def fallos():
    return [q for q in PREGUNTAS if ss.stats.get(q["n"], {}).get("ultima") == "mal"]


def pool():
    if ss.get("modo") == "Mis fallos":
        return fallos()
    parte = ss.get("parte", "Todas")
    return [q for q in PREGUNTAS if parte == "Todas" or q["parte"] == parte]


def nueva_ronda(lista):
    lista = list(lista)
    if ss.get("mezclar", True):
        random.shuffle(lista)
    ss.cola = [(q["n"], elegir_version(q["n"])) for q in lista]
    ss.idx = 0
    ss.respuesta = None
    ss.ronda_bien = 0
    ss.ronda_mal = []


def fmt_nota(nota):
    return f"{nota:.1f}" if nota % 1 else f"{nota:.0f}"


# ---------- Acciones ----------
def responder(eleccion):
    n, v = ss.cola[ss.idx]
    bien = eleccion == POR_N[n]["versiones"][v]["respuesta"]
    registrar(n, bien)
    if bien:
        ss.ronda_bien += 1
    else:
        ss.ronda_mal.append(n)
    ss.respuesta = (eleccion, bien)


def siguiente():
    ss.idx += 1
    ss.respuesta = None


def repetir_fallos():
    nueva_ronda([POR_N[n] for n in ss.ronda_mal])


def otra_ronda():
    nueva_ronda(pool())


def nuevo_examen():
    for k in [k for k in ss.keys() if str(k).startswith("ex_")]:
        del ss[k]
    inicio = time.time()
    ss.examen = {
        "id": int(inicio * 1000),
        "inicio": inicio,
        "items": [(q["n"], elegir_version(q["n"])) for q in PREGUNTAS],
        "entregado": False,
        "res": None,
    }


def ir_a_fallos():
    ss.modo = "Mis fallos"


def borrar_avance():
    ss.stats = {}
    ss.mejor_nota = 0.0
    ss.config = None
    ss.examen = None


def corregir_examen():
    ex = ss.examen
    usado = time.time() - ex["inicio"]
    bien_total, por_parte, respuestas = 0, {1: 0, 2: 0, 3: 0, 4: 0}, {}
    for n, v in ex["items"]:
        elegida = ss.get(f"ex_{ex['id']}_{n}")
        respuestas[n] = elegida
        bien = elegida == POR_N[n]["versiones"][v]["respuesta"]
        registrar(n, bien)
        if bien:
            bien_total += 1
            por_parte[POR_N[n]["parte"]] += 1
    nota = bien_total * 2.5
    en_blanco = sum(1 for r in respuestas.values() if r is None)
    if nota == 100:
        comentario = "¡Excelente! Examen perfecto."
    elif nota >= 90:
        comentario = "Excelente trabajo."
    elif nota >= 80:
        comentario = "Muy bien. Revisa lo que te marqué en rojo."
    elif nota >= 70:
        comentario = "Aprobado, pero puedes mejorar."
    else:
        comentario = "Hay que estudiar más antes del viernes."
    debil = min(por_parte, key=lambda p: por_parte[p])
    if nota == 100:
        consejo = "Nota del profesor: dominas el contenido. Haz otro simulacro el jueves para confirmarlo."
    else:
        consejo = (
            f"Nota del profesor: tu parte más débil fue la Parte {ROMANO[debil]} "
            f"({PARTES[debil]}), con {por_parte[debil]} de 10. Léela en la hoja de repaso "
            "y después practica tus fallos."
        )
    if en_blanco:
        consejo += (
            f" Dejaste {en_blanco} sin contestar; en el examen real contesta todas, "
            "porque una en blanco vale cero."
        )
    ss.mejor_nota = max(ss.mejor_nota, nota)
    ex["entregado"] = True
    ex["res"] = {
        "bien": bien_total, "nota": nota, "por_parte": por_parte, "debil": debil,
        "comentario": comentario, "consejo": consejo, "respuestas": respuestas,
        "fuera_de_tiempo": usado > DURACION_EXAMEN, "minutos": usado / 60,
    }


# ---------- Barra lateral ----------
with st.sidebar:
    st.header("Repaso para el viernes")
    st.radio("Modo", MODOS, key="modo")
    if ss.modo in ("Practicar", "Hoja de repaso"):
        st.selectbox(
            "Parte", ["Todas", 1, 2, 3, 4], key="parte",
            format_func=lambda p: "Todas las partes" if p == "Todas" else f"Parte {ROMANO[p]}: {PARTES[p]}",
        )
    if ss.modo in ("Practicar", "Mis fallos"):
        st.checkbox("Mezclar orden", value=True, key="mezclar")

    st.divider()
    try:
        from zoneinfo import ZoneInfo
        hoy = datetime.now(ZoneInfo("America/Santo_Domingo"))
    except Exception:
        hoy = datetime.now()
    dias = (4 - hoy.weekday()) % 7
    if dias == 0:
        st.markdown("**El examen es hoy. ¡Éxito!**")
    else:
        st.markdown(f"**Falta{'' if dias == 1 else 'n'} {dias} día{'' if dias == 1 else 's'} para el viernes**")
    acertadas = sum(1 for s in ss.stats.values() if s["ultima"] == "ok")
    st.write(f"Acertadas: {acertadas} de 40")
    if ss.mejor_nota:
        st.write(f"Mejor nota en simulacro: {fmt_nota(ss.mejor_nota)} / 100")

    cuadro = ""
    for p in range(1, 5):
        cuadro += f"<small>Parte {ROMANO[p]}</small><div class='casillas'>"
        for q in [q for q in PREGUNTAS if q["parte"] == p]:
            estado = ss.stats.get(q["n"], {}).get("ultima", "")
            cuadro += f"<div class='casilla {estado}'>{q['n']}</div>"
        cuadro += "</div>"
    st.markdown(cuadro, unsafe_allow_html=True)
    st.caption("Verde: acertada la última vez. Rojo: fallada. Tu avance dura mientras tengas la página abierta.")
    st.button("Borrar mi avance", on_click=borrar_avance)


# Reinicia la ronda cuando cambian el modo, la parte o el orden
if ss.modo in ("Practicar", "Mis fallos"):
    config = (ss.modo, ss.get("parte", "Todas"), ss.get("mezclar", True))
    if config != ss.config:
        ss.config = config
        nueva_ronda(pool())
else:
    ss.config = None


# ---------- Vistas ----------
def vista_practica():
    if not ss.cola:
        st.markdown('<p class="marca ok">¡Nada pendiente!</p>', unsafe_allow_html=True)
        st.write(
            "No tienes fallos guardados. Practica una ronda y aquí aparecerán las "
            "afirmaciones que falles, para repetirlas hasta acertarlas."
        )
        return

    if ss.idx >= len(ss.cola):
        total, bien = len(ss.cola), ss.ronda_bien
        nota = round(bien / total * 100)
        if nota == 100:
            msg = "¡Perfecto!"
        elif nota >= 80:
            msg = "¡Muy bien!"
        elif nota >= 60:
            msg = "Vas bien, sigue"
        else:
            msg = "A repasar un poco más"
        clase = "ok" if nota >= 60 else "mal"
        st.markdown(f'<p class="marca {clase}">{msg}</p>', unsafe_allow_html=True)
        st.subheader(f"{bien} / {total}")
        texto = f"Nota de esta ronda: {nota} sobre 100."
        if ss.ronda_mal:
            texto += f" Fallaste {len(ss.ronda_mal)}: {', '.join(map(str, ss.ronda_mal))}."
        st.write(texto)
        c1, c2 = st.columns(2)
        if ss.ronda_mal:
            c1.button("Repetir las que fallé", on_click=repetir_fallos, type="primary")
        c2.button("Otra ronda", on_click=otra_ronda)
        return

    n, v = ss.cola[ss.idx]
    q = POR_N[n]
    ver = q["versiones"][v]
    st.caption(f"Pregunta {ss.idx + 1} de {len(ss.cola)}. Parte {ROMANO[q['parte']]}: {PARTES[q['parte']]}")
    st.markdown(f'<p class="afirmacion"><b>{n}.</b> {esc(ver["texto"])}</p>', unsafe_allow_html=True)

    if ss.respuesta is None:
        c1, c2 = st.columns(2)
        c1.button("Verdadero", on_click=responder, args=("V",), type="primary", key=f"v_{ss.idx}")
        c2.button("Falso", on_click=responder, args=("F",), type="primary", key=f"f_{ss.idx}")
        st.caption("Consejo: si la afirmación tiene una sola palabra equivocada, ya es falsa.")
    else:
        _, bien = ss.respuesta
        if bien:
            st.markdown('<p class="marca ok">¡Correcto!</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="marca mal">Incorrecto, revisa esta</p>', unsafe_allow_html=True)
        correcta = "Verdadero" if ver["respuesta"] == "V" else "Falso"
        st.markdown(f"**La respuesta es {correcta}.**")
        st.markdown(f'<div class="porque">{esc(ver["explicacion"])}</div>', unsafe_allow_html=True)
        ultima = ss.idx == len(ss.cola) - 1
        st.button("Ver mi resultado" if ultima else "Siguiente pregunta", on_click=siguiente, type="primary")


def vista_examen():
    ex = ss.examen
    if ex is None:
        st.subheader("Simulacro de examen")
        st.write(
            "Las 40 afirmaciones en una sola hoja, como en el examen real: 45 minutos y "
            "2.5 puntos cada una. No verás las respuestas hasta entregar. Cada vez que lo "
            "haces, las preguntas salen redactadas de otra forma."
        )
        st.button("Empezar simulacro", on_click=nuevo_examen, type="primary")
        return

    if not ex["entregado"]:
        fin_ms = int((ex["inicio"] + DURACION_EXAMEN) * 1000)
        components.html(
            f"""<div id="t" style="font:700 1.15rem system-ui,sans-serif;color:#1F3A93"></div>
<script>
const fin = {fin_ms};
function pinta() {{
  const s = Math.max(0, Math.ceil((fin - Date.now()) / 1000));
  document.getElementById('t').textContent = s === 0
    ? 'Se acabó el tiempo: entrega tu examen.'
    : 'Tiempo restante: ' + Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
  document.getElementById('t').style.color = s < 300 ? '#C92E2E' : '#1F3A93';
}}
pinta(); setInterval(pinta, 1000);
</script>""",
            height=36,
        )
        with st.form("examen"):
            parte_actual = 0
            for n, v in ex["items"]:
                q = POR_N[n]
                if q["parte"] != parte_actual:
                    parte_actual = q["parte"]
                    st.subheader(f"Parte {ROMANO[parte_actual]}: {PARTES[parte_actual]}")
                st.radio(
                    f"**{n}.** {md(q['versiones'][v]['texto'])}",
                    ["V", "F"], index=None, horizontal=True, key=f"ex_{ex['id']}_{n}",
                    format_func=lambda x: "Verdadero" if x == "V" else "Falso",
                )
            entregar = st.form_submit_button("Entregar examen", type="primary")
        if entregar:
            corregir_examen()
            st.rerun()
        return

    r = ex["res"]
    clase = "ok" if r["nota"] >= 70 else "mal"
    st.markdown(
        f'<span class="nota {clase}">{fmt_nota(r["nota"])}</span>'
        f'<span class="marca {clase}">{r["comentario"]}</span>',
        unsafe_allow_html=True,
    )
    st.write(f"{r['bien']} correctas de 40, a 2.5 puntos cada una.")
    if r["fuera_de_tiempo"]:
        st.warning(f"Lo entregaste fuera de tiempo: tardaste {r['minutos']:.0f} minutos y el límite es 45.")
    cols = st.columns(4)
    for i, p in enumerate(range(1, 5)):
        cols[i].metric(f"Parte {ROMANO[p]}", f"{r['por_parte'][p]} de 10")
    st.info(r["consejo"])
    c1, c2 = st.columns(2)
    c1.button("Hacer otro simulacro", on_click=nuevo_examen, type="primary")
    if r["bien"] < 40:
        c2.button("Practicar mis fallos", on_click=ir_a_fallos)

    st.divider()
    st.subheader("Tu examen corregido")
    parte_actual = 0
    for n, v in ex["items"]:
        q = POR_N[n]
        ver = q["versiones"][v]
        if q["parte"] != parte_actual:
            parte_actual = q["parte"]
            st.markdown(f"#### Parte {ROMANO[parte_actual]}: {PARTES[parte_actual]}")
        elegida = r["respuestas"][n]
        bien = elegida == ver["respuesta"]
        marca = '<span class="marca ok">✓</span>' if bien else '<span class="marca mal">✗</span>'
        tu = {"V": "Verdadero", "F": "Falso", None: "sin contestar"}[elegida]
        st.markdown(
            f'{marca} <b>{n}.</b> {esc(ver["texto"])} <small>(Tu respuesta: {tu})</small>',
            unsafe_allow_html=True,
        )
        if not bien:
            correcta = "Verdadero" if ver["respuesta"] == "V" else "Falso"
            st.markdown(
                f'<p class="correccion">Es {correcta}: {esc(ver["explicacion"])}</p>',
                unsafe_allow_html=True,
            )


def vista_hoja():
    tapar = st.toggle("Tapar respuestas para ponerme a prueba", key="tapar")
    parte = ss.get("parte", "Todas")
    for p in range(1, 5):
        if parte != "Todas" and p != parte:
            continue
        st.subheader(f"Parte {ROMANO[p]}: {PARTES[p]}")
        for q in [q for q in PREGUNTAS if q["parte"] == p]:
            orig, *otras = q["versiones"]
            st.markdown(f"**{q['n']}.** {md(orig['texto'])}")
            lineas = [f"**{'Verdadero' if orig['respuesta'] == 'V' else 'Falso'}.** {md(orig['explicacion'])}", "",
                      "*Otras formas en que te lo pueden preguntar:*"]
            for o in otras:
                lineas.append(f"- **({o['respuesta']})** {md(o['texto'])}")
            contenido = "\n".join(lineas)
            if tapar:
                with st.expander("Ver respuesta"):
                    st.markdown(contenido)
            else:
                st.markdown(contenido)
            st.write("")


st.title("Repaso para el viernes")
st.caption(
    "Algoritmos, estructuras de datos y complejidad. Cada afirmación tiene tres versiones "
    "que se alternan, y a veces es verdadera y a veces falsa: entiende el tema, no memorices."
)

if ss.modo in ("Practicar", "Mis fallos"):
    vista_practica()
elif ss.modo == "Simulacro de examen":
    vista_examen()
else:
    vista_hoja()
