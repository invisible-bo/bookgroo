import auth from "./auth.js"; // 인증 모듈 가져오기

document.addEventListener("DOMContentLoaded", async function () {
    if (!auth.isLoggedIn()) {
        alert("로그인이 필요합니다.");
        window.location.href = "homelogin.html";
        return;
    }

    // 로그인된 사용자 정보 표시
    document.getElementById("nickname").textContent = localStorage.getItem("nickname") || "알 수 없음";
    document.getElementById("username").textContent = localStorage.getItem("username") || "알 수 없음";
    document.getElementById("email").textContent = localStorage.getItem("email") || "알 수 없음";

    // 사용자가 선택한 장르 목록 가져오기
    const selectedGenreIds = JSON.parse(localStorage.getItem("preferredGenres")) || [];
    const genreContainer = document.getElementById("selected-genres");

    if (selectedGenreIds.length === 0) {
        genreContainer.textContent = "선택한 장르가 없습니다.";
        return;
    }

    try {
        // 서버에서 전체 장르 목록 가져오기
        const response = await fetch("http://127.0.0.1:8000/api/v1/accounts/genres/");
        if (!response.ok) {
            throw new Error(`API 요청 실패: ${response.status}`);
        }
        const genres = await response.json();

        // 선택한 장르 ID에 해당하는 장르명 찾기
        const selectedGenreNames = genres
            .filter(genre => selectedGenreIds.includes(genre.id))
            .map(genre => genre.name);

        // 장르 목록 표시
        genreContainer.innerHTML = selectedGenreNames.map(name => `<span class="genre-tag">${name}</span>`).join(", ");
    } catch (error) {
        console.error("장르 정보를 가져오는 데 실패했습니다:", error);
        genreContainer.textContent = "장르 정보를 불러오지 못했습니다.";
    }
});
