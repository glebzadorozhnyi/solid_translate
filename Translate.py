import streamlit as st

@st.cache_data
def get_alphabtes():
    solid_alphabet_big = 'ÀÁÂÃÄÅ¨ÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß'
    solid_alphabet_small = 'àáâãäå¸æçèéêëìíîïðñòóôõö÷øùúûüýþÿ'
    normal_alphabet_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    normal_alphabet_small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return solid_alphabet_big, solid_alphabet_small, normal_alphabet_big, normal_alphabet_small

@st.cache_data
def translate(text, solid_alphabet_big, solid_alphabet_small, normal_alphabet_big, normal_alphabet_small):
    translated_string = str()
    for j in text:
        if j in solid_alphabet_big:
            translated_string += normal_alphabet_big[solid_alphabet_big.find(j)]
        elif j in solid_alphabet_small:
            translated_string += normal_alphabet_small[solid_alphabet_small.find(j)]
        else:
            translated_string += j
    return translated_string

@st.cache_data
def font_style():
    st.markdown("""
    <style>
    .big-font {
        font-size:14px !important;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":

    st.set_page_config("Переводчик с Солидворковского")

    font_style()
    st.title('Áîáûøêà -> Бобышка')

    solid_alphabet_big, solid_alphabet_small, normal_alphabet_big, normal_alphabet_small = get_alphabtes()

    st.text_area(label = 'Скопируйте сюда текст из SolidWorks', value="", key='input_text', placeholder='Скопируйте сюда текст из SolidWorks')

    text_output = translate(st.session_state['input_text'], solid_alphabet_big, solid_alphabet_small, normal_alphabet_big, normal_alphabet_small)

    st.markdown('<p class="big-font">Потом нажмите на окошко ниже. Справа у окошка есть кнопочка Скопировать</p>', unsafe_allow_html=True)
    st.code(text_output if len(text_output) > 0 else 'Потом нажмите на это ниже. Справа у окошка есть кнопочка Скопировать', line_numbers=False, language='None')
