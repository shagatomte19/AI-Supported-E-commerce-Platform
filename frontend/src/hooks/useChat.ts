import { useState, useCallback, useRef, useEffect } from "react";
import { apiClient } from "../services/api";
import { useWebSocket } from "./useWebSocket";
import type { Message, ChatResponse } from "../types";

const generateId = () => `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;

export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const { connected, sendMessage: wsSendMessage, onMessage } = useWebSocket();
  const messageEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messageEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (connected) {
      onMessage((wsMessage) => {
        // Backend sends either {status: "connected"} or ChatResponse directly
        if ("status" in wsMessage && wsMessage.status === "connected") {
          console.log("WebSocket connected");
        } else if ("answer" in wsMessage) {
          // This is a ChatResponse (may not have context_sources from WebSocket)
          const response = wsMessage as ChatResponse & { context_sources?: ChatResponse["context_sources"] };
          addMessage({
            id: generateId(),
            sender: "assistant",
            text: response.answer,
            timestamp: new Date(),
            intent: response.intent,
            model: response.model,
            context_sources: response.context_sources,
          });
          setIsLoading(false);
        } else if ("error" in wsMessage) {
          setError((wsMessage as { error: string }).error);
          setIsLoading(false);
        }
      });
    }
  }, [connected, onMessage]);

  const addMessage = useCallback((message: Message) => {
    setMessages((prev) => [...prev, message]);
  }, []);

  const sendMessage = useCallback(
    async (text: string, userId?: string) => {
      if (!text.trim()) return;

      const userMessage: Message = {
        id: generateId(),
        sender: "user",
        text: text.trim(),
        timestamp: new Date(),
      };

      addMessage(userMessage);
      setIsLoading(true);
      setError(null);

      try {
        if (connected) {
          // Use WebSocket if available
          const sent = wsSendMessage(text.trim());
          if (!sent) {
            throw new Error("WebSocket not ready");
          }
        } else {
          // Fallback to REST API
          const response = await apiClient.chat({
            message: text.trim(),
            user_id: userId,
          });

          addMessage({
            id: generateId(),
            sender: "assistant",
            text: response.answer,
            timestamp: new Date(),
            intent: response.intent,
            model: response.model,
            context_sources: response.context_sources,
          });
          setIsLoading(false);
        }
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : "Failed to send message";
        setError(errorMessage);
        setIsLoading(false);
        console.error("Error sending message:", err);
      }
    },
    [connected, wsSendMessage, addMessage]
  );

  const clearMessages = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return {
    messages,
    isLoading,
    error,
    connected,
    sendMessage,
    clearMessages,
    messageEndRef,
  };
};

