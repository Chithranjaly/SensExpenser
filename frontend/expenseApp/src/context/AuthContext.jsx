import { createContext, useState, useEffect } from "react";
import API from "../api/authApi";

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  // Check auth on app load
  useEffect(() => {
    API.get("accounts/protected/")
      .then(() => setIsAuthenticated(true))
      .catch(() => setIsAuthenticated(false))
      .finally(() => setLoading(false));
  }, []);

  const loginUser = async (data) => {
    await API.post("accounts/login/", data);
    setIsAuthenticated(true);
  };

  const logoutUser = async () => {
    await API.post("accounts/logout/");
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider
      value={{ isAuthenticated, loginUser, logoutUser, loading }}>
      {children}
    </AuthContext.Provider>
  );
}