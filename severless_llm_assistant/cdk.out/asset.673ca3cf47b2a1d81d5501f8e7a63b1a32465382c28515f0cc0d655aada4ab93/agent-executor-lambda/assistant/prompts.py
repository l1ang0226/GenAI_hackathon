from datetime import datetime
from langchain.prompts.prompt import PromptTemplate

# ============================================================================
# Claude basic chatbot prompt construction
# ============================================================================

date_today = str(datetime.today().date())

_CALUDE_PROMPT_TEMPLATE = f"""

Human: The following description is an adventure story.
First, create a short story. Then, wait until the user input is entered.

Below is the user input format:

Water : score
Earth : score
Fire : score
Wind : score
Remain : score


If the score of "Remain" is less than or equal to zero, then continue the story that leads toward a bad ending.
If story ended 
If not, then the plot continues to develop based on the highest score among the above elements excluding the score of "Remain".


The current story is within the <current_story> XML tags below, where Hu refers to user input and AI refers to the story:
<current_story>
{{history}}
</current_story>

Here is the user's next input:
<user_input>
{{input}}
</user_input>
"""

CLAUDE_PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=_CALUDE_PROMPT_TEMPLATE
)

## Placeholder for lab 3 - agent prompt code
## replace this placeholder with code from lab 3, step 2 as instructed.
