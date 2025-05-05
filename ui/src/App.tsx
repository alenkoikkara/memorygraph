import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import "./App.css";

import SearchPage from "./pages/SearchPage";

function App() {
  return (
    <Router>
      <div className="relative">
        <div className="min-h-screen bg-gray-50">
          <nav className="fixed">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <div className="flex justify-between h-16">
                <div className="flex">
                  <div className="flex-shrink-0 flex items-center">
                    memorysearch
                  </div>
                </div>
              </div>
            </div>
          </nav>

          <main className="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <Routes>
              <Route
                path="/web"
                element={<Navigate to="/web/search" replace />}
              />
              <Route path="/web/search" element={<SearchPage />} />
            </Routes>
          </main>

          <div className="h-16 absolute bottom-0 right-10">
            <div className="px-4 sm:px-6 lg:px-8 flex flex-col items-start justify-between">
              <p className="text-center text-gray-500 text-xs">
                &copy; {new Date().getFullYear()} Memory Search
              </p>
              <p className="text-center text-gray-500 text-xs">alenkoikkara</p>
            </div>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
