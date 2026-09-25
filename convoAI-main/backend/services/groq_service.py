import logging
import time
import requests
import json
from config import get_settings

logger = logging.getLogger(__name__)

class GroqLLMService:
    """Service wrapper for Groq LLM inference using direct HTTP requests."""

    def __init__(self):
        settings = get_settings()
        self.api_key = settings.GROQ_API_KEY
        self.model_name = settings.GROQ_MODEL
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("Groq API key not found. Groq service will be unavailable.")
            self.available = False
        else:
            self.available = True
            logger.info(f"GroqLLMService initialized with model={self.model_name}")

    async def generate(self, prompt: str) -> str:
        """
        Generate text response using Groq API via direct HTTP requests.
        """
        if not self.available:
            raise RuntimeError("Groq service not available - API key not configured")

        start_time = time.time()
        try:
            logger.info(f"Generating Groq response for prompt (length={len(prompt)})")
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 2048,
            }
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code != 200:
                error_msg = f"Groq API returned status {response.status_code}: {response.text}"
                logger.error(error_msg)
                raise RuntimeError(error_msg)
            
            result = response.json()
            response_text = result["choices"][0]["message"]["content"]
            elapsed = time.time() - start_time
            logger.info(f"Groq response generated in {elapsed:.2f}s")
            
            return response_text.strip()
            
        except requests.RequestException as e:
            logger.error(f"Network error communicating with Groq API: {e}", exc_info=True)
            raise RuntimeError(f"Groq API connection failed: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            logger.error(f"Error parsing Groq response: {e}", exc_info=True)
            raise RuntimeError(f"Groq response parsing failed: {str(e)}")
        except Exception as e:
            logger.error(f"Error generating Groq response: {e}", exc_info=True)
            raise RuntimeError(f"Groq generation failed: {str(e)}")

