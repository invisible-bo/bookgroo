const api = {                                  // backend로 post 요청 보내는 모듈 생성
    async post(url, data) {
        return fetch(`http://127.0.0.1:8000/api/v1/accounts/${url}`, {      //fetch API로 django server에 post 요청
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        }).then((response) => response.json());         //json 형태로 변환
    },

    async get(url) {  
        return fetch(`http://127.0.0.1:8000/api/v1/accounts/${url}`, {      
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        }).then(response => response.json());
    }
};

export default api;