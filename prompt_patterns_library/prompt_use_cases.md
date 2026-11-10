# Prompt Use Cases

This document identifies recurring situations where reusable AI prompts can support C#/.NET backend development. Each use case defines the goal, required input, and expected output.

## Code Quality

### 1. Code Review
- **Goal:** Identify correctness, readability, maintainability, and security issues without unnecessary changes.
- **Input:** C# source code, relevant business requirements, and project conventions.
- **Output:** Prioritized findings with explanations and minimal recommended fixes.

### 2. Refactoring
- **Goal:** Improve code readability and maintainability while preserving existing behavior.
- **Input:** An ASP.NET Core service or controller, its responsibilities, and any relevant tests.
- **Output:** Refactored code, a summary of changes, and potential regression risks.

### 3. SOLID Principles Review
- **Goal:** Evaluate whether a class design follows relevant SOLID principles and identify practical improvements.
- **Input:** Related C# classes, interfaces, dependencies, and their intended responsibilities.
- **Output:** Specific design concerns, justified improvements, and concise code examples when necessary.

## Debugging

### 4. Exception Analysis
- **Goal:** Determine the likely root cause of a runtime exception.
- **Input:** Exception message, stack trace, relevant C# code, and reproduction steps.
- **Output:** Root-cause analysis, a minimal fix, and steps to verify the solution.

### 5. EF Core Error Investigation
- **Goal:** Diagnose Entity Framework Core query, relationship, or migration errors without risking existing data.
- **Input:** EF Core entities, DbContext configuration, migration details, and exact error messages.
- **Output:** Explanation of the issue, data-safe resolution options, and verification steps.

### 6. ASP.NET Core API Debugging
- **Goal:** Find why an API endpoint returns an unexpected response or status code.
- **Input:** Controller action, request URL and payload, expected response, actual response, and relevant logs.
- **Output:** Explanation of the request flow, identified issue, targeted correction, and test requests.

## Documentation

### 7. XML Documentation for C# Methods
- **Goal:** Produce accurate XML documentation comments for public methods.
- **Input:** Method signatures, implementations, parameter meanings, and expected behavior.
- **Output:** C# XML comments describing summaries, parameters, return values, and relevant exceptions.

### 8. REST API Endpoint Documentation
- **Goal:** Document API endpoints so other developers can integrate with them correctly.
- **Input:** Endpoint routes, HTTP methods, DTOs, validation rules, and response codes.
- **Output:** Markdown API documentation with request examples, response examples, and status-code explanations.

## Testing

### 9. Unit Test Case Generation
- **Goal:** Identify meaningful unit tests for business logic in .NET services.
- **Input:** Service methods, dependencies, business rules, and existing test conventions.
- **Output:** Test scenarios and sample xUnit tests covering expected behavior and relevant failures.

### 10. Edge Case Identification
- **Goal:** Discover realistic boundary conditions and regression risks before implementing or changing code.
- **Input:** Feature requirements, validation rules, and relevant controller or service code.
- **Output:** Prioritized edge cases with expected results and suggested test scenarios.
