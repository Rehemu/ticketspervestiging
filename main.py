import folium
import pandas as pd

# Load the locations and tickets data from Excel sheets
locations = pd.read_excel(r"branches.xlsx")
tickets = pd.read_excel(r"incidents.xlsx")
changes = pd.read_excel(r"C:\Users\reinder.huizinga\PycharmProjects\Tickets per vestiging\venv\simple_changes.xlsx")
changes = \
    changes.rename(columns={"requester.branch.name": "Adres", "priority.name": "Prio", "number": "TicketNummer"})
tickets = tickets.rename(columns={"caller.branch.name": "Adres", "priority.name": "Prio", "number": "TicketNummer"})

df = tickets.merge(changes, on="adress")

# # Merge the locations and tickets data into one dataframe
# df = pd.merge(locations, combo, on="Adres")
# df = df[['Adres', 'Coordinates', 'Count']]
# df.to_excel(r"C:\Users\reinder.huizinga\PycharmProjects\Tickets per vestiging\venv\testtt.xlsx")
# # Add markers to the map for each location, with the size of the marker representing the number of tickets
# bounds = [[50.75, 3.25], [53.75, 7.25]]
# m = folium.Map(location=[52.3780, 4.9036], zoom_start=8)
# m.fit_bounds(bounds)
# ## what

for i, row in df.iterrows():
    try:
        coordinates = eval(row["Coordinates"])
        longitude, latitude = coordinates[1], coordinates[0]
        folium.CircleMarker(
            location=[latitude, longitude],
            radius=row["Count"],
            color="red",
            fill=True,
            fill_color="red",
            popup=f"{row[0]}:<br> {row['Count']} tickets<br>",
            min_width=1000
        ).add_to(m)
    except TypeError:
        continue
# Save the map to an HTML file

m.save(r"C:\Users\reinder.huizinga\PycharmProjects\Tickets per vestiging\venv\tickets_per_location.html")
