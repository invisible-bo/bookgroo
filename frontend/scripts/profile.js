import auth from "../scripts/auth.js"; // 인증 모듈 가져오기

document.addEventListener("DOMContentLoaded", function () {

    if (!auth.isLoggedIn()) {      //로그인 여부 확인
        alert("로그인이 필요합니다."); // 로그인하지 않은 경우 경고 메시지 표시
        window.location.href = "homelogin.html"; // 로그인 페이지로 이동
        return;
    }

    //로그인된 사용자 정보 가져오기 (localStorage에서 불러오기)
    document.getElementById("nickname").textContent = localStorage.getItem("nickname") || "알 수 없음";
    document.getElementById("username").textContent = localStorage.getItem("username") || "알 수 없음"; 
    document.getElementById("email").textContent = localStorage.getItem("email") || "알 수 없음";
    
});
