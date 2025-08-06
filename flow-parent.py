import prefect
from prefect import flow

@flow
def toto():
    print("Hello")
    with open("/tmp/log", "a") as f:
        f.write("FDSDSFDS")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/moulin-louis/tmp-prefect.git",
        entrypoint="flow-parent.py:toto"
    ).deploy(
        name="parent-deployement",
        work_pool_name="test-work-pool",
        cron="*/5 * * * *",
    )
