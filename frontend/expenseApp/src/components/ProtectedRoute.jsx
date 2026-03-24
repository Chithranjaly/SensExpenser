import { Navigate, useLocation } from "react-router-dom";

export default function ProtectedRoute({ children, isAuthenticated }) {
  const location = useLocation();

  return isAuthenticated ? (
    children
  ) : (
    <Navigate to="/login" state={{ from: location }} />
  );
}