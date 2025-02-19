import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/v1/accounts';

//회원가입 (POST)
export const registerUser = async (userData) => {
    try {
      const response = await axios.post(`${API_URL}/`, userData);
      return response.data;
    } catch (error) {
      throw error.response?.data || { message: '서버 오류' };
    }
  };

//로그인 (POST)
export const loginUser = async (credentials) => {
    try {
      const response = await axios.post(`${API_URL}/login/`, credentials, {
        withCredentials: true,  // 쿠키 전달
      });
      return response.data;
    } catch (error) {
      throw error.response?.data || { message: '로그인 실패' };
    }
  };
  
  //로그아웃 (POST)
  export const logoutUser = async (refreshToken) => {
    try {
      const response = await axios.post(`${API_URL}/logout/`, { refresh_token: refreshToken }, {
        withCredentials: true,  // 쿠키 포함
      });
      return response.data;
    } catch (error) {
      throw error.response?.data || { message: '로그아웃 실패' };
    }
  };

//이메일 인증 (GET)
export const activateUser = async (token) => {
  try {
    const response = await axios.get(`${API_URL}/emailauth/${token}/`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { message: '서버 오류' };
  }
};



// JWT 재발급 (POST)
export const refreshToken = async (refreshToken) => {
    try {
      const response = await axios.post(`${API_URL}/token/refresh/`, {
        refresh: refreshToken,
      });
      return response.data;
    } catch (error) {
      throw error.response?.data || { message: '토큰 재발급 실패' };
    }
  };