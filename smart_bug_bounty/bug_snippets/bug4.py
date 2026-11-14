def add_task(title: str, tasks: list[str] = []) -> list[str]:
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Task title cannot be empty.")

    tasks.append(cleaned_title)
    return tasks


if __name__ == "__main__":
    print(add_task("Read chapter 1"))
    print(add_task("Review notes"))
