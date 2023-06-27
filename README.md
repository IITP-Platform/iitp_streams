# How to execute?

A basic command for stream process to execute is as follows: 
```shell
faust -A <app_name> worker
```

* `app_name`: stream application name(or process name).
* `app_name` should be same with name of python file.
* In this demo, you can execute faust stream application with the command as follows:
  ```shell
    faust -A main worker
    ```
  
## State Store

* faust uses RocksDB as memory cache for stateful stream processing.
* This cache is represented as `Table` object.
  ```python
    cache = app.Table(
        "cache_name",
        partitions=1,
        default=None,
    )
    ```
* The value of `partitions` parameter should be as same as the number of partitions that consumer(application) subscribe.
  * For this demo, assume that `chest` topic has only one partition.
  * Accordingly, the `partition` parameter is just 1.

### Usage of State Store

* `Table` object is very similar to dictionary of python.
* You can easily access an element of state store with subscription method(`[]`).