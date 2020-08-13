"""
https://refactoring.guru/design-patterns/factory-method/python/example

client: main
product: _serialize_to_json() and _serialize_to_xml
creator: get_serializer()
"""

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)

# this is the **creator**
def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)

# this is the product
def _serialize_to_json(song):
    pass # return json object or string

# this is the product
def _serialize_to_xml(song):
    pass # return xml object or string

if __name__ == "__main__":
    song = Song(1, "When the leeve breaks", "led zeppelin")
    serializer = SongSerializer()

    # the code section that calls tha serialize() is called client code
    song_json = serializer.serialize(song, 'JSON')
    song_xml = serializer.serialize(song, 'XML')
