import streamlit as st
from agent import agent_executor

# ページ設定（タブのタイトルなど）
st.set_page_config(page_title="LLM Multi-Tool Agent", layout="wide")

# チャット履歴を保持する
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💡 LLM Multi-Tool Agent")

# 入力欄（チャット形式）
user_input = st.chat_input("質問を入力してください...")

# 入力があったとき
if user_input:
    # ユーザーの発言を履歴に追加
    st.session_state.chat_history.append(("user", user_input))

    # LLM Agent からの応答を取得
    with st.spinner("考え中..."):
        try:
            response = agent_executor.run(user_input)
        except Exception as e:
            response = f"エラーが発生しました：{str(e)}"

    # 応答を履歴に追加
    st.session_state.chat_history.append(("ai", response))

# 履歴を上から順に表示
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"🧑‍💻 **あなた**: {msg}")
    else:
        st.markdown(f"🤖 **AI**: {msg}")
