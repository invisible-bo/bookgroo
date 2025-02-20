document.addEventListener("DOMContentLoaded", function () {
    // 헤더 로드
    fetch("../components/header.html")
        .then((response) => response.text())
        .then((data) => {
            document.body.insertAdjacentHTML("afterbegin", data);  //헤더를 body 상단에 추가
            setupHeader();  //헤더 설정 (로그아웃 버튼 표시/숨김)
        });

    fetch("../components/footer.html")
        .then((response) => response.text())
        .then((data) => {
            document.body.insertAdjacentHTML("beforeend", data);  // 
        });    

        
    function setupHeader() {
        const logoutBtn = document.getElementById("logout-btn");

        if (localStorage.getItem("access_token")) {
            logoutBtn.style.display = "block";  //로그인 상태면 로그아웃 버튼 표시
        } else {
            logoutBtn.style.display = "none";  //비로그인 상태면 숨김
        }

        // 로그아웃 버튼 클릭 이벤트
        logoutBtn.addEventListener("click", function () {
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            localStorage.removeItem("nickname");
            alert("로그아웃 되었습니다.");
            window.location.href = "homelogin.html";  //로그아웃 후 홈으로 이동
        });
    }
});
