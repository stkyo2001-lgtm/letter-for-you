import streamlit as st
import time

# 設定網頁標題與圖示
st.set_page_config(page_title="我們的半年紀念", page_icon="💖")

# 自定義 CSS 讓介面更漂亮
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #ff4b4b;
        color: #ff4b4b;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 初始化 Session State (用來紀錄答題進度)
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# 最新版本信件內容
letter = [
    "你好啊！",
    "先偷偷告訴你一個秘密，其實前幾天我就一直在想你這個放假會不會來找我",
    "但我又不敢真的很期待，因為我怕會失望（因為上次你說你這次放假來只能來陪我睡覺而已，因為我要下牧場又要上課）",
    "但我又很想期待，因為我好想見你，想抱著你睡覺，想和你親親，就想和你待在一起就算什麼都沒做",
    "所以昨天晚上聽到你真的要來的時候，其實很開心，開心到後來睡得不太好，一直醒來看時間，就希望可以趕快天亮，趕快到夜巡結束的時候",
    "好的，進入正題",
    "時間過得真快，居然就已經在一起半年了！",
    "都說「快樂的時光總是過得特別快」，看來跟你在一起的時候很快樂，所以才會不知不覺就半年了吧！",
    "先恭喜我們，合作愉快，平平安安的度過了這半年",
    "雖然前陣子迎來了 算是第一次的小小爭論（也雖然他的發起點是因為我的無理取鬧）",
    "謝謝你，當時理智、客觀且冷靜地對待我的無理取鬧，我們才避免了一次的爭吵！",
    "也",
    "對不起，那個時候一直拒絕你，一直不接受，讓你有一點點難過了吧！",
    "明明這件事根本和你沒什麼關係，完全只是因為我自己不能去，才在那邊生氣",
    "還有",
    "也對你很抱歉，有時候前一秒聊天還好好的，結果下一秒就不開心了",
    "有時候單純只是因為想你了，然後想到還要很久才能見面，就不嘻嘻了☹️",
    "然後結果你就被當成我發洩的目標😬",
    "然後問我不開心了嗎？ 我還硬是不說",
    "希望你不要覺得我很煩",
    "也不要覺得是你的錯，就單純只是我還沒有辦法處理好我自己的情緒而已",
    "所以有時候有可能會說反話或者一直對你說不要，希望你不要覺得難過",
    "那些都不會是我真心想說的",
    "因為是真心想說的，會不好說出口🫣",
    "真心想說的是",
    "雖然上次我說我有時候會去想要是沒有認識你，我可能就不會因為想你但見不到你而不開心，又或者因為不知道下一次見面是什麼時候而不開心",
    "但，我想說的是，認識你之後你帶給我的開心和幸福，遠遠超過那些",
    "只要想到能和你見面，就覺得一切好像都不是什麼大問題了！",
    "我很開心可以認識你，而我也比你想像中的還要早注意？（關注？）到你",
    "雖然不知道那個時候我是帶著什麼樣的心情",
    "但是 反正 就是 一切都很奇妙",
    "我們就這樣認識、熟悉、相愛、互相成長",
    "雖然我的愛可能不太成熟，常常無理取鬧",
    "所以比起說「我愛你」，我覺得「我很喜歡和你待在一起」",
    "更適合我想對你說的",
    "最後，",
    "那就祝我們",
    "還有下一個半年 再下一個半年 再下一個半年",
    "也希望我們可以努力維持這異地戀的關係",
    "以後還要一起去日本玩！！"
]

# --- 遊戲邏輯 ---

st.title("✨ 半年專屬限定解謎 ✨")

if st.session_state.stage == 0:
    st.subheader("歡迎進入『半年專屬限定』解謎活動")
    st.write("✨嘿！想要得到在一起半年的卡片嗎？✨")
    st.write("提示：只有答對所有問題，才能解鎖！😏")
    if st.button("GO! 開始挑戰"):
        st.session_state.stage = 1
        st.rerun()

elif st.session_state.stage == 1:
    ans1 = st.text_input("第一題：我們在一起是幾月幾號呢？ (提示：四位數字)")
    if ans1:
        if ans1 == "0929": #
            st.success("第一關 通過！算你還有心😎")
            if st.button("下一題"):
                st.session_state.stage = 2
                st.rerun()
        else:
            st.error("這都能記錯！😡 再給你一次機會哦！")

elif st.session_state.stage == 2:
    ans2 = st.text_input("第二題：我們第一次一起出去的地方是哪裡？（不是下課後一起吃飯的那種）")
    if ans2:
        if "動物園" in ans2: #
            st.success("答對了！其實那天在捷運上碰面的時候有點緊張尷尬😳")
            if st.button("下一題"):
                st.session_state.stage = 3
                st.rerun()
        else:
            st.info("提示：是我很喜歡去的地方！再想想！")

elif st.session_state.stage == 3:
    ans3 = st.text_input("第三題：當我突然訊息回很慢的時候，其實是因為：(A) 我睡著了😪 (B) 手機沒電了🪫 (C) 我去洗澡了🛁 (D) 我不太開心了😕") #
    if st.button("確認第三題答案"):
        if "(D)" in ans3:
            st.success("哦！答對了！！😤 有時候只是因為想你了不開心了🥲")
            if st.button("下一題"):
            st.session_state.stage = 4
            st.rerun()
        else:
            st.error("哈哈哈 雖然這個也有可能，但不對！🙅‍♂️")

elif st.session_state.stage == 4:
    st.write("第四題：你猜 我有沒有曾經因為你的某個小小的行動而不太開心過？") #
    ans4 = st.selectbox("請選擇", ["請選擇", "有", "沒有"])
    if ans4 == "有":
        st.write("哦！真的嗎？")
        ans_detail = st.text_area("那你覺得是什麼？說來聽聽")
        if st.button("誠實交代"):
            if len(ans_detail) >= 4:
                st.warning(f"『{ans_detail}』...嗯～原來是這樣。但可能不是這個哦！")
                st.session_state.stage = 5
                st.rerun()
            else:
                st.error("太短了啦！說的詳細一點！")
    elif ans4 == "沒有":
        st.error("嘿嘿嘿 我還是隱藏的很好的嘛🤪 但答錯了請重新回答！ 至於答案，我想一下要不要和你說🤪")

elif st.session_state.stage == 5:
    ans5 = st.text_input("第五題：猜猜你女朋友現在最想要被你怎樣？(A) 摸頭 (B) 抱抱 (C) 親親 (D) 一發不可收拾") #
    if st.button("最後一關！解鎖卡片"):
        if "(C)" in ans5:
            st.balloons()
            st.success("哦！居然一次就猜對了！好的！現在可以親你的女朋友😗 然後看卡片了～")
            st.session_state.stage = 6
            st.rerun()
        elif "(A)" in ans5:
            st.info("嗯～還不錯～ 但現在不是最想要這個🙂‍↔️")
        elif "(B)" in ans5:
            st.info("這個～也喜歡！那就等你猜對以後 都做吧！🤩")
        elif "(D)" in ans5:
            st.warning("哦...這個有點刺激🫨 雖然也有點想要🫣，但不行😭")

elif st.session_state.stage == 6:
    st.header("💖 你的專屬卡片已解鎖 💖")
    st.write("系統正在加載卡片內容...")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    # 顯示信件內容
    for line in letter:
        st.write(line)
    
    st.divider()
    if st.button("再玩一次"):
        st.session_state.stage = 0
        st.rerun()
