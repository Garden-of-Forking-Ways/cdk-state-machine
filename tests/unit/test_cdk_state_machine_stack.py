# import aws_cdk as core
# import aws_cdk.assertions as assertions

# from cdk_state_machine.cdk_state_machine_stack import CdkStateMachineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_state_machine/cdk_state_machine_stack.py
# def test_sqs_queue_created():
    # app = core.App()
    # stack = CdkStateMachineStack(app, "cdk-state-machine")
    # template = assertions.Template.from_stack(stack)

    # template.has_resource_properties("AWS::SQS::Queue", {
    #     "VisibilityTimeout": 300
    # })
    # assert [0, 1, 2] == [0, 1, 3]
