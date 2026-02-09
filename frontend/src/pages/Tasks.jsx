import { useAuth } from '../context/AuthContext';
import ProtectedRoute from '../components/Routes/ProtectedRoute';
import TaskList from '../components/Tasks/TaskList';

const TasksPage = () => {
  const { user } = useAuth();

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-50">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <h1 className="text-xl font-semibold text-gray-800">Todo App</h1>
              </div>
              <div className="flex items-center">
                <span className="text-gray-700 mr-4">Welcome, {user?.email}</span>
              </div>
            </div>
          </div>
        </nav>
        
        <main>
          <TaskList />
        </main>
      </div>
    </ProtectedRoute>
  );
};

export default TasksPage;