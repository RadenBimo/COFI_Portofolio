import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np


class AdsPlot():
    df = pd.read_csv("./Modeling/data/Social_Network_Ads.csv")

    def corr_plot(self):
        plot = sns.heatmap(self.df.select_dtypes(include='number').corr(), annot=True)
        plot.figure.set_facecolor('none')
        plot.set_xticklabels(plot.get_xticklabels(), color='white')
        plot.set_yticklabels(plot.get_yticklabels(), color='white')
        return plot.get_figure()
    
    def box_gender(self):
        fig = px.histogram(
            self.df.groupby(["Purchased","Gender"])
            .count()
            .reset_index(),
        x= 'Purchased',
        y= 'User ID',
        color= 'Gender',
        barmode= 'group',
        )
        return fig
    
    def pie_gender(self):
        purchased_counts = self.df['Purchased'].value_counts()
        fig = go.Figure(data=[go.Pie(labels=purchased_counts.index, values=purchased_counts.values)])
        fig.update_traces(
        hoverinfo='label+percent',
        textfont_size=15,
        marker=dict(
            colors=['#008B8B','#4682B4'],
            line=dict(color='#000000', width=2)
            )
        )
        return fig
    
    def dist_age_plot(self):
        fig = px.histogram(x=self.df["Age"], marginal='rug')
        fig.update_traces(nbinsx=30, autobinx=True, selector={'type':'histogram'}) 
        fig.update_layout(title_text='Histogram of Age',xaxis_title='Age')
        fig.data[0].autobinx = True
        return fig

    def dist_essalary_plot(self):
        fig = px.histogram(x=self.df["EstimatedSalary"], marginal='rug')
        fig.update_traces(nbinsx=30, autobinx=True, selector={'type':'histogram'})
        fig.update_layout(title_text='Histogram of Estimated Salary',xaxis_title='Estimated Salary')
        fig.data[0].autobinx = True
        return fig

    