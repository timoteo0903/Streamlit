import streamlit as st
import pickle
import pandas as pd
with open('Pipe.pkl', 'rb') as Pipeline:
    Pipe = pickle.load(Pipeline)
def classify(num):
    if num == 0:
        return 'No sobrevives'
    else:
        return 'Sobrevives'

def main():
    #titulo
    st.title('Holaaaa! Veamos si hubieses sobrevivido al Titanic o no.')
    #titulo de sidebar
    st.sidebar.header('User Input Parameters')
    def user_input_parameters():
        ticket_class = st.text_input('Ticket Class')
        name = st.text_input('Name')
        sex = st.text_input('Sex')
        age = st.number_input('Age', min_value = 0)
        siblings_spouses = st.number_input('Hermanos o Esposa')
        parents_children = st.number_input('Hijos o padres')
        fare = st.number_input('Precio')
        data = {
            'Ticket Class':ticket_class,
            'Name':name,
            'Sex': sex,
            'Age':age,
            'Hermanos o Esposa': siblings_spouses,
            'Hijos o padres': parents_children,
            'Precio': fare}
        features = pd.DataFrame(data, index=[0])
        return features
    df = user_input_parameters()
    model = Pipe
    st.subheader('User Input Parameters')
    st.subheader(model)
    st.write(df)
    if st.button('RUN'):
        st.success(classify(GB.predict(df)))
if __name__ == '__main__':
    main()