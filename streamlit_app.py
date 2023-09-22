import streamlit as st
import random

# タイトルを作成する
st.title("恋みくじアプリ")

# ユーザーが名前を入力するためのテキストボックスを作成する
name = st.text_input("あなたの名前を入力してください")

# おみくじを引くためのボタンを作成する
if st.button("おみくじを引く"):
    # おみくじの結果をランダムに選択する
    results = ["恋実らず", "明日はいい日になるよ", "あきらめも大事よ", "そんな日もある", "恋が叶うかも"，"恋って楽しいよね。わかるわかる！"]
    fortune = random.choice(results)
    
    # 結果を表示する
    st.write(f"{name}さんの恋愛運は{fortune}です！")