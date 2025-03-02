import functions as func
import pandas as pd
import streamlit as st
import local_save as save

# save.pegar_competidores()

page_icon = 'https://techcrunch.com/wp-content/uploads/2025/01/duolingo-owl.png'

st.set_page_config(page_title='Duolingo Rank', page_icon=page_icon, layout="wide")


linguas = func.collect_languages()


carregar = save.pegar_competidores()
competitors = carregar

colleft, coltitle, colright = st.container().columns([3, 8, 3]) 
with coltitle:
    st.title("🏆 Ranking de competidores")

container = st.container()
col1, col2, col3, = container.columns([1, 3, 1])



with col1:
    username = st.text_input('Nome do Participante', placeholder='Usuário')
    lingua = st.selectbox("Qual idioma escolhido?", list(func.bandeiras.keys()))
with col3:
    if st.button('Adicionar competidor'):
        sucess = save.adicionar_na_lista(username, lingua)
        if sucess:
            st.success(str(f"{username} Adicionado com sucesso!"), icon='✅')
            save.atualizar_rank()
        elif sucess == None:
            st.error(str(f'{username} não é um usuário válido!'), icon='❗️')
        else:
            st.warning(str(f"{username} já está na lista.."), icon='🤝🏽')

    if st.button("Atualizar Rank"):
        if competitors != []:
            save.atualizar_rank()
            st.success("Lista atualizada!", icon='♻️')
        else:
            st.error("Lista sem competidores..")

# competitors = func.get_competitors()
with col2:
    if competitors:
        df = pd.DataFrame(competitors, columns=save.cabecalho)

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

if username:
    st.info('Não confie no input, dar Enter não vai fazer nada..', icon='👀')
    
