document.addEventListener("DOMContentLoaded", function () {

    const toggleBtn = document.querySelector(".toggle-btn");
    const chatHistory = document.querySelector(".chat-history");

    // 사이드바 열기/닫기
    toggleBtn.addEventListener("click", function () {
        chatHistory.classList.toggle("open");
    });
});    