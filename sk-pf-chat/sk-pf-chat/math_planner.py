import asyncio

from plugins.math_plugin.Math import Math

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.planning.sequential_planner import SequentialPlanner
from semantic_kernel.planning.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)

from promptflow import tool
from promptflow.connections import AzureOpenAIConnection


@tool
def chat(
    question: str,
    deployment_name: str,
    connection: AzureOpenAIConnection,
):

    # Create kernel for math plugin
    math_kernel = sk.Kernel(log=sk.NullLogger())
    
    gpt35_chat_service = AzureChatCompletion(
        deployment_name=deployment_name,
        endpoint=connection.api_base,
        api_key=connection.api_key,
    )

    math_kernel.add_chat_service("azure_gpt35_chat_completion", gpt35_chat_service)
    
    # Import the math plugin
    math_kernel.import_skill(Math())
    
    # Create the planner to solve the math problem
    planner = SequentialPlanner(kernel=math_kernel)

    # Create a plan to solve the math problem
    ask = "Solve this math problem: " + question
    plan = asyncio.run(planner.create_plan_async(ask))
        
    # Get the result of the math problem
    math_answer = asyncio.run(math_kernel.run_async(plan)).result

    for index, step in enumerate(plan._steps):
        print("Function:" + step.skill_name + "." + step._function.name)
        print("Input varsı "+str(step.parameters.variables))
        print("Output vars: " + str(step._outputs))
        print("Result: " + str(math_answer))

    # Add the answer of the math problem to the context
    return "The bot should respond with this answer to the user's question: " + math_answer
