import panel as pn
from bokeh.client import show_session

def callback_open_link(b):
    global output
    open_link = "http://localhost:5007/app2"
    print('Open url:', open_link)
    show_session(url=open_link)
    # set output text
    output.object = open_link



# create output pane which displays the link which is supposed to be opened
output = pn.pane.Markdown("")

# create button
button = pn.widgets.Button(name="Open app2 in new tab", button_type="primary")
button.on_click(callback_open_link)


# build page
page = pn.Column()
page.append(pn.pane.Markdown("## Test page 1"))
page.append(button)
page.append(output)
# serve the page
page.servable()
