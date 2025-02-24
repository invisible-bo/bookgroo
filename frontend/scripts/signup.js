import api from "./api.js"; 

document.addEventListener("DOMContentLoaded", async function () {
    const registerForm = document.getElementById("signup-form");
    const genreListContainer = document.getElementById("genre-list");  // 장르 목록을 표시할 div

    // 장르 목록 불러오기 및 체크박스 생성
    async function loadGenres() {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/v1/accounts/genres/");
            if (!response.ok) {
                throw new Error(`API 요청 실패: ${response.status}`);
            }
            const genres = await response.json();  // JSON 데이터 가져오기
            
            genreListContainer.innerHTML = "";  // 기존 내용 초기화
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

    await loadGenres();  // 페이지 로드 시 장르 목록 불러오기

    // 장르 선택 개수 제한 (최대 5개)
    genreListContainer.addEventListener("change", function () {
        const checkedGenres = document.querySelectorAll(".genre-checkbox:checked");
        if (checkedGenres.length > 5) {
            checkedGenres[5].checked = false;  // 5개 초과 선택 시 해제
            document.getElementById("genre-error").textContent = "최대 5개의 장르만 선택할 수 있습니다";
        } else {
            document.getElementById("genre-error").textContent = "";
        }
    });

    // 회원가입 요청
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

                    // 선택한 장르를 localStorage에 저장
                    localStorage.setItem("preferredGenres", JSON.stringify(selectedGenres));
                    
                    setTimeout(() => {
                        window.location.href = "/frontend/pages/homelogin.html"; 
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
