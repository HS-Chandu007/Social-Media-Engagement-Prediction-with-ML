📊 Social Media Engagement Predictor

“What if you could know how your post will perform before you even publish it?”

This project answers exactly that.

It is a complete machine learning application that predicts how engaging a social media post will be — using real ML models, real deployment decisions, and a clean interactive interface.

🌱 Why this project exists

Social media success is unpredictable.
Sometimes a post goes viral. Sometimes it disappears.

This project tries to bring data-driven clarity into that uncertainty.

Instead of guessing, we let machine learning estimate:

“Out of 100 people, how many are likely to interact with this post?”

And then we explain that result in a way anyone can understand.

🚀 What this app does

You enter details about a post:

Post size

Views, likes, comments, shares

Platform and post type

And the system instantly predicts:

Engagement percentage

Engagement category (Low / Medium / High)

A simple business-friendly explanation

No ML jargon. No confusion.

🤖 Models behind the scenes

This project uses two different ML models, each chosen for a specific strength:

Model	Why it was used
LightGBM	Extremely fast and accurate for numerical encoded data
CatBoost	Excellent at handling categorical features directly

You can switch between them directly from the UI.

🧠 How to read the result

The output is not just a number.

It is translated into human meaning:

Engagement %	Meaning
< 10%	🔴 Low engagement
10–30%	🟡 Medium engagement
> 30%	🟢 High engagement

Example:

Out of 100 users, about 18.5 may interact with this post.

That sentence is intentional — it makes ML understandable.

🖥 User Interface

The interface is designed like a small product dashboard:

Everything fits in one screen

No scrolling

No confusing inputs

Only relevant fields are shown based on model mode

This project treats UX as seriously as ML.

⚠️ A real engineering story: why FastAPI is not used here

Originally, this project was designed as:

Which is how real production systems often work.

However, Hugging Face Python Spaces only support one exposed service.

Trying to run two servers caused:

Connection failures

Localhost API issues

Deployment instability

So instead of forcing the architecture, a decision was made:

The prediction logic was moved directly into Gradio for Hugging Face deployment.

This was not a shortcut.
It was an engineering trade-off based on platform constraints.

The FastAPI version is still maintained separately for production-style API deployment.

This decision reflects how real engineers work:

Architecture is not about perfection — it’s about choosing what works best in real conditions.

▶️ Run locally
pip install -r requirements.txt
python app.py

🌍 Deployment

This application is deployed on Hugging Face Spaces using Gradio.

It runs fully in the browser and requires no backend setup for users.

🏆 What this project actually demonstrates

This is not just a model.

It demonstrates:

✔ Machine learning modeling
✔ Feature engineering
✔ Dual-model system design
✔ UI/UX thinking
✔ Business interpretation
✔ Deployment constraints handling
✔ Product mindset

In short: end-to-end ML engineering.

----Built with curiosity, frustration, learning, debugging, and a lot of persistence.

⭐ If you reached here

Thank you for reading this far.

If you liked the idea, the execution, or the learning process — a ⭐ means a lot.
