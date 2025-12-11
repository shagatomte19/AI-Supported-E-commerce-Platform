import React from "react";
import { ChatWidget } from "./components/ChatWidget";

const App: React.FC = () => {
  return (
    <div className="app">
      <h1>AI Support</h1>
      <ChatWidget />
    </div>
  );
};

export default App;

