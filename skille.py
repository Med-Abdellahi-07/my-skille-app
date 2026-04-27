import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="QCM · Machine Learning",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Questions ──────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "topic": "Fondements du ML",
        "icon": "⚙️",
        "color": "#38bdf8",
        "question": "Quelle est la différence fondamentale entre la programmation classique et le Machine Learning ?",
        "options": [
            "La programmation classique utilise des données, le ML n'en a pas besoin",
            "En ML, les règles sont apprises automatiquement à partir des données ; en programmation classique, elles sont écrites manuellement",
            "Le ML est toujours plus rapide à exécuter que la programmation classique",
            "La programmation classique ne peut traiter que du texte",
        ],
        "answer": 1,
        "explanation": "En programmation classique, le développeur écrit les règles explicitement. En ML, l'algorithme découvre les règles (patterns) automatiquement à partir des données.",
    },
    {
        "topic": "Vocabulaire ML",
        "icon": "📖",
        "color": "#a78bfa",
        "question": "Dans un problème d'apprentissage supervisé, que représente le label (y) ?",
        "options": [
            "Une variable d'entrée décrivant un exemple",
            "L'ensemble complet des données d'entraînement",
            "La valeur cible à prédire, fournie dans les données d'entraînement",
            "Le paramètre interne du modèle après entraînement",
        ],
        "answer": 2,
        "explanation": "Le label (y) est la valeur cible que le modèle doit apprendre à prédire. Il est fourni lors de l'entraînement mais absent lors de la prédiction sur de nouvelles données.",
    },
    {
        "topic": "Généralisation",
        "icon": "🎯",
        "color": "#34d399",
        "question": "Pourquoi la généralisation est-elle l'objectif ultime d'un modèle ML ?",
        "options": [
            "Pour obtenir un score parfait sur les données d'entraînement",
            "Pour réduire la taille du modèle et économiser de la mémoire",
            "Pour que le modèle performe bien sur des données nouvelles, jamais vues",
            "Pour accélérer l'entraînement du modèle",
        ],
        "answer": 2,
        "explanation": "Un modèle qui mémorise les données d'entraînement (overfitting) est inutile en production. La généralisation mesure la capacité à bien prédire sur de nouvelles données réelles.",
    },
    {
        "topic": "Types de tâches",
        "icon": "🏠",
        "color": "#fb923c",
        "question": "Un modèle prédit le prix d'un appartement selon sa superficie. De quel type de tâche s'agit-il ?",
        "options": [
            "Classification binaire",
            "Clustering non supervisé",
            "Régression",
            "Apprentissage par renforcement",
        ],
        "answer": 2,
        "explanation": "La régression prédit une valeur continue (ici un prix ∈ ℝ). La classification prédit une catégorie discrète (spam/non-spam, malade/sain…).",
    },
    {
        "topic": "Pipeline ML",
        "icon": "⏱️",
        "color": "#f472b6",
        "question": "Quelle étape du pipeline ML consomme approximativement 80 % du temps réel d'un projet ?",
        "options": [
            "La modélisation et le choix d'algorithme",
            "Le déploiement en production",
            "La collecte, le nettoyage et l'exploration des données",
            "L'évaluation des performances du modèle",
        ],
        "answer": 2,
        "explanation": "La réalité du ML professionnel : 80 % du temps est consacré aux données (collecte, nettoyage, exploration), et seulement 20 % à la modélisation.",
    },
    {
        "topic": "Régression vs Classification",
        "icon": "📊",
        "color": "#38bdf8",
        "question": "Quelle est la différence entre régression et classification en apprentissage supervisé ?",
        "options": [
            "La régression nécessite toujours plus de données que la classification",
            "La régression prédit une valeur continue (y ∈ ℝ), la classification prédit une catégorie discrète",
            "La classification est toujours plus précise que la régression",
            "La régression est non-supervisée, la classification est supervisée",
        ],
        "answer": 1,
        "explanation": "Régression → sortie continue (prix, température). Classification → sortie discrète (spam/non-spam, bénigne/maligne). Les deux sont des tâches supervisées.",
    },
    {
        "topic": "Apprentissage non supervisé",
        "icon": "🔍",
        "color": "#a78bfa",
        "question": "Lequel de ces problèmes relève de l'apprentissage NON supervisé ?",
        "options": [
            "Détecter si un email est un spam",
            "Prédire si une tumeur est bénigne ou maligne",
            "Segmenter des clients en groupes selon leurs comportements d'achat",
            "Prédire le cours d'une action boursière",
        ],
        "answer": 2,
        "explanation": "La segmentation (clustering) ne nécessite pas de labels. L'algorithme découvre lui-même des groupes cachés dans les données X, sans valeur cible y.",
    },
    {
        "topic": "Renforcement",
        "icon": "♟️",
        "color": "#34d399",
        "question": "AlphaGo apprend à jouer au Go. Quel type d'apprentissage est utilisé ?",
        "options": [
            "Supervisé — il apprend des parties d'experts humains",
            "Non supervisé — il regroupe des stratégies similaires",
            "Par renforcement — il apprend par essais/erreurs en maximisant une récompense",
            "Semi-supervisé — il combine labels et données non étiquetées",
        ],
        "answer": 2,
        "explanation": "L'apprentissage par renforcement : un agent apprend par essais/erreurs. Gagner = récompense positive. AlphaGo a joué des millions de parties contre lui-même pour s'améliorer.",
    },
    {
        "topic": "Dataset",
        "icon": "🗃️",
        "color": "#fb923c",
        "question": "Qu'est-ce qu'un dataset (jeu de données) en ML ?",
        "options": [
            "L'algorithme utilisé pour entraîner le modèle",
            "Les paramètres internes du modèle (poids)",
            "Un ensemble structuré d'exemples utilisés pour entraîner ou évaluer un modèle",
            "Le résultat final produit par la prédiction",
        ],
        "answer": 2,
        "explanation": "Un dataset est une collection d'exemples (lignes) avec leurs features (colonnes X) et éventuellement leurs labels (y), utilisée pour l'entraînement et l'évaluation.",
    },
    {
        "topic": "Train / Test Split",
        "icon": "✂️",
        "color": "#f472b6",
        "question": "Pourquoi sépare-t-on les données en ensemble d'entraînement et ensemble de test ?",
        "options": [
            "Pour réduire la taille du dataset et accélérer l'entraînement",
            "Pour évaluer objectivement la généralisation sur des données non vues",
            "Parce que le modèle ne peut pas traiter toutes les données à la fois",
            "Pour satisfaire une obligation légale sur les données",
        ],
        "answer": 1,
        "explanation": "Le test set simule de nouvelles données inconnues, permettant d'évaluer la vraie capacité de généralisation du modèle sans biais.",
    },
    {
        "topic": "Overfitting",
        "icon": "📉",
        "color": "#38bdf8",
        "question": "Qu'est-ce que l'overfitting (sur-apprentissage) ?",
        "options": [
            "Le modèle ne converge pas pendant l'entraînement",
            "Le modèle mémorise les données d'entraînement mais généralise mal sur de nouvelles données",
            "Le modèle est trop simple pour capturer les patterns des données",
            "Le modèle prend trop de temps à s'entraîner",
        ],
        "answer": 1,
        "explanation": "L'overfitting = excellent sur train, mauvais sur test. Le modèle a mémorisé le bruit des données au lieu d'apprendre les vrais patterns. C'est l'ennemi de la généralisation.",
    },
    {
        "topic": "Notation mathématique",
        "icon": "🔢",
        "color": "#a78bfa",
        "question": "Dans la notation f(X) → ŷ, que représente ŷ (y-chapeau) ?",
        "options": [
            "La valeur réelle du label dans les données",
            "La valeur prédite par le modèle",
            "L'erreur commise par le modèle",
            "La moyenne des valeurs du dataset",
        ],
        "answer": 1,
        "explanation": "ŷ (y-hat) est la valeur prédite par le modèle f(X). On compare ŷ à y (la vraie valeur) pour mesurer l'erreur du modèle lors de l'évaluation.",
    },
    {
        "topic": "Ordre du Pipeline",
        "icon": "🔄",
        "color": "#34d399",
        "question": "Quelle étape précède immédiatement la modélisation dans le pipeline ML ?",
        "options": [
            "Le déploiement en production",
            "L'évaluation des performances",
            "L'exploration — visualisation et compréhension des distributions",
            "La mise en monitoring",
        ],
        "answer": 2,
        "explanation": "Ordre du pipeline : Collecte → Nettoyage → Exploration (EDA) → Modélisation → Évaluation → Déploiement. L'exploration précède toujours la modélisation.",
    },
    {
        "topic": "Avantage du ML",
        "icon": "💡",
        "color": "#fb923c",
        "question": "Un filtre spam basé sur des règles manuelles est remplacé par un modèle ML. Quel est l'avantage principal ?",
        "options": [
            "Le modèle ML est plus simple à implémenter",
            "Le modèle ML peut capturer des patterns complexes invisibles aux règles manuelles",
            "Le modèle ML consomme moins de ressources informatiques",
            "Le modèle ML ne nécessite aucune donnée d'entraînement",
        ],
        "answer": 1,
        "explanation": "Les règles manuelles sont limitées et rigides. Le ML peut capturer des milliers de patterns complexes (combinaisons de mots, fréquences, expéditeurs…) impossibles à écrire à la main.",
    },
    {
        "topic": "Nettoyage des données",
        "icon": "🧹",
        "color": "#f472b6",
        "question": "Qu'est-ce que l'étape de nettoyage (preprocessing) dans le pipeline ML ?",
        "options": [
            "Choisir le meilleur algorithme de ML pour la tâche",
            "Visualiser les distributions et corrélations des features",
            "Gérer les valeurs manquantes, les outliers et les doublons",
            "Déployer le modèle en production et le monitorer",
        ],
        "answer": 2,
        "explanation": "Le nettoyage traite les valeurs manquantes (imputation/suppression), les outliers (valeurs aberrantes) et les doublons pour obtenir des données de qualité.",
    },
    {
        "topic": "Dimensionnalité",
        "icon": "📐",
        "color": "#38bdf8",
        "question": "La réduction de dimensionnalité (ex: PCA) appartient à quel type d'apprentissage ?",
        "options": [
            "Supervisé — car elle utilise les labels pour réduire les dimensions",
            "Par renforcement — car elle optimise une récompense",
            "Non supervisé — car elle trouve des structures cachées sans labels",
            "Semi-supervisé — car elle combine labels et données non étiquetées",
        ],
        "answer": 2,
        "explanation": "La réduction de dimensionnalité (PCA, t-SNE…) cherche des structures dans X sans utiliser y. C'est de l'apprentissage non supervisé, comme le clustering.",
    },
    {
        "topic": "Déploiement & Monitoring",
        "icon": "📡",
        "color": "#a78bfa",
        "question": "Pourquoi le monitoring est-il crucial après le déploiement d'un modèle ML ?",
        "options": [
            "Pour réentraîner le modèle chaque heure automatiquement",
            "Pour détecter le data drift — les performances se dégradent si la distribution des données change",
            "Pour afficher des statistiques visuelles à l'utilisateur final",
            "Pour respecter les exigences légales de publication",
        ],
        "answer": 1,
        "explanation": "Le 'data drift' : les données réelles évoluent avec le temps. Un modèle performant en janvier peut devenir mauvais en décembre. Le monitoring détecte cette dégradation.",
    },
    {
        "topic": "Application bancaire",
        "icon": "🏦",
        "color": "#34d399",
        "question": "Une banque veut détecter des transactions frauduleuses. C'est un exemple de :",
        "options": [
            "Régression — car on prédit le montant de la fraude",
            "Clustering — car on groupe les transactions similaires",
            "Classification — car on prédit fraude (1) ou non-fraude (0)",
            "Renforcement — car le système s'améliore avec le temps",
        ],
        "answer": 2,
        "explanation": "Détecter une fraude = prédire une classe binaire : frauduleux (1) ou légitime (0). C'est une classification binaire supervisée nécessitant des exemples historiques étiquetés.",
    },
    {
        "topic": "Entraînement",
        "icon": "🏋️",
        "color": "#fb923c",
        "question": "Qu'apprend réellement un modèle ML lors de la phase d'entraînement ?",
        "options": [
            "Il mémorise toutes les lignes du dataset",
            "Il ajuste ses paramètres internes pour minimiser l'erreur entre ŷ et y",
            "Il télécharge des règles depuis Internet",
            "Il copie les règles écrites par le développeur",
        ],
        "answer": 1,
        "explanation": "L'entraînement = optimisation des paramètres (poids) du modèle pour minimiser une fonction de perte (loss). Plus l'erreur |y − ŷ| est petite, meilleur est le modèle.",
    },
    {
        "topic": "Évaluation honnête",
        "icon": "⚠️",
        "color": "#f472b6",
        "question": "Quel est le risque si on évalue un modèle uniquement sur ses données d'entraînement ?",
        "options": [
            "L'évaluation sera trop lente et coûteuse en calcul",
            "On obtiendra des métriques trop pessimistes",
            "On obtiendra des métriques trop optimistes — le modèle a déjà vu ces données",
            "Il n'y a aucun risque, c'est une pratique recommandée",
        ],
        "answer": 2,
        "explanation": "Évaluer sur les données d'entraînement = tricher (data leakage). Le modèle les a déjà mémorisées → score artificiellement élevé qui ne reflète pas la vraie performance.",
    },
]

