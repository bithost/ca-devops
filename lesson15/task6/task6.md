# Learn about YAML anchors and aliases. Then, refactor the YAML student to utilize an anchor for one of the and use alias to add that suffect to another student

```yaml
students:
  - name: John Doe
    age: 20
    grade: A
    subjects:
      - Mathematics
      - Physics
      - Chemistry
  - name: Jade Doe
    age: 19
    grade: B
    subjects:
      - History
      - English
      - Biology

```

```yaml
subjects: &main_subjects        
    - math
    - science
    - grammar
students:
  - name: John Doe
    age: 20
    grade: A
    subjects: *main_subjects
  - name: Jade Doe
    age: 19
    grade: B
    subjects: *main_subjects
```