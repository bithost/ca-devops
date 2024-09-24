# Read about JSON Schema and write a basic schema for the student JSON ppj.egt from the 1st tasks.

```json
{
  "$schema": "http://json-schema.org/draft-04/schema",
  "$id": "https://example.com/employee.schema.json",
  "title": "Record of students",
  "description": "This document provides information about students",
  "type": "object",
  "properties": {
    "students": {
      "description": "Students information",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "description": "Name of the student",
            "type": "string"
          },
          "age": {
            "description": "Age of the student",
            "type": "integer"
          },
          "grade": {
            "description": "Grade of the student",
            "type": "string"
          },
          "subjects": {
            "description": "Subjects student is having at school",
            "type": "array",
            "items": {
              "description": "Student learning objects",
              "type": "string"
            }
          }
        },
        "required": ["name", "age", "grade", "subjects"]
      }
    }
  }
}
```