#!/usr/bin/env python3
"""One-line office joke entry for make.fun."""
import os

LINE = "I've written 'per my last email' so often that HR asked if I was threatening anyone, and honestly, I was."

def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(LINE)}")
    if LINE.strip() != LINE or not LINE.strip():
        raise SystemExit("entry must not be whitespace-only or padded")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
