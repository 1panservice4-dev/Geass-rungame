import IPython.display
import base64

def play_geass_run():
    # 1. 너무 길었던 이미지 데이터를 변수로 분리했습니다.
    BLUE_IMG = "data:image/png;base64,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"
    OBS_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAB8klEQVR4nO2Yv0vDQBjHn8S9QXByFAdnB0cHJ0cHZwcHB0cHZwcHB0cHZwcHB0fBydHBydHBydHBydHBydHBydHBydHByf0DOnSJpEnSptf2vS88SAtp8vnc98f7XpI6Ozt/Sshms9vNZvMskUis6fV6vUqlUnE8HndO0v1+v9NoNLp+v78vCMLZ6urq9ubm5tH6+no8Ozs7f9oZBAH/H9vPz8/bV1dXH61W68ZiseDhcLhVq9UuTk5O7vAnYI1AILC8vr6+vbm5eZ9MJm9isRhcXFzc8Cdgj7m5ueXFxcXtcrl86fP5IJPJ7Ofz+Yvj4+N7O8F6wBohS0tL97u7u/fFYvG8Xq9DPB7fzefz58fHx64SCAK+mU6nN7e2tu6LxeKlUgr9fv/S8vLyZSKRWHeV9IDVAn57e3v3xWLxXCmFSqXyZWVl5fzo6GjHVTIIAs6Mjo4ubm5u3pdKpUulFCKRyE4mk9mX9IC/BPzOzs7u7u7unvSA77ZfXFzcLpfLl76/BAH7EonE7fX19Z0S8M3ExMTK8vLypat+fA6wz9TU1PrGxsbOnxMgCHgjEAis8D0AtvB9AnuMjo4u8j0An+R7BOwRCoXW+B4An/geAV/U6/VrvgfApf/77+D7A/Yxm83Y7u7u+TfE9/jRPhf68AAAAABJRU5ErkJggg=="

    # 2. html_code 변수에 웹 코드를 문자열로 담습니다. (f-string 사용)
    # CSS의 중괄호 { }를 파이썬 f-string에서 쓰려면 {{ }} 처럼 두 번 써야 합니다.
    html_code = f"""
    <style>
        #game-container {{ position: relative; width: 600px; height: 200px; background: #eee; overflow: hidden; border: 2px solid #333; margin: 0 auto; }}
        #player {{ position: absolute; bottom: 0; left: 50px; width: 40px; height: 40px; background: url('{BLUE_IMG}') no-repeat center/contain; z-index: 10; }}
        #obstacle {{ position: absolute; bottom: 0; right: -50px; width: 40px; height: 40px; background: url('{OBS_IMG}') no-repeat center/contain; }}
        
        /* 29라인 오류 해결 지점: {{ }} 로 감싸서 파이썬 문법과 분리 */
        @keyframes popUp {{ 0% {{ bottom: -100px; }} 100% {{ bottom: 0px; }} }}
        
        #gameover {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); display: none; flex-direction: column; justify-content: center; align-items: center; color: white; animation: popUp 0.5s ease-out; z-index: 100; }}
        .btn {{ padding: 10px 20px; background: #f00; color: #fff; cursor: pointer; border: none; border-radius: 5px; margin: 5px; font-weight: bold; }}
    </style>

    <div id="game-container">
        <div id="player"></div>
        <div id="obstacle"></div>
        <div id="gameover">
            <h2>GAME OVER</h2>
            <button class="btn" onclick="location.reload()">RETRY</button>
        </div>
    </div>

    <script>
        // 여기에 게임 로직 자바스크립트가 들어갑니다.
        console.log("Game Start!");
    </script>
    """

    # 3. 마지막으로 화면에 출력합니다.
    IPython.display.display(IPython.display.HTML(html_code))

# 함수 실행
if __name__ == "__main__":
    play_geass_run()
