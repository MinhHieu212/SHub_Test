import requests

response = requests.get("https://share.shub.edu.vn/api/intern-test/input")
data = response.json()

print(data)

token = data["token"]
arr = data["data"]
queries = data["query"]

prefixSum = [0] * (len(arr) + 1)
evenSum = [0] * (len(arr) + 1)
oddSum = [0] * (len(arr) + 1)

for i in range(len(arr)):
    prefixSum[i + 1] = prefixSum[i] + arr[i]
    if i % 2 == 0:
        evenSum[i + 1] = evenSum[i] + arr[i]
    else:
        oddSum[i + 1] = oddSum[i] + arr[i]

# print("arr: " , arr)
# print("prefixSum: " , prefixSum)

results = []
for query in queries:
    query_type = query["type"]
    l, r = query["range"]

    if query_type == "1":
        result = prefixSum[r + 1] - prefixSum[l]
    else:
        result = evenSum[r + 1] - evenSum[l] - (oddSum[r + 1] - oddSum[l])

    results.append(result)
    
# print("Result:" , results)

headers = {"Authorization": f"Bearer {token}"}
response = requests.post("https://share.shub.edu.vn/api/intern-test/output", json=results, headers=headers)

print(response.text)