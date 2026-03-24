import { motion } from "framer-motion";

export default function Hero() {
  return (
    <section className="text-center py-24 px-6 bg-gradient-to-b from-white to-gray-100">
      
      <motion.h1
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="text-5xl font-bold leading-tight"
      >
        Smart Expense Tracking <br />
        <span className="text-indigo-600">Powered by AI</span>
      </motion.h1>

      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="mt-6 text-lg text-gray-600 max-w-xl mx-auto"
      >
        Track, analyze, and optimize your spending effortlessly.
        Get insights that actually matter.
      </motion.p>

      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="mt-8 flex justify-center gap-4"
      >
        <button className="px-6 py-3 bg-indigo-600 text-white rounded-xl hover:scale-105 transition">
          Get Started
        </button>

        <button className="px-6 py-3 border rounded-xl hover:bg-gray-100 transition">
          Learn More
        </button>
      </motion.div>
    </section>
  );
}