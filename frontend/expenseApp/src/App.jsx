import { Routes, Route, Navigate } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "./context/AuthContext";

import Login from "./components/auth/Login";
import Home from "./pages/Home";

function App() {
  const { isAuthenticated, loading } = useContext(AuthContext);

  // wait until auth check finishes
  if (loading) return <p>Loading...</p>;

  return (
    <Routes>
      {/*  Public Route */}
      <Route
        path="/login"
        element={
          isAuthenticated ? <Navigate to="/" /> : <Login />
        }
      />

      {/* Protected Route */}
      <Route
        path="/"
        element={
          isAuthenticated ? <Home /> : <Navigate to="/login" />
        }
      />
    </Routes>
  );
}

export default App;