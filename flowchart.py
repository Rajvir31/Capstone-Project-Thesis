from graphviz import Digraph

dot = Digraph(comment='Thesis Workflow')

dot.node('A', 'Download GDELT + S&P 500 Data')
dot.node('B', 'Clean & Aggregate GDELT Features')
dot.node('C', 'Merge with S&P 500 Data')
dot.node('D', 'Feature Engineering\n(AvgTone, GoldsteinScale, Lags)')
dot.node('E', 'Train/Test Split')
dot.node('F', 'Train XGBoost Model')
dot.node('G', 'Evaluate Model')
dot.node('H', 'Visualize Results')
dot.node('I', 'Draw Conclusions & Report')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI'])

# Save to file and render
dot.render('thesis_flowchart', format='png', cleanup=True)
dot.view()
