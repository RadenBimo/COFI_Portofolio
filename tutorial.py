import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.title(":blue[**Tutorial**]")

text_tab, data_tab,layout_tab, widget_tab, chart_tab, load_tab  = st.tabs(["Text Elements", "Data Elements",
                                                                "Layouts and Containers","Widget",
                                                                "Chart","Loading Animation"])

#--------Text Elements---------
with text_tab:
    st.header("Text Elements")
    st.divider()

    st.title("st.title()")
    st.header("st.header()")
    st.subheader("st.subheader()")
    st.markdown("st.markdown()")
    st.text("st.text()")    
    st.caption('st.caption()')
    st.code("st.code()")
    st.latex(r'''
        st.latex( a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right))
        ''')

    st.divider()
    st.header("Streamlit Magic Command")
    st.code("st.write(*args: any),  unsafe_allow_html=False")
    st.write("""
    This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique properties:
    1. You can pass in multiple arguments, all of which will be written.
    2. Its behavior depends on the input types as follows.
    3.It returns None, so its "slot" in the App cannot be reused.

    Arguments are handled as follows:

    1. write(string) : Prints the formatted Markdown string, with
        support for LaTeX expression, emoji shortcodes, and colored text. See docs for st.markdown for more.
    2. write(data_frame) : Displays the DataFrame as a table.
    3. write(error) : Prints an exception specially.
    4. write(func) : Displays information about a function.
    5. write(module) : Displays information about the module.
    6. write(class) : Displays information about a class.
    7. write(dict) : Displays dict in an interactive widget.
    8. write(mpl_fig) : Displays a Matplotlib figure.
    9. write(generator) : Streams the output of a generator.
    10. write(openai.Stream) : Streams the output of an OpenAI stream.
    11. write(altair) : Displays an Altair chart.
    12. write(PIL.Image) : Displays an image.
    13. write(keras) : Displays a Keras model.
    14. write(graphviz) : Displays a Graphviz graph.
    15. write(plotly_fig) : Displays a Plotly figure.
    16. write(bokeh_fig) : Displays a Bokeh figure.
    17. write(sympy_expr) : Prints SymPy expression using LaTeX.
    18. write(htmlable) : Prints _repr_html_() for the object if available.
    19. write(obj) : Prints str(obj) if otherwise unknown.

"""
)

#--------Data Elements---------
df = pd.DataFrame([
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
])

with data_tab:
    st.header("Data Element")
    st.divider()

    st.subheader("Dataframe")
    st.code("""
        st.dataframe(data=None, width=None, height=None, *, use_container_width=False, 
                    hide_index=None, column_order=None, column_config=None)
    """)
    st.dataframe(df)
    st.divider()

    st.subheader("Data Editor")
    st.code("""
        st.data_editor(data, *, width=None, height=None, use_container_width=False, 
                    hide_index=None, column_order=None,column_config=None, num_rows="fixed",
                    disabled=False, key=None, on_change=None, args=None, kwargs=None)
    """)
    df_baru = st.data_editor(df)
    st.divider()

    st.subheader("Table")
    st.code('st.table(data=None)')
    st.table(df)
    st.divider()

    st.subheader("Metric")
    st.code("""
        st.metric(label, value, delta=None, delta_color="normal",
                help=None, label_visibility="visible")
    """)
    st.metric("Temperature", "70 °F", "1.2 °F")
    st.divider()

#-------WIDGET--------
with widget_tab:
    st.header("Widget")
    st.divider()

    st.subheader("Button")
    st.code('st.button("text")')
    st.button('Hit me')
    st.divider()

    st.subheader("Checkbox")
    st.code("st.checkbox('text')")
    st.checkbox('Check me out')
    st.divider()

    st.subheader("Radio")
    st.code("st.radio('text', [ops1,ops2,...])")
    st.radio('Pick one:', ['nose','ear'])
    st.divider()

    st.subheader("Select Box")
    st.code("st.selectbox('text', [ops1,ops2,...])")
    st.selectbox('Select', [1,2,3])
    st.divider()

    st.subheader("Multi Select")    
    st.code("st.multiselect('text', [ops1,ops2,...])")
    st.multiselect('Multiselect', [1,2,3])
    st.divider()

    st.subheader("Slider")
    st.code("st.slider('text', min_value, max_value)")
    st.slider('Slide me', min_value=0, max_value=10)
    st.divider()

    st.subheader("Select Slider")
    st.code("st.select_slider('text', [ops1,ops2,...])")
    st.select_slider('Slide to select', options=["null",'1'])
    st.divider()

    st.subheader("Text Input")
    st.code("st.text_input('text')")
    st.text_input('Enter some text')
    st.divider()

    st.subheader("Number Input")
    st.code("st.number_input('text')")
    st.number_input('Enter a number')
    st.divider()

    st.subheader("Text Area")
    st.code("st.text_area('text')")
    st.text_area('Area for textual entry')
    st.divider()

    st.subheader("Date Input")
    st.code("st.date_input('text')")
    st.date_input('Date input')
    st.divider()
    
    st.subheader("Time Input")
    st.code("st.time_input('text')")
    st.time_input('Time entry')
    st.divider()

    st.subheader("File Uploader")
    st.code("st.file_uploader('text')")
    st.file_uploader('File uploader')
    st.divider()

    st.subheader("Download Button")
    st.code("""
        st.download_button('text', file)

        #for image
        with open("path to your file/image.<filetype>", "rb") as file:
        btn = st.download_button(
                label="text",
                data=file,
                file_name="text.png",
                mime="images/<file type>"
            )
    """)
            
    with open("images/COFI.png", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="COFI.png",
                mime="image/png"
            )

    st.subheader("Camera Input")
    st.code("st.camera_input('text')")
    st.camera_input("say Cheese!")
    st.divider()

    st.subheader("Color Picker")
    st.code("st.color_picker('text')")
    st.color_picker('Pick a color')
    st.divider()

