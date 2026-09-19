import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CropSynq | Smart Packaging",
    page_icon="🌱",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main {
    background: #f4faf5;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(135deg, #e2f6e7, #f8fff9);
    padding: 35px;
    border-radius: 22px;
    border: 1px solid #ccebd4;
    margin-bottom: 25px;
}

.hero h1 {
    color: #123d25;
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    color: #486653;
    font-size: 18px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e1ebe3;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.result {
    background: #f8fff9;
    border: 2px solid #b9dfc2;
    padding: 28px;
    border-radius: 20px;
    margin-top: 25px;
}

.tag {
    display: inline-block;
    padding: 7px 12px;
    margin: 4px;
    border-radius: 20px;
    background: #e8f6ec;
    color: #246238;
    font-size: 14px;
}

.spec {
    background: #ffffff;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #e1ebe3;
    margin-bottom: 10px;
}

.benefit {
    background: #f7fcf8;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #55a66a;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- PACKAGING DATABASE ----------------

packaging_data = {

    "Tomato": {
        "icon": "🍅",
        "package": "Protective Ventilated Corrugated Box",
        "material": "Food-grade corrugated fibreboard",
        "box_type": "Ventilated corrugated box",
        "ventilation": "High",
        "protection": "High",
        "moisture": "Moderate",
        "handling": "Careful stacking and reduced crushing",
        "use": "Short-distance and local-market transport",
        "farmer": "Helps reduce bruising and physical damage while transporting tomatoes to the market.",
        "seller": "Provides ventilation and protection during handling and temporary storage.",
        "reason": "Tomatoes are sensitive to bruising and need ventilation. Since the selected priority is damage reduction, CropSynq gives higher importance to physical protection.",
        "match": 80,
        "damage": "High"
    },

    "Potato": {
        "icon": "🥔",
        "package": "Ventilated Jute / Corrugated Produce Bag",
        "material": "Breathable jute or food-grade corrugated fibreboard",
        "box_type": "Ventilated produce bag/box",
        "ventilation": "High",
        "protection": "Medium",
        "moisture": "Moderate",
        "handling": "Avoid excessive compression",
        "use": "Local transport and short-term storage",
        "farmer": "Allows air movement and helps reduce moisture accumulation during transportation.",
        "seller": "Supports breathable storage and easier handling of potato produce.",
        "reason": "Potatoes benefit from airflow. CropSynq gives priority to breathable packaging when ventilation is important.",
        "match": 82,
        "damage": "Medium"
    },

    "Apple": {
        "icon": "🍎",
        "package": "Ventilated Corrugated Fruit Box",
        "material": "Food-grade corrugated fibreboard",
        "box_type": "Partitioned ventilated fruit box",
        "ventilation": "High",
        "protection": "High",
        "moisture": "Moderate",
        "handling": "Use partitions or cushioning where required",
        "use": "Transport and market distribution",
        "farmer": "Helps protect apples from impact and compression during transportation.",
        "seller": "Improves product presentation and reduces physical damage during handling.",
        "reason": "Apples can be damaged by impact and compression. CropSynq therefore considers both ventilation and physical protection.",
        "match": 86,
        "damage": "High"
    },

    "Banana": {
        "icon": "🍌",
        "package": "Ventilated Corrugated Banana Box",
        "material": "Food-grade corrugated fibreboard",
        "box_type": "Ventilated banana transport box",
        "ventilation": "High",
        "protection": "Medium",
        "moisture": "Moderate",
        "handling": "Avoid excessive pressure and rough handling",
        "use": "Transport to market",
        "farmer": "Supports safer transportation while allowing airflow around the produce.",
        "seller": "Helps maintain product quality during handling and market transportation.",
        "reason": "Bananas are sensitive to handling damage and require airflow. CropSynq balances ventilation and protection.",
        "match": 84,
        "damage": "High"
    },

    "Carrot": {
        "icon": "🥕",
        "package": "Ventilated Produce Crate",
        "material": "Food-grade reusable plastic or corrugated produce container",
        "box_type": "Ventilated produce crate",
        "ventilation": "High",
        "protection": "Medium",
        "moisture": "Moderate",
        "handling": "Avoid excessive compression",
        "use": "Local market transport",
        "farmer": "Provides airflow and practical protection during transportation.",
        "seller": "Supports organized handling and reduces unnecessary compression of produce.",
        "reason": "Carrots require airflow and protection from excessive handling pressure. CropSynq therefore recommends ventilated packaging.",
        "match": 81,
        "damage": "Medium"
    }
}


# ---------------- RECOMMENDATION FUNCTION ----------------

def recommend(commodity, storage, transport, priority):

    data = packaging_data[commodity]

    match = data["match"]

    if priority == "Reduce Damage":
        match += 5

    elif priority == "Increase Ventilation":
        if data["ventilation"] == "High":
            match += 5

    elif priority == "Reduce Cost":
        match -= 3

    if transport == "Long Distance":
        match -= 3

    if storage == "Cold Storage":
        match += 2

    match = max(60, min(match, 95))

    return data, match


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
    <h1>🌱 CropSynq</h1>
    <p>AI-Based Intelligent Food Packaging Recommendation System</p>
    <p>Smart packaging decisions for farmers, sellers and food businesses.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

st.sidebar.title("⚙️ Packaging Inputs")

commodity = st.sidebar.selectbox(
    "🍅 Commodity",
    ["Tomato", "Potato", "Apple", "Banana", "Carrot"]
)

storage = st.sidebar.selectbox(
    "🌡️ Storage Condition",
    ["Ambient", "Cold Storage", "Short-Term Storage"]
)

transport = st.sidebar.selectbox(
    "🚚 Transport",
    ["Local Market", "Long Distance", "Wholesale Market"]
)

priority = st.sidebar.selectbox(
    "🎯 Main Priority",
    ["Reduce Damage", "Increase Ventilation", "Reduce Cost"]
)

generate = st.sidebar.button(
    "🔍 Generate AI Recommendation",
    use_container_width=True
)


# ---------------- INTRO CARDS ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h2>👨‍🌾 Farmer</h2>
    <p>Get a practical packaging option before sending produce to the market.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h2>🏪 Seller</h2>
    <p>Choose packaging based on handling, transport and storage conditions.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h2>🤖 AI Logic</h2>
    <p>Matches commodity characteristics with user-selected conditions and priorities.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- RESULT ----------------

if generate:

    data, match = recommend(
        commodity,
        storage,
        transport,
        priority
    )

    st.markdown("""
    <div class="result">
    <h2>📦 Smart Packaging Recommendation</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"## {data['icon']} {commodity}"
    )

    st.markdown(
        f"### 📦 {data['package']}"
    )

    st.write(data["reason"])

    st.markdown(
        f"**Storage:** {storage} &nbsp; | &nbsp; "
        f"**Transport:** {transport} &nbsp; | &nbsp; "
        f"**Priority:** {priority}"
    )

    st.markdown(
        f"""
        <span class="tag">Food-grade</span>
        <span class="tag">{data['ventilation']} Ventilation</span>
        <span class="tag">{data['protection']} Protection</span>
        <span class="tag">Practical Impact</span>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # -------- SPECIFICATIONS --------

    st.subheader("📋 Recommended Packaging Specifications")

    s1, s2 = st.columns(2)

    with s1:
        st.markdown(
            f"""
            <div class="spec">
            <b>Material</b><br>
            {data['material']}
            </div>

            <div class="spec">
            <b>Packaging Type</b><br>
            {data['box_type']}
            </div>

            <div class="spec">
            <b>Ventilation Requirement</b><br>
            {data['ventilation']}
            </div>
            """,
            unsafe_allow_html=True
        )

    with s2:
        st.markdown(
            f"""
            <div class="spec">
            <b>Protection Level</b><br>
            {data['protection']}
            </div>

            <div class="spec">
            <b>Moisture Protection</b><br>
            {data['moisture']}
            </div>

            <div class="spec">
            <b>Handling Guidance</b><br>
            {data['handling']}
            </div>
            """,
            unsafe_allow_html=True
        )

    # -------- PRACTICAL PACKAGING INSIGHTS --------

    st.subheader("💡 Practical Packaging Insights")

    i1, i2, i3 = st.columns(3)

    with i1:
        st.markdown("""
        <div class="spec">
        <h3>💰 Estimated Cost</h3>
        <b>₹8–₹15 per box*</b>
        <p>Illustrative prototype estimate.</p>
        </div>
        """, unsafe_allow_html=True)

    with i2:
        st.markdown("""
        <div class="spec">
        <h3>♻️ Sustainability</h3>
        <b>High Recyclability</b>
        <p>Corrugated fibreboard can be recycled.</p>
        </div>
        """, unsafe_allow_html=True)

    with i3:
        st.markdown("""
        <div class="spec">
        <h3>⏳ Quality Impact</h3>
        <b>High Protection</b>
        <p>Helps reduce bruising and physical damage.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec">
    <b>📦 Suggested Packaging Capacity</b><br>
    5–10 kg per box
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "*Cost is an illustrative prototype estimate and should be replaced "
        "with verified local supplier prices before real-world use."
    )

    # -------- MATCH --------

    st.subheader("📊 Recommendation Match")

    st.progress(match / 100)

    st.metric(
        "Recommendation Match",
        f"{match}%"
    )

    m1, m2 = st.columns(2)

    with m1:
        st.metric(
            "Ventilation Need",
            data["ventilation"]
        )

    with m2:
        st.metric(
            "Damage Sensitivity",
            data["damage"]
        )

    # -------- BENEFITS --------

    st.subheader("👨‍🌾 Farmer Benefit")

    st.markdown(
        f"""
        <div class="benefit">
        {data['farmer']}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🏪 Seller Benefit")

    st.markdown(
        f"""
        <div class="benefit">
        {data['seller']}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------- DECISION EXPLANATION --------

    st.subheader("🧠 Why CropSynq Selected This Packaging")

    st.markdown(f"""
    **1️⃣ Commodity:** {commodity}

    ↓

    **2️⃣ Commodity characteristics:**  
    Ventilation = **{data['ventilation']}** | 
    Damage sensitivity = **{data['damage']}**

    ↓

    **3️⃣ User conditions:**  
    Storage = **{storage}** | 
    Transport = **{transport}**

    ↓

    **4️⃣ User priority:**  
    **{priority}**

    ↓

    **5️⃣ Final recommendation:**  
    📦 **{data['package']}**
    """)

else:

    st.info(
        "👉 Select the inputs and click **Generate AI Recommendation** "
        "to see the packaging decision."
    )


# ---------------- FOOTER ----------------

st.caption(
    "CropSynq • Prototype: intelligent rule-based packaging recommendation"
)