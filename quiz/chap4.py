import streamlit as st

def run_chap4():
	header = st.beta_container()
	q1 = st.beta_container()
	q2 = st.beta_container()
	q3 = st.beta_container()
	q4 = st.beta_container()
	q5 = st.beta_container()
	form = st.form(key='my_form')

	user_answer = []
	user_answer = [0 for i in range(5)]
	idx = 0
	counter = 0
	chap4_ans = ['c', 'c', 'a', 'b', 'd']


	with header:
		st.title('Test your understanding')
		st.image("quiz/images/thinking.png")
		st.header('Chapter 4: Model Representation')

	with form:
		with q1:
			st.text('1. Suppose m=4 students have taken some classes, and the class had a midterm exam')
			st.text('and a final exam. You have collected a dataset of their scores on the two exams:')
			st.image("quiz/images/c4q1.png")
			st.text('Hint: midterm = 69, final = 78 is training example 4.')
			st.text(' Please round off your answer to two decimal places and choose the appropriate answer.')
			st.text('a. 0.47')
			st.text('b. -0.64')
			st.text('c. -0.47')
			st.text('d. 0.64')

			sel_col_q1, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q1.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q2:
			st.text('2. Which of the following statements is true about the sum of residuals of A and B?')
			st.text('Below graphs show two fitted regression lines (A & B) on randomly generated data.')
			st.text('Now, I want to find the sum of residuals in both cases A and B.')
			st.image("images/c4q2.png")
			st.text('Note: Scale is the same in both graphs for both axes.')
			st.text('X axis is independent variable and Y-axis is dependent variable.')
			st.text('a. A has higher sum of residuals than B')
			st.text('b. A has lower sum of residual than B')
			st.text('c. Both have same sum of residuals')
			st.text('d. None of these.')

			sel_col_q2, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q2.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q3:
			st.text('3. Which of the following statements is true about outliers in Linear regression?')
			st.text('a. Linear regression is sensitive to outliers')
			st.text('b. Linear regression is not sensitive to outliers')
			st.text('c. Can’t say')
			st.text('d. None of these.')

			sel_col_q3, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q3.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q4:
			st.text('4. Suppose that you have a dataset D1 and you design a linear regression model')
			st.text('of degree 3 polynomial and you found that the training and testing error is 0')
			st.text('or in another terms it perfectly fits the data. What will happen when you fit')
			st.text('degree 2 polynomial in linear regression?')
			st.text('a. It is high chances that degree 2 polynomial will over fit the data')
			st.text('b. It is high chances that degree 2 polynomial will under fit the data')
			st.text('c. It is high chances that degree 2 polynomial will perfectly fit the data')
			st.text('d. None of these.')

			sel_col_q4, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q4.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q5:
			st.text('5. We can also compute the coefficient of linear regression with the help of')
			st.text('an analytical method called “Normal Equation”.')
			st.text('Which of the following is/are true about Normal Equation?')
			st.image("quiz/images/c4q5.png")
			st.text('a. 1 and 2')
			st.text('b. 1 and 3')
			st.text('c. 2 and 3')
			st.text('d. 1,2 and 3')

			sel_col_q5, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q5.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		submit = form.form_submit_button('Submit')

	if submit:
		for j in range(len(user_answer)):
			if user_answer[j] == chap4_ans[j]:
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

		for k in range(len(chap4_ans)):
			text = "Q" + str(k+1) + " - " + chap4_ans[k]
			st.text(text)
