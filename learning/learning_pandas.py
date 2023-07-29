import pandas as pd

scores = {"name": ['Ray', 'Japsy', 'Zosa'],
          "city": ['San Franscisco', 'San Franscisco', 'Denver'],
          "score": [75, 92, 94]

          }

df = pd.DataFrame(scores)

print(df)