import gradio as gr

opt_courses = ["Python", "R", "Java", ".Net", "JavaScript"]


def course_selection(course):
    return f"You selected: {course}"


interface = gr.Interface(
    fn=course_selection,
    inputs=gr.Radio(choices=opt_courses, label="Select a Course"),
    outputs="text",
    title="Course Selection",
    description="Select your preferred course.",
)

interface.launch()
