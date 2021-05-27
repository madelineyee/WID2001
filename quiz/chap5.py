import streamlit as st

def run_chap5():
	header = st.beta_container()
	q1 = st.beta_container()
	q2 = st.beta_container()
	q3 = st.beta_container()
	q4 = st.beta_container()
	form = st.form(key='my_form')

	user_answer = []
	user_answer = [0 for i in range(3)]
	idx = 0
	counter = 0
	chap5_ans = ['a', 'd', 'c']

	with header:
		st.title('Test your understanding')
		st.image("quiz/images/thinking.png")
		st.header('Chapter 5: Cost Function')

	with form:
		with q1:
			st.text('1. Which of the following offsets, do we use in linear regression’s least square line fit?')
			st.text('Suppose the horizontal axis is independent variable and the vertical axis is dependent variable.')
			st.image("quiz/images/c5q1.png")
			st.text('a. Vertical offset')
			st.text('b. Perpendicular offset')
			st.text('c. Both, depending on the situation')
			st.text('d. None of above')

			sel_col_q1, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q1.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q2:
			st.text('2. We have been given a dataset with n records in which we have input attribute as x')
			st.text('and output attribute as y. Suppose we use a linear regression method to model this data.')
			st.text('To test our linear regressor, we split the data in the training set and the test set randomly.')
			st.text('Now we increase the training set size gradually. As the training set size increases,')
			st.text('what do you expect will happen with the mean training error?')
			st.text('a. Increase')
			st.text('b. Decrease')
			st.text('c. Remain constant')
			st.text('d. None of above')

			sel_col_q2, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q2.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q3:
			st.text('3. Consider the following data where one input(X) and one output(Y) is given.')
			st.image("quiz/images/c5q3.png")
			st.text('What would be the root mean square training error for this data if you run a')
			st.text('Linear Regression model of the form (Y = A0+A1X)?')
			st.text('a. Less than 0')
			st.text('b. Greater than zero')
			st.text('c. Equal to 0')
			st.text('d. None of above')

			sel_col_q3, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q3.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		submit = form.form_submit_button('Submit')

	if submit:
		for j in range(len(user_answer)):
			if user_answer[j] == chap5_ans[j]:
				counter +=1

		if counter / len(user_answer) >= (len(user_answer)-1) / len(user_answer):
			st.header(str((counter / len(user_answer))*100), ' %')
			st.markdown('Congratulations for passing the quiz. Ready to move on to the next chapter?')
			st.balloons()
		else:
			st.header(str((counter / len(user_answer)) * 100))
			st.markdown('Hi buddy you did not pass the quiz this time round but no worries!')
			st.markdown('Cheer up! Practice makes perfect they say. Continue studying and practicing your knowledge!')

		st.markdown('The correct answer for the quiz:')

		for k in range(len(chap5_ans)):
			text = "Q" + str(k+1) + " - " + chap5_ans[k]
			st.text(text)