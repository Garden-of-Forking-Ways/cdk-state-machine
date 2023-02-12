#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_state_machine.cdk_state_machine_stack import CdkStateMachineStack

app = cdk.App()
CdkStateMachineStack(
    app,
    "CdkStateMachineStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEPLOY_ACCOUNT'),
        region=os.getenv('CDK_DEPLOY_REGION')
    ),
)

app.synth()
