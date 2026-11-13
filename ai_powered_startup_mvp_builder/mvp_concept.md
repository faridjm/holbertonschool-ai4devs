MVP Concept - CargoFlow
Problem Statement
Moving-company operators need to know which trucks, drivers, and movers are available when a customer books a move. When order details and crew assignments are tracked separately, an operator can assign someone who is already on another job or miss that a crew has finished and is free again.

CargoFlow is an internal web app that lets operators create moving orders, assign available crews, and see their availability update when drivers complete a job. The pilot tests whether an operator can coordinate a move from booking to completion in one place.
Target Users
- Dispatch operators create moving orders, assign crews, and track order progress.
- Drivers view their assigned jobs and mark them complete once the move is finished.
Core Features
1. Create a moving order. The operator records the customer's contact details, pickup and drop-off addresses, and scheduled date and time.
2. Check resource availability. The operator can see which truck–driver pairs and movers are Available or Busy.
3. Assign a crew. The operator selects one available truck with its designated driver and three distinct available movers. CargoFlow marks the assigned resources as Busy and prevents their assignment to another active order.
4. Track order progress. The operator can see each order's assigned crew and status. Orders move from Pending Assignment to Assigned to Completed.
5. Complete a move. The assigned driver marks the order as Completed. CargoFlow returns the truck, driver, and movers to Available.
Constraints
- The pilot serves one moving company with eight trucks and a fixed driver for each truck.
- Operators and drivers use the app. Movers are assigned by the operator and do not need accounts.
- Availability reflects active assignments. Calendar-based scheduling and conflict checks for future time slots are outside the pilot scope.
- Crew selection is manual. AI assignment recommendations, customer self-service, payment processing, cancellation penalties, and payroll are outside the pilot scope.
- 
