import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="StellarX | Space Mission Simulator",
    page_icon="🚀",
    layout="wide",
)

# Custom Gamified Aerospace Theme Styling
st.markdown(
    """
    <style>
    /* Global Page & Container */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #0d1527 0%, #060913 70%, #020408 100%);
        color: #f1f5f9;
    }
    .block-container {
        max-width: 1200px;
        padding-top: 1.8rem;
        padding-bottom: 3.5rem;
    }

    /* Hero Main Title */
    .hero-title-box {
        text-align: center;
        margin-bottom: 1.2rem;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: -0.5px;
        margin-bottom: 0.1rem;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 40%, #f43f5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 35px rgba(56, 189, 248, 0.3);
    }
    .subtitle {
        font-size: 1.25rem;
        color: #94a3b8;
        font-weight: 500;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }

    /* NASA Badge */
    .nasa-badge-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }
    .nasa-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(14, 165, 233, 0.14);
        border: 1px solid rgba(56, 189, 248, 0.4);
        color: #38bdf8;
        padding: 6px 18px;
        border-radius: 9999px;
        font-size: 0.88rem;
        font-weight: 600;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    }
    .game-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(244, 63, 94, 0.12);
        border: 1px solid rgba(244, 63, 94, 0.35);
        color: #fb7185;
        padding: 6px 18px;
        border-radius: 9999px;
        font-size: 0.88rem;
        font-weight: 600;
    }
    .disclaimer-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(148, 163, 184, 0.12);
        border: 1px solid rgba(148, 163, 184, 0.35);
        color: #cbd5e1;
        padding: 6px 18px;
        border-radius: 9999px;
        font-size: 0.84rem;
        font-weight: 500;
    }

    /* Slider Custom Styling */
    div[data-testid="stSlider"] {
        margin-bottom: 0px !important;
    }
    .slider-labels {
        display: flex;
        justify-content: space-between;
        font-size: 0.85rem;
        font-weight: 600;
        color: #94a3b8;
        margin-top: -10px;
        margin-bottom: 10px;
        padding: 0 4px;
        user-select: none;
    }

    /* Gamified Metric Cards */
    div[data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 14px 16px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        border-color: rgba(56, 189, 248, 0.5);
        transform: translateY(-3px);
        box-shadow: 0 6px 22px rgba(56, 189, 248, 0.25);
    }

    /* Rank & Achievement Badges */
    .rank-card {
        text-align: center;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        font-family: monospace;
    }
    .rank-s {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(6, 95, 70, 0.3) 100%);
        border: 1.5px solid #10b981;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.3);
    }
    .rank-a {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.2) 0%, rgba(30, 58, 138, 0.3) 100%);
        border: 1.5px solid #38bdf8;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.3);
    }
    .rank-f {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(127, 29, 29, 0.3) 100%);
        border: 1.5px solid #ef4444;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.3);
    }

    .achievement-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 10px;
        margin-top: 12px;
    }
    .achievement-pill {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(148, 163, 184, 0.25);
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.85rem;
        color: #e2e8f0;
    }
    .achievement-pill.active {
        border-color: #38bdf8;
        background: rgba(14, 165, 233, 0.15);
        color: #38bdf8;
        font-weight: 600;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
    }
    .achievement-pill.locked {
        opacity: 0.45;
        border-style: dashed;
    }

    /* Container border styling */
    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        border-color: rgba(56, 189, 248, 0.2) !important;
        border-radius: 14px !important;
        background: rgba(15, 23, 42, 0.45);
        backdrop-filter: blur(8px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.html(
    '<div class="hero-title-box">'
    '<div class="main-title">🚀 StellarX</div>'
    '<div class="subtitle">Space Mission Design & Systems Engineering Simulator</div>'
    '<div class="nasa-badge-container">'
    '<span class="nasa-badge">🏛️ Inspired by NASA Systems Engineering Concepts</span>'
    '<span class="game-badge">🎮 Interactive Educational Simulator</span>'
    '<span class="disclaimer-badge">ℹ️ Educational Project • Not Affiliated with or Endorsed by NASA</span>'
    '</div>'
    '</div>'
)

st.caption(
    "⚠️ **Educational Simulation Disclaimer:** StellarX is an independent educational tool inspired by systems engineering principles from NASA and JPL. "
    "All numerical values (such as the 220 kg bus mass, rocket payload limits, arbitrary cost points, and scoring weights) are educational gameplay assumptions "
    "designed to provide an intuitive trade space, and are not official NASA specifications. Not certified, sponsored, or endorsed by NASA."
)

st.info(
    "🛰️ **Mission Control Directive:** Take command as Lead Systems Architect! "
    "Select your scientific payload, balance electrical power demands against solar/nuclear supply, "
    "match downlinked science data with communication bandwidth, and fit your spacecraft mass into the rocket's payload capacity."
)

# Simulation data (Educational gameplay assumptions calibrated for systems engineering trade-offs)
rockets = {
    "Small Rocket": {"cost": 20, "capacity": 400, "segment": "Launch Segment", "class": "Lightweight Launch Vehicle"},
    "Medium Rocket": {"cost": 35, "capacity": 500, "segment": "Launch Segment", "class": "Workhorse Rideshare Launcher"},
    "Heavy Rocket": {"cost": 50, "capacity": 800, "segment": "Launch Segment", "class": "Heavy-Lift Exploration Booster"},
}
instruments = {
    "Radar": {"cost": 30, "mass": 120, "power": 65, "data": 40, "science": 80, "segment": "Space Segment", "wave": "Microwave / Radio"},
    "Camera": {"cost": 20, "mass": 60, "power": 35, "data": 20, "science": 65, "segment": "Space Segment", "wave": "Visible / Near-IR"},
    "Spectrometer": {"cost": 25, "mass": 75, "power": 45, "data": 25, "science": 75, "segment": "Space Segment", "wave": "EUV / X-ray / Infrared"},
}
power_systems = {
    "Basic Solar Panels": {"cost": 15, "mass": 80, "supply": 85, "segment": "Space Segment", "type": "Dual-Wing Photovoltaic"},
    "Advanced Solar Panels": {"cost": 25, "mass": 110, "supply": 115, "segment": "Space Segment", "type": "High-Efficiency Multi-Junction"},
    "Nuclear Power Unit": {"cost": 35, "mass": 120, "supply": 140, "segment": "Space Segment", "type": "Radioisotope Thermoelectric (RTG)"},
}
antennas = {
    "Standard Antenna": {"cost": 5, "mass": 20, "power": 5, "capacity": 45, "segment": "Ground/Comms Segment", "type": "Omni Whip Monopole"},
    "High-Gain Antenna": {"cost": 15, "mass": 35, "power": 10, "capacity": 80, "segment": "Ground/Comms Segment", "type": "Parabolic Reflector Dish"},
}
orbits = {
    "Low Orbit": {
        "cost": 0,
        "coverage": 85,
        "communication_factor": 0.90,
        "altitude": "400 km (Low Earth Orbit - LEO)",
        "description": "Low launch delta-V cost and high spatial resolution; frequent ground station passes.",
    },
    "Polar Orbit": {
        "cost": 10,
        "coverage": 100,
        "communication_factor": 0.85,
        "altitude": "700 km (Sun-Synchronous Polar)",
        "description": "Global 100% planetary surface coverage across both poles with moderate insertion cost.",
    },
    "High Orbit": {
        "cost": 15,
        "coverage": 60,
        "communication_factor": 1.40,
        "altitude": "35,786 km (Geostationary Earth Orbit - GEO)",
        "description": "Continuous line-of-sight communication with fixed hemispheric planetary coverage.",
    },
}
mission_goals = {
    "Map a Planetary Surface": {"preferred_instrument": "Radar", "minimum_coverage": 80, "target": "Topography & Moisture Mapping"},
    "Photograph a Target Area": {"preferred_instrument": "Camera", "minimum_coverage": 60, "target": "High-Res Geomorphology"},
    "Study Surface Composition": {"preferred_instrument": "Spectrometer", "minimum_coverage": 70, "target": "Mineralogy & Chemical Signatures"},
}

# 1. Mission Configuration Section
st.header("1. Mission Configuration & Assembly")

with st.expander("💡 Mission Design Hints & Principles (NASA “Build It Yourself: Satellite!”)", expanded=False):
    st.info(
        "**Playing Hints & Trade-Offs:** As you configure your spacecraft, consider how science objectives, instruments, "
        "and wavelengths complement one another. A more ambitious scientific payload generates higher data volume and draws more power, "
        "requiring upgraded communication systems and power generation. If choices conflict with vehicle capacity or budget limits, "
        "iterate across your parameters to find a viable system baseline."
    )

with st.container(border=True):
    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        st.subheader("🎯 Objective & Payload")
        mission_goal = st.selectbox(
            "Mission Objective",
            list(mission_goals.keys()),
        )
        rocket_name = st.selectbox(
            "Launch Vehicle (Launch Segment)",
            list(rockets.keys()),
            index=1,
        )
        instrument_name = st.selectbox(
            "Scientific Instrument (Space Segment)",
            list(instruments.keys()),
            index=0,
        )

    with col_right:
        st.subheader("🛰️ Orbit & Systems")
        orbit_name = st.selectbox(
            "Target Orbit",
            list(orbits.keys()),
        )
        st.caption(f"ℹ️ {orbits[orbit_name]['description']} ({orbits[orbit_name]['altitude']})")

        power_name = st.selectbox(
            "Power System (Space Segment)",
            list(power_systems.keys()),
        )
        antenna_name = st.selectbox(
            "Communication System (Ground/Comms Segment)",
            list(antennas.keys()),
        )

    st.divider()

    budget = st.slider(
        "Available Budget (Simulation Points)",
        min_value=50,
        max_value=150,
        value=95,
        step=5,
    )
    # Explicit min and max labels directly beneath the slider track
    st.html(
        '<div class="slider-labels">'
        '<span>50</span>'
        '<span>150</span>'
        '</div>'
    )

# Dynamic Visual Spacecraft Blueprint SVG Component
def render_spacecraft_blueprint(inst, pwr, ant, orb, rkt):
    is_solar = "Solar" in pwr
    is_adv = "Advanced" in pwr
    wing_w = 95 if is_adv else 75
    cells = 4 if is_adv else 3

    pwr_elements = []
    if is_solar:
        pwr_elements.append(f'<line x1="-35" y1="0" x2="-{35 + wing_w}" y2="0" stroke="#94a3b8" stroke-width="3"/>')
        pwr_elements.append(f'<rect x="-{35 + wing_w}" y="-26" width="{wing_w}" height="52" rx="4" fill="url(#solarGrad)" stroke="#38bdf8" stroke-width="1.5"/>')
        for c in range(1, cells):
            step = wing_w / cells
            pwr_elements.append(f'<line x1="-{35 + c*step}" y1="-26" x2="-{35 + c*step}" y2="26" stroke="#38bdf8" stroke-width="1" opacity="0.7"/>')
        pwr_elements.append(f'<line x1="-{35 + wing_w}" y1="0" x2="-35" y2="0" stroke="#38bdf8" stroke-width="1" opacity="0.7"/>')

        pwr_elements.append(f'<line x1="35" y1="0" x2="{35 + wing_w}" y2="0" stroke="#94a3b8" stroke-width="3"/>')
        pwr_elements.append(f'<rect x="35" y="-26" width="{wing_w}" height="52" rx="4" fill="url(#solarGrad)" stroke="#38bdf8" stroke-width="1.5"/>')
        for c in range(1, cells):
            step = wing_w / cells
            pwr_elements.append(f'<line x1="{35 + c*step}" y1="-26" x2="{35 + c*step}" y2="26" stroke="#38bdf8" stroke-width="1" opacity="0.7"/>')
        pwr_elements.append(f'<line x1="35" y1="0" x2="{35 + wing_w}" y2="0" stroke="#38bdf8" stroke-width="1" opacity="0.7"/>')
    else:
        pwr_elements.append('<line x1="-35" y1="0" x2="-55" y2="0" stroke="#94a3b8" stroke-width="4"/>')
        pwr_elements.append('<rect x="-95" y="-22" width="40" height="44" rx="6" fill="#475569" stroke="#f59e0b" stroke-width="2"/>')
        pwr_elements.append('<line x1="-95" y1="-12" x2="-55" y2="-12" stroke="#f59e0b" stroke-width="1.5"/>')
        pwr_elements.append('<line x1="-95" y1="0" x2="-55" y2="0" stroke="#f59e0b" stroke-width="1.5"/>')
        pwr_elements.append('<line x1="-95" y1="12" x2="-55" y2="12" stroke="#f59e0b" stroke-width="1.5"/>')
        pwr_elements.append('<circle cx="-75" cy="0" r="4" fill="#fbbf24"/>')
        pwr_elements.append('<circle cx="-75" cy="0" r="9" stroke="#fbbf24" stroke-width="1.5" fill="none" stroke-dasharray="6,4"/>')

    pwr_svg = "".join(pwr_elements)

    if "High-Gain" in ant:
        ant_svg = (
            '<line x1="0" y1="-35" x2="0" y2="-52" stroke="#94a3b8" stroke-width="3"/>'
            '<path d="M -24 -58 Q 0 -44 24 -58" stroke="#38bdf8" stroke-width="3.5" fill="none"/>'
            '<line x1="0" y1="-44" x2="0" y2="-66" stroke="#f43f5e" stroke-width="2"/>'
            '<circle cx="0" cy="-66" r="3" fill="#f43f5e" filter="url(#glow)"/>'
            '<path d="M -16 -74 A 20 20 0 0 1 16 -74" stroke="#38bdf8" stroke-width="1.5" fill="none" opacity="0.8"/>'
            '<path d="M -26 -82 A 32 32 0 0 1 26 -82" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.4"/>'
        )
    else:
        ant_svg = (
            '<line x1="0" y1="-35" x2="16" y2="-72" stroke="#e2e8f0" stroke-width="2.5"/>'
            '<circle cx="16" cy="-72" r="3" fill="#38bdf8" filter="url(#glow)"/>'
            '<path d="M 12 -80 A 12 12 0 0 1 24 -70" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.7"/>'
        )

    if inst == "Radar":
        inst_svg = (
            '<line x1="0" y1="35" x2="0" y2="52" stroke="#94a3b8" stroke-width="3"/>'
            '<rect x="-30" y="52" width="60" height="12" rx="2" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>'
            '<line x1="-20" y1="52" x2="-20" y2="64" stroke="#38bdf8" stroke-width="1"/>'
            '<line x1="0" y1="52" x2="0" y2="64" stroke="#38bdf8" stroke-width="1"/>'
            '<line x1="20" y1="52" x2="20" y2="64" stroke="#38bdf8" stroke-width="1"/>'
            '<path d="M -22 66 L -40 100 M 0 66 L 0 102 M 22 66 L 40 100" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.7"/>'
        )
    elif inst == "Camera":
        inst_svg = (
            '<rect x="-14" y="35" width="28" height="24" rx="3" fill="#1e293b" stroke="#cbd5e1" stroke-width="1.5"/>'
            '<ellipse cx="0" cy="59" rx="14" ry="5" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>'
            '<ellipse cx="0" cy="59" rx="7" ry="2.5" fill="#38bdf8" filter="url(#glow)"/>'
            '<path d="M -12 63 L -35 105 M 12 63 L 35 105" stroke="#facc15" stroke-width="1.2" stroke-dasharray="4,3" opacity="0.6"/>'
        )
    else:
        inst_svg = (
            '<polygon points="0,35 -16,60 16,60" fill="#475569" stroke="#a855f7" stroke-width="1.5"/>'
            '<circle cx="0" cy="50" r="4" fill="#c084fc" filter="url(#glow)"/>'
            '<line x1="-8" y1="62" x2="-25" y2="102" stroke="#f43f5e" stroke-width="1.5" opacity="0.8"/>'
            '<line x1="-3" y1="62" x2="-10" y2="104" stroke="#eab308" stroke-width="1.5" opacity="0.8"/>'
            '<line x1="2" y1="62" x2="5" y2="104" stroke="#22c55e" stroke-width="1.5" opacity="0.8"/>'
            '<line x1="7" y1="62" x2="20" y2="102" stroke="#3b82f6" stroke-width="1.5" opacity="0.8"/>'
        )

    svg_content = f"""
    <div style="display:flex; flex-direction:column; align-items:center; background: radial-gradient(circle at center, #0f172a 0%, #030712 100%); border-radius:14px; border:1px solid rgba(56, 189, 248, 0.3); padding:16px; margin: 15px 0; box-shadow: 0 4px 25px rgba(0,0,0,0.6);">
      <div style="width:100%; display:flex; justify-content:space-between; align-items:center; padding: 0 10px 8px 10px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 8px;">
        <span style="font-family:monospace; font-size:0.85rem; color:#38bdf8; font-weight:700;">🛰️ ASSEMBLED SPACECRAFT BLUEPRINT</span>
        <span style="font-family:sans-serif; font-size:0.80rem; color:#94a3b8;">ORBIT: <b style="color:#f1f5f9;">{orb.upper()}</b> | VEHICLE: <b style="color:#f1f5f9;">{rkt}</b></span>
      </div>
      <svg width="100%" height="240" viewBox="0 0 480 240" xmlns="http://www.w3.org/2000/svg" style="max-width:550px;">
        <defs>
          <linearGradient id="solarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="50%" stop-color="#2563eb"/>
            <stop offset="100%" stop-color="#1d4ed8"/>
          </linearGradient>
          <linearGradient id="goldBus" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fbbf24"/>
            <stop offset="70%" stop-color="#d97706"/>
            <stop offset="100%" stop-color="#b45309"/>
          </linearGradient>
          <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3.5" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>

        <circle cx="35" cy="35" r="1.5" fill="#ffffff" opacity="0.8"/>
        <circle cx="85" cy="180" r="1" fill="#38bdf8" opacity="0.6"/>
        <circle cx="420" cy="45" r="1.5" fill="#ffffff" opacity="0.7"/>
        <circle cx="445" cy="190" r="1" fill="#93c5fd" opacity="0.5"/>
        <circle cx="160" cy="25" r="1" fill="#ffffff" opacity="0.4"/>
        <circle cx="330" cy="210" r="1.2" fill="#ffffff" opacity="0.7"/>

        <path d="M -50 300 Q 240 170 530 300" fill="#0369a1" opacity="0.35"/>
        <path d="M -50 310 Q 240 185 530 310" fill="#0284c7" opacity="0.5"/>
        <path d="M -50 320 Q 240 200 530 320" fill="#38bdf8" opacity="0.7" filter="url(#glow)"/>

        <g transform="translate(240, 115)">
            {pwr_svg}
            <rect x="-35" y="-35" width="70" height="70" rx="8" fill="url(#goldBus)" stroke="#fef08a" stroke-width="1.5" filter="url(#glow)"/>
            <rect x="-26" y="-26" width="52" height="52" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
            <circle cx="0" cy="0" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <circle cx="0" cy="0" r="5" fill="#38bdf8" filter="url(#glow)"/>
            {ant_svg}
            {inst_svg}
        </g>
      </svg>
    </div>
    """
    return "\n".join(line.strip() for line in svg_content.splitlines() if line.strip())

# Display dynamic blueprint
blueprint_html = render_spacecraft_blueprint(instrument_name, power_name, antenna_name, orbit_name, rocket_name)
st.html(blueprint_html)

# Simulation trigger and guidance action bar
if "simulation_started" not in st.session_state:
    st.session_state.simulation_started = False

col_btn, col_msg = st.columns([1.2, 2.8], vertical_alignment="center")

with col_btn:
    btn_label = "🚀 Launch & Simulate Mission"
    if st.button(btn_label, type="primary", width="stretch"):
        st.session_state.simulation_started = True

with col_msg:
    if not st.session_state.simulation_started:
        st.info("Assemble your spacecraft systems above, then click “Launch & Simulate Mission” to initiate orbit injection.")

if not st.session_state.simulation_started:
    st.stop()

# Retrieve selected components
rocket = rockets[rocket_name]
instrument = instruments[instrument_name]
power_system = power_systems[power_name]
antenna = antennas[antenna_name]
orbit = orbits[orbit_name]
goal = mission_goals[mission_goal]

# Calculate mission resources
base_mass = 220
base_cost = 10
base_power_demand = 10

total_mass = base_mass + instrument["mass"] + power_system["mass"] + antenna["mass"]
total_cost = base_cost + rocket["cost"] + instrument["cost"] + power_system["cost"] + antenna["cost"] + orbit["cost"]

power_demand = base_power_demand + instrument["power"] + antenna["power"]
power_supply = power_system["supply"]
data_generated = instrument["data"]
communication_capacity = antenna["capacity"] * orbit["communication_factor"]
coverage = orbit["coverage"]

power_ratio = min(power_supply / power_demand * 100, 100)
communication_ratio = min(communication_capacity / data_generated * 100, 100)

science_value = instrument["science"]
if instrument_name == goal["preferred_instrument"]:
    science_value = min(science_value + 10, 100)

# Identify design problems
problems = []
if total_mass > rocket["capacity"]:
    problems.append("Spacecraft mass exceeds the selected launch vehicle's payload capacity.")
if total_cost > budget:
    problems.append("Total mission cost exceeds the allocated budget.")
if power_demand > power_supply:
    problems.append("The onboard power system cannot supply enough energy to operate all systems.")
if data_generated > communication_capacity:
    problems.append("Communication bandwidth is insufficient to downlink all generated scientific data.")
if coverage < goal["minimum_coverage"]:
    problems.append("Orbital surface coverage does not meet the minimum requirement for this scientific objective.")

# Calculate mission score
budget_efficiency = max(0, 100 - (total_cost / budget * 20))
score = (
    science_value * 0.35
    + coverage * 0.25
    + power_ratio * 0.15
    + communication_ratio * 0.15
    + budget_efficiency * 0.10
)
score -= len(problems) * 10
score = max(0, min(round(score), 100))

# Celebration effect on high score
if score >= 85 and not problems:
    st.balloons()

# Recommendations
recommendations = []
if total_mass > rocket["capacity"]:
    recommendations.append("Choose a lighter instrument or power unit, or upgrade to a heavier launch vehicle.")
if total_cost > budget:
    recommendations.append("Select a lower-cost orbit or vehicle, or increase the available mission budget.")
if power_demand > power_supply:
    recommendations.append("Upgrade to a higher-output power system or select instruments with lower power draw.")
if data_generated > communication_capacity:
    recommendations.append("Upgrade to a High-Gain Antenna or choose an orbit with a higher communication factor.")
if coverage < goal["minimum_coverage"]:
    recommendations.append("Choose an orbit with broader planetary coverage, such as a Polar Orbit.")
if instrument_name != goal["preferred_instrument"]:
    recommendations.append(f"The selected instrument is operational, but a {goal['preferred_instrument']} is optimal for this goal.")

# 2. Mission Resources Section
st.divider()
st.header("2. Flight Telemetry & Resources")

# Gamified Mission Rank Card
if score >= 85 and not problems:
    st.html(
        '<div class="rank-card rank-s">'
        '<span style="font-size:1.6rem; font-weight:800; color:#10b981;">🎖️ RANK S: MASTER MISSION ARCHITECT</span><br/>'
        '<span style="font-size:0.95rem; color:#a7f3d0;">Outstanding systems architecture! All subsystems are balanced within design margins and safety reserves.</span>'
        '</div>'
    )
elif score >= 65:
    st.html(
        '<div class="rank-card rank-a">'
        '<span style="font-size:1.6rem; font-weight:800; color:#38bdf8;">🎖️ RANK A: MISSION VIABLE</span><br/>'
        '<span style="font-size:0.95rem; color:#bae6fd;">Spacecraft is flight-capable, but engineering trade-offs or margins can be further optimized.</span>'
        '</div>'
    )
else:
    st.html(
        '<div class="rank-card rank-f">'
        '<span style="font-size:1.6rem; font-weight:800; color:#ef4444;">⚠️ RANK F: MISSION SCRUBBED</span><br/>'
        '<span style="font-size:0.95rem; color:#fecaca;">Critical engineering conflicts detected. Spacecraft cannot be manifested for flight without redesign.</span>'
        '</div>'
    )

with st.container(border=True):
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Spacecraft Mass ⚖️", f"{total_mass} kg")
    m2.metric("Total Cost 💰", f"{total_cost} / {budget}")
    m3.metric("Power Draw ⚡", f"{power_demand} / {power_supply} W")
    m4.metric("Data / Comms 📡", f"{data_generated} / {communication_capacity:.1f} Mbps")
    m5.metric("Coverage 🌐", f"{coverage}%")

    st.progress(score / 100, text=f"Mission Performance Score: {score} / 100")

    if not problems:
        st.success("✅ Spacecraft systems are balanced and fully compatible under simulation assumptions.")
    else:
        st.warning("⚠️ Engineering trade-offs required: resolve the detected conflicts below.")

# Gamified Achievements Section
st.subheader("🏆 Mission Achievements")
achievements = [
    ("🛡️ Zero Defects", not problems, "No engineering conflicts detected"),
    ("🎯 NASA Synergy", instrument_name == goal["preferred_instrument"], f"Equipped {goal['preferred_instrument']} for {mission_goal}"),
    ("⚡ Power Surplus", power_supply >= power_demand * 1.25, "Power supply exceeds demand by ≥ 25%"),
    ("📡 High-Speed Link", communication_capacity >= 60, "Effective data downlink exceeds 60 Mbps"),
    ("🌍 Global Surveyor", coverage == 100, "100% surface planetary coverage"),
    ("💰 Frugal Budget", (budget - total_cost) >= 20, "Reserved ≥ 20 budget points for contingencies"),
]

ach_cols = st.columns(3)
for i, (ach_title, ach_active, ach_desc) in enumerate(achievements):
    with ach_cols[i % 3]:
        if ach_active:
            st.html(
                f'<div class="achievement-pill active">'
                f'<div><b>{ach_title}</b><br/>'
                f'<span style="font-size:0.75rem; color:#bae6fd;">{ach_desc}</span></div>'
                f'</div>'
            )
        else:
            st.html(
                f'<div class="achievement-pill locked">'
                f'<div><b>🔒 {ach_title}</b><br/>'
                f'<span style="font-size:0.75rem; color:#64748b;">{ach_desc}</span></div>'
                f'</div>'
            )

# 3. Design Analysis Section
st.divider()
st.header("3. Design Analysis & Diagnostic Report")

col_prob, col_rec = st.columns(2, gap="medium")
with col_prob:
    with st.container(border=True):
        st.subheader("⚠️ Detected Engineering Conflicts")
        if problems:
            for p in problems:
                st.markdown(f"- ❌ **{p}**")
        else:
            st.success("✨ Zero conflicts detected! All engineering constraints satisfied.")

with col_rec:
    with st.container(border=True):
        st.subheader("💡 Flight Systems Advisor")
        if recommendations:
            for r in recommendations:
                st.markdown(f"- 🔧 {r}")
        else:
            st.write("All mission systems are well-balanced and meet primary mission objectives.")

# 4. Performance Dashboard Section
st.header("4. Performance Telemetry Dashboard")
chart_labels = ["Scientific Value", "Coverage", "Power Adequacy", "Comms Adequacy"]
chart_data = pd.DataFrame(
    {
        "Metric": chart_labels,
        "Score (%)": [science_value, coverage, power_ratio, communication_ratio],
    }
)
chart = (
    alt.Chart(chart_data)
    .mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8)
    .encode(
        x=alt.X(
            "Metric:N",
            axis=alt.Axis(
                labelAngle=0,
                title=None,
                labelFontSize=12,
            ),
            sort=None,
        ),
        y=alt.Y(
            "Score (%):Q",
            scale=alt.Scale(domain=[0, 100]),
            axis=alt.Axis(title="Score (%)", labelFontSize=12),
        ),
        color=alt.value("#38bdf8"),
    )
    .properties(height=280)
)
st.altair_chart(chart, width="stretch")

# 5. Mission Report Section
st.header("5. Mission Flight Report")

# NASA Heritage Mission Analogue Matching (inspired by NASA's "Build It Yourself: Satellite!")
if instrument_name == "Radar" and mission_goal == "Map a Planetary Surface":
    matched_mission = {
        "name": "SMAP (Soil Moisture Active Passive) & Magellan",
        "type": "Radar Earth & Planetary Observation",
        "desc": "Utilizes synthetic aperture radar to map surface topography, soil moisture, and geological structures through clouds and surface layers.",
        "icon": "🛰️📡",
    }
elif instrument_name == "Camera" and mission_goal == "Photograph a Target Area":
    matched_mission = {
        "name": "BisonSat (ELaNa XII) & LRO (Lunar Reconnaissance Orbiter)",
        "type": "Multispectral & Visual Optical Survey",
        "desc": "Employs high-resolution optical cameras for surface imaging, geomorphological mapping, and target identification.",
        "icon": "🛰️📷",
    }
elif instrument_name == "Spectrometer" and mission_goal == "Study Surface Composition":
    matched_mission = {
        "name": "MinXSS (ELaNa IX) & Dellingr (ELaNa 22 / NASA GSFC)",
        "type": "Spectrometric & Solar Physics Investigation",
        "desc": "Measures fine spectral emission lines to determine mineralogy, atmospheric chemistry, and solar flare energetics.",
        "icon": "🛰️🔬",
    }
else:
    matched_mission = {
        "name": "Dawn & Mars Reconnaissance Orbiter (MRO)",
        "type": "Multi-Sensor Planetary Science Platform",
        "desc": "A multi-payload science orbiter requiring careful trade studies between high instrument draw, broad trajectory coverage, and downlink bandwidth.",
        "icon": "🛰️🌐",
    }

with st.container(border=True):
    st.markdown(
        f"""
**Mission Architecture Breakdown (NASA Segments)**

- **Mission Objective (User Segment):** {mission_goal}
- **Launch Segment (Vehicle):** {rocket_name} (Payload Capacity: {rocket['capacity']} kg)
- **Space Segment (Payload & Power):** {instrument_name} & {power_name}
- **Orbital Profile (Trajectory):** {orbit_name} ({orbit['coverage']}% surface coverage)
- **Ground / Comms Segment:** {antenna_name} (Effective Downlink: {communication_capacity:.1f} Mbps)
- **Final Evaluation Score:** {score} / 100
"""
    )

    st.markdown("---")
    st.markdown(
        f"""
#### {matched_mission['icon']} Real-World NASA Mission Analogue
*(Educational analogue mapping inspired by NASA's “Build It Yourself: Satellite!” mission concepts)*

- **Closest NASA Heritage Mission:** **{matched_mission['name']}**
- **Mission Classification:** {matched_mission['type']}
- **Systems Engineering Parallels:** {matched_mission['desc']}
"""
    )

with st.expander("ℹ️ How is the score calculated? (Mathematical Formulations)"):
    st.markdown(
        """
        The overall mission score uses a multi-objective systems engineering utility formulation:
        - **Scientific Value ($S$):** 35% weight (+10 bonus if the primary instrument matches the mission objective).
        - **Surface Coverage ($C$):** 25% weight (determined by orbital inclination and altitude).
        - **Power Adequacy ($P_r$):** 15% weight ($\\min(100, \\frac{\\text{Power Supply}}{\\text{Power Demand}} \\times 100)$).
        - **Communication Downlink ($K_r$):** 15% weight ($\\min(100, \\frac{\\text{Effective Downlink}}{\\text{Data Generated}} \\times 100)$).
        - **Budget Efficiency ($B_e$):** 10% weight ($\\max(0, 100 - (\\frac{\\text{Total Cost}}{\\text{Budget}} \\times 20))$).
        - **Penalty ($N_{\\text{conflicts}}$):** -10 points deducted for each unresolved engineering conflict.

        *Note: The weights, numerical values, and arbitrary cost units are educational gameplay assumptions calibrated to simulate system trade-offs, rather than empirical NASA cost or performance models.*
        """
    )

# 6. NASA & JPL Systems Engineering Alignment
with st.expander("🏛️ Systems Engineering Concepts & Frameworks (NASA & JPL Inspired)", expanded=False):
    tab_resources, tab_cml, tab_segments, tab_cubesat, tab_tools, tab_case = st.tabs([
        "📚 Conceptual References & Frameworks",
        "📊 JPL Concept Maturity Levels",
        "🛰️ NASA 4 Mission Segments",
        "📦 CubeSat 101 & Mission Lifecycle",
        "🛠️ Enterprise Tools (MDL & GMAT)",
        "🌱 BioNutrients-2 Case Study",
    ])

    with tab_resources:
        st.markdown(
            """
            ### 🏛️ Conceptual Foundations & Educational References

            > **⚠️ Educational Simulation Notice & Disclaimer:**  
            > StellarX is an independent educational simulator developed to teach space systems engineering concepts. **It is not certified, sponsored, or endorsed by NASA.**  
            >  
            > The numerical values used in the simulator (e.g., base dry mass of 220 kg, rocket payload limits of 400/500/800 kg, power ratings, arbitrary cost points, and scoring coefficients) are **educational gameplay assumptions** designed to make the simulation playable, intuitive, and balanced.  
            >  
            > NASA technical handbooks and educational resources provided the **conceptual principles of systems engineering trade-offs**:
            > - **System Interdependence:** How power generation and storage (e.g., solar arrays, RTG) directly drive spacecraft mass and thermal architecture.
            > - **Communications vs. Energy:** How RF link margin and downlink rates depend on transmitter power, antenna aperture mass, frequency, and orbital altitude.
            > - **Design Margins:** How systems engineering guidelines mandate contingency margins (mass and power reserves) to account for uncertainty during early formulation.

            #### Referenced Standards & Educational Inspiration:
            1. **NASA CubeSat Launch Initiative (CSLI) — CubeSat 101**:
               - *Basic Concepts and Processes for First-Time CubeSat Developers* (NASA LSP / PolySat Cal Poly, Doc ID: NP-2017-10-2470-HQ).
               - Conceptual reference for the 16-phase lifecycle, P-POD dispenser constraints, and flight readiness milestones.
            2. **NASA Jet Propulsion Laboratory (JPL / Caltech)**:
               - *Space Mission Concept Development Using Concept Maturity Levels (CMLs)* (Wessen, Borden, Ziemer, Kwok).
               - Guides the Pre-Phase A trade space exploration and iterative feedback loop between CML 2, 3, and 4.
            3. **NASA SmallSat Institute & Science Mission Directorate (SMD)**:
               - *Design and Develop Science Missions* (Julie Levri, Access to Space for All Systems Engineering Series).
               - Establishes the 4-segment mission breakdown (Launch, Space, Ground, User) and ConOps framework (NPR 7123.1).
            4. **NASA Goddard Space Flight Center (GSFC) — Mission Design Lab (MDL)**:
               - Collaborative concurrent engineering facility modeling multi-disciplinary trades across 11 spacecraft disciplines.
            5. **NASA General Mission Analysis Tool (GMAT)**:
               - Trajectory analysis and orbital transfer mechanics.
            6. **NASA Web-based Space Mission Visualization (WSMV)**:
               - Space flight visualization suite and Space Situational Awareness Ontology (`github.com/nasa/mission-viz`).
            7. **NASA Science "Build It Yourself: Satellite!" & "Scope It Out"**:
               - NASA educational product review-approved game mechanics linking scientific questions to instrument selection, wavelength compatibility, and real-world mission analogues.
            """
        )

    with tab_cml:
        st.markdown(
            """
            ### JPL Concept Maturity Levels (CML 1–9)
            *(Reference: Wessen, Borden, Ziemer, Kwok — NASA Jet Propulsion Laboratory / Caltech)*

            CMLs measure and communicate the maturity of space mission concepts during early formulation:
            - **CML 1 (Cocktail Napkin):** Core science questions articulated and rudimentary sketches created.
            - **CML 2 (Initial Feasibility):** Quantifying key parameters; first-order calculations of mass, power, and feasibility.
            - **CML 3 (Trade Space Exploration):** Architectural trades across spacecraft subsystems, trajectories, and launch capabilities vs. science return, cost, and risk (**JPL A-Team**).
            - **CML 4 (Point Design):** Selecting a specific, viable system architecture with verified subsystem reserves and margins (**JPL Team X**).
            - **CML 5 (Baseline Concept):** Mission Concept Review (MCR) or Step 1 proposal baseline.
            - **CML 6 (Integrated Concept):** Comprehensive Concept Study Report (CSR Step 2).
            - **CML 7–9:** Preliminary Implementation Baseline (PDR) through Critical Design Review (CDR).

            > **Iterative CML 2–4 Feedback Loop:** Mission design is non-linear. When conflicts are discovered in Point Design (CML 4), engineers return to Trade Space Exploration (CML 3) to test alternate configurations. StellarX models this exact feedback loop.
            """
        )

    with tab_segments:
        st.markdown(
            """
            ### The 4 NASA Mission Segments
            *(Reference: NASA Systems Engineering Handbook, NASA SmallSat Institute — Julie Levri)*

            1. **Launch Segment:**
               - Launch vehicles (Small, Medium, Heavy rockets, Falcon, SLS, NG-18).
               - Payload adapters, fairing capacity, launch site integration, and orbital insertion services.
            2. **Space Segment:**
               - Spacecraft bus, structure, and subsystem avionics.
               - Scientific payload instruments (Radar, Optical Camera, Spectrometer).
               - Power generation and storage (Solar arrays, Nuclear Power Units).
            3. **Ground / Comms Segment:**
               - Ground stations, antennas (Standard, High-Gain), and Deep Space Network (DSN) complexes.
               - Mission operations system (MOS), telemetry downlink, command uplinks, and tracking.
            4. **User Segment:**
               - The scientific community, principal investigators (PIs), and academic institutions.
               - Consuming processed data products to generate published peer-reviewed research (*"Begin with the End in Mind"*).
            """
        )

    with tab_cubesat:
        st.markdown(
            """
            ### NASA CubeSat 101 & CSLI Mission Lifecycle
            *(Reference: NASA CubeSat Launch Initiative — Basic Concepts & Processes for Developers)*

            The NASA CubeSat Launch Initiative (CSLI) provides auxiliary flight opportunities (ELaNa missions) for university and research satellites.

            #### Key Development Phases & Milestones
            1. **Concept Development & Strategic Partnering (1–6 mo):** Aligning mission science with the NASA Strategic Plan.
            2. **Merit & Feasibility Reviews (1–2 mo):** Independent peer reviews evaluating intrinsic science merit and technical feasibility.
            3. **CubeSat Design & Envelope Standards:** Adhering strictly to CubeSat Design Specifications (CDS) — 1U (10×10×11 cm, ≤1.33 kg), 3U (10×10×34 cm, ≤4.0 kg), and 6U dispensers.
            4. **Selection, Manifesting & ELaNa Assignment:** Pairing with launch vehicles (Atlas V, Falcon 9, Delta II, or ISS cargo resupply).
            5. **Regulatory Licensing (4–6 mo):**
               - **FCC Licensing:** Part 5 (Experimental via Form 442 or STA) or Part 97 (Amateur Radio).
               - **NOAA Remote Sensing:** Required under 15 CFR Part 960 for any Earth-observing sensor/camera.
               - **IARU Frequency Coordination:** Mandatory international coordination for amateur satellite frequency bands.
            6. **Hardware Verification & Testing:**
               - *FlatSat:* Tabletop operational testing of avionics and bus PCBs before structural assembly.
               - *ETU (Engineering Test Unit):* Practice unit for fit checks and environmental qualification.
               - *Day In The Life (DITL):* Verifying timer logic (minimum 30-min timer after P-POD ejection before deployables release; 45-min timer before RF transmission).
               - *Dynamic & Thermal Testing:* Vibration, shock, and Thermal Vacuum (TVAC) bakeout to eliminate outgassing.
            7. **Flight Deliverables & Mission Readiness Review (MRR):**
               - *ODAR:* Orbital Debris Assessment Report (via NASA DAS software) verifying re-entry demise and non-hazardous materials (low melting points).
               - *Electrical & Inhibit Verification:* Multiple independent physical inhibits, separation switches on rails, and Remove Before Flight (RBF) pins.
               - *Battery Certification:* UL 1642 / UL 2054 listed cells with integrated short-circuit and overcharge protection.
            8. **On-Orbit Operations:** Space-track TLEs (Two-Line Elements) generated by JSpOC for ground station tracking and telemetry acquisition.
            """
        )

    with tab_tools:
        st.markdown(
            """
            ### Enterprise NASA Collaborative Environments & Tools
            - **NASA MDL (Mission Design Lab at GSFC):**
              A dedicated concurrent design facility where multi-disciplinary engineering teams rapidly iterate on mission concepts through 4 study levels:
              1. *Office Hours:* Rapid brainstorming and bottleneck identification.
              2. *Concept Development:* Feasibility and risk assessment.
              3. *Trade Studies:* Evaluating competing architectures.
              4. *Point Design:* Detailed CAD, equipment lists, and cost estimates across 11 spacecraft disciplines.
            - **NASA GMAT (General Mission Analysis Tool):**
              NASA's enterprise open-source trajectory design and orbital analysis software. Used for trajectory optimization, high-fidelity orbit propagation, maneuver planning, and launch window analysis.
            - **NASA WSMV (Web-based Space Mission Visualization):**
              NASA open-source visualization suite (GitHub: `nasa/mission-viz`) utilizing Three.js and X3DOM to render 3D solar system orreries, Keplerian orbits, and Earth-Moon orbital transfers.
            """
        )

    with tab_case:
        st.markdown(
            r"""
            ### Real-World Mission Case Study: BioNutrients-2
            *(NASA Ames Research Center / International Space Station)*

            Demonstrating systems engineering in action:
            - **Need & Goal:** Enable on-demand production of essential vitamins (beta-carotene) using genetically engineered yeast to protect astronauts on long-duration Mars missions.
            - **User Segment Requirements Drive System Design:**
              - Science requirement: $\ge 12$ replicate samples, $\ge 30$ mL volume, $\ge 3\ \mu\text{g}$ beta-carotene/mL.
              - Hardware constraints derived: $< 250\text{ g}$ bag container, $< 300\text{ mL}$ total volume.
            - **Segment Execution:**
              - *Launch Segment:* NG-18 cargo mission to the ISS.
              - *Space Segment:* Hydration, incubation, and cold stowage aboard the ISS.
              - *Ground Segment:* Real-time temperature and initiation telemetry monitoring.
              - *User Segment:* Ground laboratory analysis and peer-reviewed scientific findings.
            """
        )
