import prefect
from prefect import flow

@flow
def toto():
    print("Hello")

if __name__ == "__main__":
    toto.deploy(
        name="parent-flow",
        work_pool_name="test-work-pool",
        cron="*/5 * * * *",
    )
