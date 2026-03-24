import { Routes, Route, Navigate } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "./context/AuthContext";

import Login from "./components/auth/Login";
import Landing from "./pages/Landing";
import Home from "./pages/Home";

function App() {
  const { isAuthenticated, loading } = useContext(AuthContext);

  if (loading) return <p>Loading...</p>;

  return (
    <Routes>

      {/* 🌐 Public Landing Page */}
      <Route path="/" element={<Landing />} />

      {/* 🔐 Login */}
      <Route
        path="/login"
        element={
          isAuthenticated ? <Navigate to="/dashboard" /> : <Login />
        }
      />

      {/* 🔒 Protected Dashboard */}
      <Route
        path="/dashboard"
        element={
          isAuthenticated ? <Home /> : <Navigate to="/login" />
        }
      />

    </Routes>
  );
}

export default App;