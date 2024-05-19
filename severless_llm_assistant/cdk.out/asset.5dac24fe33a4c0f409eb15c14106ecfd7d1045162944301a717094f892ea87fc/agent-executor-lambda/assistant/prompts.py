from datetime import datetime
from langchain.prompts.prompt import PromptTemplate

# ============================================================================
# Claude basic chatbot prompt construction
# ============================================================================

date_today = str(datetime.today().date())

_CALUDE_PROMPT_TEMPLATE = f"""
You are RPG story creater.you will create advanture story base on user input.

If history is empty , create short background about story beggin.

Then, wait until the user input is entered.
Below is the user input format:

Water : score
Earth : score
Fire : score
Wind : score
Remain : score


the plot continues to develop based on the highest score among the above elements excluding the score of "Remain".
If the score of "Remain" is less than or equal to zero, then continue the story that leads toward a bad ending.

The story should be in few sentence.

Only response the story content.


Here is the previously happened story:
{{history}}

Here is the user's next input:
<user_input>
{{input}}
</user_input>

Here is ouput format:
<story>
Story content
</story>

Note that story must in few sentence
"""

CLAUDE_PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=_CALUDE_PROMPT_TEMPLATE
)

## Placeholder for lab 3 - agent prompt code
## replace this placeholder with code from lab 3, step 2 as instructed.
