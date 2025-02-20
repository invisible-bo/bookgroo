import api from "./api.js";

document.addEventListener("DOMContentLoaded", function () {
    const logoutBtn = document.getElementById("logout");

    if (logoutBtn) {
        logoutBtn.style.display = "block";
        logoutBtn.addEventListener("click", async function () {
            try {
                const refresh_token = localStorage.getItem("refresh_token");
                await api.post("logout/", { refresh_token });

                localStorage.removeItem("access_token");
                localStorage.removeItem("refresh_token");

                window.location.href = "homelogin.html";
            } catch (error) {
                console.error("로그아웃 실패:", error);
            }
        });
    }
});
