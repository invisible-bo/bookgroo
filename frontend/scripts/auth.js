import api from "./api.js";  //api.js에서 API 함수 불러오기, 인증 && 권한 관리 모듈 생성

document.addEventListener("DOMContentLoaded", function () {
    // 로그인 기능
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
                    localStorage.setItem("access_token", access_token);             //로그인시 localStorage에 토큰 저장
                    localStorage.setItem("refresh_token", refresh_token);
                    localStorage.setItem("username", response.user.username);       ////로그인시 localStorage에 user profile 저장
                    localStorage.setItem("nickname", response.user.nickname);
                    localStorage.setItem("email", response.user.email);

                    alert(`환영합니다 ${response.user.nickname}님!`); //로그인 성공 시 nick name환영 문구
                    window.location.href = "chatbot.html";  //로그인 성공 시 챗봇 페이지로 이동
                } else {
                    throw new Error("로그인 실패");
                }
            } catch (error) {
                document.getElementById("login-error").textContent = "로그인 실패. 이메일 또는 비밀번호를 확인하세요.";
            }
        });
    }

  
    const registerForm = document.getElementById("signup-form");
    if (registerForm) {
        registerForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            const username = document.getElementById("username").value;
            const nickname = document.getElementById("nickname").value;
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;
            const passwordConfirm = document.getElementById("passwordConfirm").value;

            // 비밀번호 확인 체크
            if (password !== passwordConfirm) {
                document.getElementById("password-error").textContent = "비밀번호가 일치하지 않습니다!";
                return;
            }

            try {
                const response = await api.post("", { username, nickname, email, password });

                if (response) {
                    alert("회원가입 성공! 이메일 인증 후 로그인하세요.");
                    window.location.href = "homelogin.html";  //회원가입 성공 후 로그인 페이지로 이동X작동안됨
                } else {
                    throw new Error("회원가입 실패");
                }
            } catch (error) {
                document.getElementById("signup-error").textContent = "회원가입 실패. 다시 시도해주세요.";
            }
        });
    }

    // 자동 로그인 체크 (로그인된 사용자는 chatbot.html로 이동)
    if (localStorage.getItem("access_token") && window.location.pathname.includes("homelogin.html")) {
        window.location.href = "chatbot.html";
    }
});

const auth = {
    isLoggedIn: () => {
        return !!localStorage.getItem("access_token");  // 로그인 여부 확인
    },
    logout: () => {
        localStorage.removeItem("access_token");
        window.location.href = "login.html";  // 로그아웃 후 로그인 페이지로 이동
    }
};

export default auth;  // 모듈화
