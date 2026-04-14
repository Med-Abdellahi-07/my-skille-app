import streamlit as st

if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

st.title("🎓 EXAMEN : MÉTHODE GRAPHIQUE (RO)")

questions = [
    {
        "q": "1. Quelle est la limite théorique de variables pour la méthode graphique ?",
        "options": ["1 variable", "2 variables", "3 variables", "Aucune limite"],
        "answer": "2 variables"
    },
    {
        "q": "2. Si la région réalisable est vide, comment qualifie-t-on le problème ?",
        "options": ["Optimal", "Dégénéré", "Non réalisable", "Non borné"],
        "answer": "Non réalisable"
    },
    {
        "q": "3. Où se situe mathématiquement la solution optimale dans un polyèdre convexe ?",
        "options": ["Au centre", "Sur un sommet", "À l'origine", "À l'infini"],
        "answer": "Sur un sommet"
    },
    {
        "q": "4. Que représente une droite d'iso-profit ?",
        "options": ["Une contrainte", "Les points ayant le même Z", "La frontière du domaine", "Une variable"],
        "answer": "Les points ayant le même Z"
    },
    {
        "q": "5. La contrainte 2x1 + 3x2 <= 12 coupe l'axe x2 (ordonnée) au point :",
        "options": ["(6, 0)", "(0, 4)", "(0, 6)", "(4, 0)"],
        "answer": "(0, 4)"
    },
    {
        "q": "6. Dans quel quadrant travaille-t-on avec x1 >= 0 et x2 >= 0 ?",
        "options": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
        "answer": "Quadrant I"
    },
    {
        "q": "7. Si Z augmente sans jamais rencontrer de sommet limite, le problème est :",
        "options": ["Borné", "Standard", "Non borné", "Impossible"],
        "answer": "Non borné"
    },
    {
        "q": "8. Deux droites de contraintes parallèles et de sens opposés peuvent rendre le domaine :",
        "options": ["Infini", "Vide", "Circulaire", "Optimal"],
        "answer": "Vide"
    },
    {
        "q": "9. Une contrainte qui ne touche pas la région réalisable est dite :",
        "options": ["Active", "Saturée", "Redondante", "Optimale"],
        "answer": "Redondante"
    },
    {
        "q": "10. Pour Max Z = 5x1 + 5x2, si la pente est identique à une contrainte active :",
        "options": ["Solution unique", "Zéro solution", "Infinité de solutions", "Solution nulle"],
        "answer": "Infinité de solutions"
    },
    {
        "q": "11. Quel est l'effet d'une contrainte x1 + x2 >= 0 sur le premier quadrant ?",
        "options": ["Elle réduit le domaine", "Elle est redondante", "Elle l'annule", "Elle le divise"],
        "answer": "Elle est redondante"
    },
    {
        "q": "12. Le point (0,0) est-il toujours une solution réalisable ?",
        "options": ["Oui", "Non", "Seulement en Max", "Seulement si b >= 0"],
        "answer": "Seulement si b >= 0"
    },
    {
        "q": "13. La méthode graphique utilise quel outil pour l'exactitude des sommets ?",
        "options": ["Calcul intégral", "Système d'équations", "Matrice inverse", "Dérivées"],
        "answer": "Système d'équations"
    },
    {
        "q": "14. En minimisation, la direction d'amélioration de Z va vers :",
        "options": ["L'origine", "L'infini", "La droite", "La gauche"],
        "answer": "L'origine"
    },
    {
        "q": "15. La région réalisable est toujours un ensemble :",
        "options": ["Concave", "Discontinu", "Convexe", "Ouvert"],
        "answer": "Convexe"
    },
    {
        "q": "16. Un point extrême est aussi appelé :",
        "options": ["Point de selle", "Sommet", "Point moyen", "Vecteur nul"],
        "answer": "Sommet"
    },
    {
        "q": "17. Si x1 = 2 et x2 = 3 dans Max Z = 10x1 + 20x2, alors Z vaut :",
        "options": ["50", "70", "80", "100"],
        "answer": "80"
    },
    {
        "q": "18. Une contrainte active est une contrainte où l'égalité est :",
        "options": ["Vérifiée", "Fausse", "Négative", "Inutile"],
        "answer": "Vérifiée"
    },
    {
        "q": "19. Le déplacement de la droite iso-profit doit rester :",
        "options": ["Perpendiculaire", "Parallèle", "Vertical", "Horizontal"],
        "answer": "Parallèle"
    },
    {
        "q": "20. La RO cherche l'optimum, ce qui signifie :",
        "options": ["Le plus grand Z", "Le plus petit Z", "Le meilleur Z possible", "Z = 0"],
        "answer": "Le meilleur Z possible"
    }
]

if st.session_state.current_q < len(questions):
    item = questions[st.session_state.current_q]
    st.write(f"Question {st.session_state.current_q + 1} sur {len(questions)}")
    st.subheader(item["q"])
    
    user_choice = st.radio("Faites votre choix :", item["options"], key=f"radio_{st.session_state.current_q}")
    
    if not st.session_state.answered:
        if st.button("Valider la réponse"):
            st.session_state.answered = True
            if user_choice == item["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct !"
            else:
                st.session_state.feedback = f"❌ Erreur. La réponse était : {item['answer']}"
            st.rerun()
    else:
        st.write(st.session_state.feedback)
        if st.button("Question suivante"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.rerun()
else:
    st.header("Résultat Final")
    st.write(f"Votre score : {st.session_state.score} / 20")
    if st.session_state.score >= 16:
        st.balloons()
        st.success("Niveau Expert confirmé !")
    elif st.session_state.score >= 10:
        st.info("Niveau Intermédiaire.")
    else:
        st.error("Révision nécessaire.")
    
    if st.button("Recommencer le test"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
