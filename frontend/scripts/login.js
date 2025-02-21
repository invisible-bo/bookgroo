import api from "./api.js";  // API 요청 모듈 가져오기

document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("access_token") && window.location.pathname.includes("homelogin.html")) {
        window.location.href = "chatbot.html";
    } //이미 로그인된 경우 chatbot.html로 이동

    //로그인 폼
    const loginForm = document.getElementById("login-form");

    if (loginForm) {
        loginForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            const username = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            try {
                const response = await api.post("login/", { username, password });

                if (response.jwt_token) {
                    const { access_token, refresh_token } = response.jwt_token;      
                    localStorage.setItem("access_token", access_token);
                    localStorage.setItem("refresh_token", refresh_token);
                    localStorage.setItem("username", response.user.username);
                    localStorage.setItem("nickname", response.user.nickname);
                    localStorage.setItem("email", response.user.email);

                    alert(`환영합니다 ${response.user.nickname}님!`);
                    window.location.href = "chatbot.html";
                } else {
                    throw new Error("로그인 실패");
                }
            } catch (error) {
                document.getElementById("login-error").textContent = "로그인 실패. 이메일 또는 비밀번호를 확인하세요.";
            }
        });
    }
});
