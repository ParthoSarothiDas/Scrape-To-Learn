import streamlit as st
import pandas as pd

st.set_page_config('🌐 Globe', layout='wide')
st.title('Learn with Fun')
df_country_info = pd.read_csv('data/df_country_info_all.csv') # ------------------------------> Import Dataset
options = ['Learn About Country', 'Globe Quiz', 'Flag Quiz','Continent Quiz','Capital City Quiz']
selected = st.sidebar.radio('',options=options )
if selected == 'Learn About Country':
    st.subheader('Want to learn about countries? Just select country !!!')
    option_list = sorted(df_country_info['country'].values)
    selected_country = st.selectbox("Select Country:", options=[None] + option_list)
    if selected_country is not None:
        capital = df_country_info[df_country_info['country']==selected_country]['capital'].iloc[0]
        continent = df_country_info[df_country_info['country']==selected_country]['continent'].iloc[0]
        flag_img = df_country_info[df_country_info['country']==selected_country]['image_flag'].iloc[0]
        country_details = df_country_info[df_country_info['country'] == selected_country]['details'].iloc[0]
        globe_img = df_country_info[df_country_info['country'] == selected_country]['image_globe'].iloc[0]

        col1, col2 = st.columns(2)
        with col1:
            col3, col4 = st.columns([2,1])
            with col3:
                st.write(f'Capital City : **{capital}**')
                st.write(f"Continent : **{continent}**")
            with col4:
                with st.container(border=True):
                    if flag_img and flag_img != "nan" and not isinstance(flag_img, float):
                        st.image(f"flag_image/{flag_img}", width= 100)
                    else:
                        flag_img = "default.png"
                        st.image(f"flag_image/{flag_img}")

            st.markdown(f'''
            <p style='text-align: justify;'>
            {country_details}</p>''', unsafe_allow_html=True)
            st.caption("Source: Wikipedia")
        
        with col2:
            if globe_img and globe_img != "nan" and not isinstance(globe_img, float):
                st.image(f"globe_image/{globe_img}")
            else:
                globe_img = "default.png"
                st.image(f"globe_image/{globe_img}")
elif selected =='Globe Quiz':
    st.subheader('Check your knowledge about location of countries !!!')
    continent_list = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    selected_continent = st.radio("Select Continent", options=continent_list, horizontal=True, key=4)
    
    col1, col2 = st.columns(2)
    # Initialize game state
    if 'score_globe' not in st.session_state:
        st.session_state.score_globe = 0
    if 'wrong_streak_globe' not in st.session_state:
        st.session_state.wrong_streak_globe = 0
    if 'game_over_globe' not in st.session_state:
        st.session_state.game_over_globe = False

    with col1:
        st.markdown(f"##### 🧮 Score: {st.session_state.score_globe}")
        st.markdown(f"##### ❌ Wrong Streak: {st.session_state.wrong_streak_globe} / 3")

    if selected_continent:
        df = df_country_info[(df_country_info['continent'] == selected_continent) & (df_country_info['image_globe'].notnull())]

        if df.empty:
            st.warning(f"No questions available for continent: {selected_continent}")
        elif st.session_state.game_over_globe:
            st.error("❌ Game Over! You got 3 incorrect answers in a row.")
            st.info(f"Your final score: {st.session_state.score_globe}")
            if st.button("🔄 Restart Game"):
                st.session_state.score_globe = 0
                st.session_state.wrong_streak_globe = 0
                st.session_state.game_over_globe = False
                st.session_state.pop('q_set', None)
                st.rerun()
        else:
            # Sample once per session or when continent changes
            if 'q_set' not in st.session_state or st.session_state.get('continent') != selected_continent:
                st.session_state.q_set = df.sample(min(5, len(df))).reset_index(drop=True)
                st.session_state.continent = selected_continent

            q_set = st.session_state.q_set
            correct_answer = q_set.loc[0, 'country']
            image = q_set.loc[0, 'image_globe']
            options = sorted(q_set['country'].unique().tolist())

            col2.image(f'globe_image/{image}', width=500)  # ----------------> Globe Image

            with col1:
                with st.container(border=True):
                    selected = st.radio("Choose the country displayed on the globe:", options=[None] + options, key=1)
                    if st.button('✅ Submit', key=2):
                        if selected is None:
                            st.warning("Please select an option before submitting.")
                        elif selected == correct_answer:
                            st.success("Correct! 🎉 +5 points")
                            st.session_state.score_globe += 5
                            st.session_state.wrong_streak_globe = 0
                            st.balloons()
                        else:
                            st.session_state.wrong_streak_globe += 1
                            st.error(f"Wrong! Correct Answer: {correct_answer}")
                            if st.session_state.wrong_streak_globe >= 3:
                                st.session_state.game_over_globe = True
                                st.rerun()

                if st.button("➡️ Next Question"):
                    st.session_state.pop('q_set', None)
                    st.rerun()
