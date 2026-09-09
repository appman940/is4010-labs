# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticates GitHub Copilot Successfully. I verified that the tool was working by launching it. Version 1.0.83 is the version I am running.

### Antigravity CLI

I installed and authenticated Antigravity. I confirmed it operation and am running 1.1.28.

## Shared task

### Shared prompt

```text
I am completing a beginner Python lab. I need to implement this function:

def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""

Suggest a simple implementation appropriate for a beginner Python student. Explain how your solution works and any edge cases I should consider. Do not modify any files yet.
```

### Copilot CLI observations

Copilot suggested using a string containing the vowels "aeiou", creating a counter, and then looping through the lowercase version of the input text. Each time a character matched one of the vowels, the counter increased by one. I thought the approach was simple and easy to follow for a beginner. I also liked that converting the text to lowercase handled uppercase vowels without needing extra conditions. I wanted to verify that it also worked correctly with empty strings, words with no vowels, and the letter y.

### Antigravity CLI observations

Antigravity suggested almost the same implementation as Copilot. It recommended storing "aeiou" as the valid vowels, converting the text to lowercase, looping through the characters, and increasing a counter when a vowel was found. The explanation was clear and the code was easy to understand. I specifically checked that y was not included in the vowel string because the assignment says not to count it. I also wanted to test uppercase letters, empty text, and words that contain no vowels.

### Comparison

The Copilot CLI and Antigravity CLI responses were very similar in both their code and their explanations. Both suggested converting the text to lowercase, storing the vowels in the string "aeiou", looping through each character, and increasing a counter whenever a vowel was found. Both approaches appeared to satisfy the requirements because they ignored capitalization and did not count y as a vowel. I thought both responses were clear and appropriate for a beginner because neither used complicated Python features. Copilot and Antigravity also pointed out similar edge cases, including uppercase letters, empty strings, and text without vowels. Since the two suggestions were nearly identical, I used the simple loop-and-counter approach. I chose it because it was easy to read, easy to explain, and straightforward to test.

## Test-guided implementation

After creating the three required functions, I ran the provided pytest grader from the repository root. All of the Python behavior tests passed. The greeting function worked for a simple name, a multiword name, and an empty name. The even-number function passed tests for positive numbers, zero, and negative numbers. The count_vowels function also passed tests for case-insensitive vowels, text with no vowels, and empty text. This showed me that the actual Python implementation matched the required function contracts. The only failed tests were related to the unfinished prompt journal rather than the Python code, so I knew I did not need to change the functions. Instead, I needed to finish the required journal sections and remove the remaining template placeholders. :contentReference[oaicite:0]{index=0}

## Preferred tool combination

Each tool seems useful for a different part of my workflow. A browser chat is helpful when I need a detailed explanation, troubleshooting help, or step-by-step guidance. GitHub Copilot inside VS Code is useful while I am actually writing code because suggestions appear directly in the editor. Copilot CLI and Antigravity CLI are useful when I want an agent to work from the context of the repository while I am in the terminal. Right now, I prefer using VS Code for editing, browser chat for explanations, and a CLI agent when I want help that depends on the repository. I do not think I would use every tool for every task. I would probably change my preference if one CLI agent became noticeably better at understanding larger projects, making reliable edits, or explaining why its changes were correct.