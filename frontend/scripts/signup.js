import api from "./api.js"; 

document.addEventListener("DOMContentLoaded", function () {
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
                
                console.log("회원가입 응답:", response);

                if (response) {
                    alert("회원가입 성공! 이메일 인증 후 로그인하세요.");
                    setTimeout(() => {
                        window.location.href = "/frontend/pages/homelogin.html"; 
                    }, 500);  //회원가입 성공 후 로그인 페이지로 이동X작동안됨
                } else {
                    throw new Error("회원가입 실패");
                }
            } catch (error) {
                document.getElementById("signup-error").textContent = "회원가입 실패. 다시 시도해주세요.";
            }
        });
    }
});
