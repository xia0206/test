from flask import Flask, render_template_string
import random

app = Flask(__name__)

# 扩充的温馨提示词库（150+条）
tips = [
    '多喝水哦~💧', '保持微笑呀😊', '每天都要元气满满✨', '记得吃水果🍎', '保持好心情🌞',
    '好好爱自己❤️', '期待下一次见面👋', '顺顺利利🎯', '早点休息🌙', '愿所有烦恼都消失🌈',
    '别熬夜⏰', '今天过得开心嘛🎉', '天冷了，多穿衣服🧥', '保护眼睛哦👀', '深呼吸放松一下🌬️',
    '你真棒！🎊', '一切都会好的🌻', '保持积极心态⚡', '加油！🚀', '相信自己💪',
    '今天也是美好的一天🌞', '保持耐心⏳', '慢慢来比较快🐢', '你很特别🌟', '世界因你而美丽🌍',
    '放松一下🎵', '享受当下🎯', '感恩生活🙏', '保持好奇心🔍', '勇敢做自己🦁',
    '进步一点点📈', '温暖如春🌺', '心平气和🍃', '梦想成真🎠', '快乐很简单😄',
    '阳光总在风雨后🌦️', '坚持就是胜利🏆', '你是最棒的⭐', '生活很美好🌷', '向前看👣',
    '温柔待人💝', '珍惜当下🎁', '幸福在身边🎈', '保持热情🔥', '微笑是最好的语言😄',
    '健康最重要💪', '保持学习📚', '成长每一天🌱', '相信奇迹🌈', '爱与被爱都幸福💖',
    '简单就是快乐☀️', '心怀感恩🙏', '保持希望🌟', '勇敢前行🚶‍♂️', '善待他人🤝',
    '保持平衡⚖️', '静心思考🧠', '快乐分享🎁', '温暖传递🔥', '梦想启航⛵',
    '坚持不懈🏃‍♂️', '乐观向上📈', '心存善念💕', '珍惜缘分🔗', '把握当下⏰',
    '快乐工作💼', '享受生活🏡', '保持年轻心态🎯', '追求卓越🏆', '感恩遇见👥',
    '保持真诚💎', '宽容大度🌊', '积极进取🚀', '热爱生活🎨', '保持幽默😄',
    '珍惜友谊👫', '家庭幸福🏠', '工作顺利💻', '学业进步📖', '身体健康💊',
    '心情愉快🎵', '财源广进💰', '好运连连🍀', '平安喜乐🕊️', '心想事成🎯',
    '爱情甜蜜💑', '友谊长存👭', '事业有成💼', '梦想成真🌟', '快乐无限🎊',
    '幸福满满💝', '好运相伴🌈', '平安健康🌿', '快乐每一天🎉', '微笑面对😊',
    '勇敢追梦🚀', '保持热情🔥', '坚持到底🏁', '相信自己💪', '你是独一无二的⭐',
    '世界因你不同🌎', '保持初心💖', '不断进步📈', '享受过程🎨', '珍惜时光⏳',
    '爱自己❤️', '保持冷静❄️', '积极思考💡', '拥抱变化🔄', '感恩所有🙏',
    '分享快乐🎁', '传递温暖🔥', '保持善良🌼', '坚持梦想🌟', '勇敢尝试🚀',
    '保持好奇🔍', '学习成长📚', '享受孤独🌙', '珍惜相遇👥', '把握机会🎯',
    '保持耐心⏰', '宽容理解💕', '积极沟通🗣️', '团队合作👥', '创新思维💡',
    '保持专注🎯', '平衡生活⚖️', '健康饮食🍎', '适量运动🏃‍♀️', '充足睡眠😴',
    '保持乐观🌞', '面对挑战🛡️', '克服困难💪', '庆祝成功🎉', '反思成长📝',
    '规划未来🗺️', '活在当下🌍', '珍惜拥有💎', '传递爱心💝', '创造价值⭐'
]

# 扩充的背景颜色库
bg_colors = [
    '#FFF0F5', '#F0FFFF', '#F5FFFA', '#FFF8DC', '#F0F8FF', '#F8F8FF', 
    '#F5F5F5', '#FAFAD2', '#E6E6FA', '#FFE4E1', '#FFFAF0', '#FDF5E6',
    '#FAF0E6', '#FFF5EE', '#F0FFF0', '#F5F5DC', '#FFEFD5', '#FFE4B5',
    '#FAF0E6', '#F8F8FF', '#F0F8FF', '#E0FFFF', '#E6E6FA', '#FFF0F5',
    '#FFE4E1', '#FFFAFA', '#F5F5F5', '#F0F0F0', '#FFF8DC', '#FFE4C4',
    '#FFDAB9', '#FFEFD5', '#FFFACD', '#F0E68C', '#E6E6FA', '#D8BFD8',
    '#DDA0DD', '#EE82EE', '#DA70D6', '#FFB6C1', '#FFA07A', '#98FB98',
    '#AFEEEE', '#DDA0DD', '#F0E68C', '#FFFACD', '#E6E6FA', '#FFE4E1',
    '#FFDAB9', '#98FB98', '#AFEEEE', '#DDA0DD', '#F0E68C', '#FFFACD'
]

