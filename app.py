import streamlit as st

# Titre de la page
st.title("🍏 Suivi des déchets de la cantine")
st.write("Bienvenue sur l'application de la CDSG du Vaucluse.")
st.write("Saisissez le poids des déchets pour chaque catégorie (en kg) :")

# Poubelles de saisie
dechets_pain = st.number_input("🍞 Déchets de Pain (kg)", min_value=0.0, step=0.1)
dechets_alimentaires = st.number_input("🍲 Déchets Alimentaires / Reste des plateaux (kg)", min_value=0.0, step=0.1)
dechets_papier = st.number_input("🧻 Serviettes en papier (kg)", min_value=0.0, step=0.1)
dechets_emballage = st.number_input("📦 Emballages (yaourts, plastiques...) (kg)", min_value=0.0, step=0.1)
dechets_fruits = st.number_input("🍎 Fruits entamés (kg)", min_value=0.0, step=0.1)

st.divider()

# Bouton de calcul
if st.button("Calculer le total des déchets"):
    total = dechets_pain + dechets_alimentaires + dechets_papier + dechets_emballage + dechets_fruits
    st.success(f"📊 Le total des déchets aujourd'hui est de : **{total:.2f} kg**")
