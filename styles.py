def load_css():
    return  """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

        /* Global */
        html, body, [class*="css"] {
            font-family: 'DM Mono', monospace;
        }

        /* Background */
        .stApp {
            background-color: #0d0d0f;
            color: #e8e4dc;
        }

        /* Hide default Streamlit header/footer */
        #MainMenu, footer, header { visibility: hidden; }

        /* Title */
        h1 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 2.6rem !important;
            letter-spacing: -1px !important;
            color: #f0ebe0 !important;
        }

        h2, h3 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 700 !important;
            color: #f0ebe0 !important;
        }

        /* Metric cards */
        [data-testid="stMetric"] {
            background: #17171a;
            border: 1px solid #2a2a2f;
            border-radius: 12px;
            padding: 20px 24px !important;
            transition: border-color 0.2s;
        }
        [data-testid="stMetric"]:hover {
            border-color: #c8f55a;
        }
        [data-testid="stMetricLabel"] p {
            font-family: 'DM Mono', monospace !important;
            font-size: 0.72rem !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #6b6b72 !important;
        }
        [data-testid="stMetricValue"] {
            font-family: 'Syne', sans-serif !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: #c8f55a !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] {
            background: #17171a;
            border: 1px dashed #2a2a2f;
            border-radius: 12px;
            padding: 12px;
        }

        /* Chart container */
        [data-testid="stArrowVegaLiteChart"] {
            background: #17171a !important;
            border-radius: 12px;
            padding: 16px;
            border: 1px solid #2a2a2f;
        }

        /* Divider */
        hr {
            border-color: #2a2a2f !important;
            margin: 28px 0 !important;
        }

        /* Subheader accent */
        .section-label {
            font-family: 'DM Mono', monospace;
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #6b6b72;
            margin-bottom: 8px;
        }

        /* Warning / info box */
        [data-testid="stAlert"] {
            background: #17171a;
            border: 1px solid #2a2a2f;
            border-radius: 12px;
            color: #e8e4dc;
        }

        /* Savings badge */
        .savings-badge {
            display: inline-block;
            background: #c8f55a;
            color: #0d0d0f;
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 2rem;
            padding: 10px 28px;
            border-radius: 100px;
            letter-spacing: -0.5px;
        }

        .savings-label {
            font-family: 'DM Mono', monospace;
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #6b6b72;
            margin-top: 8px;
        }
        </style>
    """