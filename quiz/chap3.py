import streamlit as st

def run_chap3():
	header = st.beta_container()
	q1 = st.beta_container()
	q2 = st.beta_container()
	q3 = st.beta_container()
	form = st.form(key='my_form')

	user_answer = []
	user_answer = [0 for i in range(3)]
	idx = 0
	counter = 0
	chap3_ans = ['b', 'd', 'd']

	with header:
		st.title('Test your understanding')
		st.image("quiz/images/thinking.png")
		st.header('Chapter 3: Unsupervised Learning')

	with form:
		with q1:
			st.text('1. For which of the following tasks might K-means clustering be a suitable algorithm')
			st.text('Select the one that does not apply.')
			st.image("quiz/images/q1c3.png")

			sel_col_q1, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q1.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd', 'e'], index=0, key=idx)
		idx += 1

		with q2:
			st.image("images/kmeans.png")
			st.text('2. Suppose you have an unlabeled dataset. You run K-means with 50 different random')
			st.text('initializations, and obtain 50 different clusterings of the data. What is the')
			st.text('recommended way for choosing which one of these 50 clusterings to use?')
			st.image("quiz/images/q2c3.png")
			sel_col_q2, _ = st.beta_columns(2)

			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q2.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd', 'e'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		with q3:
			st.text('3. Which of the following statements is false? Select the one that applies.')
			st.image("quiz/images/q3c3.png")

			sel_col_q3, _ = st.beta_columns(2)


			# selectbox provides answer options, index=0 means default to display the first element
			user_answer[idx] = sel_col_q3.selectbox('Choose ONE option', options=['a', 'b', 'c', 'd', 'e'], index=0, key=idx)
		# st.text(user_answer[idx])
		idx += 1

		submit = form.form_submit_button('Submit')

	if submit:
		for j in range(len(user_answer)):
			if user_answer[j] == chap3_ans[j]:
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

		for k in range(len(chap3_ans)):
			text = "Q" + str(k+1) + " - " + chap3_ans[k]
			st.text(text)
