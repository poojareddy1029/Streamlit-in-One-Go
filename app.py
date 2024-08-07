import streamlit as  st

st.title('Title -> Pooja Pabbathi Reddy')
st.header('Header -> Pooja Pabbathi Reddy')
st.subheader('SubHeader -> Pooja Pabbathi Reddy')
st.text('Text -> Pooja Pabbathi Reddy')

st.subheader('Headings :')
st.markdown('# Hello')
st.markdown('## Hello')
st.markdown('### Hello')
st.markdown('#### Hello')
st.markdown('##### Hello')

st.subheader('Types of Text Boxes :')
st.success('Success')         # Green Text box
st.info('Information')        # Blue Text box
st.warning('Warning')         # Yellow Text box
st.error('Error')             # Red Text box
st.exception(ZeroDivisionError('Division not possible'))
st.help(ZeroDivisionError)                   #gives info about the exception

st.subheader('Write Keyword :')
st.write('range(1,10)')      # Normal tExt
st.write(range(1,10))        #Green color text
st.write(1+2+3)

st.subheader('Code :')
st.code('x= 10\n'
        'for i in range(x):\n'
        '\tprint(x)')

st.subheader('Check Box :')
st.checkbox('Male')
if st.checkbox('Adult'):
    st.write('You are an Adult')

st.subheader('Radio Button :')
radiobutton = st.radio('select:', ('Male', "Female", 'Other'))
if radiobutton == 'Male':
    st.write("You are a male")
elif radiobutton == 'Female':
    st.write("You are a Female")
else:
    st.write("You are an other Gender")

st.subheader('Select Box :')
sel = st.selectbox('Data Science:', ('ML','DL','NLP','CV','DW','WS'))
st.write('You have selected', sel, 'Course')

st.subheader('Multi-Select Box :')
sels= st.multiselect('Data Science:',('ML','DL','NLP','CV','DW','WS') )
st.write('You have selected', len(sels) ,'Courses')

st.subheader('Button :')
if st.button('Click Me'):
     st.write('You have clicked me')

st.subheader('Slider :')
lev = st.slider('select your level',1,100,step=1)
st.write('Level is :', lev)

st.subheader('Text Input')
username= st.text_input('Userame : ')
password= st.text_input('Password :', type= 'password')

st.subheader('Text Area')
textarea = st.text_area(' Write something about urself')

st.subheader('Number Input')
st.number_input('Select your Age', 18, 110)

st.subheader('Date Input')
st.date_input('Date')

st.subheader('Time Input')
st.time_input('Time')
