import streamlit as st

def run_chap6():

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
	chap6_ans = ['b', 'c', 'c', 'a']

	with header:
		st.title('Test your understanding')
		st.image("quiz/images/thinking.png")
		st.header('Chapter 6: Gradient Descent') 

	with form:
		with q1:
			st.header('Question 1')
			st.image("quiz/images/c6q1.png")
			st.text('a. 1 & 3')
			st.text('b. 1 & 4')
			st.text('c. 2 & 3')
			st.text('d. 2 & 4')

			sel_col_q1, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q1.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q2:
			st.header('Question 2')
			st.image("quiz/images/c6q2.png")

			sel_col_q2, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q2.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q3:
			st.header('Question 3')
			st.text('You run gradient descent for 15 iterations with alpha = 0.3 and compute after each')
			st.text('iteration.  You find that the value of J(theta) decreases quickly then levels off.')
			st.text('Based on this, which of the following conclusions seems most plausible?')
			st.image("quiz/images/c6q3.png")
			sel_col_q3, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q3.selectbox('Choose ONE option', options=['a', 'b', 'c'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q4:
			st.header('Question 4')
			st.text('Which of the following is true about below graphs(A, B, C left to right)')
			st.text('between the cost function and Number of iterations?')
			st.image("quiz/images/c6q4.png")
			st.text('Suppose l1, l2 and l3 are the three learning rates for A,B,C respectively.')
			st.text('Which of the following is true about l1,l2 and l3?')
			st.text('a. l2 < l1 < l3')
			st.text('b. l1 > l2 > l3')
			st.text('c. l1 = l2 = l3')
			st.text('d. None of these')

			sel_col_q4, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q4.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		submit = form.form_submit_button('Submit')

	if submit:
		for j in range(len(user_answer)):
			if user_answer[j] == chap6_ans[j]:
				counter +=1

		if counter / len(user_answer) >= (len(user_answer)-1) / len(user_answer):
			st.header(str((counter / len(user_answer))*100), ' %')
			st.markdown('Congratulations for passing the quiz. You are now at the end of the chapter!')
			st.balloons()
		else:
			st.header(str((counter / len(user_answer)) * 100))
			st.markdown('Hi buddy you did not pass the quiz this time round but no worries!')
			st.markdown('Cheer up! Practice makes perfect they say. Continue studying and practicing your knowledge!')

		st.markdown('The correct answer for the quiz:')

		for k in range(len(chap6_ans)):
			text = "Q" + str(k+1) + " - " + chap6_ans[k]
			st.text(text)
		



