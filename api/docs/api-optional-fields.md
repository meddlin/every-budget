# API: Optional Fields

Ref: [https://stackoverflow.com/questions/67699451/make-every-fields-as-optional-with-pydantic](https://stackoverflow.com/questions/67699451/make-every-fields-as-optional-with-pydantic)

We want to allow users to submit models with missing fields for partial
updates.

Example

The full class would look something like this:

```python
Model {
    id: uuid
    name: str
    age: int
    class_type: str
    hp: int
}
```

A potential payload for updating this object could look like:

```python
Model {
    id: uuid
    class_type: str
    hp: int
}
```