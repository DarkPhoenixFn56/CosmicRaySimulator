# 🚀 Cosmic Ray Classifier – Simulator

Presenting a small but powerful ML project close to my heart — The **Cosmic Ray Simulator**, built using real Cherenkov telescope data. 🔭

## 🎯 Objective

The goal of this project is to **classify atmospheric particle events** as either **gamma rays** or **hadrons**, using **statistical features** extracted from detector images.

## 🧠 How it Works

- **Data**: Trained a **logistic regression model** on **19,000+ instances** of cosmic ray data.
- **Hyperparameter Tuning**: Used `GridSearchCV` to find the best model parameters.
- **Model Saving**: The best model was **pickled** for easy deployment.
- **Deployment**: Built an interactive app with **Streamlit** where users can input physical features (like `fAlpha`, `fLength`, `fConc`) and get real-time predictions from the model.
- The app returns a **class label** (gamma ray or hadron) and a **confidence score**.

Check the video below for a quick demonstration of the working!

## 📊 Behind the Scenes

- **Full Pipeline**: Complete preprocessing, scaling, and model training pipeline.
- **Real-Time Prediction**: An intuitive **UI** built using **Streamlit**, allowing users to simulate and predict cosmic ray classifications interactively.
- **Technologies Used**:
  - `scikit-learn`: For machine learning.
  - `joblib`: For model serialization.
  - `pandas`: For data manipulation.
  - `Streamlit`: For building the interactive app.

A heartfelt project born out of **bugs**, **retries**, a ton of **debugging**, and a quiet little **win** that reminded me why I love this process. 🌠
---

## Live Demo? Check this out:
https://darkphoenixfn56-cosmicraysimulator-abc-vructh.streamlit.app/


## 🔧 Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/DarkPhoenixFn56/CosmicRaySimulator.git
    cd cosmic-ray-simulator
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Enjoy the simulation!

---

## 🌠 What’s Next?

- [ ] **Extend features**: Add more particle classes for classification.
- [ ] **Real-time data**: Integrate real-time cosmic ray detection data.
- [ ] **Advanced models**: Explore deep learning models for improved predictions.
- [ ] **UI Enhancements**: Improve the user experience with more detailed visualizations.

---

## 🤝 Contributing

If you’re passionate about physics, machine learning, or open-source contributions — feel free to fork and enhance this project! Pull requests are always welcome.

---

## 📜 License

MIT License.

---

## 🙋‍♀️ About Me

I’m an AI student and a passionate learner. Feel free to connect with me:
https://github.com/DarkPhoenixFn56
