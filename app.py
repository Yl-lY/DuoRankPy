import functions as func
import pandas as pd
import streamlit as st

st.title("Ranking de Competidores 🏆")

if st.button("Atualizar Lista"):
    for user, lang in {
        'ianearcolezi': 'Greek',
        'joaozingam1': 'Chinese',
        'julianolima.py': 'English',
        'MelissaBra949315': 'Italian',
        'Thalys187940': 'Korean'
    }.items():
        func.include_competitor(user, lang)
    st.success("Lista atualizada!")

competitors = func.get_competitors()

if competitors:
    df = pd.DataFrame(competitors, columns=["Nome", "Avatar", "Display Name", "Língua", "XP"])

    st.dataframe(
        df.sort_values(by="XP", ascending=False),
        column_config={
            "Nome": "Nome",
            "Avatar": st.column_config.ImageColumn(
                label="",
                help="Avatar do usuário",
                pinned=True,
                width="small"
            ),
            "Display Name": "Nome de Exibição",
            "Língua": "Idioma",
            "XP": "Experiência",
        },
        hide_index=True,
    )
else:
    st.write("Nenhum competidor cadastrado.")
