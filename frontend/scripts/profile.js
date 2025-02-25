import auth from "./auth.js"; // 인증 모듈 가져오기

document.addEventListener("DOMContentLoaded", function () {
    if (!auth.isLoggedIn()) {
        alert("로그인이 필요합니다.");
        window.location.href = "homelogin.html";
        return;
    }

  
    const nicknameInput = document.getElementById("nickname-input");
    const nicknameSpan = document.getElementById("nickname");
    const usernameSpan = document.getElementById("username");
    const emailSpan = document.getElementById("email");

    nicknameInput.value = localStorage.getItem("nickname") || "닉네임 없음";
    usernameSpan.textContent = localStorage.getItem("username") || "알 수 없음";
    emailSpan.textContent = localStorage.getItem("email") || "알 수 없음";

    // 장르 정보 불러오기
    const selectedGenres = JSON.parse(localStorage.getItem("preferredGenres")) || [];
    const genreContainer = document.getElementById("selected-genres");

    if (selectedGenres.length === 0) {
        genreContainer.textContent = "선택한 장르가 없습니다.";
    } else {
        genreContainer.innerHTML = selectedGenres
            .map(genre => `<span class="genre-tag">${genre.name}</span>`)
            .join(", ");
    }

    // 닉네임 수정 
    const editBtn = document.getElementById("edit-nickname-btn");
    const saveBtn = document.getElementById("save-nickname-btn");

    editBtn.addEventListener("click", function () {
        nicknameInput.removeAttribute("disabled");
        nicknameInput.focus();
        editBtn.style.display = "none";
        saveBtn.style.display = "inline-block";
    });

    saveBtn.addEventListener("click", function () {
        const newNickname = nicknameInput.value.trim();

        if (newNickname === "") {
            alert("닉네임을 입력하세요.");
            return;
        }

        localStorage.setItem("nickname", newNickname);
        nicknameInput.setAttribute("disabled", "true");
        editBtn.style.display = "inline-block";
        saveBtn.style.display = "none";
    });
});
