import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import json

# 페이지 설정
st.set_page_config(page_title="GEASS RUN", layout="centered")

def get_b64(path):
    """파일 경로에서 base64 데이터를 추출 (파일이 없을 경우 빈 문자열 반환)"""
    if not os.path.exists(path): 
        return ""
    with open(path, 'rb') as f:
        ext = path.split('.')[-1].lower()
        if ext == 'webp': mime = "image/webp"
        elif ext in ['png', 'jpg', 'jpeg']: mime = "image/png"
        elif ext == 'mp3': mime = "audio/mp3"
        else: mime = "application/octet-stream"
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')

# 1. 파일 설정 (기존 경로 그대로 사용)
char_files = {
    'blue': '/content/drive/MyDrive/R.png',
    'red': '/content/drive/MyDrive/OIP.png',
    'purple': '/content/drive/MyDrive/GZN7HXW.png',
    'green': '/content/drive/MyDrive/WMq4hw2.png'
}
cutin_files = {
    'blue': '/content/drive/MyDrive/images (1).jpeg',
    'red': '/content/drive/MyDrive/nma_uYdzx8yD-pw8lEX4WGyCC2ELX5_6zd2gk_5MBo9izS1mCJo_4KtLrWxUk2xEqPtD3yzyPj3cS_5xOCP4cw.webp',
    'purple': '/content/drive/MyDrive/images (2).jpeg',
    'green': '/content/drive/MyDrive/MFay8JcfL1LlgyCi-tJSfrP8gHXHfSVagbP-SuvqqWQ-4PxJOQe_v4YeudlvLIQomwbYyUhoDSpGbLKPNrKeXA.webp'
}
obs_file = '/content/drive/MyDrive/IMG_0071.PNG'
bgm_file = '/content/drive/MyDrive/1776756741121Converted.mp3'
lobby_bg_file = '/content/drive/MyDrive/uRvTq_pxvdDatefZ10LZQ8HYFRyGV7cMbZzc7V_T0kdIezPlKAm-dyajjfSRE3hdXzJfckt1pgLUOXAxolQP-Q.jpg'

# 2. 데이터 변환 (캐싱 처리하여 속도 향상)
@st.cache_data
def load_game_assets():
    imgs = {k: get_b64(v) for k, v in char_files.items()}
    cutins = {k: get_b64(v) for k, v in cutin_files.items()}
    img_obs = get_b64(obs_file)
    img_lobby = get_b64(lobby_bg_file)
    audio_data = get_b64(bgm_file)
    return imgs, cutins, img_obs, img_lobby, audio_data

imgs, cutins, img_obs, img_lobby, audio_data = load_game_assets()

