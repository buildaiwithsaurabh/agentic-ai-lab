"use client";

import { useEffect, useRef, useCallback } from "react";

/**
 * A custom hook to handle smart auto-scrolling for chat interfaces.
 * It scrolls to the bottom when messages or loading states change,
 * but locks scroll if the user has scrolled up manually to read older messages.
 */
export default function useAutoScroll(dependencies: any[], isUserMessage: boolean = false) {
  const scrollContainerRef = useRef<HTMLDivElement | null>(null);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  const scrollToBottom = useCallback((behavior: ScrollBehavior = "smooth") => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior });
    }
  }, []);

  useEffect(() => {
    const container = scrollContainerRef.current;
    if (!container) return;

    // Check if the user is near the bottom (within a threshold of 150px)
    const threshold = 150;
    const isNearBottom =
      container.scrollHeight - container.scrollTop - container.clientHeight <= threshold;

    // Always scroll if the user just sent a message, or if they are already near the bottom
    if (isNearBottom || isUserMessage) {
      // Use setTimeout to ensure DOM has updated with the latest message height
      const timer = setTimeout(() => {
        scrollToBottom("smooth");
      }, 50);
      return () => clearTimeout(timer);
    }
  }, [dependencies, isUserMessage, scrollToBottom]);

  return {
    scrollContainerRef,
    messagesEndRef,
    scrollToBottom,
  };
}
