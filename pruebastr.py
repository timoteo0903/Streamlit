import streamlit as st
import pickle
import pandas as pd
with open('GB.pkl', 'rb') as GBoost:
    GB = pickle.load(GBoost)
def classify(num):
    if num == 0:
        return 'No Default'
    else:
        return 'Default'
def main():
    #titulo
    st.title('Modelamiento de Credit Card Defaults')
    #titulo de sidebar
    st.sidebar.header('User Input Parameters')

    #funcion para poner los parametrso en el sidebar
    def user_input_parameters():
        PAY_0 = st.sidebar.slider('PAY 0', -2, 6, 0)
        PAY_2 = st.sidebar.slider('PAY 2', -2, 5, 0)
        PAY_3 = st.sidebar.slider('PAY 3', -2, 4, 0)
        PAY_4 = st.sidebar.slider('PAY 4', -2, 3, 0)
        PAY_5 = st.sidebar.slider('PAY 5', -2, 2, 0)
        PAY_6 = st.sidebar.slider('PAY 6', -2, 1, 0)
        LIMIT_BAL = st.sidebar.slider('LIMIT_BAL', 0, 1000000, 0)
        data = {'PAY_0': PAY_0,
                'PAY_2': PAY_2,
                'PAY_3': PAY_3,
                'PAY_4': PAY_4,
                'PAY_5': PAY_5,
                'PAY_6': PAY_6,
               'LIMIT_BAL': LIMIT_BAL}
        features = pd.DataFrame(data, index=[0])
        return features
    df = user_input_parameters()
    model = GB
    st.subheader('User Input Parameters')
    st.subheader(model)
    st.write(df)
    
    if st.button('RUN'):
        st.success(classify(GB.predict(df)))
if __name__ == '__main__':
    main()
