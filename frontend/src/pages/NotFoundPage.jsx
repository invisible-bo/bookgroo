import React from 'react';
import { Link } from 'react-router-dom';
const NotFoundPage = () => {
    return (
      <div className="not-found-container">
        <h1>404 - page not found </h1>
        <Link to="/">Home</Link>
      </div>
    );
  };
  
  export default NotFoundPage;
  