# 3. 게임 실행 함수
def play_geass_run():
    # 모든 기능과 스타일을 유지한 HTML
    game_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        #game-area {{ width: 600px; height: 350px; position: relative; font-family: 'Malgun Gothic', sans-serif; background: #111; overflow: hidden; border-radius: 12px; user-select: none; outline:none; margin: 0 auto; }}
        .overlay {{ width: 100%; height: 100%; position: absolute; top: 0; left: 0; z-index: 100; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white; text-align: center; }}
        #fx-flash {{ position: absolute; inset: 0; background: red; opacity: 0; z-index: 200; pointer-events: none; transition: 0.3s; }}
        #fx-cutin {{ position: absolute; width: 100%; height: 200px; top: 50%; left: 50%; transform: translate(-150%, -50%) skewX(-20deg); background-size: contain; background-repeat: no-repeat; background-position: center; z-index: 201; opacity: 0; pointer-events: none; transition: 0.7s cubic-bezier(0.23, 1, 0.32, 1); }}
        #lobby-main {{ background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('{img_lobby}'); background-size: cover; background-position: center; }}
        #lobby-title {{ font-size: 50px; font-weight: 900; text-shadow: 0 0 20px red; margin-bottom: 25px; font-style: italic; letter-spacing: 2px; }}
        #lobby-select {{ background: rgba(0,0,0,0.95); display: none; }}
        .char-card {{ width: 100px; padding: 15px; margin: 8px; cursor: pointer; border-radius: 15px; transition: 0.3s; border: 2px solid rgba(255,255,255,0.1); text-align: center; }}
        .char-card:hover {{ transform: scale(1.1); border-color: gold; box-shadow: 0 0 15px gold; }}
        #game-container {{ width: 100%; height: 200px; border-bottom: 5px solid #222; position: relative; background: #fff; display: none; margin-top: 100px; overflow: hidden; }}
        #player {{ width: 48px; height: 48px; position: absolute; bottom: 0; left: 50px; background-size: cover; border: none; z-index: 10; }}
        .ghost {{ width: 48px; height: 48px; position: absolute; background-size: cover; opacity: 0.4; pointer-events: none; z-index: 9; filter: brightness(1.5) sepia(1); }}
        #obstacle {{ width: 42px; position: absolute; bottom: 0; right: -60px; background-size: 100% 100%; z-index: 5; background-image: url('{img_obs}'); }}
        @keyframes popUp {{ 0% {{ bottom: -100px; }} 100% {{ bottom: 0px; }} }}
        .pop-anim {{ animation: popUp 0.4s ease-out forwards; }}
        #ui-bar {{ position: absolute; top: 0; width: 100%; height: 80px; display: none; align-items: center; justify-content: space-between; padding: 0 25px; box-sizing: border-box; background: white; border-bottom: 3px solid #222; z-index: 50; }}
        #skill-gauge-container {{ width: 150px; height: 18px; background: #eee; border-radius: 9px; overflow: hidden; border: 2px solid #222; position: relative; }}
        #skill-gauge {{ width: 0%; height: 100%; background: linear-gradient(90deg, #ffd700, #ff4500); transition: width 0.1s; }}
        .skill-btn {{ width: 80px; height: 80px; background: rgba(0,0,0,0.5); color: rgba(255, 215, 0, 0.5); border-radius: 50%; display: none; align-items: center; justify-content: center; font-size: 16px; font-weight: 900; border: 4px solid rgba(255, 215, 0, 0.5); cursor: pointer; position: absolute; bottom: 20px; left: 20px; z-index: 60; opacity: 0.5; transition: opacity 0.3s; }}
        .skill-btn.ready {{ background: rgba(255, 215, 0, 0.7); color: black; opacity: 0.7; border-color: gold; box-shadow: 0 0 25px gold; animation: pulse 1s infinite; }}
        @keyframes pulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.1); }} 100% {{ transform: scale(1); }} }}
        .btn-main {{ padding: 15px 50px; font-size: 20px; font-weight: 900; color: white; background: #e74c3c; border: none; border-radius: 50px; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.4); transition: 0.2s; }}
        @keyframes shake {{ 0%, 100% {{ transform: translate(0,0); }} 25% {{ transform: translate(5px, 5px); }} 75% {{ transform: translate(-5px, -5px); }} }}
        .shaking {{ animation: shake 0.1s 5; }}
    </style>
    </head>
    <body onload="document.getElementById('game-area').focus()">
    <div id="game-area" tabindex="0">
        <div id="fx-flash"></div>
        <div id="fx-cutin"></div>
        <div id="lobby-main" class="overlay">
            <div id="lobby-title">GEASS RUN</div>
            <button class="btn-main" onclick="showSelect()">INITIATE ➔</button>
            <div style="margin-top:20px; font-weight:bold; color: white;">RECORD: <span id="lobby-best">0</span></div>
        </div>
        <div id="lobby-select" class="overlay">
            <h2 style="margin-bottom:20px; color:gold;">CHOOSE YOUR GEASS</h2>
            <div style="display: flex;" id="card-container"></div>
            <button style="margin-top:20px; color:#ccc; background:none; border:1px solid #555; cursor:pointer; padding:5px 15px; border-radius:15px;" onclick="showMain()">BACK</button>
        </div>
        <div id="ui-bar">
            <div id="hp-ui" style="font-size:24px;"></div>
            <div id="score-ui" style="font-size:24px; font-weight:bold; color:#222;">0</div>
            <div id="skill-gauge-container"><div id="skill-gauge"></div></div>
        </div>
        <div id="gameover" class="overlay" style="display: none; background:rgba(0,0,0,0.8);">
            <h1 style="color:#ff4d4d; font-size:45px; text-shadow:0 0 10px red;">MISSION FAILED</h1>
            <div id="final-score" style="font-size:24px; margin-bottom:20px; color: white;"></div>
            <button class="btn-main" onclick="retryGame()">RETRY</button>
            <button style="margin-top:20px; color:white; background:none; border:none; cursor:pointer;" onclick="resetToLobby()">LOBBY</button>
        </div>
        <div id="m-skill-btn" class="skill-btn" onmousedown="useSkill(event)">GEASS</div>
        <div id="game-container" onmousedown="jump()">
            <div id="player"></div>
            <div id="obstacle"></div>
        </div>
        <audio id="bgm" loop src="{audio_data}"></audio>
    </div>

    <script>
        const IMGS = {json.dumps(imgs)};
        const CUTINS = {json.dumps(cutins)};
        let bestScore = localStorage.getItem('geass_best_score') || 0;
        document.getElementById('lobby-best').innerText = bestScore;

        let active = false, score = 0, hp = 3, maxHp = 3, obsPos = 650, obsSpeed = 7;
        let skillType = '', skillVal = 0, baseSkillRate = 0.5, skillReady = false, charId = '';
        let isInvincible = false, isHurt = false, currentImg = '';
        let jumpY = 0, velocityY = 0, gravity = 0.65, canDoubleJump = false;

        const area = document.getElementById('game-area'), gc = document.getElementById('game-container'),
              p = document.getElementById('player'), o = document.getElementById('obstacle'),
              bgm = document.getElementById('bgm'), mSkillBtn = document.getElementById('m-skill-btn'),
              sGauge = document.getElementById('skill-gauge'), fxFlash = document.getElementById('fx-flash'),
              fxCutin = document.getElementById('fx-cutin');

        const chars = [
            {{ id: 'blue', name: '무적', type: 'invincible', hp: 3, rate: 0.5, color: '#4db8ff' }},
            {{ id: 'red', name: '파괴', type: 'destroy', hp: 2, rate: 0.8, color: '#ff4d4d' }},
            {{ id: 'purple', name: '느리게', type: 'slow', hp: 4, rate: 0.4, color: '#9933ff' }},
            {{ id: 'green', name: '보너스', type: 'bonus', hp: 1, rate: 1.2, color: '#2eb82e' }}
        ];

        chars.forEach(c => {{
            const card = document.createElement('div');
            card.className = 'char-card'; card.style.background = c.color;
            card.onclick = () => {{
                charId = c.id; skillType = c.type; maxHp = c.hp; hp = c.hp;
                baseSkillRate = c.rate; currentImg = IMGS[c.id]; startGame();
            }};
            card.innerHTML = `<div style="width:50px; height:50px; background-image:url(${{IMGS[c.id]}}); background-size:cover; border-radius:50%; margin:0 auto 10px; border:2px solid white;"></div><b style="color:white;">${{c.name}}</b>`;
            document.getElementById('card-container').appendChild(card);
        }});

        function showSelect() {{ document.getElementById('lobby-main').style.display = 'none'; document.getElementById('lobby-select').style.display = 'flex'; }}
        function showMain() {{ document.getElementById('lobby-main').style.display = 'flex'; document.getElementById('lobby-select').style.display = 'none'; }}

        function startGame() {{
            p.style.backgroundImage = `url(${{currentImg}})`;
            document.getElementById('lobby-select').style.display = 'none';
            document.getElementById('ui-bar').style.display = 'flex';
            gc.style.display = 'block'; mSkillBtn.style.display = 'flex';
            score = 0; obsPos = 650; obsSpeed = 7; skillVal = 0; skillReady = false;
            jumpY = 0; velocityY = 0; active = true; isInvincible = false; isHurt = false; hp = maxHp;
            bgm.currentTime = 0; bgm.play().catch(()=>{{}});
            area.focus(); resetObstacle(); requestAnimationFrame(loop);
        }}

        function resetObstacle() {{
            obsPos = 700; o.style.height = (Math.random() > 0.5) ? '85px' : '45px';
            o.classList.remove('pop-anim'); void o.offsetWidth; o.classList.add('pop-anim');
        }}

        function jump() {{ if (jumpY === 0) {{ velocityY = -13; canDoubleJump = true; }} else if (canDoubleJump) {{ velocityY = -11; canDoubleJump = false; createGhost(); }} }}

        function useSkill(e) {{
            if (e) e.stopPropagation();
            if (!skillReady || !active) return;
            skillReady = false; skillVal = 0; mSkillBtn.classList.remove('ready');
            fxFlash.style.transition = 'none'; fxFlash.style.opacity = '0.8'; void fxFlash.offsetWidth; fxFlash.style.transition = '0.5s'; fxFlash.style.opacity = '0';
            fxCutin.style.backgroundImage = `url(${{CUTINS[charId]}})`;
            fxCutin.style.transform = 'translate(-50%, -50%) skewX(-20deg)'; fxCutin.style.opacity = '1';
            setTimeout(() => {{ fxCutin.style.transform = 'translate(150%, -50%) skewX(-20deg)'; fxCutin.style.opacity = '0'; }}, 800);
            setTimeout(() => {{ fxCutin.style.transform = 'translate(-150%, -50%) skewX(-20deg)'; }}, 1500);

            if (skillType === 'invincible') {{
                isInvincible = true; p.style.boxShadow = "0 0 30px gold";
                setTimeout(() => {{ isInvincible = false; p.style.boxShadow = "none"; }}, 3500);
            }} else if (skillType === 'destroy') {{
                area.classList.add('shaking'); resetObstacle(); score += 5;
                setTimeout(() => area.classList.remove('shaking'), 500);
            }} else if (skillType === 'slow') {{
                let s = obsSpeed; obsSpeed = 3; gc.style.filter = "sepia(1) hue-rotate(240deg)";
                setTimeout(() => {{ obsSpeed = s; gc.style.filter = "none"; }}, 4500);
            }} else if (skillType === 'bonus') {{ score += 20; }}
        }}

        function createGhost() {{
            const ghost = document.createElement('div');
            ghost.className = 'ghost'; ghost.style.backgroundImage = `url(${{currentImg}})`;
            ghost.style.left = p.offsetLeft + 'px'; ghost.style.bottom = p.style.bottom;
            gc.appendChild(ghost); setTimeout(() => ghost.remove(), 400);
        }}

        function loop() {{
            if (!active) return;
            velocityY += gravity; jumpY += velocityY;
            if (jumpY > 0) {{ jumpY = 0; velocityY = 0; }}
            p.style.bottom = (-jumpY) + 'px';

            if (!skillReady) {{
                skillVal += baseSkillRate;
                if (skillVal >= 100) {{ skillVal = 100; skillReady = true; mSkillBtn.classList.add('ready'); }}
            }}
            sGauge.style.width = skillVal + '%';

            obsPos -= obsSpeed;
            if (obsPos < -60) {{ score++; obsSpeed += 0.15; resetObstacle(); }}
            o.style.left = obsPos + 'px';

            let pr = p.getBoundingClientRect(), or = o.getBoundingClientRect();
            if (!isInvincible && !isHurt && pr.right > or.left+12 && pr.left < or.right-12 && pr.bottom > or.top+12) {{
                hp--;
                if (hp <= 0) {{
                    active = false; bgm.pause();
                    if (score > bestScore) {{ bestScore = score; localStorage.setItem('geass_best_score', score); }}
                    document.getElementById('final-score').innerText = "SCORE: " + score;
                    document.getElementById('gameover').style.display = 'flex';
                }} else {{
                    isHurt = true; p.style.opacity = '0.3';
                    setTimeout(()=>{{ p.style.opacity = '1'; isHurt = false; }}, 1200);
                    resetObstacle();
                }}
            }}
            document.getElementById('hp-ui').innerText = "❤️".repeat(Math.max(0, hp));
            document.getElementById('score-ui').innerText = score;
            requestAnimationFrame(loop);
        }}

        area.onkeydown = (e) => {{
            if (e.code === 'Space') {{ e.preventDefault(); jump(); }}
            if (e.code === 'Enter') {{ e.preventDefault(); useSkill(); }}
        }};

        function retryGame() {{ document.getElementById('gameover').style.display = 'none'; startGame(); }}
        function resetToLobby() {{ active = false; document.getElementById('gameover').style.display = 'none'; gc.style.display = 'none'; mSkillBtn.style.display = 'none'; document.getElementById('ui-bar').style.display = 'none'; showMain(); }}
    </script>
    </body>
    </html>
    """
    # Streamlit 화면에 출력 (가로 600px에 맞춤)
    components.html(game_html, width=650, height=400)

if __name__ == "__main__":
    play_geass_run()
