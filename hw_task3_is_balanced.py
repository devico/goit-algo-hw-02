def is_balanced(s: str) -> bool:
    """Перевірка симетрії дужок (), [], {}. Інші символи ігноруються."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


if __name__ == "__main__":
    line = input()
    print("Симетрично" if is_balanced(line) else "Несиметрично")
