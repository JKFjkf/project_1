from rich.progress import track

for step in track(range(10000000)):
    track(step)