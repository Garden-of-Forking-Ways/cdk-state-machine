from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy,
    aws_sqs as sqs,
)
from constructs import Construct


class CdkStateMachineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self,
            "CdkStateMachineQueue",
            visibility_timeout=Duration.seconds(300),
            removal_policy=RemovalPolicy.DESTROY,
        )
