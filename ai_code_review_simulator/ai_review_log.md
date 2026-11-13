AI Review Log
- PR: #1 — Add Task Filtering by Status and Due Date
- Reviewed diff: Base 3ff4305, PR head c052a41. File and line references point to the PR head.
- Tool: ChatGPT. The PR diff was reviewed in three passes using the prompts below. This file records the feedback for the follow-up review exercise.
Review Prompts
The Holberton review-prompt link redirected to a sign-in page. The prompts below were written for the three personas named in the assignment.
Persona	Prompt
Security	Review the PR diff as a security reviewer. Follow untrusted JSON from file input through validation to stdout. Identify inputs that can silently change a task's meaning or escape the documented error handling. For each finding, cite the relevant line and suggest a small fix or test.
Performance	Review the PR diff as a performance reviewer. Trace file parsing, filtering, and JSON output. Identify where the CLI keeps multiple copies of data in memory. Explain when the cost matters and suggest the smallest change that preserves output order and validation behavior.
Maintainability	Review the PR diff as a maintainer. Compare the implementation, tests, and PR description. Check how invalid arguments are reported and whether the input/output contract is explicit. Tie each comment to an observable behavior or a testable requirement.


Inline Comments
ID	Persona and priority	Location	Feedback
I1	Security · Medium	task_filter.py:118	A JSON title containing an escaped unpaired UTF-16 surrogate reaches stdout and raises UnicodeEncodeError in a UTF-8 environment. The CLI exits with code 1 and a traceback. Reject unpaired surrogates during title validation so the existing error handler can report the record number and return 2.
I2	Security · Low	task_filter.py:88	The JSON decoder silently keeps the last value for duplicate keys. A task with two status fields can be filtered using a different status than the first one a reader sees. If input files are expected to reject ambiguous records, detect duplicate keys with object_pairs_hook and return a validation error.
I3	Performance · Low	task_filter.py:118	The CLI keeps the task list, match list, converted dictionaries, and complete serialized JSON string in memory during output. For large result sets, use json.dump after validation to avoid allocating the whole output string. Preserve the trailing newline and JSON format.
I4	Maintainability · Medium	task_filter.py:49	Output projects every record to title, status, and due_date. A source field such as id is dropped, and an omitted due_date becomes null. State the output schema in the PR description and add a contract test. Preserve extra fields if the intended behavior is to return original records.
I5	Maintainability · Low	task_filter.py:109–113	A reversed date range is checked only after the file is opened and parsed. A missing file therefore masks the invalid argument, and a large file is read before an invalid command is rejected. Validate the range before loading the file and keep the same validation for callers of filter_tasks().
I6	Maintainability · Low	test_task_filter.py:61–66	The subprocess tests have no timeout. A regression that hangs the CLI would stall the suite. Add a finite timeout to run_cli so such a failure surfaces at the specific test.
I7	Maintainability · Low	test_task_filter.py:68–76	The CLI success test supplies only --status. Unit tests cover the combined filter, but they cannot catch a date flag parsed correctly and then dropped by main(). Add a CLI test that supplies a status and both date flags, with a record on each boundary and records excluded by each filter.


Global Suggestions
ID	Persona and priority	Feedback
G1	Security · Advisory	Keep the current boundary explicit. The CLI reads a local file named by its caller. If it later accepts uploads or runs as a service, require a bounded upload size and a controlled input location before reusing the loader in that setting.
G2	Performance · Advisory	Keep the single-pass filter and preserve input order. Record an expected input size and measure representative files before adding streaming parsing or indexing. Streaming input would also need a plan to preserve the current all-or-nothing validation behavior.
G3	Maintainability · Low	State the minimum supported Python version in the PR description. The type unions use Python 3.10+ syntax. Record the tested interpreter version alongside the test commands so reviewers can reproduce the run.


Verification
- All 10 existing feature tests passed against the PR head using Python 3.12.14.
- Separate CLI checks reproduced the behaviors in I1, I2, I4, and I5.
- The performance comments are based on inspection of the allocation path. No benchmark was run.
