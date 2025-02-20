const api = {
    async post(url, data) {
        return fetch(`http://127.0.0.1:8000/api/v1/accounts/${url}`, { 
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        }).then((response) => response.json());
    },
};

export default api;  
