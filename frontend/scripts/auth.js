const auth = {
    isLoggedIn: () => {
        return !!localStorage.getItem("access_token");  // 로그인 여부 확인
    },
};

export default auth;  // 모듈화
