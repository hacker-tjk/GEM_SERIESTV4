# utils/ai.py
from ddgs import DDGS # Обновленный импорт согласно предупреждению в консоли

def get_gpt_response(messages):
    prompt = messages[-1]['content'] 
    try:
        # Использование актуального метода библиотеки
        results = DDGS().chat(prompt, model='gpt-4o-mini')
        return results
    except Exception as e:
        return f"Ошибка запроса: {str(e)}"
