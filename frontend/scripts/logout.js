import api from "./api.js";  //api.js에서 API 함수 불러오기, backend에 로그아웃 요청

document.addEventListener("DOMContentLoaded", function () {
    const logoutBtn = document.getElementById("logout");

    if (logoutBtn) {
        logoutBtn.style.display = "block";
        logoutBtn.addEventListener("click", async function () {
            try {
                const refresh_token = localStorage.getItem("refresh_token");   //refresh token 가져오고 서버에 로그아웃 요청
                await api.post("logout/", { refresh_token });

                localStorage.removeItem("access_token");    //로컬에 저장된 jmt토큰 삭제
                localStorage.removeItem("refresh_token");

                window.location.href = "homelogin.html";   //homelogin.html로 리다이렉션
            } catch (error) {
                console.error("로그아웃 실패:", error);   //오류시 console오류 출력
            }
        });
    }
});