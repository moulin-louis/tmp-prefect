from prefect import flow


@flow
def tata():
    print("TATA")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/moulin-louis/tmp-prefect.git",
        entrypoint="flow-child.py:tata"
    ).deploy(
        name="child-deployement",
        work_pool_name="test-work-pool",
        triggers=[
            DeploymentEventTrigger(
                expect={"prefect.flow-run.Completed"},
                match_related={"prefect.resource.name": "parent-deployement"},
            )
        ],
    )
