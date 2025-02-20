document.addEventListener("DOMContentLoaded", function () {
    if (!localStorage.getItem("access_token")) {
        window.location.href = "homelogin.html"; // 로그인 안 한 경우 홈로그인 페이지로 리다이렉트
    }
});
