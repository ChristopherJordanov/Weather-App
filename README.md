<h1 align="center" id="title">Weather App</h1>

<p id="description">An interactive responsive Streamlit application that lets you explore the next 5‑day weather forecast for any city worldwide. Pick your favourite time of day toggle between °C/°F and view beautiful charts metrics and icons that update instantly.</p>

<h2>🚀 Demo</h2>

[https://openweatherapp.streamlit.app](https://openweatherapp.streamlit.app)

<h2>Project Screenshots:</h2>

<table>
  <tr>
    <td><img src="https://i.imgur.com/p3XChWl.png" width="600"/></td>
    <td><img src="https://i.imgur.com/x5NwBCO.png" width="600"/></td>
    <td><img src="https://i.imgur.com/ZQC5bav.png" width="600"/></td>
  </tr>
</table>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Forecast Visualization - Line chart of the forecasted temperature and dynamic weather icons
*   User Controls - Get your information about the weather by searching a city name or automatically by location Time of day filter Metric/imperial unit toggle
*   Smart UI - st.metric cards with responsive layout
*   Deployment - One‑click deploy on Streamlit Cloud • Requirements pinned for reproducibility

<h2>🛠️ Installation Steps:</h2>

<p>1. Python&nbsp;3.9 or newer</p>

<p>2. A free OpenWeatherMap API key</p>

<p>3. Clone the repo</p>

```
$ git clone https://github.com/your‑username/weather‑app.git | $ cd weather‑app
```

<p>4. Install dependencies</p>

```
$ pip install -r requirements.txt
```

<p>5. Add your API key</p>

```
$ cp .env.example .env   # then edit .env and paste your key
```

<p>6. Run locally</p>

```
$ streamlit run app.py
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
  
*   Streamlit

<h2> 🧠 What I Learned </h2>
*   Making authenticated API calls and handling JSON responses

*   Parsing and structuring data for visualisation

*   Building responsive layouts in Streamlit with columns and custom HTML/CSS

*   Data visualisation with matplotlib / Plotly inside Streamlit

*   Environment variables and secret handling in deployed apps

*   Cloud deployment & CI basics with Streamlit Community Cloud
