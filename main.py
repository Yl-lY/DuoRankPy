import functions as func
import pandas as pd
import streamlit as st

# Estilização de ícones e imagens da página #
page_icon = 'https://techcrunch.com/wp-content/uploads/2025/01/duolingo-owl.png'

st.set_page_config(page_title='Duolingo Rank', page_icon=page_icon, layout="wide")
st.logo('https://images.cults3d.com/h2AL3aObyStbXlc706uekBr1y5c=/516x516/filters:no_upscale()/https://fbi.cults3d.com/uploaders/29241666/illustration-file/119d67c6-bbdd-49d5-ab08-c9ad7b049476/You-Missed-your-SPANISH-lesson-Duolingo-2.png', size='large')
#############################################

# Carregando as línguas oferecidas pelo Duolingo #
linguas = func.collect_languages()
##################################################

#  Puxando os dados do BD  #
carregar = func.get_competitors()
competitors = carregar
############################

colleft, colimage, coltitle, colright = st.container().columns([4.5, 2, 13, 3])
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
        sucess = func.insert_competitor(username, lingua)
        if sucess == True:
            st.toast(str(f"{username} Adicionado com sucesso!"), icon='✅')
            func.atualizar_rank()
            st.rerun()
        elif sucess == None:
            st.toast(str(f'{username} não existe!'), icon='❗️')
        elif sucess == False:
            st.toast(str(f"{username} já está na lista.."), icon='🤝🏽')
        elif sucess == '':
            st.toast('Língua não selecionada!', icon='🧐')
      

    if st.button("Atualizar Rank", icon='🌐'):
        if competitors != []:
            func.atualizar_rank()
            st.rerun()
            st.toast("Lista atualizada!", icon='♻️')
        else:
            st.toast("Lista sem competidores..", icon='🫥')


with col2:
    if competitors:
        df = pd.DataFrame(competitors)

        st.dataframe(
            data = df.sort_values(by="xp", key=lambda x: x.astype(int), ascending=False),
            use_container_width= True,
            column_config={
                "name": st.column_config.TextColumn(
                    label="Nome",
                    help="Nome de usuário",
                    disabled=False
                ),
                "avatar": st.column_config.ImageColumn(
                    label="",
                    help="Avatar do usuário",
                    pinned=True,
                    width="small"
                ),
                "display_name": st.column_config.TextColumn(
                    label="Nickname",
                    help="Nome exibido",
                ),
                "flag": st.column_config.ImageColumn(
                    label='',
                    width='small'
                ),
                "language": "Idioma",
                "xp": st.column_config.NumberColumn(
                    label="⭐️Experiência",
                    help="Experiência na lingua escolhida"
                ),
                "streak": "🔥Streak"
            },
            hide_index=True,
        )
    else:
        st.write("Nenhum competidor cadastrado.")

if username:
    col1, col2, col3 = st.columns([4, 5, 4])
    with col2:
        st.info('Não confie no input, dar Enter não vai fazer nada..', icon='💡')

    
