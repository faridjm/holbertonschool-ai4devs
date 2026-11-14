# Team Ideation

## Brainstormed Ideas

1. **CargoFlow Dispatch (chosen)** — A dashboard for a small moving company to record jobs, assign vehicles and their drivers, and track completion. The full workflow fits into one demo using a small sample fleet.
2. **StudyRoom Booker** — A booking board where students reserve available study rooms for specific time slots. The main challenge is preventing overlapping bookings.
3. **Dev Task Triage** — A shared board for small development teams to capture bug reports, set priorities, and assign owners. The team would need to agree on how to distinguish urgent reports from routine ones.

## Problem Statement

Dispatch operators at small moving companies often coordinate jobs by phone and track assignments in messages. When a new job arrives, the operator may have to call drivers to learn which vehicles are free. This can delay dispatch or lead to double-booking. CargoFlow Dispatch gives operators one place to see job status and vehicle availability.

## MVP Features

1. **Create a moving job.** The operator enters a customer name, pickup and drop-off addresses, and a scheduled time. The job starts as `Pending`.
2. **View jobs and availability.** The dispatch board shows jobs by status and lists vehicles with their designated drivers and current availability. The demo starts with a small preloaded fleet.
3. **Assign an available vehicle and driver.** The operator selects an available vehicle together with its designated driver. The job becomes `Assigned`, and the vehicle and driver become busy. Each pair can have one active assignment at a time.
4. **Complete an assigned job.** The driver marks the job as `Completed`, and the vehicle and driver become available for another assignment.

## Team Roles

Proposed assignments for the hackathon simulation. Open roles can be assigned once the team roster is confirmed.

| Member | Role | Responsibilities |
| --- | --- | --- |
| Fərid Məmmədov | Backend/API Developer | Implement the moving job workflow, assignment rules, and data persistence. |
| To be assigned | Frontend Developer | Build the job form and dispatch board, then connect them to the API. |
| To be assigned | QA and Deployment Lead | Test the job lifecycle and double-booking rule, deploy the MVP, and verify the live demo. |
| To be assigned | Product and AI Workflow Lead | Keep the MVP within scope, record AI-assisted decisions, and prepare the demo walkthrough. |
