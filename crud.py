from fastapi import FastAPI

app = FastAPI()

students = []

@app.post("/students")
def add_students(student: dict):
    students.append(student)
    return {"message": "student added"}

@app.get("/students")
def get_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    for index, s in enumerate(students):
        if s["id"] == student_id:
            students[index] = student
            return {"message": "updated"}

    return {"message": "student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "deleted"}

    return {"message": "student not found"}
