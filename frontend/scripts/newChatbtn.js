document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ newChatbtn.js 로드 완료");

    setTimeout(() => {  // 🚀 HTML 요소가 완전히 로드된 후 실행하도록 약간의 딜레이 추가
        const newChatBtn = document.getElementById("newChatbtn");
        const chatBox = document.querySelector(".chat-box");

        if (!newChatBtn) {
            console.error("❌ 'newChatbtn' 버튼을 찾을 수 없습니다. HTML 파일에서 ID가 정확한지 확인하세요.");
            return;
        }

        if (!chatBox) {
            console.error("❌ '.chat-box' 요소를 찾을 수 없습니다.");
            return;
        }

        newChatBtn.addEventListener("click", function () {
            console.log("➕ 새 채팅방 버튼 클릭됨");

            // 🚀 채팅창 초기화
            chatBox.innerHTML = ""; 

            console.log("✅ 채팅창 초기화 완료 (모든 메시지 삭제됨)");
        });
    }, 100); // 100ms 딜레이 (브라우저가 요소를 렌더링할 시간을 줌)
});
