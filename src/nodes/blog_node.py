from langchain_core.messages import HumanMessage

from src.states.blogstate import BlogState
from src.states.blogstate import Blog


class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        Create the title of the blog
        """
        topic=state["topic"]
        if topic is not None:
            prompt = f"""
                    You are an expert blog content writter. Use markdown formatting. Generate a blog title 
                    for the {topic}. This title should be creative.
                    """
            system_message = prompt.format(topic=topic)
            response = self.llm.invoke(system_message)
            return {"blog": Blog(title=response.content.strip(), content="")}

    def content_creation(self, state: BlogState):
        """
        Create the content of the blog
        """
        topic=state["topic"]
        blog = state["blog"]
        if topic is not None:
            prompt = f"""
                      You are an expert blog content writter. Use markdown formatting. 
                      Generate a blog content for the {topic}. This title should be creative.
                      """
            system_message = prompt.format(topic=topic)
            response = self.llm.invoke(system_message)
            return {"blog": Blog(title=blog.title, content=response.content.strip())}

    def translation(self, state: BlogState):
        """
        Change the language of the blog based on the user input
        """
        language=state["language"]
        blog_content = state['blog']

        if language is not None:
            message_prompt = f"""
        You are an expert translator.
        Translate the following blog into {language} language without changing meaning, tone, style for the
        title {blog_content.title} and the content: {blog_content.content}
        """

            messages=[
                HumanMessage(content=message_prompt)
            ]
            content_response = self.llm.with_structured_output(Blog).invoke(messages)
            return {"blog": content_response}
