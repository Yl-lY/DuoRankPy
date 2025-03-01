import functions as func
import pandas as pd
import streamlit as st
import local_save as save

save.pegar_competidores()

page_icon = 'https://techcrunch.com/wp-content/uploads/2025/01/duolingo-owl.png'

st.set_page_config(page_title='Duolingo Rank', page_icon=page_icon, layout="centered")
st.title("Ranking de Competidores 🏆")

carregar = save.pegar_competidores()
competitors = carregar

if st.button("Adicionar João"):
    # if competitors != {}:
    #     for user, lang in competitors.items():
    #         func.include_competitor(user, lang)
    #     st.success("Lista atualizada!")
    # else:
    #     st.error("Lista sem competidores..")
    sucess = save.adicionar_na_lista('joaozingam1', 'Chinese')
    if sucess:
        st.success("João adicionado!")
    else:
        st.error("João já está na lista..")


competitors = func.get_competitors()

if competitors:
    df = pd.DataFrame(competitors, columns=["Nome", "Avatar", "Display Name", "Lingua", "XP"])

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
