export type Message = {
  id: string;
  sender: "user" | "assistant";
  text: string;
  timestamp: Date;
  intent?: string;
  model?: string;
  context_sources?: Array<{
    doc: string;
    score: number;
    source?: string;
  }>;
};

export type ChatResponse = {
  intent: string;
  answer: string;
  model: string;
  context_sources: Array<{
    doc: string;
    score: number;
    source?: string;
  }>;
};

export type ChatRequest = {
  message: string;
  user_id?: string;
};

export type WebSocketMessage = ChatResponse | { status: string } | { error: string };

