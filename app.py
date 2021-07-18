import streamlit as st

import pandas as pd
import numpy as np
import pickle

import base64

eductation_sector_ls = ['', 'Art, Music or Design', 'Economic Sciences, Business Studies, Commerce and Law', 
        'Engineering Sciences', 'Humanities and Social Sciences', 'Language and Cultural Studies',
        'Mathematics or Natural Sciences', 'Medicine, Health Sciences', 'Others', 'Teaching Degree (e.g., B.Ed)']

dict_esector = {}
for i in range(1,len(eductation_sector_ls)):
    dict_esector[eductation_sector_ls[i]] = 0

key_traits_ls = ['', 'Passion', 'Positivity', 'Resilience', 'Vision', 'Work Ethic']
dict_key_traits = {}
for i in range(1,len(key_traits_ls)):
    dict_key_traits[key_traits_ls[i]] = 0


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            }
        </style>
        """,
    unsafe_allow_html=True
)

def main():
    html1 = '''<body style>
    <h1 style="font-family:georgia;color:#06FF48;font-size:60px;">Can you be an Entrepreneur?</h1>
    </body>'''
    st.markdown(html1,unsafe_allow_html = True)
    pickle_in = open('KNNC.pkl','rb')
    classifier = pickle.load(pickle_in)
    st.markdown('### Select Educatiom Sector')
    eductation_sector = st.selectbox("",eductation_sector_ls,index = 0,key = 's1')
    dict_esector[eductation_sector] = 1

    st.markdown("### Individual Project")
    individual_project = st.radio("",['-','Yes','No'],key = 'r1')
    if individual_project == "Yes":
        individual_project = 1
    else :
        individual_project = 0

    st.markdown('### Enter your age')
    age = st.number_input("", min_value=0, value=18, step=1, format=None, key='ni1')
    age = int(age)

    st.markdown('### Gender')
    Gender = st.radio("",['-','Male','Female'],key = 'r2')
    if Gender == "Male":
        Gender = 1
    else :
        Gender = 0

    st.markdown('### City')
    City = st.radio("",['-','Yes','No'],key = 'r3')
    if City == "Yes":
        City = 1
    else :
        City = 0

    st.markdown('### Influenced')
    Influenced = st.radio("",['-','Yes','No'],key = 'r4')
    if Influenced == "Yes":
        Influenced = 1
    else :
        Influenced = 0

    st.markdown('### Perseverance')
    Perseverance = st.radio("",['0','1','2','3','4','5'],key = 'r5')
    Perseverance = int(Perseverance)

    st.markdown('### Desire To Take Initiative')
    DesireToTakeInitiative = st.radio("",['0','1','2','3','4','5'],key = 'r6')
    DesireToTakeInitiative = int(DesireToTakeInitiative)

    st.markdown('### Competitiveness')
    Competitiveness = st.radio("",['0','1','2','3','4','5'],key = 'r7')
    Competitiveness = int(Competitiveness)

    st.markdown('### Self Reliance')
    SelfReliance = st.radio("",['0','1','2','3','4','5'],key = 'r8')
    SelfReliance = int(SelfReliance)

    st.markdown('### Strong Need To Achieve')
    StrongNeedToAchieve = st.radio("",['0','1','2','3','4','5'],key = 'r9')
    StrongNeedToAchieve = int(StrongNeedToAchieve)

    st.markdown('### Self Confidence')
    SelfConfidence = st.radio("",['0','1','2','3','4','5'],key = 'r10')
    SelfConfidence = int(SelfConfidence)

    st.markdown('### Good Physical Health')
    GoodPhysicalHealth = st.radio("",['0','1','2','3','4','5'],key = 'r11')
    GoodPhysicalHealth = int(GoodPhysicalHealth)
    
    st.markdown('### Mental Disorder')
    MentalDisorder = st.radio("",['','Yes','No'],key = 'r12')
    if MentalDisorder == "Yes":
        MentalDisorder = 1
    else :
        MentalDisorder = 0

    st.markdown('### Select Key trait')
    key_trait = st.selectbox("",key_traits_ls,index = 0,key = 's2')
    dict_key_traits[key_trait] = 1

    values_ls = [int(individual_project),int(age),int(Gender),int(City),int(Influenced),int(Perseverance),int(DesireToTakeInitiative),int(Competitiveness),\
        int(SelfReliance),int(StrongNeedToAchieve),int(SelfConfidence),int(GoodPhysicalHealth),int(MentalDisorder)]\
             + list(dict_esector.values()) + list(dict_key_traits.values())

    if st.button("Submit"):

        try:
            pred = classifier.predict([np.asarray(values_ls)])
            if int(pred) == 1:
                html_yes = '''<body style>
                    <h1 style="font-family:georgia;color:#06FF48;font-size:30px;">YES (👍 ͡❛ ͜ʖ ͡❛)👍</h1>
                    </body>'''
                st.markdown(html_yes,unsafe_allow_html = True)

                file_ = open("leo1.gif", "rb")
                contents = file_.read()
                data_url = base64.b64encode(contents).decode("utf-8")
                file_.close()

                st.markdown(
                    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                    unsafe_allow_html=True,
                )
        
                st.balloons()
            else:
                html_no = '''<body style>
                    <h1 style="font-family:georgia;color:#06FF48;font-size:30px;">NO ( ͡ಥ ͜ʖ ͡ಥ)👎</h1>
                    </body>'''
                st.markdown(html_no,unsafe_allow_html = True)

                file_ = open("tenor.gif", "rb")
                contents = file_.read()
                data_url = base64.b64encode(contents).decode("utf-8")
                file_.close()

                st.markdown(
                    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                    unsafe_allow_html=True,
                )

        except :
            st.warning('Please Enter valid values')





if __name__ == "__main__":
    main()
