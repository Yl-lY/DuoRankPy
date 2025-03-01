import functions as func
import pandas as pd
import streamlit as st
import local_save as save

# save.pegar_competidores()

page_icon = 'https://techcrunch.com/wp-content/uploads/2025/01/duolingo-owl.png'

st.set_page_config(page_title='Duolingo Rank', page_icon=page_icon, layout="centered")
st.title("Ranking de Competidores 🏆")

linguas = func.collect_languages()
print(len(linguas))

carregar = save.pegar_competidores()
competitors = carregar

if st.button("Atualizar Rank"):
    if competitors != []:
        save.atualizar_rank()
        st.success("Lista atualizada!")
    else:
        st.error("Lista sem competidores..")
    # sucess = save.adicionar_na_lista('joaozingam1', 'Chinese')
    # if sucess:
    #     st.success("João adicionado!")
    # else:
    #     st.error("João já está na lista..")


# competitors = func.get_competitors()

if competitors:
    df = pd.DataFrame(competitors, columns=save.cabecalho)
    
    # df['Lingua'] = df["Lingua"].apply(lambda x: f'<image src="{func.get_bandeiras(x)}" width="20"> ')

    st.dataframe(
        df.sort_values(by="XP", key=lambda x: x.astype(int), ascending=False),
        column_config={
            "Nome": st.column_config.TextColumn(
                label="Nome",
                help="Nome de usuário",
            ),
            "Avatar": st.column_config.ImageColumn(
                label="",
                help="Avatar do usuário",
                pinned=True,
                width="small"
            ),
            "Display Name": st.column_config.TextColumn(
                label="Nickname",
                help="Nome exibido",
            ),
            "Bandeira": st.column_config.ImageColumn(
                label='',
                width='small'
            ),
            "Idioma": "Idioma",
            "XP": st.column_config.NumberColumn(
                label="⭐️Experiência",
                help="Experiência na lingua escolhida"
            ),
            "STREAK": "🔥Streak"
        },
        hide_index=True,
    )
else:
    st.write("Nenhum competidor cadastrado.")
