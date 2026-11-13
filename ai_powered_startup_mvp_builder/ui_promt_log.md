CargoFlow UI Prompt Log
AI tool: ChatGPT. The prompts below were used as design briefs for the initial and revised artboards. The linked PNGs capture each iteration at its intended viewport. All orders, names, and contact details are demo data.

Design scope: Desktop screens for dispatch operators and a mobile screen for drivers. The examples follow the CargoFlow user stories from order creation through crew assignment and move completion.
1. Dispatch orders
Initial prompt
Design a desktop CargoFlow dispatch screen with a New order button and a table of six moving orders. Show the order ID, customer, route, scheduled time, status, and truck–driver pair. Give each row a View order action. Use a dark sidebar, warm neutral surfaces, and distinct labels for Pending Assignment, Assigned, and Completed.

Screenshot (v1)

Review: Pending orders were visible in the table, but their row action did not indicate how to assign a crew.

Revision prompt
Keep the table columns and group the six orders into three status totals above the table. Change the action for Pending Assignment rows to Assign crew. Keep View order for assigned and completed orders.

Screenshot (v2)

2. New order
Initial prompt
Mock up a desktop order form with customer name, phone number, pickup address, drop-off address, scheduled date, and scheduled time. Place the six fields in a two-column grid under Order details. Include Cancel and Create order actions.

Screenshot (v1)

Review: The single group gave all fields the same visual weight. The empty phone field did not explain what the operator should do after an invalid submission.

Revision prompt
Group the fields under Customer contact, Route, and Schedule. Show a failed submission caused by a missing phone number. Place the error directly under the field, preserve the other field values, and label the scheduled time as Baku time.

Screenshot (v2)

3. Assign crew
Initial prompt
Create a desktop crew assignment screen for a pending moving order. Show eight trucks paired with their designated drivers in one panel and movers with checkboxes in another. Include the order ID, customer, route, status, and an Assign crew button.

Screenshot (v1)

Review: The first version showed how to pick a crew, but it gave the operator no way to distinguish busy resources or confirm the selected mover count.

Revision prompt
Add a text badge for Available or Busy to every resource row. Show busy rows as disabled. Highlight one selected available truck–driver pair and three selected available movers. Display 3 of 3 selected and summarize the crew next to the final Assign crew action.

Screenshot (v2)

4. Driver job
Initial prompt
Design a mobile My jobs screen showing one active job for the signed-in driver. Show the order ID, Assigned status, schedule, pickup and drop-off addresses, customer contact details, and three movers. Put Mark complete below the job details.

Screenshot (v1)

Review: Pickup and drop-off looked like unrelated text blocks. Calling the customer relied on finding the phone number, and the completion action sat inline below the content.

Revision prompt
Connect pickup and drop-off visually in a single vertical route. Add a Call customer action beside the contact details. Place a full-width Mark complete button in a footer at the bottom of the mobile screen so the driver can find it easily.

Screenshot (v2)

The four final PNGs are static mockups. Form validation, assignment conflicts, and move completion are specified in the user stories for implementation.
