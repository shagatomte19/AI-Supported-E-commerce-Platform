import React from "react";
import type { Message } from "../types";

interface MessageListProps {
  messages: Message[];
  messageEndRef: React.RefObject<HTMLDivElement>;
}

export const MessageList: React.FC<MessageListProps> = ({ messages, messageEndRef }) => {
  const formatTime = (date: Date) => {
    return new Date(date).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  };

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.length === 0 ? (
        <div className="flex items-center justify-center h-full text-gray-400">
          <div className="text-center">
            <p className="text-lg font-medium">Welcome to AI Support</p>
            <p className="text-sm mt-2">Start a conversation by typing a message below</p>
          </div>
        </div>
      ) : (
        messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.sender === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] rounded-lg px-4 py-2 ${
                message.sender === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-100 text-gray-800"
              }`}
            >
              <p className="text-sm whitespace-pre-wrap break-words">{message.text}</p>
              <div
                className={`text-xs mt-1 ${
                  message.sender === "user" ? "text-blue-100" : "text-gray-500"
                }`}
              >
                {formatTime(message.timestamp)}
              </div>
              {message.intent && message.sender === "assistant" && (
                <div className="text-xs mt-1 text-gray-500">
                  Intent: <span className="font-medium">{message.intent}</span>
                </div>
              )}
            </div>
          </div>
        ))
      )}
      <div ref={messageEndRef} />
    </div>
  );
};

