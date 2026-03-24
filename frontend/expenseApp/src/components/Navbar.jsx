
import { motion } from "framer-motion";

export default function Navbar() {
  return (
    <motion.nav
      initial={{ y: -40, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="flex justify-between items-center px-8 py-4 bg-white shadow-sm"
    >
      <h1 className="text-xl font-bold">SensExpenser</h1>

      <div className="space-x-4">
        <button className="px-4 py-2 text-gray-700 hover:text-black transition">
          Login
        </button>

        <button className="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition">
          Logout
        </button>
      </div>
    </motion.nav>
  );
}