CargoFlow MVP User Stories
User Story 1 — Create a moving order
As a dispatch operator, I want to record a customer's move so that I can assign a crew to it.

Acceptance criteria
- The form captures the customer's name and phone number, pickup and drop-off addresses, and scheduled date and time.
- A valid submission creates an order with status Pending Assignment.
User Story 2 — Correct order details
As a dispatch operator, I want to see which order fields need correction so that I can submit a complete booking.

Acceptance criteria
- A missing required field or invalid date and time produces a message identifying the field.
- The form keeps the entered values for correction, and the invalid submission creates no order.
User Story 3 — Check resource availability
As a dispatch operator, I want to see the availability of truck–driver pairs and movers so that I can select a crew.

Acceptance criteria
- Each truck is displayed with its designated driver. Each pair and each mover shows Available or Busy.
- A resource assigned to an order with status Assigned shows Busy, regardless of the order's scheduled date and time.
User Story 4 — Assign a crew to an order
As a dispatch operator, I want to assign a truck and movers to a pending order so that the driver knows which move to handle.

Acceptance criteria
- Assignment requires one available truck with its designated driver and exactly three distinct available movers.
- A successful assignment records the truck and crew together, moves the order to Assigned, and makes those resources Busy.
User Story 5 — Resolve a crew assignment conflict
As a dispatch operator, I want to know when a selected resource has just been assigned to another order so that I can choose a different crew.

Acceptance criteria
- When two operators try to assign the same truck–driver pair or mover to different pending orders, at most one conflicting assignment succeeds.
- The operator whose assignment is rejected sees that a selected resource is already busy. The rejected order stays Pending Assignment with no crew saved.
User Story 6 — Track order progress
As a dispatch operator, I want to see each order's status and assigned crew so that I can follow work from booking through completion.

Acceptance criteria
- The order list shows each order's scheduled date and time and its current status: Pending Assignment, Assigned, or Completed.
- The details of an assigned or completed order show its truck, designated driver, and three movers.
User Story 7 — View my assigned jobs
As a driver, I want to see the jobs assigned to me so that I know which moves I need to handle.

Acceptance criteria
- The driver's active job list shows only orders with status Assigned for that driver.
- The API denies access when a driver requests another driver's order directly.
User Story 8 — View the details of my move
As a driver, I want to see where and when a move is scheduled so that I can carry it out.

Acceptance criteria
- The job details show the scheduled date and time, pickup and drop-off addresses, customer contact details, and assigned movers.
User Story 9 — Complete my assigned move
As a driver, I want to mark my assigned move as complete so that dispatch knows the job is finished.

Acceptance criteria
- Only the assigned driver can complete an order with status Assigned.
- Successful completion changes the status to Completed and records the completion time. A repeated request does not change that time.
User Story 10 — Reuse a crew after completion
As a dispatch operator, I want a crew to become available as soon as its move is completed so that I can assign it to the next order.

Acceptance criteria
- The next availability request after completion shows the truck–driver pair and its three movers as Available unless another order has already claimed them.
- Completing an order preserves its crew details for the operator to review.