elif selected == 'Flag Quiz':
    st.subheader('Test your knowledge about flags !!!')

    # Initialize game state for tab3
    if 'score_flags_tab3' not in st.session_state:
        st.session_state.score_flags_tab3 = 0
    if 'wrong_streak_flags_tab3' not in st.session_state:
        st.session_state.wrong_streak_flags_tab3 = 0
    if 'game_over_flags_tab3' not in st.session_state:
        st.session_state.game_over_flags_tab3 = False

    level_options = ['Easy', 'Medium', 'Hard']
    selected_level = st.radio("Select Difficulty Level", options=level_options, horizontal=True, key=201)

    st.markdown(f"##### 🧮 Score: {st.session_state.score_flags_tab3}")
    st.markdown(f"##### ❌ Wrong Streak: {st.session_state.wrong_streak_flags_tab3} / 3")

    col1, col2 = st.columns(2)

    if selected_level:
        df_level = df_country_info[df_country_info['level'] == selected_level]

        if df_level.empty:
            st.warning(f"No questions available for level: {selected_level}")
        elif st.session_state.game_over_flags_tab3:
            st.error("❌ Game Over! You got 3 incorrect answers in a row.")
            st.info(f"Your final score: {st.session_state.score_flags_tab3}")
            if st.button("🔄 Restart Game"):
                st.session_state.score_flags_tab3 = 0
                st.session_state.wrong_streak_flags_tab3 = 0
                st.session_state.game_over_flags_tab3 = False
                st.session_state.pop('q_set2', None)
                st.rerun()
        else:
            # Load question set if not already loaded or if level has changed
            if 'q_set2' not in st.session_state or st.session_state.get('level') != selected_level:
                st.session_state.q_set2 = df_level[df_level['image_flag'].notnull()].sample(min(5, len(df_level))).reset_index(drop=True)
                st.session_state.level = selected_level

            q_set2 = st.session_state.q_set2
            correct_answer = q_set2.loc[0, 'country']
            image = q_set2.loc[0, 'image_flag']
            options = sorted(q_set2['country'].unique().tolist())

            with col2.container(border=True):
                st.image(f"flag_image/{image}", width=500)

            with col1:
                with st.container(border=True):
                    selected = st.radio("Select Correct Country", options=[None] + options, key=202)

                    if st.button('✅ Submit', key=203):
                        if selected is None:
                            st.warning("Please select an option before submitting.")
                        elif selected == correct_answer:
                            st.success("Correct! 🎉 +5 points")
                            st.session_state.score_flags_tab3 += 5
                            st.session_state.wrong_streak_flags_tab3 = 0
                            st.balloons()
                        else:
                            st.session_state.wrong_streak_flags_tab3 += 1
                            st.error(f"Wrong! Correct Answer: {correct_answer}")
                            if st.session_state.wrong_streak_flags_tab3 >= 3:
                                st.session_state.game_over_flags_tab3 = True
                                st.rerun()

                if st.button("➡️ Next Question", key=204):
                    st.session_state.pop('q_set2', None)
                    st.rerun()
elif selected == 'Continent Quiz':
    st.subheader('Test your knowledge about continents !!!')

    # Initialize game state
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'wrong_streak' not in st.session_state:
        st.session_state.wrong_streak = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

    level_options = ['Easy', 'Medium', 'Hard']
    selected_level = st.radio("Select Difficulty Level", options=level_options, horizontal=True, key=205)

    
    st.markdown(f"##### 🧮 Score: {st.session_state.score}")
    st.markdown(f"##### ❌ Wrong Streak: {st.session_state.wrong_streak} / 3")

    col1, col2 = st.columns([1, 1])

    if selected_level:
        df_level = df_country_info[df_country_info['level'] == selected_level]

        if df_level.empty:
            st.warning(f"No questions available for level: {selected_level}")
        elif st.session_state.game_over:
            st.error("❌ Game Over! You got 3 incorrect answers in a row.")
            st.info(f"Your final score: {st.session_state.score}")
            if st.button("🔄 Restart Game"):
                st.session_state.score = 0
                st.session_state.wrong_streak = 0
                st.session_state.game_over = False
                st.session_state.pop('q_set3', None)
                st.rerun()
        else:
            # Load or generate new question
            if 'q_set3' not in st.session_state or st.session_state.get('level') != selected_level:
                st.session_state.q_set3 = df_level.sample(1).reset_index(drop=True)
                st.session_state.level = selected_level

            q_set3 = st.session_state.q_set3
            country_name = q_set3.loc[0, 'country']

            with col2.container(border=True):
                st.markdown(f'### {country_name}')
                st.image(f"flag_image/{q_set3.loc[0, 'image_flag']}", width=300)

            with col1:
                with st.container(border=True):
                    option = sorted(df_country_info['continent'].unique())
                    selected = st.radio("Select Continent:", options=[None] + option, key=500)

                    if st.button('✅ Submit', key=2003):
                        if selected is None:
                            st.warning("Please select a continent before submitting.")
                        elif selected == q_set3.loc[0, 'continent']:
                            st.success("Correct! 🎉 +5 points")
                            st.session_state.score += 5
                            st.session_state.wrong_streak = 0
                            st.balloons()
                        else:
                            st.session_state.wrong_streak += 1
                            st.error(f"Wrong! Correct Answer: {q_set3.loc[0, 'continent']}")
                            if st.session_state.wrong_streak >= 3:
                                st.session_state.game_over = True
                                st.rerun()

                if st.button("➡️ Next Question", key=200004):
                    st.session_state.pop('q_set3', None)
                    st.rerun()
