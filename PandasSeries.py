import pandas as pd
seriesObj = pd.Series([1,2,2],index=["one","two","three"])
listseriesobj= pd.Series({1:1,2:2},index=["one","two"])
print(listseriesobj)
print(seriesObj)
seriesObj.name = "numberseries"
seriesObj.index.name ="sl.no"
seriesObj["one"]=1000
print(seriesObj[::-1])
