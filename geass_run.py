import streamlit as st
import streamlit.components.v1 as components

def play_geass_run():
    # 이미지 데이터 (기존 데이터 유지)
    BLUE_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAR0AAAGwCAYAAACU6LFLAAABQWVYSWZNTQAqAAAACAAGAQAABAAAAAEAAAAAAQEABAAAAAEAAAAAh2kABAAAAAEAAABqARIABAAAAAEAAAAAATIAAgAAABQAAABWiCUABAAAAAEAAADaAAAAADIwMjY6MDQ6MjEgMTY6MTY6MTkAAAaQAwACAAAAFAAAALiSkQACAAAAAjAAAACQEAACAAAABwAAAMyQEQACAAAABwAAANOSkAACAAAAAjAAAACSCAAEAAAAAQAAAAAAAAAAMjAyNjowNDoyMSAxNjoxNjoxOQArMDk6MDAAKzA5OjAwAAACAAcABQAAAAMAAAD4AB0AAgAAAAsAAAEQAAAAAAAAAAcAAAABAAAAEAAAAAEAAAATAAAAATIwMjY6MDQ6MjEAAAEBMgACAAAAFAAAAS0AAAAAMjAyNjowNDoyMSAxNjoxNjoxOQDpw8h0AAAAAXNSR0IArs4c6QAAAARzQklUCAgICHwIZIgAACAASURBVHic7L13mBzXeeb7O5U7T09OmBlgkDMBEomZEoMoKlGkZQXbsi1pdbWr9V3vXlnr3bXl9dqWV/K99gZbsmxFW8kKlChqRZAgRQJgJgCSyGEATM4znbsrnfvH6R7MgBQt2RZBQPM+Tz8906G66lSdt77v/cIRLOIXCiUpewQYEryIEOcv9f4s4hcP4lLvwCJ+vhiWcnUJOkehsQLJAJI2mGlwXY9skwxytqVPzsLgKiGOX+r9XcSVj0XSuUIxUe5bFQqx5lwpvXZ6ZqbrxTG9aXpmJjkxnUmWSkUz7c+68UQ8u7pOz9U31E+0rNs2kIxzshFOtAjx4qXe/0VcuVgknSsMR6XcYsDqfT5LDx5kzcHDY+tGR0e6VukDqVQqpa2KzmJZlvARFItFeS4vwpmZmUwy5gwsXdpzcvVV644vXZo81QSH1wlx8FIfzyKuPCySzhWC0sxMt5NIXPWcp1/z+OPn137hUGkpyM5NV6+p27QJbWMUEYtAJxCE4AOaBuMh5PPIg88dl0eOHMn3jw8NrVix4tQv3Xj9s6u640/0CPHIpT62RVxZWCSdKwD9Uvaehe37T52986lHH72mUnG7bty4zt65c6fotQxKoUt94KLrOgkpEEKgSRshIJQQhsiCCX4IP+gbl3v27CmMuJVTO3fsfPytG1c9cI0jHr7Ux7iIKwfGpd6BRfzzMCxltwvbn+4bvOe5Z5+/xnEi7W9729u1nS315IBspUC9HSOqGXh4hF6AaZqIEDzPB2FgmuD64PuwdXkzq5a/O/KdfS8sf+TRR4Tefy48I6XsFWLPpT7WRVwZWCSdyxxnYfP+o4fe9Nj3zm9btWp924duXa3VJyCd68dwHJBZCC3c0ATfZ9ZpxsbE1aBoSwRlIjg0aVP4wiNOKyHIe67bZG9sbl72xe/fH0z/cJ97WMryeiH2X+rjXcTlD+1S78Ai/umQBbn doctors. . . " # (생략 금지: 실제 긴 데이터 넣어주세요)
    OBS_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHe. . . "

    st.markdown("### 👁️ GEASS RUN: LELOUCH'S COMMAND")
    
    html_code = f"""
    <div id="game-outer" style="width: 100%; display: flex; flex-direction: column; align-items: center; font-family: 'Arial', sans-serif;">
        <div id="ui-bar" style="width: 600px; display: flex; justify-content: space-between; align-items: center; padding: 10px; background: #000; color: #ff0000; border: 2px solid #333;">
            <div style="display: flex; align-items: center;">
                <span style="margin-right: 10px; font-weight: bold;">HP</span>
                <div style="width: 200px; height: 15px; background: #333; border: 1px solid #ff0000;">
                    <div id="hp-inner" style="width: 100%; height: 100%; background: #ff0000; transition: width 0.3s;"></div>
                </div>
            </div>
            <div id="score-display" style="font-size: 20px; font-weight: bold;">SCORE: 0</div>
        </div>

        <div id="game-container" style="position: relative; width: 600px; height: 200px; background: #eee; overflow: hidden; border: 4px solid #000;">
            <div id="player" style="position: absolute; bottom: 0; left: 50px; width: 50px; height: 50px; background: url('{BLUE_IMG}') no-repeat center/contain; z-index: 10;"></div>
            <div id="obstacle" style="position: absolute; bottom: 0; right: -60px; width: 45px; height: 45px; background: url('{OBS_IMG}') no-repeat center/contain;"></div>
            
            <div id="geass-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, transparent 30%, rgba(255,0,0,0.2) 100%); pointer-events: none; opacity: 0; z-index: 20;"></div>
            
            <div id="game-over" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); display: none; flex-direction: column; justify-content: center; align-items: center; color: white; z-index: 100;">
                <h1 style="color: #ff0000; margin-bottom: 5px;">MISSION FAILED</h1>
                <h3 id="final-score" style="margin-bottom: 20px;">SCORE: 0</h3>
                <div>
                    <button onclick="location.reload()" style="padding: 10px 25px; background: #ff0000; color: white; border: none; cursor: pointer; font-weight: bold; margin: 5px;">RETRY</button>
                    <button style="padding: 10px 25px; background: #444; color: white; border: none; cursor: pointer; font-weight: bold; margin: 5px;">LOBBY</button>
                </div>
            </div>
        </div>

        <button id="skill-btn" onclick="useGeass()" style="width: 600px; margin-top: 10px; padding: 15px; background: #4b0082; color: #fff; border: 2px solid #8a2be2; font-weight: bold; cursor: pointer; text-shadow: 0 0 5px #ff0000;">
            GEASS COMMAND (ENTER)
        </button>
        <p style="color: #666; font-size: 12px; mt: 5px;">[SPACE]: JUMP / [ENTER]: GEASS SKILL</p>
    </div>

    <script>
        const player = document.getElementById("player");
        const obstacle = document.getElementById("obstacle");
        const hpInner = document.getElementById("hp-inner");
        const scoreDisplay = document.getElementById("score-display");
        const gameOverScreen = document.getElementById("game-over");
        const geassOverlay = document.getElementById("geass-overlay");

        let score = 0;
        let hp = 100;
        let isJumping = false;
        let isGeassActive = false;
        let gameActive = true;
        let obstaclePos = 600;

        function jump() {{
            if (isJumping || !gameActive) return;
            isJumping = true;
            let height = 0;
            let upInterval = setInterval(() => {{
                if (height >= 130) {{
                    clearInterval(upInterval);
                    let downInterval = setInterval(() => {{
                        if (height <= 0) {{
                            clearInterval(downInterval);
                            isJumping = false;
                        }}
                        height -= 6;
                        player.style.bottom = height + 'px';
                    }}, 15);
                }}
                height += 6;
                player.style.bottom = height + 'px';
            }}, 15);
        }}

        function useGeass() {{
            if (isGeassActive || !gameActive) return;
            isGeassActive = true;
            geassOverlay.style.opacity = "1";
            
            // 기아스 능력: 장애물 속도 대폭 감소 및 무적
            let originalSpeed = 8;
            let geassDuration = 3000; // 3초

            setTimeout(() => {{
                isGeassActive = false;
                geassOverlay.style.opacity = "0";
            }}, geassDuration);
        }}

        function gameLoop() {{
            if (!gameActive) return;

            // 기아스 발동 시 장애물이 느려짐
            let speed = isGeassActive ? 2 : 8;
            obstaclePos -= speed;

            if (obstaclePos < -50) {{
                obstaclePos = 600;
                score += 10;
                scoreDisplay.innerText = "SCORE: " + score;
            }}
            obstacle.style.left = obstaclePos + 'px';

            // 충돌 판정
            let playerBottom = parseInt(window.getComputedStyle(player).bottom);
            if (obstaclePos < 90 && obstaclePos > 50 && playerBottom < 40) {{
                if (!isGeassActive) {{
                    hp -= 20; // 기아스 미발동 시에만 데미지
                    hpInner.style.width = hp + "%";
                    obstaclePos = -100; // 장애물 초기화
                    
                    if (hp <= 0) {{
                        gameActive = false;
                        document.getElementById("final-score").innerText = "SCORE: " + score;
                        gameOverScreen.style.display = "flex";
                    }}
                }}
            }}

            requestAnimationFrame(gameLoop);
        }}

        window.addEventListener("keydown", (e) => {{
            if (e.code === "Space") {{
                e.preventDefault();
                jump();
            }}
            if (e.code === "Enter") {{
                useGeass();
            }}
        }});

        gameLoop();
    </script>
    """
    components.html(html_code, height=450)

if __name__ == "__main__":
    play_geass_run()
