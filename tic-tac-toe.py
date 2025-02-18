import streamlit as st

# Function to check the winner
def check_winner(board):
    for row in board:
        if all(cell == "X" for cell in row):
            return "X"
        if all(cell == "O" for cell in row):
            return "O"

    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return "X"
        if all(board[row][col] == "O" for row in range(3)):
            return "O"

    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return "X"
    if all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return "O"

    if all(cell != "" for row in board for cell in row):
        return "Draw"

    return None

# Streamlit UI
def main():
    st.title("Tic-Tac-Toe Game")

    if "board" not in st.session_state:
        st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
        st.session_state.turn = "X"

    winner = check_winner(st.session_state.board)

    if winner:
        st.subheader(f"Winner: {winner} 🎉")
        if st.button("Restart Game", key="restart"):
            st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
            st.session_state.turn = "X"
            st.rerun()  # Updated function
        return

    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if cols[j].button(st.session_state.board[i][j] if st.session_state.board[i][j] else " ", key=f"button_{i}_{j}"):
                if not st.session_state.board[i][j]:
                    st.session_state.board[i][j] = st.session_state.turn
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                    st.rerun()  # Updated function

if __name__ == "__main__":
    main()
