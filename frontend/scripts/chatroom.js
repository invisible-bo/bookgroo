document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.querySelector(".toggle-btn");
    const chatHistory = document.querySelector(".chat-history");

    toggleBtn.addEventListener("click", function () {
        chatHistory.classList.toggle("open"); // open 클래스 추가/제거
    });
});