#------Layouts and Containers------
with layout_tab:
    st.header("Layouts and Containers")
    st.divider()
    
    st.subheader("Tab")
    st.code("""
        tab1, tab2,tabn = st.tabs(["Tab 1", "Tab2",....])
        tab1.write("this is tab 1")
        tab2.write("this is tab 2")
        
        # You can also use "with" notation:

        tab1, tab2,tabn = st.tabs(["Tab 1", "Tab2",....])
        with tab1:
            st.write("this is tab 1")
        with tab2:
            st.write("this is tab 1")
    """)
    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    tab1.write("this is tab 1")
    tab2.write("this is tab 2")
    st.divider()

    st.subheader("Column")
    st.code("""
        col1, col2, col-n = st.columns(n)
        col1.write('Column 1')
        col2.write('Column 2')

        # Using 'with' notation:
        with col1:
            st.write('This is column 1')
    """)
    col1, col2 = st.columns(2)
    col1.write('Column 1')
    col2.write('Column 2')
    st.divider()


    st.subheader("Container")
    st.code("""
        container = st.container(border=True)
        container.write("text")

        # Using 'with' notation:
        with st.container(height=300):
            st.markdown("text")
    """)
    container = st.container(border=True)
    container.write("This is inside the container")
    st.write("This is outside the container")
    st.markdown('###')

    st.subheader("Expander")
    st.code("""
        with st.expander("text"):
            st.write("text")
    """)
    with st.expander("See explanation"):
        st.write("text")


    st.divider()

#-------Chart---------
with chart_tab:
    st.header("Charts")
    st.divider()
    
    
    chart_data = pd.DataFrame({
        "col1":[1,3,5,4,5],
        "col2": range(1,6),
        "col3": ["A"] * 2 + ["B"] * 3 
    })


    chart_data_sum = chart_data.groupby("col3").count().reset_index()


    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    )

    st.dataframe(chart_data)

    st.subheader("Area Chart")
    st.code("""
        st.area_chart(data=None, *, x=None, y=None, color=None,
                    width=0, height=0, use_container_width=True)
    """)
    st.area_chart(data = chart_data,y= "col1",x= "col2")
    st.divider()

    st.subheader("Bar Chart")
    st.code("""
        st.bar_chart(data=None, *, x=None, y=None, color=None,
                    width=0, height=0, use_container_width=True)
    """)
    st.bar_chart(data = chart_data_sum, y= "col1", x= "col3")

    st.subheader("Line Chart")
    st.code("""
        st.line_chart(data=None, *, x=None, y=None, color=None,
                    width=0, height=0, use_container_width=True)
    """)
    st.line_chart(data = chart_data,y= "col1",x= "col2")
    st.divider()

    st.subheader("Scatter Chart")
    st.code("""
        st.scatter_chart(data=None, *, x=None, y=None, color=None, 
                        size=None, width=0, height=0, use_container_width=True)
    """)
    st.scatter_chart(chart_data, x='col1', y='col2', color='col3',)
    st.divider()
    
    st.subheader("Map Chart")
    st.dataframe(map_data)
    st.code("""
        st.map(data=None, *, latitude=None, longitude=None, color=None,
            size=None, zoom=None, use_container_width=True)
    """)
    st.map(data=map_data, latitude="lat", longitude="lon")
    st.divider()

with load_tab:
    st.subheader("Status Elements")
    st.code("""
        st.spinner(text="In progress...")
        
        # Using 'with' notation
        with st.spinner(text='In progress'):
            #ex
            time.sleep(5)
            st.success('Done')
        
    """)
    if st.button("Spinner"):
        with st.spinner(text='In progress'):
            time.sleep(5)
            st.success('Done')
    
    st.subheader("Progress Bar")
    st.code("""
        bar = st.progress(value, text=None)
        # Update progress
        bar.proress(value)
    """)
    if st.button("st.progress"):
        bar = st.progress(10)
        time.sleep(3)
        bar.progress(100)

    st.subheader("Status Bar")
    st.code("""
        st.status(label, *, expanded=False, state="running")

        # Using 'with' notation
        with st.spinner(text='In progress'):
            #ex
            st.write("Searching for data...")
            time.sleep(2)

    """)
    if st.button("st.status"):
        with st.status("Downloading data...",expanded=True):
            st.write("Searching for data...")
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)
