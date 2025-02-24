import { createChatroom, fetchMessages } from "./chatrooms.js";

document.getElementById("newChatbtn").addEventListener("click", async function () {
    console.log("➕ newChatbtn clicked");

    //  새 채팅방 생성
    const newChatroom = await createChatroom();
    console.log("생성된 채팅방 정보:", newChatroom); // newChatroom 확인

    if (!newChatroom || !newChatroom.id) {
        console.error("새 채팅방을 생성할 수 없습니다. newChatroom 값:", newChatroom);
        return;
    }

    // 현재 채팅방 ID 업데이트
    window.currentChatroomId = newChatroom.id;
    console.log(`새로운 채팅방 ID로 업데이트됨: ${window.currentChatroomId}`);

    // 기존 채팅 클리어
    const chatBox = document.querySelector(".chat-box");
    chatBox.innerHTML = "";  

    // 채팅방 메시지를 가져와서 화면 갱신
    fetchMessages(window.currentChatroomId);  // 새 채팅방의 데이터를 가져옴

});
