def run1(**inputs):
    print(f"Here run 1 {inputs}")


def run2(**inputs):
    print(f"Here run 2 {inputs}")


def run3(**inputs):
    print(f"Here run 3 {inputs}")


def run(**inputs):
    inputs = {
        key: None if value == "null" or value == "" else value
        for key, value in inputs.items()
    }
    print(inputs)

    stage = inputs.get("stage")
    print(stage)
    feed_name = inputs.get("feed_name")
    # config=get_feed_config(feed_name)
    stage_functions = {
        "run1": lambda inputs: run1(**inputs),
        "run2": lambda inputs: run1(**inputs),
        "run3": lambda inputs: run1(**inputs),
    }
    if stage in stage_functions:
        if callable(stage_functions[stage]):
            return stage_functions[stage](inputs)
        else:
            print(stage_functions[stage])
    else:
        raise NotImplementedError(f"Unkown stage: stage {stage} is not supported! ")


# inputs={"feed_name":"lol","run1"}
inputs = {"stage": "run1", "aa": "bb"}
# run(stage="run1",lol="ll")
run(**inputs)
