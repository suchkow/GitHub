from nemoguardrails import LLMRails, RailsConfig
from IPython.display import Markdown

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

res = await rails.generate_async(prompt="What does NVIDIA AI Enterprise enable?")
print(Markdown(f"{res}"))
