import React from "react";
import { ChatWidget } from "./components/ChatWidget";
import "./App.css";

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <ChatWidget />
    </div>
  );
};

export default App;

