# Given the following JSON data, find any structural issues and correct them




```json
{
  "name": "John Smith",
  "age": 25,
  "address": {
    "city": "New York",
    "country": "USA"
  },
  "hobbies": [
    "reading",
    "cooking"
  ]
}
```

Curly brackets {} - define objects
Square brackets [] - define arrays

```json
{ "name": "John Smith" "age: 25, "address": { "city": "New York" "country": "USA" }, "hobbies": ["reading", "cooking",], }
```


Missing comma between "name": "John Smith" and "age: 25.
The age key is missing a closing quotation mark ("age": instead of age:).
Missing comma between "city": "New York" and "country": "USA".
There is an extra trailing comma in the "hobbies" array after "cooking".