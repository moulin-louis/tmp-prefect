from prefect import flow
from prefect.events import DeploymentEventTrigger


@flow
def tata():
    print("TATA")


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/moulin-louis/tmp-prefect.git",
        entrypoint="flow-child.py:tata",
    ).deploy(
        name="child-deployement",
        work_pool_name="test-work-pool",
        triggers=[
            DeploymentEventTrigger(
                name="toto-succeeded-trigger",
                expect={"prefect.flow-run.Completed"},
                match={"prefect.resource.id": "prefect.flow-run.*"},
                match_related={
                    "prefect.resource.name": "parent-deployement",
                    "prefect.resource.role": "flow",
                },
            )
        ],
    )
