from lymbix import Lymbix
lymbix = Lymbix('dfcad1488854c47dd26f30d3eb424c77e5606801')

query = "I really hate the way pizza tastes"
dic = lymbix.tonalize(query)
print query
print dic["dominant_emotion"]
print dic ["clarity"]
