import { useEffect, useRef, useState, useCallback } from "react";
import { apiClient } from "../services/api";
import type { WebSocketMessage } from "../types";

export const useWebSocket = () => {
  const [connected, setConnected] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<number | null>(null);
  const reconnectAttempts = useRef(0);
  const maxReconnectAttempts = 5;

  const connect = useCallback(() => {
    try {
      const wsUrl = apiClient.getWebSocketUrl();
      const ws = new WebSocket(wsUrl);

      ws.onopen = () => {
        setConnected(true);
        setError(null);
        reconnectAttempts.current = 0;
      };

      ws.onerror = (event) => {
        console.error("WebSocket error:", event);
        setError("Connection error");
        setConnected(false);
      };

      ws.onclose = () => {
        setConnected(false);
        if (reconnectAttempts.current < maxReconnectAttempts) {
          reconnectAttempts.current += 1;
          const delay = Math.min(1000 * Math.pow(2, reconnectAttempts.current), 30000);
          reconnectTimeoutRef.current = window.setTimeout(() => {
            connect();
          }, delay);
        } else {
          setError("Failed to reconnect. Please refresh the page.");
        }
      };

      wsRef.current = ws;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to connect");
      setConnected(false);
    }
  }, []);

  const disconnect = useCallback(() => {
    if (reconnectTimeoutRef.current) {
      window.clearTimeout(reconnectTimeoutRef.current);
      reconnectTimeoutRef.current = null;
    }
    if (wsRef.current) {
      wsRef.current.close();
      wsRef.current = null;
    }
    setConnected(false);
  }, []);

  const sendMessage = useCallback((message: string) => {
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(message);
      return true;
    }
    return false;
  }, []);

  const onMessage = useCallback((callback: (data: WebSocketMessage) => void) => {
    if (wsRef.current) {
      wsRef.current.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          callback(data);
        } catch (err) {
          console.error("Failed to parse WebSocket message:", err);
        }
      };
    }
  }, []);

  useEffect(() => {
    connect();
    return () => {
      disconnect();
    };
  }, [connect, disconnect]);

  return {
    connected,
    error,
    sendMessage,
    onMessage,
    reconnect: connect,
    disconnect,
  };
};

