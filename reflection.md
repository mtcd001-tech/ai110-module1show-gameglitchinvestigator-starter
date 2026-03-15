# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It looks normal, nothing seemed to be wrong

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

+ We cannot start a new game
+ The 'go lower' and 'go higher' are wrong. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
+ GPT  4.1
+ Ai was incorrect when it told me to fix the unittest, I followed and it's still wrong for 3 times.  Fixed the restart call in app.py: replaced the incorrect `st.rerun()` with `st.experimental_rerun()` so the "New Game" button actually restarts the app and resets state.
What I changed:
- app.py: use `st.experimental_rerun()` after resetting session state.

+ The last time,  it tell me the test file now imports `random`, fixing the NameError. I also moved the actual implementations for `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` from app.py to logic_utils.py, replacing the NotImplementedError stubs. You should now be able to run your tests and have them pass (unless there are other issues). If you see any more errors, let me know! So I ran it and it ran properly. 
## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
 I decide a bug was really fixed after try many times, and ask AI if is there any bug. I ran the pytest tests/test_game_logic.py, this file help me to test the code and it appeads 4 passed in 0.50s. AI helped me to understand and design a new file test. I looked at it and understand. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
