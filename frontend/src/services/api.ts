import type { ChatRequest, ChatResponse } from "../types";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const apiClient = {
  async chat(payload: ChatRequest): Promise<ChatResponse> {
    const res = await fetch(`${API_BASE_URL}/api/chat/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const error = await res.json().catch(() => ({ detail: "Request failed" }));
      throw new Error(error.detail || "Failed to send message");
    }

    return res.json();
  },

  getWebSocketUrl(): string {
    const wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const wsHost =
      import.meta.env.VITE_WS_URL ||
      import.meta.env.VITE_API_URL?.replace(/^https?:/, wsProtocol) ||
      `${wsProtocol}//localhost:8000`;
    return `${wsHost}/ws/chat`;
  },
};

