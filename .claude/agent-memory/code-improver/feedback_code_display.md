---
name: code_display_mode
description: User uses a light VS Code theme — avoid fenced code blocks that render with dark backgrounds
type: feedback
---

Do not use fenced code blocks (triple backticks with language tags) to show code. They render with dark backgrounds which clashes with the user's light VS Code theme.

**Why:** The user explicitly wants light mode code display. Fenced code blocks in the chat panel often render dark regardless of VS Code theme.
**How to apply:** Show code changes via `git diff` output (Bash tool). When referencing code, use file:line links instead of pasting code in fenced blocks. If code must be shown inline, use plain text or minimal formatting.
