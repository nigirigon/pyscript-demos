from pyscript import display
m="Ready to play !"
display(m, target="main_pyscript")


from shiny.express import input, render, ui

ui.input_slider("val", "Slider label", min=0, max=100, value=50)

@render.text
def slider_val():
    return f"Slider value: {input.val()}"