# Given the following JSON data, find any structural issues and correct them


```json
{
     "name": "John Smith" #comma
     "age: 25, "address": 
     { "city": "New York" "country": "USA" } #missing comma
     , "hobbies": ["reading","cooking", } # missing ]
```


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
