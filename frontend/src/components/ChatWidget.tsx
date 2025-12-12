import React from "react";
import { useChat } from "../hooks/useChat";
import { MessageList } from "./MessageList";
import { InputBox } from "./InputBox";
import { TypingIndicator } from "./TypingIndicator";

export const ChatWidget: React.FC = () => {
  const { messages, isLoading, error, connected, sendMessage, clearMessages, messageEndRef } =
    useChat();

  return (
    <div className="flex flex-col h-screen max-w-4xl mx-auto bg-white shadow-lg">
      {/* Header */}
      <div className="bg-blue-600 text-white px-6 py-4 flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold">AI Customer Support</h2>
          <p className="text-sm text-blue-100">
            {connected ? "Connected" : "Connecting..."}
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <div
            className={`h-3 w-3 rounded-full ${
              connected ? "bg-green-400" : "bg-yellow-400"
            }`}
            title={connected ? "Connected" : "Connecting"}
          ></div>
          {messages.length > 0 && (
            <button
              onClick={clearMessages}
              className="px-3 py-1 text-sm bg-blue-700 hover:bg-blue-800 rounded transition-colors"
            >
              Clear
            </button>
          )}
        </div>
      </div>

      {/* Error Banner */}
      {error && (
        <div className="bg-red-50 border-l-4 border-red-500 text-red-700 px-4 py-3">
          <p className="text-sm">{error}</p>
        </div>
      )}

      {/* Messages */}
      <div className="flex-1 overflow-hidden">
        <MessageList messages={messages} messageEndRef={messageEndRef} />
      </div>

      {/* Typing Indicator */}
      <TypingIndicator isVisible={isLoading} />

      {/* Input */}
      <InputBox onSendMessage={sendMessage} disabled={isLoading || !connected} />
    </div>
  );
};