elif selected == 'Capital City Quiz':
    st.subheader('Test your knowledge about Capital City !!!')

    # Initialize game state
    if 'score_flags' not in st.session_state:
        st.session_state.score_flags = 0
    if 'wrong_streak_flags' not in st.session_state:
        st.session_state.wrong_streak_flags = 0
    if 'game_over_flags' not in st.session_state:
        st.session_state.game_over_flags = False

    level_options = ['Easy', 'Medium', 'Hard']
    selected_level = st.radio("Select Difficulty Level", options=level_options, horizontal=True, key=207)
    st.markdown(f"##### 🧮 Score: {st.session_state.score_flags}")
    st.markdown(f"##### ❌ Wrong Streak: {st.session_state.wrong_streak_flags} / 3")

    col1, col2 = st.columns([1, 1])

    if selected_level:
        df_level = df_country_info[df_country_info['level'] == selected_level]

        if df_level.empty:
            st.warning(f"No questions available for level: {selected_level}")
        elif st.session_state.game_over_flags:
            st.error("❌ Game Over! You got 3 incorrect answers in a row.")
            st.info(f"Your final score: {st.session_state.score_flags}")
            if st.button("🔄 Restart Game"):
                st.session_state.score_flags = 0
                st.session_state.wrong_streak_flags = 0
                st.session_state.game_over_flags = False
                st.session_state.pop('q_set4', None)
                st.rerun()
        else:
            # Load or generate new set of questions
            if 'q_set4' not in st.session_state or st.session_state.get('level') != selected_level:
                st.session_state.q_set4 = df_level.sample(min(5, len(df_level))).reset_index(drop=True)
                st.session_state.level = selected_level

            q_set4 = st.session_state.q_set4

            # Take the first question from q_set4
            country_name = q_set4.loc[0, 'country']
            correct_answer = q_set4.loc[0, 'capital']
            option = sorted(q_set4['capital'].unique().tolist())

            with col2.container(border=True):
                st.markdown(f"### {country_name}")
                st.image(f"flag_image/{q_set4.loc[0, 'image_flag']}", width=300)

            with col1:
                with st.container(border=True):
                    selected = st.radio("Select Correct Capital", options=[None] + option, key=20288)

                    if st.button('✅ Submit', key=20799):
                        if selected is None:
                            st.warning("Please select an option before submitting.")
                        elif selected == correct_answer:
                            st.success("Correct! 🎉 +5 points")
                            st.session_state.score_flags += 5
                            st.session_state.wrong_streak_flags = 0
                            st.balloons()
                        else:
                            st.session_state.wrong_streak_flags += 1
                            st.error(f"Wrong! Correct Answer: {correct_answer}")
                            if st.session_state.wrong_streak_flags >= 3:
                                st.session_state.game_over_flags = True
                                st.rerun()

                if st.button("➡️ Next Question", key=2088):
                    st.session_state.pop('q_set4', None)
                    st.rerun()
else:
    pass

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<hr style="margin-top: 30px;">
<div style="text-align: center; font-size: 0.9em; color: gray;">
    Created by <b>Partho Sarothi Das</b><br>
    <i>Aspiring Data Scientist | Passionate about ML & Visualization</i><br>
    Email: <a href="mailto:partho52@gmail.com">partho52@gmail.com</a><br><br>
    Globe images used in this app are sourced from <a href="https://commons.wikimedia.org" target="_blank">Wikimedia Commons</a> and licensed under 
    <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank">CC BY-SA 3.0</a>. Images may have been resized or renamed for educational use.
</div>
""", unsafe_allow_html=True)
