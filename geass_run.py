import streamlit as st
import streamlit.components.v1 as components
import json

# --- [데이터 입력부] 코랩 결과값을 여기에 복사하세요 ---
BLUE_DATA = "iVBORw0KGgoAAAANSUhEUgAAAR0AAAGwCAYAAACU6LFLAAABQWVYSWZNTQAqAAAACAAGAQAABAAAAAEAAAAAAQEABAAAAAEAAAAA...hvu1jzHGaGVUi8678X1rjmvaTZZtBDVNA1kDwHXxZZkuoEMIsX9YX+QYY4wxxhhjjPHB8n8AWWo80YrN14kAAAAASUVORK5CYII="   # 무적
RED_DATA = "iVBORw0KGgoAAAANSUhEUgAAARkAAAFlCAYAAADf8JytAAABQWVYSWZNTQAqAAAACAAGAQAABAAAAAEAAAAAAQEABAAAAAEAAAAA...MpcYc+PjW2dm5wcDSqPQVMxNz8EwDKKqKjRJhSiKbLjYb4yMrCkTjSwr5bsePXr06NHjXfO/ACmBlvPdQr6bAAAAAElFTkSuQmCC"    # 파괴
PURPLE_DATA = "iVBORw0KGgoAAAANSUhEUgAAAQUAAAGQCAYAAACnPXVhAAABQWVYSWZNTQAqAAAACAAGAQAABAAAAAEAAAAAAQEABAAAAAEAAAAA...GXyEjUI/wBgbI3k6Ekwmo9xsNCkMhktie3u7xu/3kxkzZtgyMzObCSGDosdAmDBhwoS5yfk/HBDQwioh5DwAAAAASUVORK5CYII=" # 슬로우
GREEN_DATA = "iVBORw0KGgoAAAANSUhEUgAAAisAAAJHCAYAAABRmBYJAAAgAElEQVR4nOzdd3hUVRoG8PfcO30y6QkBAgkQOqE36SBFQIoFXQv2...hBBi0iisEEIIIcSkUVghhBBCiEmjsEIIIYQQk0ZhhRBCCCEmjcIKIYQQQkwahRVCCCGEmLT/A1Wv0NLAEclUAAAAAElFTkSuQmCC"  # 보너스

CUTIN_BLUE = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3...s/vea1JXSY9+5H8QXNO3Xt9HlcuPywz9oSGzTZVdaArJFUo57+SIfWeCDJ4JIWKT6xAk8EkKA+t8E+u8ElOyCPW+CDL4JlIqUv/Z" 
CUTIN_RED = "UklGRqRRAABXRUJQVlA4IJhRAACQiAGdASqAArgBPm0ylUekIqIhJNG7sIANiWVu4MITPI65b25R108e/Ic8vrL2EJuA9wkufDo5...r5uig6U/Vbn7Mu6AX33Pe7idigGtcMQ6mHuvWga8pDz2zj2ZlRm0YtzX9v66wzJzuHmNLPePg9Dl9/FIWQVvO9euY9rwAAAAAA=="
CUTIN_PURPLE = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxATEhAQEBAWEBUVGSAbGBUVGRscEBggIB0iIiAdHx8kKDQsJCYxJx8fLTItMSsu...snJPUwtTwSOjRkB2jxqGtD05DSvbQ/OQ099IV0tmYUUUUgCiiigAIG/OucA5+ZrsjIHjXlAHJbG8T30BAGgArqigAooooA//2Q==
"
CUTIN_GREEN = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxATEhAQEBAWEBUVGSAbGBUVGRscEBggIB0iIiAdHx8kKDQsJCYxJx8fLTItMSsu...snJPUwtTwSOjRkB2jxqGtD05DSvbQ/OQ099IV0tmYUUUUgCiiigAIG/OucA5+ZrsjIHjXlAHJbG8T30BAGgArqigAooooA//2Q=="

OBS_DATA = "/9j/4QDKRXhpZgAATU0AKgAAAAgABgESAAMAAAABAAEAAAEaAAUAAAABAAAAVgEbAAUAAAABAAAAXgEoAAMAAAABAAIAAAITAAMA...ufAP/BFz/gmTefsW+GtV+InjWdLjWPEB/cxK4l+ywAnbHvHDHHev3qryz4Nf8k+07/rn/WvU6+RzPFzrV5VKm585jK8qlRykf//Z"    
BGM_DATA = "SUQzBAAAAAAAf1RYWFgAAAASAAADbWFqb3JfYnJhbmQAbXA0MgBUWFhYAAAAEQAAA21pbm9yX3ZlcnNpb24AMABUWFhYAAAAHAAA...qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqo="    
LOBBY_DATA = "/9j/4QCCRXhpZgAATU0AKgAAAAgABAEAAAMAAAABAAAAAAEBAAMAAAABAAAAAIdpAAQAAAABAAAAPgESAAMAAAABAAEAAAAAAAAA...NTgwYjQyNDIwMGNkNTUzZDgyODEyYjYvMjI4NDg2U0VGSGsAAAACAAAAAAChC9QGAABvBgAAAAChC2UAAABlAAAAJAAAAFNFRlQ="  

