import gradio as gr
import lightgbm as lgb
from catboost import CatBoostRegressor
import numpy as np
import json


lgb_model = lgb.Booster(model_file="lightgbm.txt")

cat_model = CatBoostRegressor()
cat_model.load_model("catboost.cbm")

with open("feature_order_lightgbm.json") as f:
    LGB_FEATURES = json.load(f)


def predict(mode, post_size, views, likes, comments, shares,
            platform, post_type, platform_enc, post_type_enc):

    if mode == "raw":
        row = [
            post_size, views, likes, comments, shares,
            platform_enc, post_type_enc
        ]
        x = np.array(row).reshape(1, -1)
        pred = lgb_model.predict(x)[0]

    else:
        row = [
            platform, post_type,
            post_size, views, likes, comments, shares
        ]
        x = np.array(row, dtype=object).reshape(1, -1)
        pred = cat_model.predict(x)[0]

    percent = round(pred * 100, 2)

    if percent < 10:
        category = "🔴 Low Engagement"
    elif percent < 30:
        category = "🟡 Medium Engagement"
    else:
        category = "🟢 High Engagement"

    return {
        "Predicted Engagement (%)": f"{percent}%",
        "Engagement Category": category,
        "Explanation": f"Out of 100 users, about {percent} may interact with this post."
    }


with gr.Blocks() as demo:

    gr.Markdown("""
<div id="title">📊 Social Media Engagement Predictor</div>
<div id="subtitle">Predict post performance before publishing 🚀</div>

---

### ℹ️ About This App
This application predicts how engaging a social media post will be using machine learning.

### 🤖 Models Used
• **LightGBM (Raw Mode):** Uses encoded numerical features for fast and accurate prediction.  
• **CatBoost (Categorical Mode):** Uses real platform and post type values directly.

### 📌 Engagement Meaning
The predicted value represents the **percentage of users likely to interact** with the post.

---
""")

    mode = gr.Radio(
        ["raw", "cat"],
        value="raw",
        label="Select Model Mode"
    )

    with gr.Row():

        with gr.Column(scale=1, elem_classes="section"):
            gr.Markdown("### 📥 Post Inputs")

            post_size = gr.Number(label="Post Size (MB)")
            views = gr.Number(label="Views")
            likes = gr.Number(label="Likes")
            comments = gr.Number(label="Comments")
            shares = gr.Number(label="Shares")

        with gr.Column(scale=1, elem_classes="section"):
            gr.Markdown("### 🧩 Post Type Information")

            platform = gr.Dropdown(
                ["Facebook", "Instagram", "Twitter"],
                label="Platform",
                visible=False
            )

            post_type = gr.Dropdown(
                ["Text", "Video", "Image"],
                label="Post Type",
                visible=False
            )

            platform_enc = gr.Number(
                label="Platform Encoded Value",
                visible=True
            )

            post_type_enc = gr.Number(
                label="Post Type Encoded Value",
                visible=True
            )

    def toggle_inputs(m):
        if m == "raw":
            return (
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=True),
                gr.update(visible=True),
            )
        else:
            return (
                gr.update(visible=True),
                gr.update(visible=True),
                gr.update(visible=False),
                gr.update(visible=False),
            )

    mode.change(
        toggle_inputs,
        inputs=mode,
        outputs=[platform, post_type, platform_enc, post_type_enc]
    )

    btn = gr.Button("🚀 Predict Engagement", variant="primary")
    output = gr.JSON(label="Prediction Result")

    btn.click(
        predict,
        inputs=[
            mode, post_size, views, likes, comments, shares,
            platform, post_type, platform_enc, post_type_enc
        ],
        outputs=output
    )

demo.launch(css="""
#title {text-align:center; font-size:30px; font-weight:bold;}
#subtitle {text-align:center; color:gray; margin-bottom:10px;}
.section {border:1px solid #ddd; padding:10px; border-radius:8px;}
""")
