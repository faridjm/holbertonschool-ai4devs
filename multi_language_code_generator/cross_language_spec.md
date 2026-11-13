Cross-Language Specification - API Access Log Analyzer
Algorithm
Analyze a simplified API access log to count requests, identify distinct clients, calculate the error rate, and report traffic by endpoint.
1. Read the file line by line. Skip blank lines. Count each malformed nonblank line once and continue.
2. For each valid record, count one request, add its client ID to the set of distinct clients, and increment the request count for its endpoint. An endpoint is the pair (method, path).
3. For status codes from 400 through 599, increment the overall error count and the endpoint's error count.
4. Calculate the overall error rate as 100 × errorRequests / totalRequests, rounded to two decimal places using round-half-up. If there are no valid requests, use 0.
5. Order endpoints by descending request count. Resolve ties by method in ascending ASCII order, then by path in ascending ASCII order.
Input format
The analyzer takes one UTF-8 text file without a byte order mark. Each record contains four tab-separated fields in this order. The file has no header.
clientId<TAB>method<TAB>path<TAB>statusCode
Field	Valid values
clientId	One or more ASCII letters, digits, underscores, or hyphens.
method	One of GET, POST, PUT, PATCH, DELETE, HEAD, or OPTIONS.
path	/ or slash-separated nonempty segments starting with /. Each segment may contain ASCII letters, digits, underscores, hyphens, and periods. A query string, fragment, or trailing slash on a non-root path makes the record invalid.
statusCode	Exactly three ASCII digits representing an integer from 100 through 599.


Accept LF and CRLF line endings. The last record may omit its line ending. A line is blank when it is empty or contains only ASCII spaces and tabs. A nonblank line is malformed if splitting it at every tab yields any number of fields other than four, or if any field fails validation. Validate fields as written, including any surrounding whitespace.
Output format
Return one JSON object.
Field	Type	Meaning
totalRequests	Integer	Number of valid records.
uniqueClients	Integer	Number of distinct client IDs among valid records.
errorRequests	Integer	Number of valid records with status codes from 400 through 599.
errorRatePercent	Number	Rounded percentage of valid requests that are errors, from 0 to 100.
malformedLines	Integer	Number of nonblank lines that fail validation.
endpoints	Array of objects	Each object contains method and path as strings, plus requestCount and errorCount as integers. Preserve the specified array order.


Compare parsed JSON values across implementations. JSON object key order, whitespace, and numeric spellings such as 40 and 40.00 are equivalent.
Edge cases
- Empty or whitespace-only input yields zero counts and an empty endpoint array.
- A malformed line is excluded from request totals, distinct clients, and endpoint statistics. Each malformed line contributes exactly one to malformedLines.
- Repeated valid records each count as a request. Repeated client IDs count once in uniqueClients.
- Client IDs and paths are case-sensitive. Different methods on the same path belong to separate endpoints.
- Codes 399 and 400 fall on opposite sides of the error threshold. Codes 100 and 599 are valid. Codes 099 and 600 are malformed.
Test cases
Inputs are written as JSON string literals so that tabs and line endings are explicit. Decode each string before writing it to a log file.
1. Empty file
Input
""
Expected output
{
  "totalRequests": 0,
  "uniqueClients": 0,
  "errorRequests": 0,
  "errorRatePercent": 0,
  "malformedLines": 0,
  "endpoints": []
}
2. Mixed traffic and a repeated client
Input
"c1\tGET\t/products\t200\nc1\tGET\t/products\t404\nc2\tPOST\t/orders\t201\nc3\tGET\t/products\t503\nc2\tGET\t/orders\t302\n"
Expected output
{
  "totalRequests": 5,
  "uniqueClients": 3,
  "errorRequests": 2,
  "errorRatePercent": 40,
  "malformedLines": 0,
  "endpoints": [
    {"method": "GET", "path": "/products", "requestCount": 3, "errorCount": 2},
    {"method": "GET", "path": "/orders", "requestCount": 1, "errorCount": 0},
    {"method": "POST", "path": "/orders", "requestCount": 1, "errorCount": 0}
  ]
}
3. Malformed records, blank lines, and CRLF
Input
"\r\n \t \r\nc1\tGET\t/health\t200\r\nmissing-fields\r\nc2\tget\t/health\t200\r\nc3\tGET\t/health?full=1\t200\r\nc4\tGET\t/health\t600\r\nc5\tGET\t/health\t 200\r\nc6\tGET\t/health\t200\textra"
Expected output
{
  "totalRequests": 1,
  "uniqueClients": 1,
  "errorRequests": 0,
  "errorRatePercent": 0,
  "malformedLines": 6,
  "endpoints": [
    {"method": "GET", "path": "/health", "requestCount": 1, "errorCount": 0}
  ]
}
4. Duplicate requests, case sensitivity, and sorting ties
Input
"u1\tPOST\t/items\t200\nU1\tGET\t/items\t200\nu1\tGET\t/Items\t200\nu1\tGET\t/items\t200\nu1\tGET\t/items\t200\n"
Expected output
{
  "totalRequests": 5,
  "uniqueClients": 2,
  "errorRequests": 0,
  "errorRatePercent": 0,
  "malformedLines": 0,
  "endpoints": [
    {"method": "GET", "path": "/items", "requestCount": 3, "errorCount": 0},
    {"method": "GET", "path": "/Items", "requestCount": 1, "errorCount": 0},
    {"method": "POST", "path": "/items", "requestCount": 1, "errorCount": 0}
  ]
}
5. Error boundaries and fractional percentage
Input
"c1\tGET\t/\t399\nc2\tGET\t/\t400\nc3\tGET\t/\t599\n"
Expected output
{
  "totalRequests": 3,
  "uniqueClients": 3,
  "errorRequests": 2,
  "errorRatePercent": 66.67,
  "malformedLines": 0,
  "endpoints": [
    {"method": "GET", "path": "/", "requestCount": 3, "errorCount": 2}
  ]
}
6. All records malformed
Input
"c1\tGET\t/status\t099\n\tGET\t/status\t200\nc3\tGET\tstatus\t200\n"
Expected output
{
  "totalRequests": 0,
  "uniqueClients": 0,
  "errorRequests": 0,
  "errorRatePercent": 0,
  "malformedLines": 3,
  "endpoints": []
}
7. Endpoint ties resolved by path
Input
"c1\tGET\t/z\t100\nc1\tGET\t/a\t200\nc1\tGET\t/A\t200"
Expected output
{
  "totalRequests": 3,
  "uniqueClients": 1,
  "errorRequests": 0,
  "errorRatePercent": 0,
  "malformedLines": 0,
  "endpoints": [
    {"method": "GET", "path": "/A", "requestCount": 1, "errorCount": 0},
    {"method": "GET", "path": "/a", "requestCount": 1, "errorCount": 0},
    {"method": "GET", "path": "/z", "requestCount": 1, "errorCount": 0}
  ]
}
