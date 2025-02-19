import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { activateUser } from '../api/authApi';

function Activate() {
  const { token } = useParams();
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchActivation = async () => {
      try {
        const response = await activateUser(token);
        setMessage(response.message || '이메일 인증이 완료되었습니다.');
      } catch (error) {
        setMessage(error.message || '이메일 인증 실패');
      }
    };
    fetchActivation();
  }, [token]);

  return (
    <div>
      <h2>이메일 인증 결과</h2>
      <p>{message}</p>
    </div>
  );
}

export default Activate;