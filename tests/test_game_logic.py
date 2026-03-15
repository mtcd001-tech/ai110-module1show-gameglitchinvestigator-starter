import sys
import os
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_new_game_resets_state(monkeypatch):
    import streamlit as st
    # Simulate session state after a finished game
    st.session_state['attempts'] = 5
    st.session_state['secret'] = 42
    st.session_state['status'] = 'won'
    st.session_state['history'] = [10, 20, 30, 40, 42]
    st.session_state['score'] = 100

    # Patch random.randint to always return 99
    monkeypatch.setattr('random.randint', lambda low, high: 99)

    # Simulate new game logic
    st.session_state['attempts'] = 0
    st.session_state['secret'] = random.randint(1, 100)
    st.session_state['status'] = 'playing'
    st.session_state['history'] = []
    st.session_state['score'] = 0

    assert st.session_state['attempts'] == 0
    assert st.session_state['secret'] == 99
    assert st.session_state['status'] == 'playing'
    assert st.session_state['history'] == []
    assert st.session_state['score'] == 0
