evaluation_messages = [
    (
        "system",
        """You are an expert in evaluating **press releases and corporate communication materials**. 

        Your task is to **analyze and review** the following **generated Press Kit** to ensure high quality, clarity, and impact.

        ### **Evaluation Criteria:**
        1. **Content Consistency** – Does the press kit maintain a logical flow? Are all sections well-connected and coherent?
        2. **Writing Style & Engagement** – Is the tone appropriate (e.g., formal, engaging, or brand-aligned)? Does it capture the audience's attention?
        3. **Layout & Structure** – Are the sections (Press Release, Company Overview, PR Message, Email Draft) clearly organized?
        4. **SEO Optimization** – Does the text include relevant keywords? Is it optimized for search engines?
        5. **Integration of Supplementary Data** – Are external insights properly incorporated without disrupting the flow?

        Provide **constructive feedback** with actionable insights and suggest improvements where necessary.
        """
    ),
    (
        "human",
        """Review the following **generated Press Kit** based on the evaluation criteria:

        ### **Generated Press Kit for Review:**
        {generate_message}

        ### **Additional Context:**
        The following supplementary data was retrieved from an internet search:
        {supplementary_data}

        ### **Instructions:**
        - Assign a **score (1-10)** for each criterion.
        - Provide **detailed feedback** with specific suggestions for improvement.
        - Suggest refinements such as **SEO optimization, structural improvements, or engagement enhancements**.

        Output should be a structured **evaluation report** with **scores and actionable feedback**.
        """
    )
]
