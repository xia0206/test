from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>我的 Python 应用</h1>
    <p>成功部署在 Vercel！</p>
    <a href="/api/date">查看API</a>
    '''

@app.route('/api/date')
def api_date():
    from datetime import datetime
    return {'current_time': datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(debug=True)
