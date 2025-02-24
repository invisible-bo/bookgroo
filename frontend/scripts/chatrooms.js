async function getOrCreateChatroom() {
    console.log("getOrCreateChatroom() 실행됨.");

    let chatrooms = await fetchChatrooms();

    if (chatrooms.length === 0) {
        console.log("채팅방이 없음 → 새 채팅방 생성 시도");
        const newChatroom = await createChatroom();
        
        if (!newChatroom || !newChatroom.id) {
            console.error("채팅방 생성 실패!");
            return null;
        }

        // 새 채팅방 ID를 현재 채팅방 ID로 업데이트
        window.currentChatroomId = newChatroom.id;
        console.log(`새로운 채팅방 ID 설정됨: ${window.currentChatroomId}`);

        return newChatroom;
    } else {
        console.log("기존 채팅방 존재:", chatrooms);
        
        window.currentChatroomId = chatrooms[chatrooms.length - 1].id;
        console.log(`기존 채팅방 중 최신 채팅방 ID 설정됨: ${window.currentChatroomId}`);

        return chatrooms[chatrooms.length - 1];
    }
}

// 채팅방 목록 가져오기
async function fetchChatrooms() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/v2/chatrooms/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            }
        });

        if (!response.ok) {
            throw new Error("채팅방 목록을 불러오지 못했습니다.");
        }

        const chatrooms = await response.json();
        console.log("채팅방 목록:", chatrooms);
        return chatrooms;
    } catch (error) {
        console.error("채팅방 불러오기 실패:", error);
        return [];
    }
}

// 새 채팅방 생성
export async function createChatroom() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/v2/chatrooms/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            },
            body: JSON.stringify({
                user_id_id: 1,  // _id_id로 변경
                title: "New chatroom"
            }),
        });

        if (!response.ok) {
            throw new Error("채팅방 생성 실패");
        }

        const newChatroom = await response.json();
        console.log("new 채팅방 생성 성공:", newChatroom);

        return newChatroom;
    } catch (error) {
        console.error("채팅방 생성 실패:", error);
        return null;
    }
}

// 서버에서 메시지 가져오기
export async function fetchMessages(chatroomId = window.currentChatroomId) {
    if (!chatroomId) {
        console.error("채팅방 ID가 없습니다!");
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/api/v2/chatrooms/${chatroomId}/messages/`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            }
        });

        if (!response.ok) {
            throw new Error("메시지를 불러오지 못했습니다.");
        }

        const messages = await response.json();
        console.log("받은 메시지 목록:", messages);

        // 화면에 메시지 렌더링
        displayMessages(messages);
    } catch (error) {
        console.error("메시지 가져오기 실패:", error);
    }
}

// 메시지 화면에 표시
function displayMessages(messages) {
    const chatBox = document.querySelector(".chat-box");
    chatBox.innerHTML = ""; // 기존 메시지 삭제 후 새로 추가

    const nickname = localStorage.getItem("nickname") || "사용자";

    messages.forEach(message => {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message");

        

        // true false 1 0 변환
        if (Number(message.user_or_bot) === 1) {
            messageElement.classList.add("user-message");
            
            messageElement.innerHTML = `<strong>🍀${nickname}:</strong> ${message.message_context}`;
        } else {
            messageElement.classList.add("bot-message");
            messageElement.innerHTML = `<strong>📚<span style="color: dodgerblue;">Groo2</span>:</strong> ${message.message_context}`;        }

        chatBox.appendChild(messageElement);
    });

    chatBox.scrollTop = chatBox.scrollHeight;
}

// user msg 서버로 전송
async function sendMessage(chatroomId, message) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/v2/chatrooms/${chatroomId}/messages/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            },
            body: JSON.stringify({
                message_context: message,
                user_or_bot: 1
            }),
        });

        if (!response.ok) {
            throw new Error("메시지 전송 실패");
        }

        const newMessage = await response.json();
        console.log("보낸 메시지:", newMessage);

        fetchMessages(chatroomId);
    } catch (error) {
        console.error("메시지 전송 오류:", error);
    }
}

// 페이지 로드 시 채팅방 가져오기 & 이벤트 리스너 추가
document.addEventListener("DOMContentLoaded", async function () {
    console.log("chatrooms.js 로드 완료");

    // 채팅방을 가져오거나 생성
    const chatroom = await getOrCreateChatroom();
    if (!chatroom || !chatroom.id) {
        console.error("채팅방을 가져오지 못했습니다.");
        return;
    }

    console.log("선택된 채팅방 ID:", chatroom.id);
    fetchMessages(chatroom.id); // 채팅방 메시지 가져오기

    // 메시지 입력 & 전송
    document.querySelector(".chat-input").addEventListener("submit", function (event) {
        event.preventDefault();
        const messageInput = document.querySelector(".chat-input input");
        const message = messageInput.value.trim();

        if (message) {
            sendMessage(chatroom.id, message);
            messageInput.value = "";
        }
    });
});
