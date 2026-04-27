import streamlit as st
import time

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="QCM Machine Learning",
    page_icon="🤖",
    layout="centered",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

h1, h2, h3 {
    color: #e0e0ff !important;
}

.question-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

.question-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #a78bfa;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.question-text {
    font-size: 1.05rem;
    font-weight: 600;
    color: #f1f0ff;
    margin-bottom: 12px;
    line-height: 1.5;
}

.score-box {
    background: linear-gradient(135deg, #6d28d9, #4f46e5);
    border-radius: 20px;
    padding: 32px;
    text-align: center;
    color: white;
    font-size: 1.1rem;
    margin-top: 20px;
}

.score-number {
    font-size: 4rem;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
}

.correct-answer {
    color: #4ade80;
    font-weight: 600;
}

.wrong-answer {
    color: #f87171;
    font-weight: 600;
}

.stRadio > div {
    gap: 8px !important;
}

.stRadio label {
    color: #d4d4f5 !important;
    font-size: 0.95rem !important;
}

div[data-testid="stMarkdownContainer"] p {
    color: #c4c4e0;
}

.stButton > button {
    background: linear-gradient(135deg, #6d28d9, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 32px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: opacity 0.2s !important;
}

.stButton > button:hover {
    opacity: 0.85 !important;
}

.header-badge {
    display: inline-block;
    background: rgba(167, 139, 250, 0.2);
    border: 1px solid rgba(167, 139, 250, 0.4);
    color: #a78bfa;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 3px;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ─── Questions Data ─────────────────────────────────────────────────────────────
questions = [
    {
        "question": "Quelle est la différence fondamentale entre la programmation classique et le Machine Learning ?",
        "options": [
            "A) La programmation classique utilise des données, le ML n'en a pas besoin",
            "B) En ML, les règles sont apprises automatiquement à partir des données ; en programmation classique, elles sont écrites manuellement",
            "C) Le ML est plus rapide à exécuter que la programmation classique",
            "D) La programmation classique ne peut traiter que du texte, le ML traite toutes les données"
        ],
        "answer": "B",
        "explanation": "En programmation classique, le développeur écrit les règles explicitement. En ML, l'algorithme découvre les règles (patterns) à partir des données."
    },
    {
        "question": "Dans un problème d'apprentissage supervisé, que représente le label (y) ?",
        "options": [
            "A) Une variable d'entrée décrivant un exemple",
            "B) L'ensemble des données d'entraînement",
            "C) La valeur cible à prédire, fournie dans les données d'entraînement",
            "D) Le paramètre interne du modèle après entraînement"
        ],
        "answer": "C",
        "explanation": "Le label (y) est la valeur cible que le modèle doit apprendre à prédire. Il est fourni lors de l'entraînement mais absent lors de la prédiction sur de nouvelles données."
    },
    {
        "question": "Pourquoi la généralisation est-elle l'objectif ultime d'un modèle ML ?",
        "options": [
            "A) Pour obtenir un score parfait sur les données d'entraînement",
            "B) Pour réduire la taille du modèle",
            "C) Pour que le modèle performe bien sur des données nouvelles, jamais vues",
            "D) Pour accélérer l'entraînement du modèle"
        ],
        "answer": "C",
        "explanation": "Un modèle qui mémorise les données d'entraînement (overfitting) est inutile en production. La généralisation mesure la capacité à bien prédire sur de nouvelles données réelles."
    },
    {
        "question": "Un modèle prédit le prix d'un appartement en fonction de sa superficie et de son emplacement. De quel type de tâche s'agit-il ?",
        "options": [
            "A) Classification binaire",
            "B) Clustering",
            "C) Régression",
            "D) Apprentissage par renforcement"
        ],
        "answer": "C",
        "explanation": "La régression prédit une valeur continue (ici, un prix). La classification prédit une catégorie discrète (ex: spam/non-spam)."
    },
    {
        "question": "Dans le pipeline ML, quelle étape consomme approximativement 80% du temps réel d'un projet ?",
        "options": [
            "A) La modélisation et le choix d'algorithme",
            "B) Le déploiement en production",
            "C) La collecte, le nettoyage et l'exploration des données",
            "D) L'évaluation des performances"
        ],
        "answer": "C",
        "explanation": "La réalité du ML professionnel : 80% du temps est passé sur les données (collecte, nettoyage, exploration), et seulement 20% sur la modélisation."
    },
    {
        "question": "Quelle est la différence entre la régression et la classification en apprentissage supervisé ?",
        "options": [
            "A) La régression nécessite plus de données que la classification",
            "B) La régression prédit une valeur continue (y ∈ ℝ), la classification prédit une catégorie discrète",
            "C) La classification est toujours plus précise que la régression",
            "D) La régression est non-supervisée, la classification est supervisée"
        ],
        "answer": "B",
        "explanation": "Régression : prédire un prix, une température → sortie continue. Classification : prédire spam/non-spam, tumeur bénigne/maligne → sortie discrète."
    },
    {
        "question": "Lequel de ces problèmes relève de l'apprentissage NON supervisé ?",
        "options": [
            "A) Détecter si un email est un spam",
            "B) Prédire si une tumeur est bénigne ou maligne",
            "C) Segmenter des clients en groupes selon leurs comportements d'achat",
            "D) Prédire le cours d'une action boursière"
        ],
        "answer": "C",
        "explanation": "La segmentation (clustering) ne nécessite pas de labels. L'algorithme découvre lui-même des structures cachées dans les données X sans valeur cible y."
    },
    {
        "question": "Dans AlphaGo (le programme qui joue aux échecs/Go), quel type d'apprentissage est utilisé ?",
        "options": [
            "A) Supervisé — car il apprend des parties d'experts",
            "B) Non supervisé — car il regroupe des stratégies similaires",
            "C) Par renforcement — car il apprend par essais/erreurs en maximisant une récompense",
            "D) Semi-supervisé — car il combine les deux approches"
        ],
        "answer": "C",
        "explanation": "L'apprentissage par renforcement : un agent apprend par essais/erreurs. Gagner = récompense positive, perdre = récompense négative. AlphaGo a joué des millions de parties contre lui-même."
    },
    {
        "question": "Qu'est-ce qu'un dataset (jeu de données) en ML ?",
        "options": [
            "A) L'algorithme utilisé pour entraîner le modèle",
            "B) Les paramètres internes du modèle",
            "C) Un ensemble structuré d'exemples utilisés pour entraîner ou évaluer un modèle",
            "D) Le résultat final de la prédiction"
        ],
        "answer": "C",
        "explanation": "Un dataset est une collection d'exemples (lignes) avec leurs features (colonnes X) et éventuellement leurs labels (y), utilisée pour l'entraînement et l'évaluation."
    },
    {
        "question": "Pourquoi sépare-t-on les données en ensemble d'entraînement et ensemble de test ?",
        "options": [
            "A) Pour réduire la taille du dataset et accélérer l'entraînement",
            "B) Pour évaluer objectivement la généralisation du modèle sur des données non vues",
            "C) Parce que le modèle ne peut pas traiter toutes les données à la fois",
            "D) Pour satisfaire une obligation légale sur les données"
        ],
        "answer": "B",
        "explanation": "Le modèle est entraîné sur les données d'entraînement. Le test set simule de nouvelles données inconnues, permettant d'évaluer la vraie capacité de généralisation."
    },
    {
        "question": "Qu'est-ce que l'overfitting (sur-apprentissage) ?",
        "options": [
            "A) Le modèle ne converge pas pendant l'entraînement",
            "B) Le modèle mémorise les données d'entraînement mais généralise mal sur de nouvelles données",
            "C) Le modèle est trop simple pour capturer les patterns des données",
            "D) Le modèle prend trop de temps à s'entraîner"
        ],
        "answer": "B",
        "explanation": "L'overfitting = excellent sur train, mauvais sur test. Le modèle a mémorisé le bruit des données au lieu d'apprendre les vrais patterns. C'est l'ennemi de la généralisation."
    },
    {
        "question": "Dans une notation f(X) → ŷ, que représente ŷ (y-chapeau) ?",
        "options": [
            "A) La valeur réelle du label dans les données",
            "B) La valeur prédite par le modèle",
            "C) L'erreur commise par le modèle",
            "D) La moyenne des valeurs du dataset"
        ],
        "answer": "B",
        "explanation": "ŷ (y-hat) est la valeur prédite par le modèle f(X). On compare ŷ à y (la vraie valeur) pour mesurer l'erreur du modèle."
    },
    {
        "question": "Quelle étape du pipeline ML précède la modélisation ?",
        "options": [
            "A) Le déploiement",
            "B) L'évaluation",
            "C) L'exploration (visualisation et compréhension des distributions)",
            "D) La mise en production"
        ],
        "answer": "C",
        "explanation": "Ordre du pipeline : Collecte → Nettoyage → Exploration → Modélisation → Évaluation → Déploiement. L'exploration (EDA) précède toujours la modélisation."
    },
    {
        "question": "Un filtre anti-spam basé sur des règles manuelles ('contient promo → spam') est remplacé par un modèle ML. Quel est l'avantage principal du ML ?",
        "options": [
            "A) Le modèle ML est plus simple à implémenter",
            "B) Le modèle ML peut s'adapter et capturer des patterns complexes invisibles aux règles manuelles",
            "C) Le modèle ML consomme moins de ressources informatiques",
            "D) Le modèle ML ne nécessite aucune donnée d'entraînement"
        ],
        "answer": "B",
        "explanation": "Les règles manuelles sont limitées et rigides. Le ML peut capturer des milliers de patterns complexes (combinaisons de mots, fréquences, expéditeurs...) impossibles à écrire manuellement."
    },
    {
        "question": "Qu'est-ce que l'étape de nettoyage (preprocessing) dans le pipeline ML ?",
        "options": [
            "A) Choisir le meilleur algorithme de ML",
            "B) Visualiser les distributions et corrélations des features",
            "C) Gérer les valeurs manquantes, les outliers et les doublons",
            "D) Déployer le modèle en production"
        ],
        "answer": "C",
        "explanation": "Le nettoyage traite les valeurs manquantes (imputation/suppression), les outliers (valeurs aberrantes) et les doublons pour obtenir des données de qualité avant la modélisation."
    },
    {
        "question": "La réduction de dimensionnalité (ex: PCA) appartient à quel type d'apprentissage ?",
        "options": [
            "A) Supervisé — car elle utilise les labels",
            "B) Par renforcement — car elle optimise une récompense",
            "C) Non supervisé — car elle trouve des structures cachées sans labels",
            "D) Semi-supervisé — car elle combine labels et données non étiquetées"
        ],
        "answer": "C",
        "explanation": "La réduction de dimensionnalité (PCA, t-SNE...) cherche des structures dans X sans utiliser y. C'est de l'apprentissage non supervisé, comme le clustering."
    },
    {
        "question": "Pourquoi le monitoring est-il crucial après le déploiement d'un modèle ML ?",
        "options": [
            "A) Pour réentraîner le modèle chaque heure",
            "B) Pour détecter le drift des données — les performances peuvent se dégrader si la distribution des données change",
            "C) Pour afficher des statistiques à l'utilisateur final",
            "D) Pour respecter les exigences légales de publication"
        ],
        "answer": "B",
        "explanation": "Le 'data drift' : les données réelles évoluent avec le temps. Un modèle performant en janvier peut devenir mauvais en décembre si le comportement des utilisateurs change. Le monitoring détecte cette dégradation."
    },
    {
        "question": "Une banque veut détecter des transactions frauduleuses. C'est un exemple de :",
        "options": [
            "A) Régression — car on prédit un montant de fraude",
            "B) Clustering — car on groupe les transactions similaires",
            "C) Classification — car on prédit fraude (1) ou non-fraude (0)",
            "D) Apprentissage par renforcement — car le système s'améliore avec le temps"
        ],
        "answer": "C",
        "explanation": "Détecter une fraude = prédire une classe binaire : frauduleux (1) ou légitime (0). C'est une classification binaire supervisée, nécessitant des exemples historiques étiquetés."
    },
    {
        "question": "Qu'apprend réellement un modèle ML lors de la phase d'entraînement ?",
        "options": [
            "A) Il mémorise toutes les lignes du dataset",
            "B) Il ajuste ses paramètres internes pour minimiser l'erreur entre ŷ et y sur les données d'entraînement",
            "C) Il télécharge des règles depuis Internet",
            "D) Il copie les règles écrites par le développeur"
        ],
        "answer": "B",
        "explanation": "L'entraînement = optimisation des paramètres (poids) du modèle pour minimiser une fonction de perte (loss function). Plus l'erreur |y - ŷ| est petite, meilleur est le modèle."
    },
    {
        "question": "Quel est le risque si on évalue un modèle uniquement sur ses données d'entraînement ?",
        "options": [
            "A) L'évaluation sera trop lente",
            "B) On obtiendra des métriques trop pessimistes",
            "C) On obtiendra des métriques trop optimistes — le modèle a déjà vu ces données (data leakage)",
            "D) Il n'y a aucun risque, c'est une pratique recommandée"
        ],
        "answer": "C",
        "explanation": "Évaluer sur les données d'entraînement = tricher. Le modèle a déjà vu ces exemples et peut les mémoriser. On obtient un score artificiellement élevé qui ne reflète pas la vraie performance sur des données inconnues."
    }
]

# ─── Session State ──────────────────────────────────────────────────────────────
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="header-badge">MACHINE LEARNING · NIVEAU AVANCÉ</div>', unsafe_allow_html=True)
st.title("🤖 QCM — Introduction au ML")
st.markdown("**20 questions** pour tester votre compréhension approfondie du Machine Learning.")
st.markdown("---")

# ─── Questions Form ─────────────────────────────────────────────────────────────
if not st.session_state.submitted:
    for i, q in enumerate(questions):
        with st.container():
            st.markdown(f"""
            <div class="question-card">
                <div class="question-number">Question {i+1:02d} / 20</div>
                <div class="question-text">{q['question']}</div>
            </div>
            """, unsafe_allow_html=True)

            selected = st.radio(
                label=f"q{i}",
                options=q["options"],
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            # Store only the letter (A/B/C/D)
            if selected:
                st.session_state.answers[i] = selected[0]

        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Soumettre mes réponses"):
            if len(st.session_state.answers) < len(questions):
                st.warning(f"⚠️ Répondez à toutes les questions ! ({len(st.session_state.answers)}/20 répondues)")
            else:
                st.session_state.submitted = True
                st.rerun()

# ─── Results ───────────────────────────────────────────────────────────────────
else:
    score = sum(
        1 for i, q in enumerate(questions)
        if st.session_state.answers.get(i) == q["answer"]
    )
    percentage = (score / len(questions)) * 100

    # Score emoji
    if percentage >= 80:
        emoji = "🏆"
        msg = "Excellent ! Maîtrise avancée du ML."
    elif percentage >= 60:
        emoji = "✨"
        msg = "Bon résultat ! Quelques concepts à revoir."
    elif percentage >= 40:
        emoji = "📚"
        msg = "Résultat moyen. Reprenez le cours."
    else:
        emoji = "🔄"
        msg = "À retravailler. Relisez attentivement le cours."

    st.markdown(f"""
    <div class="score-box">
        <div style="font-size:2rem; margin-bottom:8px;">{emoji}</div>
        <div class="score-number">{score} / 20</div>
        <div style="font-size:1.3rem; margin-top:8px;">{percentage:.0f}%</div>
        <div style="margin-top:12px; opacity:0.85;">{msg}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 Correction détaillée")
    st.markdown("---")

    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i, "?")
        correct = q["answer"]
        is_correct = user_ans == correct

        icon = "✅" if is_correct else "❌"
        status_color = "correct-answer" if is_correct else "wrong-answer"

        with st.expander(f"{icon} Question {i+1:02d} — {q['question'][:60]}..."):
            st.markdown(f"**Question :** {q['question']}")
            st.markdown("")
            for opt in q["options"]:
                letter = opt[0]
                if letter == correct:
                    st.markdown(f'<span class="correct-answer">✔ {opt}</span>', unsafe_allow_html=True)
                elif letter == user_ans and not is_correct:
                    st.markdown(f'<span class="wrong-answer">✘ {opt} ← votre réponse</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f"&nbsp;&nbsp;&nbsp;{opt}")

            st.markdown("")
            st.info(f"💡 **Explication :** {q['explanation']}")

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Recommencer le quiz"):
            st.session_state.submitted = False
            st.session_state.answers = {}
            st.rerun()