from collections import deque

def is_palindrome(s: str) -> bool:
    """Перевіряє, чи є рядок паліндромом (нечутливий до регістру та пробілів)."""
    d = deque(ch.lower() for ch in s if ch != ' ')
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    # Приклади перевірки
    tests = [
        "А роза упала на лапу Азора",
        "Я несу гусеня",
        "No lemon no melon",
        "hello",
    ]
    for t in tests:
        print(t, "->", is_palindrome(t))
