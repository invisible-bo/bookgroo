// src/contexts/AuthContext.jsx
import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  // ✅ 초기값: localStorage에서 직접 가져옴
  const [isLoggedIn, setIsLoggedIn] = useState(
    () => localStorage.getItem('isLoggedIn') === 'true'
  );

  // ✅ 로그인: localStorage에 true 저장
  const login = () => {
    localStorage.setItem('isLoggedIn', 'true');
    setIsLoggedIn(true);
  };

  // ✅ 로그아웃: localStorage 초기화
  const logout = () => {
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
  };

  // ✅ useEffect로 상태 유지 (예비 복구용)
  useEffect(() => {
    const storedStatus = localStorage.getItem('isLoggedIn') === 'true';
    if (storedStatus !== isLoggedIn) {
      setIsLoggedIn(storedStatus);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ isLoggedIn, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
