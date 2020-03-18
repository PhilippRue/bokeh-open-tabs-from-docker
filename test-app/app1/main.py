import panel as pn


# create output pane which displays the link which is supposed to be opened
output = pn.pane.Markdown("")

# define link which opens app2
open_link = "http://localhost:5007/app2"

#################################################################################

# this does not open the tab in a docker container

def callback_open_link(b):
    from bokeh.client import show_session
    print('Open url:', open_link)
    show_session(url=open_link)
    # set output text
    output.object = open_link


# create button
button = pn.widgets.Button(name="Open app2 in new tab", button_type="primary")
button.on_click(callback_open_link)

#################################################################################

# this works from inside the container
button2 = pn.widgets.Button(name="Open app2 with CustomJS")
button2.js_on_click(args={'url': open_link}, code='window.open(url);')

#################################################################################

# now try yo update link before executing

widget = pn.widgets.MultiSelect(options=[2, 3])
url = pn.widgets.TextInput(value=None, width=0, disabled=True, placeholder="Dummy text", height=0)


def callback(target, event): 
    # get source value
    source = event.new
    # do something to source value 
    string = '' 
    for i in source: 
        string+=str(i)+', '
    newurl = open_link.replace('app2', 'app2?id='+string)
    print('setting url:', newurl)
    # set target output
    target.value = newurl 
    print('set value:', target.value)
     
#link source to target, a change in value triggers callback
widget.link(url, callbacks={'value': callback}) 
 

button3 = pn.widgets.Button(name='Changable url')
button3.js_on_click(args={'source': url}, code="""
console.log('Open now:');
console.log(source.value);
""")

changeable = pn.Column(widget, button3, url)

#################################################################################


# build page
page = pn.Column()
page.append(pn.pane.Markdown("## Test page 1"))
page.append(button)
page.append(output)
page.append(button2)
page.append(changeable)

# serve the page
page.servable()