@app.route('/')
def home():
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>温馨提醒生成器</title>
        <style>
            body { 
                margin: 0; 
                overflow: hidden; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: 'Microsoft YaHei', sans-serif;
            }
            
            #start-btn {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                padding: 20px 40px;
                font-size: 24px;
                background: linear-gradient(45deg, #FF6B9C, #FF8E53);
                color: white;
                border: none;
                border-radius: 50px;
                cursor: pointer;
                box-shadow: 0 10px 30px rgba(255, 107, 156, 0.4);
                transition: all 0.3s;
                z-index: 1000;
            }
            
            #start-btn:hover {
                transform: translate(-50%, -50%) scale(1.1);
                box-shadow: 0 15px 40px rgba(255, 107, 156, 0.6);
            }
            
            #counter {
                position: fixed;
                top: 20px;
                right: 20px;
                background: rgba(255,255,255,0.9);
                padding: 10px 20px;
                border-radius: 20px;
                font-size: 16px;
                color: #333;
                z-index: 1000;
            }
            
            .tip {
                position: absolute;
                padding: 15px 25px;
                border-radius: 15px;
                animation: floatIn 0.4s ease-out, float 3s ease-in-out infinite;
                cursor: pointer;
                max-width: 250px;
                text-align: center;
                font-size: 18px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                border-left: 5px solid rgba(255,255,255,0.8);
                transition: all 0.3s;
                z-index: 100;
            }
            
            .tip:hover {
                transform: scale(1.08) rotate(2deg);
                box-shadow: 0 12px 35px rgba(0,0,0,0.3);
            }
            
            @keyframes floatIn {
                from { 
                    opacity: 0; 
                    transform: translateY(-40px) scale(0.7) rotate(-10deg);
                }
                to { 
                    opacity: 1; 
                    transform: translateY(0) scale(1) rotate(0);
                }
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0) rotate(0); }
                50% { transform: translateY(-10px) rotate(1deg); }
            }
            
            @keyframes fadeOut {
                to { 
                    opacity: 0; 
                    transform: translateY(30px) scale(0.8) rotate(5deg);
                }
            }
        </style>
    </head>
    <body>
        <button id="start-btn" onclick="startTips()">🎲 开始温馨提醒</button>
        <div id="counter">已显示: <span id="count">0</span> 条提示</div>
        <div id="container"></div>
        
        <script>
            const tips = {{ tips|tojson }};
            const colors = {{ bg_colors|tojson }};
            let tipCount = 0;
            let isRunning = false;
            let totalCreated = 0;
            
            function startTips() {
                if (isRunning) return;
                
                isRunning = true;
                document.getElementById('start-btn').style.display = 'none';
                
                // 高速创建弹窗（每秒3-5个）
                const fastInterval = setInterval(() => {
                    if (totalCreated >= 300) { // 总共创建300个弹窗
                        clearInterval(fastInterval);
                        return;
                    }
                    createTip();
                }, 200); // 每200毫秒创建一个
                
                // 额外的高速批次（每秒8-10个）
                setTimeout(() => {
                    const superFastInterval = setInterval(() => {
                        if (totalCreated >= 300) {
                            clearInterval(superFastInterval);
                            return;
                        }
                        for(let i = 0; i < 3; i++) {
                            setTimeout(() => createTip(), i * 50);
                        }
                    }, 300);
                }, 2000);
            }
            
            function createTip() {
                if (totalCreated >= 300) return;
                
                const tip = document.createElement('div');
                tip.className = 'tip';
                tip.textContent = tips[Math.floor(Math.random() * tips.length)];
                tip.style.background = colors[Math.floor(Math.random() * colors.length)];
                tip.style.left = Math.random() * 90 + 'vw';
                tip.style.top = Math.random() * 90 + 'vh';
                tip.style.color = '#2F4F4F';
                tip.style.fontSize = (16 + Math.random() * 6) + 'px';
                tip.style.fontWeight = Math.random() > 0.7 ? 'bold' : 'normal';
                
                // 点击移除
                tip.onclick = function() { 
                    this.style.animation = 'fadeOut 0.4s forwards';
                    setTimeout(() => {
                        if (this.parentNode) {
                            this.remove();
                            tipCount--;
                            updateCounter();
                        }
                    }, 400);
                };
                
                document.getElementById('container').appendChild(tip);
                tipCount++;
                totalCreated++;
                updateCounter();
                
                // 1.5-4秒后自动消失（更快消失）
                setTimeout(() => {
                    if (tip.parentNode) {
                        tip.style.animation = 'fadeOut 0.4s forwards';
                        setTimeout(() => {
                            if (tip.parentNode) {
                                tip.remove();
                                tipCount--;
                                updateCounter();
                            }
                        }, 400);
                    }
                }, 1500 + Math.random() * 2500);
            }
            
            function updateCounter() {
                document.getElementById('count').textContent = tipCount;
            }
            
            // 添加键盘快捷键
            document.addEventListener('keydown', function(e) {
                if (e.code === 'Space' && !isRunning) {
                    startTips();
                }
            });
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_template, tips=tips, bg_colors=bg_colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
