import streamlit as st

header = st.beta_container()
q1 = st.beta_container()
q2 = st.beta_container()
q3 = st.beta_container()
q4 = st.beta_container()
form = st.form(key='my_form')

user_answer = []
user_answer = [0 for i in range(4)]
idx = 0
counter = 0
chap1_ans = ['a', 'b', 'a', 'd']

with header:
    st.title('Test your understanding')
    st.image("images/thinking.png") 
    st.header('Chapter 1: Introduction to Machine Learning')

with form:
    with q1:
        st.header('Question 1')
        st.image("images/historical.png") 
        st.write('A computer program is said to learn from experience E with respect to some task T and some' + 
        ' performance measure P if its performance on T, as measured by P, improves with' + 
        ' experience E. Suppose we feed a learning algorithm a lot of historical weather data,' +
        ' and have it learn to predict weather. In this setting, what is T?')
        st.text('a. The weather prediction task.')
        st.text('b. None of these.')
        st.text('c. The probability of it correctly predicting a future date’s weather.')
        st.text('d. The process of the algorithm examining a large amount of historical weather data.')

        sel_col_q1,_ = st.beta_columns(2)

        # selectbox provides answer options, index=0 means default to display the first element
        user_answer[idx] = sel_col_q1.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
        # st.text(user_answer[idx])
    idx += 1

    with q2:
        st.header('Question 2')
        st.image("images/predict.png") 
        st.markdown('A computer program is said to learn from experience E with respect to some task T and ')
        st.markdown('some performance measure P if its performance on T, as measured by P, improves with')
        st.markdown('experience E. Suppose we feed a learning algorithm a lot of historical weather data,')
        st.markdown('and have it learn to predict weather. What would be a reasonable choice for P?')
        st.text('a. The weather prediction task.')
        st.text('b. The probability of it correctly predicting a future date’s weather.')
        st.text('c. The process of the algorithm examining a large amount of historical weather data.')
        st.text('d. None of these.')

        sel_col_q2,_ = st.beta_columns(2)

        # selectbox provides answer options, index=0 means default to display the first element
        user_answer[idx] = sel_col_q2.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
        # st.text(user_answer[idx])
    idx += 1

    with q3:
        st.header('Question 3')
        st.markdown('Some of the problems below are best addressed using a supervised learning ')
        st.markdown('algorithm, and the others with an unsupervised learning algorithm. Which of the')
        st.markdown('following would you apply supervised learning to? (Select all that apply.) In each case,')
        st.markdown('assume some appropriate dataset is available for your algorithm to learn from.')
        st.text('a. Given historical data of children’s ages and heights, predict children’s height as ')
        st.text('   a function of their age.')
        st.text('b. Given 50 articles written by male authors, categorize the articles into k groups ')
        st.text('   according to the handwriting of each article.')
        st.text('c. Take a collection of 1000 essays written on the US Economy, and find a way to ')
        st.text('   automatically group these essays into a small number of groups of essays that ')
        st.text('   are somehow “similar” or “related”.')
        st.text('d. Examine a large collection of emails that are known to be spam email, to discover')
        st.text('   if there are sub-types of spam mail.')

        sel_col_q3,_ = st.beta_columns(2)

        # selectbox provides answer options, index=0 means default to display the first element
        user_answer[idx] = sel_col_q3.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
        # st.text(user_answer[idx])
    idx += 1

    with q4:
        st.header('Question 4')
        st.image("images/ML.png") 
        st.markdown('Which of these is a reasonable definition of machine learning? ')
        st.text('a. Machine learning is the science of programming computers.')
        st.text('b. Machine learning learns from labeled data.')
        st.text('c. Machine learning is the field of allowing robots to act intelligently.')
        st.text('d. Machine learning is the field of study that gives computers the ability to learn without ')
        st.text('   being explicitly programmed.')

        sel_col_q4,_ = st.beta_columns(2)

        # selectbox provides answer options, index=0 means default to display the first element
        user_answer[idx] = sel_col_q4.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
        # st.text(user_answer[idx])
    idx += 1

    submit = form.form_submit_button('Submit')

if submit:
    for j in range(len(user_answer)):
        if user_answer[j] == chap1_ans[j]:
            counter +=1

    if counter / len(user_answer) >= (len(user_answer)-1) / len(user_answer):
        st.header(str((counter / len(user_answer))*100), ' %')
        st.markdown('Congratulations for passing the quiz. Ready to move on to the next chapter?')
    else:
        st.header(str((counter / len(user_answer)) * 100))
        st.markdown('Hi buddy you did not pass the quiz this time round but no worries!')
        st.markdown('Cheer up! Practice makes perfect they say. Continue studying and practicing your knowledge!')

    st.markdown('The correct answer for the quiz:')

    for k in range(len(chap1_ans)):
        text = "Q" + str(k+1) + " - " + chap1_ans[k]
        st.text(text)