# ── Session state init ─────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "q_index": 0,
        "score": 0,
        "answered": False,
        "selected": None,
        "finished": False,
        "wrong_list": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

LETTERS = ["A", "B", "C", "D"]
TOTAL   = len(QUESTIONS)

# ── Global styles ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"], .stApp {
    font-family: 'Syne', sans-serif !important;
    background: #07090f !important;
    color: #e0e8ff !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 1rem 5rem !important; max-width: 760px !important; }

/* ── progress ── */
.prog-track {
    width: 100%; height: 5px;
    background: rgba(255,255,255,0.07);
    border-radius: 99px; overflow: hidden;
    margin-bottom: 30px;
}
.prog-fill { height: 100%; border-radius: 99px; transition: width .5s ease; }

/* ── header row ── */
.hdr-row {
    display: flex; align-items: center;
    justify-content: space-between;
    margin-bottom: 18px;
}
.badge {
    display: inline-flex; align-items: center; gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem; letter-spacing: 2px; text-transform: uppercase;
    padding: 5px 13px; border-radius: 99px; border: 1px solid;
}
.counter {
    font-family: 'DM Mono', monospace; font-size: 0.72rem; color: #3a4460;
}

/* ── score mini ── */
.score-mini {
    font-family: 'DM Mono', monospace; font-size: 0.72rem;
    color: #3a4460; text-align: right; margin-bottom: 4px;
}

