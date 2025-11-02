from flask import Flask, render_template_string
import random
import time

app = Flask(__name__)

# 您的提示数据
tips = [
    '多喝水哦~💧', '保持微笑呀😊', '每天都要元气满满✨',
    '记得吃水果🍎', '保持好心情🌞', '好好爱自己❤️',
    '期待下一次见面👋', '顺顺利利🎯', '早点休息🌙',
    '愿所有烦恼都消失🌈', '别熬夜⏰', '今天过得开心嘛🎉'
]

bg_colors = [
    '#FFF0F5', '#F0FFFF', '#F5FFFA', '#FFF8DC', '#F0F8FF',
    '#F8F8FF', '#F5F5F5', '#FAFAD2', '#E6E6FA', '#FFE4E1'
]

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>温馨提醒</title>
        <style>
            body { margin: 0; overflow: hidden; background: #f0f8ff; }
            .tip {
                position: absolute;
                padding: 20px;
                border-radius: 10px;
                animation: fadeIn 0.5s;
                cursor: pointer;
                max-width: 200px;
                text-align: center;
                font-family: 'Microsoft YaHei', sans-serif;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                border-left: 5px solid #FF6B9C;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div id="container"></div>
        
        <script>
            const tips = {{ tips|tojson }};
            const colors = {{ bg_colors|tojson }};
            let tipCount = 0;
            
            function createTip() {
                if (tipCount >= 50) return;
                
                const tip = document.createElement('div');
                tip.className = 'tip';
                tip.textContent = tips[Math.floor(Math.random() * tips.length)];
                tip.style.background = colors[Math.floor(Math.random() * colors.length)];
                tip.style.left = Math.random() * 85 + 'vw';
                tip.style.top = Math.random() * 85 + 'vh';
                tip.style.color = '#2F4F4F';
                tip.style.fontSize = (14 + Math.random() * 4) + 'px';
                
                tip.onclick = function() { this.remove(); };
                
                document.getElementById('container').appendChild(tip);
                tipCount++;
                
                setTimeout(() => {
                    if (tip.parentNode) {
                        tip.remove();
                        tipCount--;
                    }
                }, 3000 + Math.random() * 2000);
            }
            
            // 随机时间间隔创建提示
            setInterval(createTip, 800);
            // 立即创建几个
            for(let i = 0; i < 5; i++) {
                setTimeout(createTip, i * 200);
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template, tips=tips, bg_colors=bg_colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
