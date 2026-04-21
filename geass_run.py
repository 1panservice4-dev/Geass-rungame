import streamlit as st
import streamlit.components.v1 as components

def play_geass_run():
    # 이미지 데이터 생략 (기존 데이터 유지)
    BLUE_IMG = "..." 
    OBS_IMG = "..."

    html_code = f"""
    <div style="background: #333; color: white; padding: 20px; text-align: center;">
        <h1>GEASS RUN 가동 중!</h1>
        <p>게임 화면이 아래에 나타나지 않으면 페이지를 새로고침 하세요.</p>
    </div>
    <style>
        /* 기존 CSS 코드들... */
        @keyframes popUp {{ 0% {{ bottom: -100px; }} 100% {{ bottom: 0px; }} }}
    </style>
    <div id="game-container">
        </div>
    """
    
    # 이 부분이 핵심입니다! Streamlit 전용 출력 함수
    components.html(html_code, height=600, scrolling=True)

if __name__ == "__main__":
    play_geass_run()
