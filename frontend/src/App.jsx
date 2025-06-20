import React, { useState } from "react";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);

  const fetchWeather = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/weather?city=${city}`);
      const data = await res.json();
      setWeather(data);
    } catch (err) {
      setWeather({ error: "Error fetching weather" });
    }
  };

  return (
    <div className="bg-gradient-to-r from-blue-100 to-indigo-200 min-h-screen flex flex-col justify-center items-center font-sans">
      <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-xl text-center">
        <h1 className="text-3xl font-bold mb-6 text-indigo-700">
          🌤️ Weather Information
        </h1>

        <form onSubmit={fetchWeather} className="space-y-4">
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Enter city name"
            required
            className="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
          <button
            type="submit"
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-200"
          >
            Get Weather & Notify
          </button>
        </form>

        {weather && !weather.error && (
          <div className="mt-6 p-4 bg-blue-50 border border-blue-300 rounded-lg shadow-sm">
            <div className="text-2xl font-semibold text-gray-800">
              {weather.icon} {weather.location}
            </div>
            <div className="text-gray-600 mt-2">{weather.description}</div>
            <div className="text-xl font-bold text-indigo-700 mt-1">
              {weather.temp}°C
            </div>
          </div>
        )}

        {weather?.error && (
          <div className="mt-6 text-red-600 font-medium">
            ⚠️ {weather.error}
          </div>
        )}
      </div>

      <footer className="text-sm text-gray-500 mt-10">
        &copy; Weather Information | Create by NT
      </footer>
    </div>
  );
}

export default App;
