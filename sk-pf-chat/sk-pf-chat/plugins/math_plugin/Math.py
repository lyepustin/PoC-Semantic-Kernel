import math

from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)

from semantic_kernel import SKContext

class Math:

    @sk_function(
        description="Takes the square root of a number",
        name="Sqrt",
        input_description="The value to take the square root of",
    )
    def square_root(self, number: str) -> str:
        return str(math.sqrt(float(number)))

    @sk_function(
        description="Takes the square of a number",
        name="Square",
        input_description="The value to square",
    )
    def square(self, number: str) -> str:
        return str(float(number) ** 2)

    @sk_function(
        description="Adds two numbers together",
        name="Add",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to add",
    )
    @sk_function_context_parameter(
        name="input2",
        description="The second number to add",
    )
    def add(self, context: SKContext) -> str:
        return str(float(context.get("input")) + float(context.get("input2")))
    
    @sk_function(
        description="Subtracts two numbers",
        name="Subtract",
    )    
    @sk_function_context_parameter(
        name="input",
        description="The number to subtract from",
    )
    @sk_function_context_parameter(
        name="input2",
        description="The number to subtract",
    )
    def subtract(self, context: SKContext) -> str:
        return str(float(context.get("input")) - float(context.get("input2")))
    
    @sk_function(
        description="Multiply two numbers together",
        name="Multiply",
    )    
    @sk_function_context_parameter(
        name="input",
        description="The first number to multiply",
    )
    @sk_function_context_parameter(
        name="input2",
        description="The second number to multiply",
    )
    def multiply(self, context: SKContext) -> str:
        return str(float(context.get("input")) * float(context.get("input2")))
    
    @sk_function(
        description="Divide two numbers",
        name="Divide",
    )    
    @sk_function_context_parameter(
        name="input",
        description="The dividend",
    )
    @sk_function_context_parameter(
        name="input2",
        description="The divisor",
    )
    def divide(self, context: SKContext) -> str:
        divisor = float(context.get("input2"))
        if divisor == 0:
            return "Error: Division by zero"
        return str(float(context.get("input")) / divisor)

