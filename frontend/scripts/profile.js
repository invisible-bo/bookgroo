import auth from "./auth.js"; // 인증 모듈 가져오기

document.addEventListener("DOMContentLoaded", function () {
    if (!auth.isLoggedIn()) {
        alert("로그인이 필요합니다.");
        window.location.href = "homelogin.html";
        return;
    }

    // 로그인된 사용자 정보 표시
    document.getElementById("nickname").textContent = localStorage.getItem("nickname") || "알 수 없음";
    document.getElementById("username").textContent = localStorage.getItem("username") || "알 수 없음";
    document.getElementById("email").textContent = localStorage.getItem("email") || "알 수 없음";

    // ✅ 사용자가 선택한 장르 목록 가져오기
    const selectedGenres = JSON.parse(localStorage.getItem("preferredGenres")) || [];
    const genreContainer = document.getElementById("selected-genres");

    if (selectedGenres.length === 0) {
        genreContainer.textContent = "선택한 장르가 없습니다.";
        return;
    }

    // ✅ 장르 데이터에서 name 값만 추출하여 UI에 추가
    genreContainer.innerHTML = selectedGenres
        .map(genre => `<span class="genre-tag">${genre.name}</span>`)
        .join(", ");
});
