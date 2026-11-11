# Reflection on AI-Assisted Debugging

## Introduction

In this project, I explored how an AI assistant can support debugging across Python, JavaScript, and C#. I worked with five deliberately flawed programs covering syntax errors, logical errors, runtime exceptions, off-by-one errors, and incorrect data type usage. The process involved identifying each problem, applying an AI-suggested fix, testing the corrected code, and documenting the results. My goal was to understand how AI can improve debugging without replacing my responsibility as a developer.

## AI Strengths

The easiest bugs for the AI to solve were the missing colon in the Python loop and the incorrect discount calculation in JavaScript. Both problems had clear causes and required minimal changes. For example, changing `return price + discount;` to `return price - discount;` corrected the discount calculation. The AI also identified that dividing two integers in C# produces an integer result before conversion to double. Casting the numerator before division preserved the fractional value.

These examples showed that AI is particularly useful for recognizing familiar programming mistakes and explaining their causes. It accelerated the initial diagnosis and helped me focus on the relevant lines instead of searching through the entire program.

## AI Weaknesses

The more demanding cases involved the C# dictionary lookup and the Python off-by-one error. Although the AI identified both causes, confirming the solutions required considering different inputs. Using `TryGetValue` needed verification for both existing and missing keys. Correcting the loop boundary also required checking empty and single-element lists.

The documentation process revealed another limitation. Our initial validation report contained additional C# cases that had not been executed. After completing those tests, the automated evaluator still rejected the report because its evidence format was inconsistent. We had to simplify the documentation and distinguish console output from function return values. This showed that a technically reasonable AI response does not automatically satisfy every acceptance criterion.

## Human Role

My trust in AI suggestions is conditional rather than absolute. I confirmed the C# fixes locally using the .NET 10 SDK, including the missing-key and existing-key scenarios and both fractional and whole-number averages. Human judgment was necessary to decide which tests were meaningful, interpret the evaluator's feedback, and preserve the original buggy files while validating corrected copies.

I also learned that expected behavior must guide debugging. A program that runs without exceptions is not necessarily correct; its output must match the intended business logic.

## Conclusion

Overall, AI made the initial debugging process faster, although repeated documentation revisions added extra work. In real backend development, I would use AI to investigate exceptions, explain unfamiliar behavior, and suggest focused fixes. However, I would still review changes, run tests, and verify requirements before accepting them. The most valuable lesson is that AI should support engineering judgment, not replace it. Reliable debugging combines AI-assisted diagnosis with human understanding, reproducible tests, and clear evidence.