/* ── question text ── */
.q-text {
    font-size: 1.22rem; font-weight: 700; line-height: 1.55;
    color: #f0f4ff; margin-bottom: 30px;
}

/* ── option buttons (rendered via st.button) ── */
.stButton > button {
    width: 100% !important;
    text-align: left !important;
    padding: 14px 20px !important;
    border-radius: 14px !important;
    border: 1.5px solid rgba(255,255,255,0.1) !important;
    background: rgba(255,255,255,0.04) !important;
    color: #c8d2f0 !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.93rem !important;
    font-weight: 500 !important;
    margin-bottom: 2px !important;
    cursor: pointer !important;
    transition: all 0.18s !important;
    letter-spacing: 0.1px !important;
    justify-content: flex-start !important;
}
.stButton > button:hover {
    background: rgba(255,255,255,0.09) !important;
    border-color: rgba(255,255,255,0.25) !important;
    color: #fff !important;
}

/* ── reviewed options (HTML divs) ── */
.opt {
    width: 100%;
    padding: 14px 20px;
    border-radius: 14px;
    border: 1.5px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.04);
    color: #c8d2f0;
    font-size: 0.93rem;
    margin-bottom: 8px;
    display: flex; align-items: center; gap: 12px;
}
.opt-correct { background: rgba(52,211,153,0.12) !important; border-color: #34d399 !important; color: #34d399 !important; font-weight: 700; }
.opt-wrong   { background: rgba(248,113,113,0.12) !important; border-color: #f87171 !important; color: #f87171 !important; font-weight: 700; }
.opt-dim     { opacity: 0.35; }

.ltr {
    width: 28px; height: 28px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace; font-size: 0.72rem; font-weight: 600;
    background: rgba(255,255,255,0.07); flex-shrink: 0;
}

/* ── feedback ── */
.fb {
    padding: 16px 20px; border-radius: 14px;
    margin-top: 18px; font-size: 0.88rem; line-height: 1.65;
    border-left: 4px solid;
}
.fb-ok  { background: rgba(52,211,153,0.09);  border-color: #34d399; color: #a7f3d0; }
.fb-err { background: rgba(248,113,113,0.09); border-color: #f87171; color: #fecaca; }

/* ── next / finish button ── */
.next-wrap > .stButton > button {
    background: linear-gradient(135deg,#6366f1,#38bdf8) !important;
    color: #fff !important; font-weight: 700 !important;
    font-size: 0.97rem !important; letter-spacing: 0.4px !important;
    border: none !important; border-radius: 14px !important;
    padding: 14px 28px !important; margin-top: 14px !important;
}
.next-wrap > .stButton > button:hover { opacity: 0.85 !important; }

/* ── score card ── */
.score-card {
    border-radius: 24px; padding: 50px 32px 40px;
    text-align: center;
    background: linear-gradient(145deg,#0d1525,#131e35);
    border: 1px solid rgba(255,255,255,0.08);
}
.s-num  { font-size: 5.5rem; font-weight: 800; font-family: 'DM Mono', monospace; line-height: 1; }
.s-pct  { font-size: 1.6rem; font-weight: 700; color: #e0e8ff; margin-top: 10px; }
.s-lbl  { font-size: 0.9rem; color: #64748b; margin-top: 6px; }
.s-grid { display: flex; justify-content: center; gap: 48px; flex-wrap: wrap; margin-top: 28px; }
.s-stat { text-align: center; }
.s-stat-n { font-size: 1.8rem; font-weight: 800; font-family: 'DM Mono', monospace; }
.s-stat-l { font-size: 0.7rem; letter-spacing: 2px; text-transform: uppercase; color: #3a4460; margin-top: 2px; }

.div-line { border: none; border-top: 1px solid rgba(255,255,255,0.07); margin: 28px 0; }

/* wrong list */
.wrong-item {
    background: rgba(248,113,113,0.06); border: 1px solid rgba(248,113,113,0.18);
    border-radius: 12px; padding: 14px 18px; margin-bottom: 10px;
    font-size: 0.87rem; color: #fca5a5; line-height: 1.55;
}
.wrong-q { color: #e0e8ff; margin-bottom: 5px; font-weight: 600; }
.wrong-a { color: #a7f3d0; }

/* restart button */
.restart-wrap > .stButton > button {
    background: rgba(255,255,255,0.06) !important;
    border: 1.5px solid rgba(255,255,255,0.15) !important;
    color: #a0aec8 !important; font-weight: 600 !important;
    border-radius: 14px !important; padding: 13px 28px !important;
    margin-top: 14px !important;
}
.restart-wrap > .stButton > button:hover {
    background: rgba(255,255,255,0.12) !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  FINISHED SCREEN
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.finished:
    score = st.session_state.score
    pct   = int(score / TOTAL * 100)

    if pct >= 80:
        color = "#34d399"; icon = "🏆"; label = "Maîtrise excellente !"
    elif pct >= 60:
        color = "#38bdf8"; icon = "✨"; label = "Bonne compréhension"
    elif pct >= 40:
        color = "#fb923c"; icon = "📚"; label = "À consolider"
    else:
        color = "#f87171"; icon = "🔄"; label = "Reprenez le cours"

    st.markdown(f"""
    <div class="score-card">
        <div style="font-size:3.2rem;margin-bottom:16px;">{icon}</div>
        <div class="s-num" style="color:{color};">
            {score}<span style="font-size:2rem;color:#2a3450;">/{TOTAL}</span>
        </div>
        <div class="s-pct">{pct} %</div>
        <div class="s-lbl">{label}</div>
        <hr class="div-line">
        <div class="s-grid">
            <div class="s-stat">
                <div class="s-stat-n" style="color:#34d399;">{score}</div>
                <div class="s-stat-l">Correctes</div>
            </div>
            <div class="s-stat">
                <div class="s-stat-n" style="color:#f87171;">{TOTAL - score}</div>
                <div class="s-stat-l">Incorrectes</div>
            </div>
            <div class="s-stat">
                <div class="s-stat-n" style="color:#38bdf8;">{TOTAL}</div>
                <div class="s-stat-l">Questions</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.wrong_list:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:1rem;font-weight:700;color:#f0f4ff;margin-bottom:14px;'>❌ Questions à retravailler</div>", unsafe_allow_html=True)
        for w in st.session_state.wrong_list:
            q = QUESTIONS[w["idx"]]
            st.markdown(f"""
            <div class="wrong-item">
                <div style="font-size:0.72rem;color:#6b7a9e;font-family:'DM Mono',monospace;
                            letter-spacing:1px;text-transform:uppercase;margin-bottom:5px;">
                    {q['icon']} {q['topic']}
                </div>
                <div class="wrong-q">{q['question']}</div>
                <div class="wrong-a">✅ {LETTERS[q['answer']]}. {q['options'][q['answer']]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="restart-wrap">', unsafe_allow_html=True)
    if st.button("🔄  Recommencer le quiz"):
        for k in ["q_index","score","answered","selected","finished","wrong_list"]:
            del st.session_state[k]
        init_state()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  QUIZ SCREEN
# ══════════════════════════════════════════════════════════════════════════════
else:
    idx      = st.session_state.q_index
    q        = QUESTIONS[idx]
    acc      = q["color"]
    answered = st.session_state.answered
    selected = st.session_state.selected
    correct  = q["answer"]
    pct_fill = int(idx / TOTAL * 100)

    # ── progress bar ──
    st.markdown(f"""
    <div class="prog-track">
        <div class="prog-fill" style="width:{pct_fill}%;background:{acc};"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── header row ──
    score_now = st.session_state.score
    st.markdown(f"""
    <div class="hdr-row">
        <div class="badge" style="color:{acc};border-color:{acc}45;background:{acc}12;">
            {q['icon']} {q['topic']}
        </div>
        <div style="text-align:right;">
            <div class="counter">{idx+1} / {TOTAL}</div>
            <div class="score-mini">✅ {score_now} pts</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── question text ──
    st.markdown(f'<div class="q-text">{q["question"]}</div>', unsafe_allow_html=True)

    # ── options ──
    if not answered:
        for i, opt in enumerate(q["options"]):
            ltr = LETTERS[i]
            if st.button(f"{ltr}.  {opt}", key=f"opt_{idx}_{i}"):
                st.session_state.selected = i
                st.session_state.answered = True
                if i == correct:
                    st.session_state.score += 1
                else:
                    st.session_state.wrong_list.append({"idx": idx, "chosen": i})
                st.rerun()
    else:
        for i, opt in enumerate(q["options"]):
            ltr = LETTERS[i]
            if i == correct:
                css = "opt opt-correct"
                sym = "✓"
            elif i == selected and i != correct:
                css = "opt opt-wrong"
                sym = "✗"
            else:
                css = "opt opt-dim"
                sym = ltr
            st.markdown(f"""
            <div class="{css}">
                <span class="ltr">{sym}</span>{opt}
            </div>
            """, unsafe_allow_html=True)

        # ── feedback ──
        is_ok = selected == correct
        if is_ok:
            st.markdown(f"""
            <div class="fb fb-ok">
                <strong>✅ Correct !</strong><br>{q['explanation']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="fb fb-err">
                <strong>❌ Incorrect.</strong>
                Bonne réponse : <strong>{LETTERS[correct]}. {q['options'][correct]}</strong><br><br>
                {q['explanation']}
            </div>
            """, unsafe_allow_html=True)

        # ── next / finish ──
        st.markdown("<br>", unsafe_allow_html=True)
        is_last = (idx == TOTAL - 1)
        lbl = "🏁  Voir mes résultats" if is_last else "Question suivante →"
        st.markdown('<div class="next-wrap">', unsafe_allow_html=True)
        if st.button(lbl, key="next_btn"):
            if is_last:
                st.session_state.finished = True
            else:
                st.session_state.q_index  += 1
                st.session_state.answered  = False
                st.session_state.selected  = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)