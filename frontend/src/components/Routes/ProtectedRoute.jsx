import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../context/AuthContext';
import { isTokenExpired, getToken } from '../../utils/auth';

const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading) {
      // Check if user exists and token is not expired
      const token = getToken();
      if (!user || !token || isTokenExpired(token)) {
        router.push('/login');
      }
    }
  }, [user, loading, router]);

  // Show nothing while checking authentication status
  if (loading) {
    return <div>Loading...</div>;
  }

  // If user is authenticated and token is valid, render the protected content
  const token = getToken();
  if (user && token && !isTokenExpired(token)) {
    return children;
  }

  // If not authenticated or token is expired, return null (the redirect happens in useEffect)
  return null;
};

export default ProtectedRoute;