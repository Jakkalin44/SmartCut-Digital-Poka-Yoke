
import streamlit as st
import cv2
import numpy as np
from pathlib import Path

from notepad_adapter import send_to_notepad




st.set_page_config(
    page_title="SmartCut | Automation System",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)




def load_css():
    css_path = Path(__file__).parent / "style.css"

    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        st.html(f"<style>{css}</style>")
    else:
        st.warning("style.css not found")


load_css()



jobs = {
    "Abcdf2221": {
        "material": "Steel",
        "thickness": 2.0,
        "quantity": 10
    },
    "Xyz12345": {
        "material": "Aluminum",
        "thickness": 3.0,
        "quantity": 5
    }
}




def validate_job_code(code):

    if not isinstance(code, str):
        return None, "Invalid Job Code"

    code = code.strip()

    if not code:
        return None, "Please enter a Job Code"

    if code not in jobs:
        return None, "Job Code not found"

    return jobs[code], None




def decode_qr_image(uploaded_file):

    file_bytes = np.frombuffer(
        uploaded_file.getvalue(),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    if image is None:
        return None

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if data:
        return data.strip()

    return None




st.markdown("""
<div class="hero">
    <div class="hero-content">
        <div class="hero-icon">✂️</div>
        <div>
            <div class="hero-title">
                SMART<span>CUT</span>
            </div>
            <div class="hero-subtitle">
                AUTOMATION SYSTEM
            </div>
            <div class="hero-description">
                Intelligent CNC Cutting Assistant
            </div>
        </div>
    </div>
    <div class="hero-status">
        <span class="status-dot"></span>
        SYSTEM ONLINE
    </div>
</div>
""", unsafe_allow_html=True)




st.markdown("""
<div class="process-bar">
    <div class="process-step active">
        <div class="step-icon">01</div>
        <div>SCAN JOB</div>
    </div>
    <div class="process-line"></div>
    <div class="process-step">
        <div class="step-icon">02</div>
        <div>PROCESS</div>
    </div>
    <div class="process-line"></div>
    <div class="process-step">
        <div class="step-icon">03</div>
        <div>CUT</div>
    </div>
    <div class="process-line"></div>
    <div class="process-step">
        <div class="step-icon">04</div>
        <div>COMPLETE</div>
    </div>
</div>
""", unsafe_allow_html=True)




if "scanned_job_code" not in st.session_state:
    st.session_state.scanned_job_code = None

if "manual_job_code" not in st.session_state:
    st.session_state.manual_job_code = ""




st.markdown(
    '<div class="section-heading">01 / JOB IDENTIFICATION</div>',
    unsafe_allow_html=True
)

manual_col, qr_col = st.columns(2, gap="large")




with manual_col:

    with st.container(border=True):

        st.markdown("### ⌨️ Manual Job Code")

        st.caption("Enter your production Job Code")

        manual_code = st.text_input(
            "Job Code",
            placeholder="Example: Abcdf2221",
            key="manual_job_code",
            label_visibility="collapsed"
        )

        if st.button(
            "✓  Validate Job Code",
            key="validate_manual",
            use_container_width=True
        ):

            data, error = validate_job_code(manual_code)

            if error:
                st.error(error)
            else:
                st.session_state.scanned_job_code = None
                st.success("Job Code Verified!")




with qr_col:

    with st.container(border=True):

        st.markdown("### ▦ QR Code Scanner")

        st.caption("Upload a QR Code image to scan")

        uploaded_file = st.file_uploader(
            "Upload QR Code",
            type=["png", "jpg", "jpeg"],
            key="qr_upload",
            label_visibility="collapsed"
        )

        if uploaded_file is not None:

            qr_code = decode_qr_image(uploaded_file)

            if qr_code:

                st.session_state.scanned_job_code = qr_code

                st.success(
                    f"Scanned: {qr_code}"
                )

            else:

                st.session_state.scanned_job_code = None

                st.error("Unable to detect QR Code")



st.markdown(
    '<div class="section-heading">02 / JOB DATA</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    st.markdown("### Production Job Information")

    source = st.radio(
        "Select Job Code Source",
        ["Manual Input", "QR Scanner"],
        horizontal=True
    )

    if source == "Manual Input":
        selected_code = manual_code.strip()
    else:
        selected_code = st.session_state.scanned_job_code or ""

    job_data, error = validate_job_code(selected_code)

    if error:

        st.info(
            "Enter or scan a valid Job Code "
            "to display production information."
        )

    else:

        st.success("JOB CODE VERIFIED")

        st.markdown(
            f"### Job Code: `{selected_code}`"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "MATERIAL",
                job_data["material"]
            )

        with col2:
            st.metric(
                "THICKNESS",
                f'{job_data["thickness"]} mm'
            )

        with col3:
            st.metric(
                "QUANTITY",
                job_data["quantity"]
            )




st.markdown(
    '<div class="section-heading">03 / AUTOMATION</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    st.markdown("### 🖥️ Notepad Automation Demo")

    st.warning(
        "DEMO MODE — Sends Job Code to Notepad only. "
        "Never connect this demo to CNC."
    )

    if error:

        st.info("A valid Job Code is required to enable automation.")

    else:

        st.write(
            f"Ready to send: **{selected_code}**"
        )

        confirm = st.checkbox(
            "I confirm sending this Job Code to Notepad",
            key=f"confirm_{source}_{selected_code}"
        )

        if st.button(
            "➜  Send to Notepad (Demo)",
            disabled=not confirm,
            type="primary",
            use_container_width=True
        ):

            success, message = send_to_notepad(
                selected_code
            )

            if success:

                st.success(message)

                st.info(
                    "Check Notepad to verify the received Job Code."
                )

            else:

                st.error(message)




st.markdown("""
<div class="footer">
    SMARTCUT AUTOMATION SYSTEM
    <br>
    <span>Digital Poka-Yoke | Prototype Version 4.0</span>
    <br>
    <span>Notepad Demo Only — No CNC Connection</span>
</div>
""", unsafe_allow_html=True)
