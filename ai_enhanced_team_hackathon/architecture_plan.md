# CargoFlow Dispatch — Architecture Plan

## Scope and Stack

Build a single deployable ASP.NET Core application. It serves a lightweight HTML, CSS, and JavaScript interface and exposes a JSON API. The frontend and API share the same origin. EF Core persists the three MVP entities in SQLite, and a migration creates the schema and its constraints. Seed two vehicle–driver pairs for the demo.

- **Operator view** — Job form, dispatch board grouped by status, and fleet list with availability and assignment controls.
- **Driver view** — Demo driver selector, active job queue, and a completion action. The selector simulates driver identity for the hackathon. Use fictional data in the hosted demo.
- **Backend** — Controllers validate request inputs and call a dispatch service for assignment and completion. The service checks job state and driver–vehicle ownership, then persists the change with EF Core. SQLite enforces the single active assignment rule.
- **MVP boundary** — One dispatch board, seeded fleet, and demo driver selection. Production authentication, fleet administration, payments, and AI recommendations are outside this sprint.

## API Contract

| Method and path | Behavior |
| --- | --- |
| `GET /api/jobs` | Return jobs for the operator board, including status, schedule, and assignment details when available. |
| `POST /api/jobs` | Create a pending job from the customer name, route addresses, and scheduled timestamp with an offset. Return `201 Created` and the job. |
| `GET /api/vehicles` | Return vehicles with designated drivers and derived availability. Use the same response to populate the demo driver selector. |
| `POST /api/jobs/{jobId}/assign` | Accept `vehicleId`, assign an available pair to a pending job, and return the updated job. |
| `GET /api/drivers/{driverId}/jobs` | Return the selected driver's assigned jobs. |
| `POST /api/drivers/{driverId}/jobs/{jobId}/complete` | Complete the selected driver's assigned job and return the updated job. |

Return `400 Bad Request` for invalid input, `404 Not Found` for unknown IDs, `403 Forbidden` for completion by a driver outside the job's pairing, and `409 Conflict` for stale job state or a vehicle assignment conflict. Show actionable errors in the UI and refresh the affected lists after successful mutations or assignment conflicts. Convert scheduled timestamps to UTC for persistence and display them in the browser's local time.

## Dispatch Flow

1. The operator creates a job. The API validates its details and stores it as `Pending`.
2. The operator selects an available vehicle. The dispatch service assigns it and changes the job to `Assigned` in one save. If another request wins the race for the same job or vehicle, the API returns a conflict.
3. The driver opens the queue and completes the job. The service validates the pairing and changes the job to `Completed` with a UTC completion time. Availability is computed from active jobs, so the completed job no longer makes the pair busy.

## 24-Hour Delivery Plan

| Sprint time | Work | Owner |
| --- | --- | --- |
| Hours 0–3 | Agree on payloads, job states, seed data, and the demo scenario. | Product and AI Workflow Lead with Backend and Frontend |
| Hours 3–12 | Implement the model, migration, and endpoints. Build the two views in parallel using sample payloads. | Backend/API Developer and Frontend Developer |
| Hours 12–18 | Integrate the views and test validation, completion, and assignment conflicts. | Backend and Frontend with QA |
| Hours 18–24 | Deploy, verify the hosted flow, and rehearse the demo. | QA and Deployment Lead with Product |

Use short Git branches and pull requests for integration. Use AI to draft sample payloads, generate test ideas, and review changes. Team members verify suggestions against the user stories before merging and record which suggestions affected the MVP.

## Deployment and Verification

Deploy one app instance with a persistent, writable volume for the SQLite database. Apply the migration and seed the sample fleet during setup. Configure the database path to point at that volume.

Before presenting, run the hosted workflow from creating a job through releasing its vehicle. Confirm that an invalid job stays unsaved, the wrong driver cannot complete a job, simultaneous requests cannot double-book a vehicle or reassign the same job, and a completed job keeps its original pairing when the vehicle is reused. Restart the app once and confirm the job and fleet data persist.
