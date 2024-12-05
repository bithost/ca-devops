# BONUS: Convert a nested JSON data structure to YAML:
```json
{
  "employees": [
    {
      "firstName": "John",
      "lastName": "Doe",
      "skills": ["communication", "problem-solving"]
    },
    {
      "firstName": "Jane",
      "lastName": "Smith",
      "skills": ["programming", "problem-solving"]
    }
  ]
}
```

```yaml
employees:
  - firstName: John
    lastName: Doe
    skills:
      - communication
      - problem-solving
  - firstName: Jane
    lastName: Smith
    skills:
      - programming
      - problem-solving
```