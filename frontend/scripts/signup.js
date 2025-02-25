import api from "./api.js"; 

document.addEventListener("DOMContentLoaded", async function () {
    const registerForm = document.getElementById("signup-form");
    const genreListContainer = document.getElementById("genre-list");  

    // 장르 목록 불러오기
    async function loadGenres() {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/v1/accounts/genres/");
            if (!response.ok) {
                throw new Error(`API 요청 실패: ${response.status}`);
            }
            const genres = await response.json();  

            genreListContainer.innerHTML = "";  
            genres.forEach(genre => {
                const label = document.createElement("label");
                label.innerHTML = `
                    <input type="checkbox" class="genre-checkbox" value="${genre.id}"> ${genre.name}
                `;
                genreListContainer.appendChild(label);
            });
        } catch (error) {
            console.error("장르 목록을 불러오지 못했습니다:", error);
        }
    }

    await loadGenres();  

    // 장르 선택 개수 제한 (최대 5개)
    genreListContainer.addEventListener("change", function () {
        const checkedGenres = document.querySelectorAll(".genre-checkbox:checked");
        if (checkedGenres.length > 5) {
            checkedGenres[5].checked = false;  
            document.getElementById("genre-error").textContent = "최대 5개의 장르만 선택할 수 있습니다";
        } else {
            document.getElementById("genre-error").textContent = "";
        }
    });

    // 회원가입 요청
    if (registerForm) {
        registerForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const username = document.getElementById("username").value.trim();
            const nickname = document.getElementById("nickname").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();
            const passwordConfirm = document.getElementById("passwordConfirm").value.trim();

            // 에러 메시지 초기화
            document.getElementById("signup-error").textContent = "";
            document.getElementById("password-error").textContent = "";

            // 필수 입력값 체크
            if (!username || !nickname || !email || !password || !passwordConfirm) {
                document.getElementById("signup-error").textContent = "모든 필드를 입력하세요!";
                return;
            }

            // 이메일 형식 체크
            const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email)) {
                document.getElementById("signup-error").textContent = "올바른 이메일 형식을 입력하세요!";
                return;
            }

            // 비밀번호 길이 체크 (최소 8자 이상)
            if (password.length < 8) {
                document.getElementById("password-error").textContent = "비밀번호는 최소 8자 이상이어야 합니다!";
                return;
            }

            // 비밀번호 확인 체크
            if (password !== passwordConfirm) {
                document.getElementById("password-error").textContent = "비밀번호가 일치하지 않습니다!";
                return;
            }

            // 선택된 장르 가져오기
            const selectedGenres = [...document.querySelectorAll(".genre-checkbox:checked")].map(checkbox => parseInt(checkbox.value, 10));

            console.log("선택된 장르 ID:", selectedGenres); 

            try {
                const response = await api.post("", { 
                    username, 
                    nickname, 
                    email, 
                    password,
                    preferred_genres_ids: selectedGenres 
                });

                console.log("회원가입 응답:", response);

                if (response) {
                    alert("회원가입 성공! 이메일 인증 후 로그인하세요.");

                    // 선택한 장르를 로컬스토리지에 저장
                    localStorage.setItem("preferredGenres", JSON.stringify(selectedGenres));
                    
                    setTimeout(() => {
                        window.location.href = "homelogin.html"; 
                    }, 500);
                } else {
                    throw new Error("회원가입 실패");
                }
            } catch (error) {
                document.getElementById("signup-error").textContent = "회원가입 실패. 다시 시도해주세요.";
            }
        });
    }
});
