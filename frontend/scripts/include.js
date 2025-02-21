document.addEventListener("DOMContentLoaded", function () {
    // 헤더 로드
    fetch("../components/header.html")   //header.html 파일 가져오기
        .then((response) => response.text())    //response 텍스트로 변환
        .then((data) => {
            document.body.insertAdjacentHTML("afterbegin", data);  //헤더를 body 상단에 추가
            setupHeader();  //헤더 설정 (로그아웃 버튼 표시/숨김)
        });

    fetch("../components/footer.html")     //footer.html 파일 가져오기
        .then((response) => response.text())
        .then((data) => {
            document.body.insertAdjacentHTML("beforeend", data);  // footer를 body 하단에 추가
        });    

        
    function setupHeader() {
        const logoutBtn = document.getElementById("logout-btn");  // 로그아웃 버튼 가져오기

        if (localStorage.getItem("access_token")) {       //local storage에 토큰 존재 여부 체크
            logoutBtn.style.display = "block";  //로그인 상태면 로그아웃 버튼 표시
        } else {
            logoutBtn.style.display = "none";  //비로그인 상태면 숨김
        }

        // 로그아웃 버튼 클릭 이벤트
        logoutBtn.addEventListener("click", function () {
            localStorage.removeItem("access_token");     //localStorage저장 토큰 삭제
            localStorage.removeItem("refresh_token");
            localStorage.removeItem("nickname");
            alert("로그아웃 되었습니다.");
            window.location.href = "homelogin.html";  //로그아웃 후 홈으로 이동
        });
    }
});
