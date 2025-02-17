import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App.jsx';

// React 18 표준 렌더링 방식
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
  