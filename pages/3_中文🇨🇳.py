import streamlit as st
import json

@st.cache_data  # データのキャッシュ化
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


# JSONファイルから商品データをロード
products = load_data("json/products_cn.json")

# Streamlitアプリのタイトル
st.title('产品目录')
st.write("---")  # 商品間の区切り線

# JSONファイルから商品名を取得
product_names = [product["name"] for product in products]

# サイドバーに商品名をリンクとして表示
selected_product = st.sidebar.selectbox("商品を選択", product_names)
# 商品情報をカード形式で表示
for product in products:
    with st.container():
        col1, col2 = st.columns([1, 3])  # カラムを作成
        with col1:
            # 商品画像を表示
            st.image(product["image_path"], width=150)
        with col2:
            # 商品名と価格を表示
            st.subheader(product["name"])
            st.write(f"**价格: {product['price']}**")  
            st.caption(product["description"])
            st.write(f"烹饪方法: {product['usage']}")
            
            button_key = f"button_{product['name']}"
            if st.button("🔈 聆听语音描述", key=button_key):
                st.audio(product["audio_paths"])  # 音声ファイルのパス
    st.write("---")  # 商品間の区切り線
