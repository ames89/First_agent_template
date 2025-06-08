from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, load_tool
import requests
import yaml
from tools.final_answer import FinalAnswerTool
from custom_tools import (
    my_custom_tool,
    multiply_two_numbers,
    is_coffee_ready_to_drink,
    get_current_time_in_timezone,
)

from Gradio_UI import GradioUI


final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud'

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",  # it is possible that this model may be overloaded
    custom_role_conversions=None,
)


# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", "r") as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[  ## add your tools here (don't remove final answer)
        final_answer,
        multiply_two_numbers,
        is_coffee_ready_to_drink,
        get_current_time_in_timezone,
        image_generation_tool,
        DuckDuckGoSearchTool(),
    ],
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates,
)


GradioUI(agent).launch()
