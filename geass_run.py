import streamlit as st
import streamlit.components.v1 as components

def play_geass_run():
    # 1. 이미지 데이터 (기존 데이터 유지)
    BLUE_IMG = "data:image/png;base64,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"
    OBS_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB8klEQVR4nO2Yv0vDQBjHn8S9QXByFAdnB0cHJ0cHZwcHB0cHZwcHB0cHZwcHB0fBydHBydHBydHBydHBydHBydHBydHByf0DOnSJpEnSptf2vS88SAtp8vnc98f7XpI6Ozt/Sshms9vNZvMskUis6fV6vUqlUnE8HndO0v1+v9NoNLp+v78vCMLZ6urq9ubm5tH6+no8Ozs7f9oZBAH/H9vPz8/bV1dXH61W68ZiseDhcLhVq9UuTk5O7vAnYI1AILC8vr6+vbm5eZ9MJm9isRhcXFzc8Cdgj7m5ueXFxcXtcrl86fP5IJPJ7Ofz+Yvj4+N7O8F6wBohS0tL97u7u/fFYvG8Xq9DPB7fzefz58fHx64SCAK+mU6nN7e2tu6LxeKlUgr9fv/S8vLyZSKRWHeV9IDVAn57e3v3xWLxXCmFSqXyZWVl5fzo6GjHVTIIAs6Mjo4ubm5u3pdKpUulFCKRyE4mk9mX9IC/BPzOzs7u7u7unvSA77ZfXFzcLpfLl76/BAH7EonE7fX19Z0S8M3ExMTK8vLypat+fA6wz9TU1PrGxsbOnxMgCHgjEAis8D0AtvB9AnuMjo4u8j0An+R7BOwRCoXW+B4An/geAV/U6/VrvgfApf/77+D7A/Yxm83Y7u7u+TfE9/jRPhf68AAAAABJRU5ErkJggg=="

    st.title("🎮 GEASS RUN GAME")
    st.write("아래 화면을 클릭하고 'SPACE'를 눌러 점프하세요!")

    # 2. HTML/CSS/JS 통합 코드
    html_code = f"""
    <div id="game-wrap" style="width:100%; display:flex; flex-direction:column; align-items:center; background:#222; padding:20px; border-radius:10px;">
        <div id="game-container" style="position:relative; width:600px; height:200px; background:#eee; border:4px solid #444; overflow:hidden;">
            <div id="player" style="position:absolute; bottom:0; left:50px; width:40px; height:40px; background:url('{BLUE_IMG}') no-repeat center/contain;"></div>
            <div id="obstacle" style="position:absolute; bottom:0; right:-50px; width:40px; height:40px; background:url('{OBS_IMG}') no-repeat center/contain;"></div>
            <div id="score" style="position:absolute; top:10px; left:10px; font-family:Arial; font-weight:bold; font-size:20px;">SCORE: 0</div>
        </div>
    </div>

    <script>
        const player = document.getElementById("player");
        const obstacle = document.getElementById("obstacle");
        const scoreElement = document.getElementById("score");
        let score = 0;
        let isJumping = false;

        function jump() {{
            if (isJumping) return;
            isJumping = true;
            let position = 0;
            let timerId = setInterval(function () {{
                if (position === 100) {{
                    clearInterval(timerId);
                    let downTimerId = setInterval(function () {{
                        if (position === 0) {{
                            clearInterval(downTimerId);
                            isJumping = false;
                        }}
                        position -= 5;
                        player.style.bottom = position + 'px';
                    }}, 20);
                }}
                position += 5;
                player.style.bottom = position + 'px';
            }}, 20);
        }}

        // 장애물 이동 로직
        let obstaclePos = 600;
        function moveObstacle() {{
            obstaclePos -= 7;
            if (obstaclePos < -50) {{
                obstaclePos = 600;
                score++;
                scoreElement.innerHTML = "SCORE: " + score;
            }}
            obstacle.style.right = (600 - obstaclePos) + 'px';
            
            // 충돌 감지
            let playerBottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));
            if (obstaclePos > 50 && obstaclePos < 90 && playerBottom < 40) {{
                alert("GAME OVER! SCORE: " + score);
                score = 0;
                obstaclePos = 600;
                scoreElement.innerHTML = "SCORE: 0";
            }}
            
            requestAnimationFrame(moveObstacle);
        }}

        document.addEventListener('keydown', function(event) {{
            if (event.code === 'Space') {{
                jump();
            }}
        }});

        moveObstacle();
    </script>
    """

    # 3. Streamlit 컴포넌트로 HTML 실행
    components.html(html_code, height=300)

if __name__ == "__main__":
    play_geass_run()
