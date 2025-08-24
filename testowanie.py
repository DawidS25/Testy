if st.session_state.guesser_points is not None:
    if st.button("💾 Zapisz i dalej"):
        guesser_points = st.session_state.guesser_points

        # Reset wyborów
        st.session_state.guesser_points = None

        # Liczenie punktów dla respondera według zasad:
        if guesser_points == 0:
            responder_points = 0
        elif guesser_points in [2, 3]:
            responder_points = 1
        elif guesser_points == 4:
            responder_points = 2
        else:
            responder_points = 0
            
        # Aktualizacja wyników
        st.session_state.scores[guesser] += guesser_points
        st.session_state.scores[responder] += responder_points

        points_this_round = {
            responder: responder_points,
            guesser: guesser_points,
        }

        # Dopisywanie wyników do pamięci
        new_state("results_data", [])

        data_to_save = {
            "runda": current_round,
            "nr_pytania": current_question_number,
            "kategoria": q['category'],
            "pytanie": q['text'],
            "odpowiada": responder,
            "zgaduje": guesser,
            responder: points_this_round[responder],
            guesser: points_this_round[guesser],
        }

        st.session_state.results_data.append(data_to_save)

        st.session_state.questions_asked += 1

        # Po 2 pytaniach pokazujemy pytanie czy kontynuować
        if st.session_state.questions_asked % 2 == 0:
            st.session_state.ask_continue = True
            st.session_state.current_question = None
        else:
            st.session_state.current_question = draw_question()

        st.rerun()
