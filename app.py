import streamlit as st
from streamlit_option_menu import option_menu
# pip install streamlit-option-menu

# 1. 사이드바 메뉴
# with st.sidebar :
    # selected = option_menu(
    #     menu_title='GPU Compare', # 필요하지 않으면 None
    #     options=['Home', 'About'], # 메뉴 타이틀의 하위 메뉴를 생성
    #     icons=['house-fill', 'info'], # bootstrap에서 해당하는 아이콘을 가져옴
    #     menu_icon= 'justify', # 메뉴타이틀의 아이콘 역시 설정가능
    #     default_index=0 # 앱을 열었을때 기본이 되게 선택할수있음
    #     )

# https://github.com/victoryhb/streamlit-option-menu

# 2. 수평 메뉴
# selected = option_menu(
#     menu_title=None, # 필요하지 않으면 None !필수
#     options=['Home', 'About'], # 메뉴 타이틀의 하위 메뉴를 생성 !필수
#     icons=['house-fill', 'info'], # bootstrap에서 해당하는 아이콘을 가져옴 !옵션
#     menu_icon= 'justify', # 메뉴타이틀의 아이콘 역시 설정가능 !옵션
#     default_index=0, # 앱을 열었을때 기본이 되게 선택할수있음 !옵션
#     orientation='horizontal' #수평 으로 메뉴를 설정할수있음
#     # styles= 을 이용할수있음
#     )


# if selected == 'Home' :
#     st.title(f'You have selected {selected}')
# if selected == 'About' :
#     st.title(f'You have selected {selected}')
# https://www.youtube.com/watch?v=saOv9z6Fk88

# def clean_text(text) :
#     text = text.replace("`", "").replace("-\n", "").replace("\n", " ").replace("#", "/").strip()
#     return (text)

st.title('dsds')
st.sidebar.header('Options')
st.sidebar.subheader('이것은 테스트입니다')
st.sidebar.text('이것은 테스트입니다.')
text = st.sidebar.text_area('Paste Text Here')
# st.write(text)
button1 = st.sidebar.button('Clean Text')
if button1 :
    col1, col2 = st.columns(2)
    col1.header('orgin')
    col1.write(text)

    col2.header('clean')
    clean = clean_text(text)
    col2.write(clean)