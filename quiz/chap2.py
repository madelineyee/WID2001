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
chap2_ans = ['a', 'b', 'a', 'b']

with header:
	st.title('Test your understanding')
	st.image("images/thinking.png")
	st.header('Chapter 2: Supervised Learning')
	st.markdown('**Choose whether it is a classification or a regression problem**')

with form:
	with q1:

		st.image("images/weather.png")
		st.text('1. Suppose you are working on weather prediction and use a learning algorithm')
		st.text('to predict temperature in degrees Fahrenheit.')
		st.text('a. Regression')
		st.text('b. Classification')

		sel_col_q1, _ = st.beta_columns(2)

		# selectbox provides answer options, index=0 means default to display the first element
		user_answer[idx] = sel_col_q1.selectbox('Choose ONE option', options=['a', 'b'], index=0, key=idx)
	idx += 1

	with q2:
		st.text('2. Suppose you are working on weather prediction and your weather station makes one')
		st.text('of three predictions for everyday weather: Sunny, Cloudy or Rainy.')
		st.text('You would like to use a learning algorithm to predict the weather for tomorrow')
		st.text('a. Regression')
		st.text('b. Classification')

		sel_col_q2, _ = st.beta_columns(2)

		# selectbox provides answer options, index=0 means default to display the first element
		user_answer[idx] = sel_col_q2.selectbox('Choose ONE option', options=['a', 'b'], index=0, key=idx)
	idx += 1

	with q3:
		st.image("images/stock.png")
		st.text('3. Suppose you are working on stock market prediction. You would like to predict')
		st.text('whether or not a certain company will declare bankruptcy within the next 7 days')
		st.text('by training on data of similar companies that had previously been at risk of bankruptcy')
		st.text('a. Regression')
		st.text('b. Classification')

		sel_col_q3, _ = st.beta_columns(2)

		# selectbox provides answer options, index=0 means default to display the first element
		user_answer[idx] = sel_col_q3.selectbox('Choose ONE option', options=['a', 'b'], index=0, key=idx)
	idx += 1

	with q4:
		st.text('4. Suppose you are working on stock market prediction. You would like to predict')
		st.text('the price of a particular stock tomorrow that is measured in dollars.')
		st.text('You would like to use a learning algorithm for this.')
		st.text('a. Regression')
		st.text('b. Classification')

		sel_col_q4, _ = st.beta_columns(2)

		# selectbox provides answer options, index=0 means default to display the first element
		user_answer[idx] = sel_col_q4.selectbox('Choose ONE option', options=['a', 'b'], index=0, key=idx)
	idx += 1

	submit = form.form_submit_button('Submit')

if submit:
	for j in range(len(user_answer)):
		if user_answer[j] == chap2_ans[j]:
			counter += 1

	if counter / len(user_answer) >= (len(user_answer) - 1) / len(user_answer):
		st.header(str((counter / len(user_answer)) * 100), ' %')
		st.markdown('Congratulations for passing the quiz. Ready to move on to the next chapter?')
	else:
		st.header(str((counter / len(user_answer)) * 100))
		st.markdown('Hi buddy you did not pass the quiz this time round but no worries!')
		st.markdown('Cheer up! Practice makes perfect they say. Continue studying and practicing your knowledge!')

	st.markdown('The correct answer for the quiz:')

	for k in range(len(chap2_ans)):
		text = "Q" + str(k + 1) + " - " + chap2_ans[k]
		st.text(text)



                          