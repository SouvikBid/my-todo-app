import streamlit as st
import sub

todos = sub.get_todos()


def add_todo():
    to_do = st.session_state["new_todo"] + "\n"
    todos.append(to_do)
    sub.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app:")
st.write("Just for check")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        sub.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add New todo",
              on_change=add_todo, key='new_todo')
