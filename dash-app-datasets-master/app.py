import dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask

server = Flask('my app')

app = dash.Dash("Sankey Diagram Example", server=server)

app.layout = html.Div([
    dcc.Markdown("Sankey Diagram", className="header"),
    html.Iframe(src="https://plot.ly/~alishobeiri/896.embed?modebar=false&link=false&autosize=true",
                seamless="seamless", style={'border': '0'}, width="100%", height="560"),
    dcc.Markdown("Source: [Department of Energy & Climate Change](http://www.decc.gov.uk/en/content/cms/tackling/2050/calculator_on/calculator_on.aspx),\
                  [Tom Counsell](https://tamc.github.io/Sankey/) - This dash app is a recreation of [Mike Bostock's Example](https://bost.ocks.org/mike/sankey/)",
                  className="source"),
    dcc.Markdown("Sankey diagrams are closely related to [alluvial diagrams](https://en.wikipedia.org/wiki/Alluvial_diagram),\
                which show how network structure changes over time.", className="aside"),
    dcc.Markdown("[Sankey diagrams](https://en.wikipedia.org/wiki/Sankey_diagram)\
                  visualize the magnitude of flow between nodes\
                  in a network. This intricate diagram shows a possible scenario\
                  for UK energy production and consumption in 2050:\
                  energy **supplies** are on the left, and **demands** are on the right.\
                  Intermediate nodes group related forms of production and\
                  show how energy is converted and transmitted before it\
                  is consumed (or lost\!). The thickness of each link encodes\
                  the amount of flow from source to target.", className="markdown"),
    dcc.Markdown("[Plotly](https://plot.ly/)'s sankey functionality is built upon and expands the functionality of the D3 Sankey plugin. The original plugin takes as input the nodes and weighted links,\
                  computing positions via [iterative relaxation](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method). After fixing\
                  the horizontal position of each node, the algorithm starts\
                  from the sources on the left, positioning downstream nodes\
                  so as to minimize link distance. A reverse pass is then made\
                  from right-to-left, and then the entire process is repeated\
                  several times. Overlapping nodes are shifted to avoid collision. Plotly's library allows for increased customization and more granularity when looking at multiple links between nodes\
                  while also allowing users to share their findings easily.", className="markdown"),
    html.Aside("Plotly's Dash framework allows users to create and share their,\
                data analysis with no prior CSS or HTML experience required.", className="aside"),
    dcc.Markdown("The fully automatic layout is convenient for rapid\
                  visualization-positioning nodes manually is tedious\!\
                  However, the algorithm is not perfect\; links are drawn\
                  with partial transparency to highlight crossings. To improve\
                  readability and further disambiguate links, this example also\
                  lets you reposition nodes interactively. The algorithm could\
                  be improved in the future, say to minimize link crossing or\
                  to support loopback in cyclical networks.", className="markdown"),
    dcc.Markdown("This example was created using Plotly's [Dash](https://plot.ly/dash/) framework\
                  all credit is given to [Mike Bostock](https://bost.ocks.org/mike/sankey/) for his original example.", className="markdown")
],
    style={
        'width': '960px',
        'font-family': '''"PT Serif", serif''',
        'margin': "1em auto 4em auto",
        'position': 'relative',
    }
)

external_css = [ "https://codepen.io/alishobeiri/pen/qjygOK.css?v=plotly",
                "https://fonts.googleapis.com/css?family=PT+Sans"]

for css in external_css:
    app.css.append_css({ "external_url": css })

if __name__=='__main__':
    app.run_server(debug=True)
