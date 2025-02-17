// src/components/layout/Header.jsx
import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext'; 
import './Header.css';
import logo from '/Logo.png';

const Header = () => {
  const { isLoggedIn, login, logout } = useAuth();

  // ✅ 새로고침 시 로그인 상태 복원
  useEffect(() => {
    const storedStatus = localStorage.getItem('isLoggedIn') === 'true';
    if (storedStatus) {
      login();
    }
  }, [login]);

  return (
    <div className="header-container">
      <header className="header">
        {/* 로고 */}
        <Link to="/" className="logo-container">
          <img src={logo} alt="BookGroo Logo" className="logo" />
        </Link>

        {/* 네비게이션 */}
        <nav className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/signup">Sign up</Link>
          {/* ✅ 로그인 시에만 프로필과 로그아웃 표시 */}
          {isLoggedIn && (
            <>
              <Link to="/profile">Profile</Link>
              <button onClick={logout} className="logout-btn">
                Logout
              </button>
            </>
          )}
        </nav>
      </header>
    </div>
  );
};

export default Header;
