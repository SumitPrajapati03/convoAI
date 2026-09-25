import logging
import random
import asyncio
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class MockLLMService:
    """Mock LLM service for testing without external APIs."""
    
    def __init__(self):
        self.available = True
        logger.info("MockLLMService initialized (for development/testing)")
    
    async def generate(self, prompt: str) -> str:
        """
        Generate a mock response based on the prompt.
        """
        await asyncio.sleep(0.5)  # Simulate response time
        
        logger.info(f"Generating mock response for prompt (length={len(prompt)})")
        
        # Normalize prompt
        prompt_lower = prompt.lower().strip()
        
        # Check for specific keywords - order matters, more specific first
        if "joke" in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "Why did the scarecrow win an award? Because he was outstanding in his field! 😄"
        
        if "2 plus 2" in prompt_lower or "what is 2+2" in prompt_lower or "2+2" in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "2 plus 2 equals 4. This is basic arithmetic where you add two numbers together to get their sum."
        
        if "hello" in prompt_lower or "hi " in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "Hello! I'm a mock AI assistant. How can I help you today?"
        
        if "how are you" in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "I'm doing great, thanks for asking! I'm here to help you with any questions or tasks you might have."
        
        if "what is ai" in prompt_lower or "artificial intelligence" in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "AI (Artificial Intelligence) refers to computer systems designed to perform tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, and understanding language."
        
        if "what time" in prompt_lower or "current time" in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "I don't have access to real-time information, but you can check your system clock for the current time."
        
        if "help" in prompt_lower:
            logger.info("Mock response generated from predefined responses")
            return "I'm a mock AI assistant. You can ask me anything, and I'll provide helpful responses. Try asking me questions or having a conversation!"
        
        # Generate a generic response if no match found
        generic_responses = [
            "That's an interesting question! While I'm a mock AI, I can tell you that this topic is worth exploring further. Feel free to ask me more specific questions.",
            "I appreciate your question! As a mock AI assistant, I can provide general insights. If you need more specific information, please ask follow-up questions.",
            "Great question! This is something that many people wonder about. Based on the context you've provided, I'd say this deserves further discussion.",
            "I understand what you're asking. While I'm a mock assistant for testing purposes, I can engage with your question and provide thoughtful responses.",
            "That's a thoughtful inquiry. Let me provide a response: every question has value, and exploring different topics helps us learn and grow.",
        ]
        
        response = random.choice(generic_responses)
        logger.info("Mock response generated from generic responses")
        return response
    
    async def generate_with_context(self, message: str, history: List[Dict[str, Any]]) -> str:
        """
        Generate response with conversation history context.
        """
        # For mock service, we'll include history context in a simple way
        context = f"Previous messages in conversation: {len(history)} messages"
        logger.info(f"Generating mock response with context: {context}")
        
        return await self.generate(message)
