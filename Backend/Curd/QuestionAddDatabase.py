import pandas as pd

from pydantic import BaseModel, Field


class NewQuestionBase(BaseModel):
    id: int
    question: str
    options: list[str]
    answer: str
    difficulty: str
    tags: str


def get_student_details_in_excel(file):
    row_c = 1
    try:
        print(file.filename)
        df = pd.read_excel(file)

        x = []
        for index, row in df.iterrows():
            new_student = {
                "id": index + 1,
                "question": row["QUESTIONS"],
                "options": [
                    row["OPTION 1"],
                    row["OPTION 2"],
                    row["OPTION 3"],
                    row["OPTION 4"],
                ],
                "answer": row["ANSWER"],
                "difficulty": row["DIFFICULTY"],
                "tags": row["TAGS"],
            }
            if row["DIFFICULTY"] not in ["Easy", "Medium", "Hard"]:
                raise ValueError(f"Error in : row {row_c} Tags not present")
            if row["ANSWER"] not in [
                row["OPTION 1"],
                row["OPTION 2"],
                row["OPTION 3"],
                row["OPTION 4"],
            ]:
                raise ValueError(
                    f"Error in : {row_c} row options does not match answers"
                )
            if not (
                row["ANSWER"]
                and row["QUESTIONS"]
                and row["OPTION 1"]
                and row["OPTION 2"]
                and row["OPTION 3"]
                and row["OPTION 4"]
                and row["TAGS"]
                and row["DIFFICULTY"]
            ):
                raise ValueError(f"Error in : {row_c} values are not present")
            if NewQuestionBase.model_validate(new_student).model_dump():
                x.append(new_student)
                row_c += 1
            else:
                raise ValueError(f"Error in : {row_c} row")

        return {"status": True, "result": x}
    except Exception as e:
        print("error", e)
        raise ValueError(f"Error in row:{row_c}, {e}")
