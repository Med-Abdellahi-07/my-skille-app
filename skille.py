import streamlit as st

st.set_page_config(page_title="Expert RO : Méthode Graphique", page_icon="📈")

st.title("📈 Master Quiz : La Méthode Graphique")
st.write("Ce test évalue votre maîtrise absolue de la résolution graphique en Programmation Linéaire.")

questions = [
    {
        "question": "1. La méthode graphique est principalement limitée à quel nombre de variables de décision ?",
        "options": ["1 variable", "2 variables", "3 variables", "Illimité"],
        "answer": "2 variables"
    },
    {
        "question": "2. Comment appelle-t-1'ensemble des points (x1, x2) satisfaisant toutes les contraintes simultanément ?",
        "options": ["La zone d'ombre", "La région réalisable", "Le domaine de définition", "L'espace vectoriel"],
        "answer": "La région réalisable"
    },
    {
        "question": "3. Selon le théorème fondamental, où se trouve systématiquement la solution optimale ?",
        "options": ["Au centre de la région", "Sur l'axe des ordonnées", "À un point sommet (extrême)", "À l'origine (0,0)"],
        "answer": "À un point sommet (extrême)"
    },
    {
        "question": "4. Que représente graphiquement une contrainte d'égalité (ax1 + bx2 = c) ?",
        "options": ["Un demi-plan", "Une droite", "Un point unique", "Une parabole"],
        "answer": "Une droite"
    },
    {
        "question": "5. Dans quel quadrant se situe la région réalisable si les contraintes de non-négativité sont respectées ?",
        "options": ["Premier quadrant", "Deuxième quadrant", "Troisième quadrant", "Quatrième quadrant"],
        "answer": "Premier quadrant"
    },
    {
        "question": "6. Si la fonction objectif est parallèle à une contrainte active, que se passe-t-il ?",
        "options": ["Pas de solution", "Solution unique", "Infinité de solutions", "Solution non bornée"],
        "answer": "Infinité de solutions"
    },
    {
        "question": "7. Si les zones définies par les contraintes ne se recoupent jamais, on dit que le problème est :",
        "options": ["Optimal", "Dégénéré", "Non réalisable (Infeasible)", "Non borné"],
        "answer": "Non réalisable (Infeasible)"
    },
    {
        "question": "8. Pour Max Z = 3x1 + 2x2, quelle est la pente de la droite d'iso-profit ?",
        "options": ["-3/2", "-2/3", "3/2", "2/3"],
        "answer": "-3/2"
    },
    {
        "question": "9. Un polyèdre de solutions qui s'étend à l'infini dans le sens de l'optimisation indique un problème :",
        "options": ["Standard", "Borné", "Non borné (Unbounded)", "Nul"],
        "answer": "Non borné (Unbounded)"
    },
    {
        "question": "10. Comment appelle-t-on une contrainte qui passe par le point optimal ?",
        "options": ["Contrainte saturée (active)", "Contrainte inutile", "Contrainte lâche", "Contrainte fictive"],
        "answer": "Contrainte saturée (active)"
    },
    {
        "question": "11. Soit la contrainte 2x1 + 4x2 <= 20. Si x1 = 0, quelle est la valeur maximale de x2 ?",
        "options": ["2", "4", "5", "10"],
        "answer": "5"
    },
    {
        "question": "12. La méthode des droites d'iso-valeur consiste à déplacer la droite de la fonction objectif :",
        "options": ["De manière circulaire", "Parallèlement à elle-même", "Perpendiculairement à l'axe X", "De manière aléatoire"],
        "answer": "Parallèlement à elle-même"
    },
    {
        "question": "13. Un point intérieur à la région réalisable peut-il être optimal pour un problème linéaire classique ?",
        "options": ["Oui, toujours", "Non, jamais", "Seulement si Z=0", "Seulement en minimisation"],
        "answer": "Non, jamais"
    },
    {
        "question": "14. Si le point optimal est (4, 5) pour Max Z = 10x1 + 20x2, quelle est la valeur de Z ?",
        "options": ["100", "120", "140", "150"],
        "answer": "140"
    },
    {
        "question": "15. La contrainte x1 + x2 >= 10 définit une zone située :",
        "options": ["En dessous de la droite", "Au-dessus de la droite", "À gauche de l'axe Y", "Uniquement sur l'origine"],
        "answer": "Au-dessus de la droite"
    },
    {
        "question": "16. Quel outil mathématique est essentiel pour trouver l'intersection exacte de deux contraintes ?",
        "options": ["Le calcul intégral", "Le système d'équations linéaires", "Les probabilités", "La trigonométrie"],
        "answer": "Le système d'équations linéaires"
    },
    {
        "question": "17. Dans un polygone de solutions, les sommets sont aussi appelés :",
        "options": ["Points de selle", "Points de base réalisables", "Points médians", "Vecteurs nuls"],
        "answer": "Points de base réalisables"
    },
    {
        "question": "18. Si l'ajout d'une contrainte ne modifie pas la région réalisable, elle est dite :",
        "options": ["Redondante", "Cruciale", "Active", "Négative"],
        "answer": "Redondante"
    },
    {
        "question": "19. En minimisation graphique, on cherche le sommet :",
        "options": ["Le plus éloigné de l'origine", "Le plus proche de l'origine (selon Z)", "Ayant les coordonnées les plus grandes", "Sur l'axe X uniquement"],
        "answer": "Le plus proche de l'origine (selon Z)"
    },
    {
        "question": "20. La forme de la région réalisable dans un problème de PL est toujours :",
        "options": ["Concave", "Convexe", "Circulaire", "Discontinue"],
        "answer": "Convexe"
    }
]

score = 0
responses = []

for i, q in enumerate(questions):
    st.subheader(q["question"])
    res = st.radio("Sélectionnez votre réponse :", q["options"], key=f"q{i}")
    responses.append(res)
    st.markdown("---")

if st.button("Valider mes réponses"):
    for i, q in enumerate(questions):
        if responses[i] == q["answer"]:
            score += 1
    
    if score == 20:
        st.balloons()
        st.success(f"Score Parfait : {score}/20 ! Vous êtes un expert en Méthode Graphique.")
    elif score >= 14:
        st.info(f"Bon score : {score}/20. Vous maîtrisez les bases.")
    else:
        st.warning(f"Score : {score}/20. Une révision de la construction des polygones de solutions est nécessaire.")
