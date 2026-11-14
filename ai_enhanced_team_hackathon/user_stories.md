# CargoFlow Dispatch — User Stories

The MVP follows one dispatch workflow from job creation through completion. The demo uses a seeded fleet with designated drivers.

## US-01 — Create a moving job

As a dispatch operator, I want to record a moving job so that it can be assigned to a vehicle.

- I can submit a customer name, pickup address, drop-off address, and scheduled date and time.
- A valid submission creates a job with a unique ID and the `Pending` status. The job appears on the dispatch board.

## US-02 — Correct invalid job details

As a dispatch operator, I want feedback on invalid fields so that I can correct a job before it is saved.

- Blank customer names or addresses and missing or invalid scheduled times produce field-level errors.
- The form retains my input for correction, and the invalid submission creates no job.

## US-03 — View jobs by status

As a dispatch operator, I want to see jobs grouped by status so that I can identify work that needs assignment or follow-up.

- The board groups jobs under `Pending`, `Assigned`, and `Completed`.
- Each job shows its customer, route, and scheduled time. Assigned and completed jobs also show the vehicle and designated driver.

## US-04 — View the fleet and driver availability

As a dispatch operator, I want to see vehicles and their designated drivers so that I can choose an available pair.

- The board lists each seeded vehicle by plate number, shows its designated driver, and displays `Available` or `Busy`.
- A pair is busy while its vehicle has an assigned job. Only available pairs can be selected in the assignment form.

## US-05 — Assign a job

As a dispatch operator, I want to assign an available vehicle and its driver to a pending job so that the driver can see the job in their queue.

- Selecting an available vehicle also selects its designated driver.
- A successful assignment moves the job to `Assigned`, makes the pair busy, and adds the job to that driver's queue.

## US-06 — Resolve an assignment conflict

As a dispatch operator, I want feedback when another operator has already used a vehicle or assigned a job so that I can act on current availability.

- An assignment is rejected if the vehicle is already busy or the job is already assigned or completed. The board shows the reason and refreshes its job and fleet data.
- If two requests compete for the same vehicle or the same job, at most one succeeds. The rejected request leaves the saved assignment intact.

## US-07 — View assigned jobs

As a driver, I want to view jobs assigned to my vehicle so that I know the route and scheduled time.

- Selecting my driver profile in the demo shows only my currently assigned jobs.
- Each job displays the customer, pickup and drop-off addresses, and scheduled time. The view shows an empty state when I have no assigned jobs.

## US-08 — Complete an assigned job

As a driver, I want to mark my assigned job as complete so that the dispatch operator knows it is finished.

- The demo accepts completion for an assigned job that belongs to the selected driver. It rejects completion for a different driver or a job that is already complete.
- A successful completion records the completion time, moves the job to `Completed`, and removes it from my active queue.

## US-09 — Reuse a released vehicle and driver

As a dispatch operator, I want a completed job to release its vehicle and driver so that I can assign them to the next job.

- When the board refreshes after completion, the pair appears as `Available` and is selectable for another pending job.
- The completed job remains visible with its vehicle and driver after the pair receives a new assignment.
