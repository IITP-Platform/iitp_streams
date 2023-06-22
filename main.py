import faust

from schema import ChestDeviceSensorValue


# Faust application definition.
app = faust.App(
    "main",
    broker="kafka://localhost:19092",
    value_serializer="json",
)

# Topic for stream application to subscribe.
chest_topic = app.topic(
    "chest",
    key_type=str,
    value_type=ChestDeviceSensorValue,
)

# State store for tracking previous data.
cache = app.Table(
    "windowing_queue",
    partitions=1,
    default=None,
)

# Stream topology definition.
@app.agent(chest_topic)
async def process(sensor_data):
    async for user_id, data in sensor_data.items():
        # If there is no same user_id, push empty list.
        if cache.get(user_id) is None:
            cache[user_id] = []

        # Append newer version of data.
        # TODO: this demo pushed connection_id of value. you need to push the main body of data for processing.
        cache[user_id].append(data.connection_id)

        # If the size of cache is bigger than window_size, extract features.
        if len(cache[user_id]) > 2:
            # Pop the oldest value in queue.
            cache[user_id].pop(0)
            # TODO: extract feature data for given windowing cache.
            print("window operation is needed: ", cache[user_id])
