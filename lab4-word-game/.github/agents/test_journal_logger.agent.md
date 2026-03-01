---
name: test_journal_logger
description: updates the journal.md file after each prompt
argument-hint: The inputs this agent expects, e.g., "a task to implement" or "a question to answer".
# tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo'] # specify the tools this agent can use. If not set, all enabled tools are allowed.
---
after each prompt, update the journal.md file in the repository root with first the prompt, followed by the response. Use markdown formatting to make it easy to read. For example:

'''## Prompt
Write a function that adds two numbers.