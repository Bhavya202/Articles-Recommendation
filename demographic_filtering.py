import pandas as pd

df = pd.read_csv('articles.csv')
df = df.loc[df["eventType"] == "CONTENT SHARED"]

interaction_event = df["eventType"]
# # Sum Of All Events Of Interactions
# print(len(interaction_event))

df["eventType_"] = interaction_event

df = df.sort_values(by='eventType_', ascending=False)
output = df[["title"]].head(20)