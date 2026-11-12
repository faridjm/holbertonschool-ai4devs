CargoFlow — User Stories
CargoFlow is an internal cargo transportation management system used by company managers, operators, and drivers. The stories below describe intended product behavior and are not claims that these features are already implemented.
User Story 1 — Create a Transportation Order
As an operator, I want to create an order with customer, pickup, delivery, and cargo details so that the company can organize a transportation job.

Acceptance Criteria:
- The operator can enter customer contact details, pickup and delivery locations, and cargo information.
- The system rejects an order when required information is missing.
- A successfully created order receives a unique identifier and an initial status.
Priority: MVP
User Story 2 — View and Track Orders
As an operator, I want to view orders and their statuses so that I can coordinate ongoing work.

Acceptance Criteria:
- The operator can see a list of orders with their current statuses.
- The operator can open an order to view its details and assigned resources.
- An order's displayed status reflects its latest recorded change.
Priority: MVP
User Story 3 — Assign a Vehicle and Driver
As an operator, I want to assign an available vehicle and its designated driver to an order so that transportation can begin with the correct resources.

Acceptance Criteria:
- The operator can select a vehicle that is not assigned to another active order.
- The system assigns the selected vehicle's designated driver to the order.
- The system prevents assigning a busy vehicle or driver to another active order.
Priority: MVP
User Story 4 — Assign Movers
As an operator, I want to assign three available movers to an order so that loading and unloading work is staffed.

Acceptance Criteria:
- The operator can select three distinct, available movers for an order.
- The system prevents assigning a mover who is already busy on an active order.
- Assigned movers are marked busy until the order is completed or their assignment is released according to the cancellation rules.
Priority: MVP
User Story 5 — Complete an Order
As a driver, I want to mark my assigned order as completed so that the company can close the job and release its resources.

Acceptance Criteria:
- A driver can complete an order assigned to them, but not an unrelated order.
- Completing the order updates its status and releases its assigned driver, vehicle, and movers.
- The driver can record completion from the delivery location without returning to the company base.
Priority: MVP
User Story 6 — Record Customer Payments
As an operator, I want to record the customer's deposit and remaining payment so that the company can track the order's payment status.

Acceptance Criteria:
- The system supports recording a 50% advance deposit and the remaining 50% payment.
- The operator can see the total price, recorded payments, and outstanding balance.
- The system prevents recorded payments from exceeding the order total without an explicit adjustment process.
Priority: High
User Story 7 — Handle Order Cancellation
As an operator, I want to cancel an order using the applicable cancellation policy so that refunds and penalties are handled consistently.

Acceptance Criteria:
- The operator can record whether cancellation occurred before or after the vehicle departed.
- For a cancellation before departure, the system calculates a refund of 20% of the deposit; after departure, the deposit is non-refundable.
- The system records the cancellation outcome and releases resources that are no longer assigned to active work.
Priority: High
User Story 8 — Review Employee Bonuses
As a manager, I want to review mover bonuses for completed jobs and applicable cancellation penalties so that monthly compensation can be calculated accurately.

Acceptance Criteria:
- The system calculates a 25 AZN bonus for each mover assigned to a completed order.
- For applicable cancellation penalties, 50% of the penalty is allocated to the assigned movers as a group, with the remainder allocated to the company.
- The manager can review the bonus amounts and their source orders for a selected month.
Priority: High
User Story 9 — Receive AI-Assisted Mover Recommendations
As an operator, I want AI-assisted mover recommendations so that I can distribute assignments more fairly.

Acceptance Criteria:
- The system recommends available movers and considers recent assignment history.
- The operator can accept the recommendation or select different available movers.
- When overriding a recommendation, the operator must provide a reason that is saved for manager review.
Priority: Medium
User Story 10 — Review AI-Assisted Order Difficulty
As an operator, I want a suggested difficulty level for an order so that the team can assess the work consistently.

Acceptance Criteria:
- The system suggests Easy, Medium, or Hard using cargo weight and dimensions, item count, floor and elevator details, distance, and extra services.
- The operator can confirm or change the suggested level.
- The confirmed level is stored with the order.
Priority: Medium
User Story 11 — Review Operational Reports
As a manager, I want monthly operational reports so that I can evaluate company performance and resource utilization.

Acceptance Criteria:
- The manager can select a month and view order counts, employee workload, and vehicle usage.
- The report includes salary and bonus information based on recorded orders and assignments.
- AI-generated observations are distinguishable from calculated business metrics.
Priority: Medium
User Story 12 — Share Customer Terms
As an operator, I want to send the transportation and cancellation terms to a customer as a PDF by email so that the customer can review the conditions.

Acceptance Criteria:
- The system generates a PDF containing the applicable payment and cancellation terms.
- The operator can send the PDF to the customer's recorded email address.
- The system records whether the email delivery request succeeded or failed.
Priority: Low
