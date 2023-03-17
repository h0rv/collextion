import json


def getPodcastInfo():
    schema = loadPodcastSchema()
    print(schema)
    return NotImplemented


"""
Load the podcast JSON schema into an object
"""
def loadPodcastSchema():
    with open("../schema/podcast.json", "r") as read_file:
        schema = json.load(read_file)
    return schema

if __name__ == "__main__":
    getPodcastInfo()