# --- [게임 실행 함수] ---
def play_geass_run():
    game_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        #game-area {{ 
            width: 100%; max-width: 600px; height: 350px; position: relative; 
            font-family: 'Malgun Gothic', sans-serif; background: #111; 
            overflow: hidden; border-radius: 12px; outline:none; margin: 0 auto;
            touch-action: manipulation; user-select: none;
        }}
        
        /* 컷인 및 이펙트 스타일 */
        #fx-cutin {{ 
            position: absolute; width: 140%; height: 250px; top: 50%; left: 50%; 
            transform: translate(-180%, -50%) skewX(-25deg); 
            background-size: cover; background-position: center; 
            z-index: 500; opacity: 0; pointer-events: none; 
            transition: transform 0.6s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.3s;
            border-left: 10px solid gold; border-right: 10px solid gold;
        }}
        #fx-overlay {{ position: absolute; inset: 0; pointer-events: none; z-index: 400; opacity: 0; transition: 0.3s; }}
        
        .overlay {{ width: 100%; height: 100%; position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white; z-index: 100; text-align: center; }}
        
        #game-container {{ width: 100%; height: 200px; border-bottom: 5px solid #333; position: relative; background: #fff; display: none; margin-top: 100px; overflow: hidden; }}
        #player {{ width: 50px; height: 50px; position: absolute; bottom: 0; left: 50px; background-size: cover; z-index: 10; }}
        #obstacle {{ width: 40px; height: 40px; position: absolute; bottom: 0; right: -60px; background-image: url('data:image/png;base64,{OBS_DATA}'); background-size: 100% 100%; transition: bottom 0.1s linear; }}
        
        /* UI 및 버튼 */
        #ui {{ position: absolute; top: 0; width: 100%; display: none; justify-content: space-between; padding: 15px; box-sizing: border-box; z-index: 50; background: rgba(255,255,255,0.8); border-bottom: 2px solid #333; }}
        .skill-btn {{ width: 70px; height: 70px; background: rgba(0,0,0,0.7); color: gold; border-radius: 50%; display: none; align-items: center; justify-content: center; font-weight: 900; border: 3px solid gold; position: absolute; bottom: 20px; left: 20px; z-index: 600; opacity: 0.4; }}
        .skill-btn.ready {{ opacity: 1; box-shadow: 0 0 15px gold; }}
        
        @keyframes shake {{ 0%, 100% {{ transform:translate(0,0); }} 25% {{ transform:translate(5px,5px); }} 75% {{ transform:translate(-5px,-5px); }} }}
        .effect-shake {{ animation: shake 0.1s infinite; }}
    </style>
    </head>
    <body>
    <div id="game-area" tabindex="0">
        <div id="fx-overlay"></div>
        <div id="fx-cutin"></div>
        
        <div id="lobby-main" class="overlay" style="background-image: url('data:image/png;base64,{LOBBY_DATA}'); background-size:cover;">
            <h1 style="text-shadow: 0 0 10px red;">GEASS RUN</h1>
            <button onclick="startGame()" style="padding:15px 30px; background:red; color:white; border:none; border-radius:20px; cursor:pointer; font-weight:bold;">GAME START</button>
        </div>

        <div id="ui">
            <div id="hp-ui"></div>
            <div id="score-ui" style="font-size:24px; font-weight:bold; color:#333;">0</div>
            <div style="width:100px; height:10px; background:#ddd;"><div id="skill-gauge" style="width:0%; height:100%; background:gold;"></div></div>
        </div>

        <div id="game-container">
            <div id="player"></div>
            <div id="obstacle"></div>
        </div>
        
        <div id="m-skill-btn" class="skill-btn" onclick="useSkill()">GEASS</div>
        <audio id="bgm" loop src="data:audio/mp3;base64,{BGM_DATA}"></audio>
    </div>

    <script>
        const IMGS = {{
            blue: 'data:image/png;base64,{BLUE_DATA}',
            red: 'data:image/png;base64,{RED_DATA}',
            purple: 'data:image/png;base64,{PURPLE_DATA}',
            green: 'data:image/png;base64,{GREEN_DATA}'
        }};
        const CUTINS = {{
            blue: 'data:image/jpeg;base64,{CUTIN_BLUE}',
            red: 'data:image/jpeg;base64,{CUTIN_RED}',
            purple: 'data:image/jpeg;base64,{CUTIN_PURPLE}',
            green: 'data:image/jpeg;base64,{CUTIN_GREEN}'
        }};

        let active = false, charId = 'blue', score = 0, hp = 3, skillVal = 0, skillReady = false;
        let obsPos = 700, obsSpeed = 7, obsType = 'normal'; 
        let jumpY = 0, velocityY = 0, isInvincible = false;

        const area = document.getElementById('game-area');
        const p = document.getElementById('player'), o = document.getElementById('obstacle');

        function startGame() {{
            document.getElementById('lobby-main').style.display = 'none';
            document.getElementById('ui').style.display = 'flex';
            document.getElementById('game-container').style.display = 'block';
            document.getElementById('m-skill-btn').style.display = 'flex';
            p.style.backgroundImage = `url(${{IMGS[charId]}})`;
            active = true; document.getElementById('bgm').play();
            requestAnimationFrame(loop);
        }}

        function useSkill() {{
            if (!skillReady) return;
            skillReady = false; skillVal = 0;
            document.getElementById('m-skill-btn').classList.remove('ready');

            const cutin = document.getElementById('fx-cutin');
            const overlay = document.getElementById('fx-overlay');
            
            cutin.style.backgroundImage = `url(${{CUTINS[charId]}})`;
            cutin.style.opacity = '1'; cutin.style.transform = 'translate(-50%, -50%) skewX(-25deg)';
            
            setTimeout(() => {{ cutin.style.opacity = '0'; cutin.style.transform = 'translate(150%, -50%) skewX(-25deg)'; }}, 700);

            // 캐릭터별 고유 스킬 이펙트
            if(charId === 'blue') {{
                isInvincible = true; p.style.boxShadow = "0 0 30px gold";
                setTimeout(() => {{ isInvincible = false; p.style.boxShadow = "none"; }}, 4000);
            }} else if(charId === 'red') {{
                area.classList.add('effect-shake'); overlay.style.background = "rgba(255,0,0,0.4)"; overlay.style.opacity = '1';
                obsPos = 800; score += 5;
                setTimeout(() => {{ area.classList.remove('effect-shake'); overlay.style.opacity = '0'; }}, 600);
            }} else if(charId === 'purple') {{
                overlay.style.background = "rgba(128,0,128,0.3)"; overlay.style.opacity = '1';
                let oldSpeed = obsSpeed; obsSpeed = 3;
                setTimeout(() => {{ obsSpeed = oldSpeed; overlay.style.opacity = '0'; }}, 5000);
            }}
        }}

        function loop() {{
            if (!active) return;

            // 점프
            velocityY += 0.7; jumpY += velocityY;
            if (jumpY > 0) {{ jumpY = 0; velocityY = 0; }}
            p.style.bottom = (-jumpY) + 'px';

            // 장애물 이동 및 상승 기믹
            obsPos -= obsSpeed;
            if (obsType === 'up' && obsPos < 400 && obsPos > 100) {{
                let rising = Math.max(0, (400 - obsPos) * 0.3);
                o.style.bottom = rising + "px";
            }} else {{
                o.style.bottom = "0px";
            }}
            o.style.left = obsPos + "px";

            // 장애물 리셋 및 랜덤 타입 결정
            if (obsPos < -50) {{
                obsPos = 700; score++; obsSpeed += 0.1;
                obsType = Math.random() < 0.3 ? 'up' : 'normal';
            }}

            // 스킬 게이지
            if(!skillReady) {{
                skillVal += 0.4;
                if(skillVal >= 100) {{ skillVal = 100; skillReady = true; document.getElementById('m-skill-btn').classList.add('ready'); }}
                document.getElementById('skill-gauge').style.width = skillVal + '%';
            }}

            // 충돌 체크
            let pr = p.getBoundingClientRect(), or = o.getBoundingClientRect();
            if (!isInvincible && pr.right > or.left+10 && pr.left < or.right-10 && pr.bottom > or.top+10) {{
                hp--; obsPos = 750;
                if (hp <= 0) {{ active = false; alert("GAME OVER! SCORE: " + score); location.reload(); }}
            }}

            document.getElementById('hp-ui').innerText = "❤️".repeat(hp);
            document.getElementById('score-ui').innerText = score;
            requestAnimationFrame(loop);
        }}

        // PC 조작
        window.onkeydown = (e) => {{
            if (e.code === 'Space') {{ e.preventDefault(); if(jumpY===0) velocityY = -14; }}
            if (e.code === 'Enter') {{ e.preventDefault(); useSkill(); }}
        }};
        // 모바일 터치 점프
        area.addEventListener('touchstart', (e) => {{
            if (e.target.id !== 'm-skill-btn' && active) {{
                e.preventDefault(); if(jumpY===0) velocityY = -14;
            }}
        }}, {{ passive: false }});
    </script>
    </body>
    </html>
    """
    components.html(game_html, width=650, height=450)

if __name__ == "__main__":
    play_geass_run()
