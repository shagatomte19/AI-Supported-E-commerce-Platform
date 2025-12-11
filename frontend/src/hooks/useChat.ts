import { useState } from "react";

export const useChat = () => {
  const [messages, setMessages] = useState<string[]>([]);

  const sendMessage = (msg: string) => {
    setMessages((prev) => [...prev, msg]);
  };

  return { messages, sendMessage };
};

