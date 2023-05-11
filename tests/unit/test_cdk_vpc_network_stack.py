import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_vpc_network.cdk_vpc_network_stack import CdkVpcNetworkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_vpc_network/cdk_vpc_network_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkVpcNetworkStack(app, "cdk-vpc-network")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
