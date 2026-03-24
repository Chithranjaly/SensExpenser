// components/Features.jsx

export default function Features() {
  return (
    <section className="py-20 px-6 max-w-6xl mx-auto">
      <h2 className="text-3xl font-bold text-center mb-12">
        Why Choose SensExpenser?
      </h2>

      <div className="grid md:grid-cols-3 gap-8">
        <div className="p-6 bg-white rounded-xl shadow hover:shadow-md transition">
          <h3 className="font-semibold text-lg">AI Categorization</h3>
          <p className="text-gray-600 mt-2">
            Automatically classify expenses using AI.
          </p>
        </div>

        <div className="p-6 bg-white rounded-xl shadow hover:shadow-md transition">
          <h3 className="font-semibold text-lg">Real-time Insights</h3>
          <p className="text-gray-600 mt-2">
            Understand your spending instantly.
          </p>
        </div>

        <div className="p-6 bg-white rounded-xl shadow hover:shadow-md transition">
          <h3 className="font-semibold text-lg">Secure & Private</h3>
          <p className="text-gray-600 mt-2">
            Your data is safe and encrypted.
          </p>
        </div>
      </div>
    </section>
  );
}