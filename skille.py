import streamlit as st

# Configuration de la page
st.set_page_config(page_title="QCM sur les Matrices", page_icon="🔢", layout="centered")

# Style CSS pour une interface moderne
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .main-title { color: #6366f1; text-align: center; font-size: 2.5rem; font-weight: bold; margin-bottom: 20px; }
    .question-box { background-color: #1e293b; padding: 20px; border-radius: 15px; border-left: 5px solid #6366f1; margin-bottom: 20px; }
    div.stButton > button {
        width: 100%; background-color: #334155; color: white; border: 2px solid #475569;
        border-radius: 10px; padding: 10px; transition: all 0.3s; font-size: 1.1rem;
    }
    div.stButton > button:hover { background-color: #6366f1; border-color: #818cf8; }
    .feedback-vrai { color: #22c55e; font-weight: bold; text-align: center; }
    .feedback-faux { color: #ef4444; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">QCM sur les Matrices</h1>', unsafe_allow_html=True)

# Liste des questions en Français (Niveau L1 avancé)
questions = [
    {
        "q": "Soit A une matrice carrée d'ordre n. Si det(A) = 3, quelle est la valeur de det(2A) ?",
        "options": ["6", "3 * 2^n", "2 * 3^n", "3^n * 2"],
        "answer": "3 * 2^n"
    },
    {
        "q": "Une matrice carrée A est inversible si et seulement si :",
        "options": ["det(A) = 0", "rg(A) < n", "det(A) ≠ 0", "A est symétrique"],
        "answer": "det(A) ≠ 0"
    },
    {
        "q": "Quelle est la trace de la matrice résultant de AB - BA ?",
        "options": ["1", "det(A)det(B)", "0", "-1"],
        "answer": "0"
    },
    {
        "q": "Si A et B sont deux matrices symétriques, alors AB est symétrique si :",
        "options": ["Toujours vrai", "AB = BA", "A = B", "Jamais vrai"],
        "answer": "AB = BA"
    },
    {
        "q": "Le rang d'une matrice (rg(A)) est défini comme :",
        "options": ["Le nombre total de colonnes", "La dimension du noyau Ker(A)", "Le nombre maximal de lignes linéairement indépendantes", "La somme des éléments diagonaux"],
        "answer": "Le nombre maximal de lignes linéairement indépendantes"
    }
]

# Gestion de l'état (Session State)
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_q = 0
    st.session_state.finished = False
    st.session_state.feedback = ""

if not st.session_state.finished:
    q_idx = st.session_state.current_q
    if q_idx < len(questions):
        st.markdown(f'<div class="question-box"><h3>Question {q_idx + 1}</h3><p>{questions[q_idx]["q"]}</p></div>', unsafe_allow_html=True)
        
        # Affichage du feedback précédent s'il existe
        if st.session_state.feedback:
            st.markdown(st.session_state.feedback, unsafe_allow_html=True)

        for option in questions[q_idx]["options"]:
            if st.button(option):
                if option == questions[q_idx]["answer"]:
                    st.session_state.score += 1
                    st.session_state.feedback = '<p class="feedback-vrai">Vrai ! ✅</p>'
                else:
                    st.session_state.feedback = f'<p class="feedback-faux">Faux ! ❌ (La réponse était: {questions[q_idx]["answer"]})</p>'
                
                st.session_state.current_q += 1
                st.rerun()
    else:
        st.session_state.finished = True
        st.rerun()
else:
    st.balloons()
    st.markdown(f'<div style="text-align:center"><h2>🎊 Terminé !</h2><h1>Score: {st.session_state.score} / {len(questions)}</h1></div>', unsafe_allow_html=True)
    if st.button("Recommencer le test"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.finished = False
        st.session_state.feedback = ""
        st.rerun()
