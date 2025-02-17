// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from '@/contexts/AuthContext';
import Header from '@/components/layout/Header';
import Footer from '@/components/layout/Footer';
import HomeLoginPage from '@/pages/HomeLoginPage';
import SignUpPage from '@/pages/SignUpPage';
import ProfilePage from '@/pages/ProfilePage';
import ChatbotPage from '@/pages/ChatbotPage';
import PrivateRoute from '@/components/PrivateRoute';
import './App.css';

function App() {
  return (
    <AuthProvider> {/* Router 바깥에 위치 필수 */}
      <Router>
        <Header />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<HomeLoginPage />} />
            <Route path="/signup" element={<SignUpPage />} />
            <Route path="/profile" element={
              <PrivateRoute>
                <ProfilePage />
              </PrivateRoute>
            } />
            <Route path="/chatbot" element={
              <PrivateRoute>
                <ChatbotPage />
              </PrivateRoute>
            } />
          </Routes>
        </main>
        <Footer />
      </Router>
    </AuthProvider>
  );
}

export default App;
