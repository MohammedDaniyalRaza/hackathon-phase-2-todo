import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../context/AuthContext';

const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !user) {
      router.push('/login');
    }
  }, [user, loading, router]);

  // Show nothing while checking authentication status
  if (loading) {
    return <div>Loading...</div>;
  }

  // If user is authenticated, render the protected content
  if (user) {
    return children;
  }

  // If not authenticated, return null (the redirect happens in useEffect)
  return null;
};

export default ProtectedRoute;