import streamlit as st
import random
import time

# 页面配置
st.set_page_config(
    page_title="随机温馨提示",
    page_icon="💝",
    layout="centered"
)

# 丰富的提示内容库
tips = [
    '多喝水哦~💧', '保持微笑呀😊', '每天都要元气满满✨',
    '记得吃水果🍎', '保持好心情🌞', '好好爱自己❤️',
    # ... 您的所有提示内容
]

# 柔和的背景颜色库
bg_colors = [
    '#FFF0F5', '#F0FFFF', '#F5FFFA', '#FFF8DC', '#F0F8FF',
    # ... 您的所有颜色
]

def main():
    st.title("💝 随机温馨提示生成器")
    
    # 控制参数
    col1, col2 = st.columns(2)
    with col1:
        window_count = st.slider("提示数量", 1, 50, 10)
    with col2:
        display_time = st.slider("显示时间(秒)", 1, 10, 3)
    
    if st.button("🎲 开始随机显示", type="primary"):
        st.info(f"将在页面中随机显示 {window_count} 条温馨提示...")
        
        # 创建占位符用于动态显示
        placeholder = st.empty()
        
        for i in range(window_count):
            tip_text = random.choice(tips)
            bg_color = random.choice(bg_colors)
            
            # 使用HTML创建浮动效果
            html_content = f"""
            <div style='
                background-color: {bg_color};
                padding: 20px;
                margin: 10px;
                border-radius: 10px;
                border-left: 5px solid #FF6B9C;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                animation: fadeIn 0.5s;
            '>
                <h3 style='color: #2F4F4F; margin:0;'>{tip_text}</h3>
            </div>
            <style>
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(-10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            </style>
            """
            
            placeholder.markdown(html_content, unsafe_allow_html=True)
            time.sleep(display_time)
        
        st.success("🎉 所有温馨提示已显示完毕！")

if __name__ == "__main__":
    main()
