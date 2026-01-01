from shiny import ui

app_ui = ui.page_fluid(
    ui.h2("Dokumenten-Chatbot"),
    ui.input_text("question", "Deine Frage zu den Dokumenten:", ""),
    ui.input_action_button("ask", "Frage stellen"),
    ui.hr(),
    ui.h3("Antwort"),
    ui.output_text_verbatim("answer"),
    ui.h3("Quellen"),
    ui.output_text_verbatim("sources"),
)
