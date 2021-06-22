import json,sys
import simplekml as sk

def read_json(obj):
    lst = []
    keys = list(obj["flights"].keys())
    flight_list = obj["flights"][keys[0]]["track"]
    for item in flight_list:
        one = item["coord"][0]
        two = item["coord"][1]
        lst.append((one,two))
    return lst

def make_kml(lst,filename):
    kml = sk.Kml()
    kml.newlinestring(coords=lst)
    kml.save(filename+".kml")

if __name__ == "__main__":
    with open(sys.argv[1],"r") as f:
        j = json.load(f)
        l = read_json(j)
        make_kml(l,sys.argv[1])


