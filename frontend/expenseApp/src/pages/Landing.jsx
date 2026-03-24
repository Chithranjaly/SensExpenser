import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Footer from "../components/Footer";

export default function Landing() {
  return (
    <div className="bg-gray-50 text-gray-800 min-h-screen flex flex-col">
      <Navbar />

      <main className="flex-grow">
        <Hero />
        <Features />
      </main>

      <Footer />
    </div>
  );
}