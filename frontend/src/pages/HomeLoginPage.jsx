import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext';
import { loginUser } from '@/api/authApi'; //API 모듈 임포트

export default function HomeLoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { isLoggedIn, login } = useAuth();
  const navigate = useNavigate();

  //로그인 상태면 바로 챗봇 페이지로 이동
  useEffect(() => {
    if (isLoggedIn) {
      navigate('/chatbot');
    }
  }, [isLoggedIn, navigate]);

  //Django 로그인 요청 처리
  const handleLogin = async (e) => {
    e.preventDefault();
    if (!username || !password) {
      alert('아이디와 비밀번호를 입력해주세요.');
      return;
    }

    try {
      const response = await loginUser({ username, password });
      console.log('로그인 성공:', response);

      //AuthContext 업데이트 및 localStorage 저장
      login();  
      localStorage.setItem('username', username);

      alert(`${username}님, BookGroo에 오신 걸 환영합니다!`);
      navigate('/chatbot');
    } catch (error) {
      alert(`로그인 실패: ${error.message || '서버 오류'}`);
    }
  };

  //username 자동 복원
  useEffect(() => {
    const savedUsername = localStorage.getItem('username');
    if (savedUsername) {
      setUsername(savedUsername);
    }
  }, []);

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Welcome to BookGroo</h1>
      <form onSubmit={handleLogin} style={styles.form}>
        <input
          type="text"
          placeholder="ID"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={styles.input}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>로그인</button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    textAlign: 'center',
    padding: '50px',
  },
  title: {
    fontSize: '2.5rem',
    fontWeight: 'bold',
    marginBottom: '20px',
    color: '#2c3e50',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  input: {
    width: '250px',
    padding: '10px',
    margin: '10px 0',
    fontSize: '16px',
    border: '1px solid #ccc',
    borderRadius: '5px',
  },
  button: {
    width: '150px',
    padding: '10px',
    fontSize: '16px',
    fontWeight: 'bold',
    color: '#fff',
    backgroundColor: '#4CAF50',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
};
