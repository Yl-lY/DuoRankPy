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

colleft, colimage, coltitle, colright = st.container().columns([4.5, 2, 13, 3])
st.logo('https://images.cults3d.com/h2AL3aObyStbXlc706uekBr1y5c=/516x516/filters:no_upscale()/https://fbi.cults3d.com/uploaders/29241666/illustration-file/119d67c6-bbdd-49d5-ab08-c9ad7b049476/You-Missed-your-SPANISH-lesson-Duolingo-2.png', size='large')
with colimage:
    st.image('https://pbs.twimg.com/media/FXZhKUUXEAM_BVA.png', use_container_width=True)
with coltitle:
    st.title("Ranking de competidores")

container = st.container()
col1, col2, col3, = container.columns([1, 3, 1])



with col1:
    username = st.text_input('Nome do Participante', label_visibility='collapsed', placeholder='Usuário')
    lingua = st.selectbox("Qual idioma escolhido?", list(func.bandeiras.keys()), placeholder='Du iu spiki inglix?', index=None)
with col3:
    if st.button('Adicionar competidor', icon='➕'):
        sucess = save.adicionar_na_lista(username, lingua)
        if sucess == True:
            st.toast(str(f"{username} Adicionado com sucesso!"), icon='✅')
            save.atualizar_rank()
        elif sucess == None:
            st.toast(str(f'Usuário inválido ou Idioma não selecionado!'), icon='❗️')
        elif sucess == False:
            st.toast(str(f"{username} já está na lista.."), icon='🤝🏽')
        elif sucess == '':
            st.toast('Língua não selecionada!', icon='🧐')
      

    if st.button("Atualizar Rank", icon='🌐'):
        if competitors != []:
            save.atualizar_rank()
            st.toast("Lista atualizada!", icon='♻️')
        else:
            st.toast("Lista sem competidores..", icon='🫥')

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
    col1, col2, col3 = st.columns([4, 5, 4])
    with col2:
        st.info('Não confie no input, dar Enter não vai fazer nada..', icon='💡')

    
